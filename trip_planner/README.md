# VoyageGenie
本项目的开发并不规范，引用了https://github.com/joaomdmoura/crewAI-examples中的trip_planner源代码，同时修改了crewai的底层文件，运行除了安装需要的包以外，还需将trip_planner/libs/中的crewai包替换环境中的crewai。

# build
确保安装了npm(通过npm -V查看)
在此文件所在目录运行
npm install
npx vue-cli-service build
将生成的dist目录复制到trip_planner目录
新建虚拟环境
conda env create -f requirement.yml
将环境中的crewai包替换为trip_planner/libs/下的crewai包

在trip_planner/中使用python main.py运行程序

# .env
需要将trip_planner/中创建.env
设置如下值：
SERPER_API_KEY = SERPER的key

OPENAI_API_BASE = OpenAI API 的基础 URL 地址

OPENAI_API_KEY = 您的api_key
