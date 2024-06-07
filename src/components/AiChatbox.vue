<template>
  <div id="chat-app" :style="{ width: pr.ww + 'px', height: pr.wh + 'px', borderRadius:pr.br, backgroundColor: pr.bc}">
    <textarea readonly v-if="replying" class="title" :style="{backgroundColor:pr.bc,borderRadius:pr.br}">对方正在输入...</textarea>
    <textarea readonly v-else class="title" :style="{backgroundColor:pr.bc,borderRadius:pr.br}">向导</textarea>
    <div class="chat-window" ref="chatWindow">
      <div v-for="(message, index) in messages" :key="index" :class="['message', message.role]">
        <bub :class="['bub', message.role]">
          <msg v-html="getProcessedContent(message.content)"></msg>
        </bub>
        <button-copy-box v-if="message.role=='assistant'||message.role=='tool'" :class="[message.role]">
          <buttonCopy @click="copyMessage(message.content)" icon-html='<i class="fa-regular fa-copy"></i>' r="4" size="0.7" style="margin-left: 5%;"></buttonCopy>
        </button-copy-box>
      </div>
      <div class="message user">
        <bub :class="[userInputIdle?'':'bub', 'user']">
          <msg v-html="getProcessedContent(userInput)"></msg>
        </bub>
      </div>
      <br v-for="i in Array(10).fill(null)" :key="i">
    </div>
      <textarea class="inputBox" ref="inp" v-model="userInput" @keyup.enter="sendMessage" placeholder="Type a message..." @oninput="heightC=!heightC" :class="heightC?'ta':'tb'" style="height: 2cqh;"></textarea>
  </div>
</template>
<script>
import io from 'socket.io-client';
import buttonCopy from './CircleButton.vue';
export default {
  data() {
    return {
      markdownString: '# Marked in Vue component\n\nRendered by **marked**.',
      messages: [{role:'user',content:'你好'},{role:'assistant',content:'您好，我是您的旅行负责人，我将为您提供最佳的旅游规划~'},{role:'tool',content:'我是旅行负责人的助手，遇到较为专业的问题，我会尽我所能协助负责人给出解释'}],
      userInput: '',
      heightC:false,
      replying:false
    };
  },
  computed:{
      userInputIdle() {
        return this.userInput===''
      },
      renderedMarkdown() {
        return window.marked.parse(this.markdownString);
      }
  },
  mounted() {
    console.log(process.env.VUE_APP_AI_CHAT_URL);
    this.socket = io(process.env.VUE_APP_AI_CHAT_URL);
    this.socket.on('state', (data) => {
      if(data.state){
        this.replying=true
      }else{
        this.replying=false;
      }
    });
    this.socket.on('assistant_response', (data) => {
      /*
      if(!this.replying){
        this.messages.push({role:'assistant',content:''})
        this.replying=true
      }
      this.messages[this.messages.length-1].content=data.assistant_response;//*/
      if(data.assistant_response.role==='post'){
        console.log('chatBox findPost');
        console.log(data.assistant_response);
        this.$emit('findPost',data.assistant_response)
        return;
      }
      if(data.assistant_response.content.trim()==='')return;
      this.messages.push(data.assistant_response)
      console.log(data.assistant_response);
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    });
  },
  methods: {
    scrollToBottom() {
      const chatWindow = this.$refs.chatWindow;
      chatWindow.scrollTo(0,1E20)
    },
    sendMessage() {
      if(this.replying)return;
      this.messages.push({ role: 'user', content: this.userInput });
      this.socket.emit('message', this.userInput);
      this.userInput = '';
      this.replying = true;
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    },
    getProcessedContent(text){
      return window.marked.parse(text);
    },
    copyMessage(text){
        if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            // 复制成功的操作
        }).catch(err => {
            console.error('复制到剪贴板时出错：', err);
            alert('复制到剪贴板时出错');
            // 复制失败的操作
        });
        } else {
        console.error('Clipboard API 不支持');
            alert('Clipboard API 不支持');
        // Clipboard API 不支持时的操作
        }
    }
  }
};
</script>

<script setup>
import {defineProps} from 'vue'
const pr = defineProps(['ww','wh','bc','br'])
</script>

<style scoped>

#chat-app {
  z-index: 10;
  box-sizing: border-box;
  width: 98%;
  height: 98%;
  position: relative;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  padding: 1%;
  top: 5px; /* 调整阴影位置以确保它在元素的顶部 */
  bottom: -5px; /* 调整阴影位置以确保它在元素的底部 */
  left: 5px; /* 调整阴影位置以确保它在元素的左侧 */
  right: -5px; /* 调整阴影位置以确保它在元素的右侧 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  user-select: none;
}

.chat-window {
  flex: 1;
  position: relative;
  top: 7%;
  max-height: 93%;
  overflow-y: scroll;
  justify-content: center;
  align-items: flex-end;
}
::-webkit-scrollbar {
  display: none;
}
.title {
  z-index: 100;
  padding-top: 1%;
  height: 7%;
  width: 100%;
  position: absolute;
  text-align: center;
  resize: none;
  outline: none;
  font-size: 3cqh;
  font-weight: lighter;
  background-color: lightgray;
  border: 0;
  font-family: 'titleFont';
  
}
.title:focus {
  outline: none
}
.bub {
  position: relative;
  display: inline-block;
  padding-left: 1.5%;
  padding-right: 1.5%;
  border-radius: 10px;
  filter: drop-shadow(0 0 3px #bbbbbb);
}
.bub.assistant {
  margin-left: 5%;
  margin-right: 38.2%;
  background-color: #fff;
}
.bub.user {
  margin-left: 38.2%;
  margin-right: 5%;
  background-color: #57d253;
}
.bub.tool {
  margin-left: 5%;
  margin-right: 38.2%;
  background-color: #ffc5c5;
}

.message {
  margin: 2% 0;
  font-size: 1.5vh;
}

.message.user {
  text-align: right;
}

.message.assistant {
  text-align: left;
}
inputBox {
  margin-bottom: 2vh;
  padding-bottom: 2vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  background-color: transparent;
}
textarea.inputBox {
  position: fixed;
  top:90%;
    word-wrap: break-word;
    white-space: break-spaces;
  border-radius: 13px;  
  width: 61.8%;
  padding-bottom: 1vh;
  padding-top: 1vh;
  padding-left: 1.3%;
  padding-right: 1.3%;
  align-self: center;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
  overflow-x:hidden;
  resize: vertical;
  max-height: 40%;
  font-size: 2vh;

}
textarea::-webkit-scrollbar {
    display: none;
}
textarea:focus {
  outline: none;
}
</style>
