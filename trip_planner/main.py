#C:\Users\23664\.conda\envs\tripPlanner\Lib\site-packages\crewai\
#记得改环境的底层包crewai
import os
import subprocess
import sys
import time
from crewai import Crew
from textwrap import dedent
from trip_agents import TripAgents
from trip_tasks import TripTasks

from dotenv import load_dotenv
load_dotenv()

from dashscope import Generation
from datetime import datetime
import random
import json
import dashscope

from http import HTTPStatus
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')

class Receiver:
   #文字
   def newTaskResult(self,text):
      print('==========================================================')
      print('newTaskResult')
      print(text)
      print('==========================================================')
      message={
         "role":"tool",
         "content":text
      }
      socketio.emit('assistant_response', {'assistant_response': message})

   #结构化
   def newPrinterResult(self,text):
      print('==========================================================')
      print('newPrinterResult')
      print(text)
      print('==========================================================')
      objs=text.split('-----------------')
      print(objs)
      for obj in objs:
         lines=obj.split('\n')
         print(lines)
         for line in lines:
            print(line)
            if line.startswith('Title: '):
               i=lines.index(line)
               post={
                  'role': 'post',
                  'title':lines[i][len('Title: '):],
                  'link':lines[i+1][len('Link: '):],
                  'snippet':lines[i+2][len('Snippet: '):]
               }
               print(post)
               socketio.emit('assistant_response', {'assistant_response': post})
               break
receiver=Receiver()
def start_http_server(directory, port=8000):
    os.chdir(directory)
    subprocess.Popen(["python", "-m", "http.server", str(port)])
#===================================================end of server
class TripCrew:

  def __init__(self, origin, cities, date_range, interests):
    self.cities = cities
    self.origin = origin
    self.interests = interests
    self.date_range = date_range

  def run(self):
    agents = TripAgents()
    tasks = TripTasks()

    city_selector_agent = agents.city_selection_agent()
    local_expert_agent = agents.local_expert()
    travel_concierge_agent = agents.travel_concierge()

    identify_task = tasks.identify_task(
      city_selector_agent,
      self.origin,
      self.cities,
      self.interests,
      self.date_range
    )
    gather_task = tasks.gather_task(
      local_expert_agent,
      self.origin,
      self.interests,
      self.date_range
    )
    plan_task = tasks.plan_task(
      travel_concierge_agent, 
      self.origin,
      self.interests,
      self.date_range
    )

    crew = Crew(
      agents=[
        city_selector_agent, local_expert_agent, travel_concierge_agent
      ],
      tasks=[identify_task, gather_task, plan_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

#========================================end of tripPlannerTool

chats=[]

#========================================end of data

dashscope.api_key = os.environ.get('OPENAI_API_KEY')

# 定义工具列表，模型在选择使用哪个工具时会参考工具的name和description
#'''
tools = [
    {
       "type": "function",
       "function": {
          "name": "get_trip_plan",
          "description": "当用户已经明确提供了其所在的城市，想去的城市，什么时间段去，爱好的时候，若你想为用户生成旅游计划时非常非常非常有用。但是你要知道，用这个方法的耗时会很长，请确认用户所在的城市，想去的城市，什么时间段去，爱好，确保无误之后再谨慎调用。而且你在上下文可能已经有生成过类似的计划了，就不要大费周章再搞一次相同的了。",
          "parameters": { #需要提供 所在城市、目标城市、时间段、偏好
             "type": "object",
             "properties": {
                "location": {
                   "type": "string",
                   "description": "是用户当前所在的地方。国家、城市或县区，比如中国、美国、日本、北京市、上海、旧金山、杭州市、余杭区等。"
                },
                "destination":{
                   "type": "string",
                   "description": "是用户想要去的地方。国家、城市或县区，比如中国、美国、日本、北京市、上海、旧金山、杭州市、余杭区等。"
                },
                "timePeriod":{
                   "type": "string",
                   "descripition": "是用户计划去旅行的时间段。比如7月2日到7月9日、2024年三月、九月、July"
                },
                "hobbies":{
                   "type": "string",
                   "description":"用户喜欢做的事情。如打游戏、滑雪、看书、戏剧"
                }
             }
             
          }
       },
      "required": [
          "location",
          "destination",
          "timePeriod",
          "hobbies"
      ]
    }
]#'''

tools_test=[
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "当你想查询指定城市的天气时非常有用。",
            "parameters": {  # 查询天气时需要提供位置，因此参数设置为location
                        "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "城市或县区，比如北京市、杭州市、余杭区等。"
                    }
                }
            },
            "required": [
                "location"
            ]
        }
    }
]
#
def get_current_weather(location):
    return f"{location}今天是晴天。 "

# 生成旅行计划
def get_trip_plan(location,destination,timePeriod,hobbies):
   #return f'旅行计划:在{timePeriod}从{location}去{destination}玩{hobbies}'
  socketio.emit('assistant_response', {'assistant_response': {
    'content':'即将为您生成计划...',
    'role':'assistant'
     }})
  
  socketio.emit('assistant_response', {'assistant_response': {
    'content':f'已知悉您的概况:\n出发地:{location}\n目的地:{destination}\n旅行时间:{timePeriod}\n偏好:{hobbies}',
    'role':'tool'
     }})
  trip_crew = TripCrew(location, destination,timePeriod,hobbies)
  try:
    result = trip_crew.run()
  except:
     return '系统出现了一些小错误嗷:('
  return f'你的旅行计划如下:{result}'

# 封装模型响应函数 传入历史
def get_response(messages):
    response = Generation.call(
        model='qwen-max',
        messages=messages,
        tools=tools,
        seed=random.randint(1, 10000),  # 设置随机数种子seed，如果没有设置，则随机数种子默认为1234
        result_format='message'  # 将输出设置为message形式
    )
    return response

@socketio.on('message')
def call_with_messages(newInput,chats=chats):
    print(chats)
    if newInput=='reset' or newInput=='reset\n':
       chats.clear()
       socketio.emit('assistant_response', {'assistant_response': {
          'role':'tool',
          'content':'已重置对话'
       }})
       socketio.emit('state', {'start':False})
       print(chats)
       return
    print('\n')
    chats.append(
            {
                "content": newInput,
                "role": "user"
            }
    )
    print(chats)
    messages=chats.copy()
    # 模型的第一轮调用
    first_response = get_response(messages)
    assistant_output = first_response.output.choices[0].message
    print(f"\n大模型第一轮输出信息：{first_response}\n")
    messages.append(assistant_output)
    chats.append(assistant_output)
    socketio.emit('assistant_response', {'assistant_response': assistant_output})

    print(f"\nMessages:{messages}\n")
    if 'tool_calls' not in assistant_output:  # 如果模型判断无需调用工具，则将assistant的回复直接打印出来，无需进行模型的第二轮调用
        print(f"最终答案：{assistant_output.content}")
        socketio.emit('state', {'start':False})
        return
    # 如果模型选择的工具是get_trip_plan
    elif assistant_output.tool_calls[0]['function']['name'] == 'get_trip_plan':
        tool_info = {"name": "get_trip_plan", "role":"tool"}
        location = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['properties']['location']
        destination = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['properties']['destination']
        timePeriod = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['properties']['timePeriod']
        hobbies = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['properties']['hobbies']
        tool_info['content'] = get_trip_plan(location,destination,timePeriod,hobbies)
    elif assistant_output.tool_calls[0]['function']['name'] == 'get_current_weather':
        tool_info = {"name": "get_current_weather", "role":"tool"}
        location = json.loads(assistant_output.tool_calls[0]['function']['arguments'])['properties']['location']
        tool_info['content'] = get_current_weather(location)
    print(f"工具输出信息：{tool_info['content']}\n")
    messages.append(tool_info)
    chats.append(tool_info)
    socketio.emit('assistant_response', {'assistant_response': tool_info})
    print(f"\nMessages:{messages}\n")


    # 模型的第二轮调用，对工具的输出进行总结
    second_response = get_response(messages)
    print(f"大模型第二轮输出信息：{second_response}\n")
    print(f"最终答案：{second_response.output.choices[0].message['content']}")
    chats.append(second_response.output.choices[0].message)
    socketio.emit('assistant_response', {'assistant_response': second_response.output.choices[0].message})
    
    socketio.emit('state', {'start':False})
    

#=============================================end of dashscope

if __name__ == "__main__":
   directory_to_serve = "./dist"  # 要服务的目录的路径
   server_port = 8000  # 服务器端口，默认为8000
   start_http_server(directory_to_serve, server_port)
   print(f"HTTP server is running at http://localhost:{server_port}/")
   socketio.run(app, port=5050, host='0.0.0.0')
  
