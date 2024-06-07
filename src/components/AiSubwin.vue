<template>
  <background class="background">
      <ssb ref="ssbIns" :wid="sidebarRatio*100" v-model:items="pages" @cliPageEv="cliPageSidebar" @cliLobbyEv="cliLobby" @cliAddEv="cliAdd" @cliHideEv="cliHide" @del="del" @transShowChat="onTransShowChat"></ssb>
      <div :style="{width:'96.5vw'}">
      <div class="entryBlockContainer">
        <sr :searchResults="searchResults"></sr>
      </div></div>
      <br><br><br><br><br><br><br><br><br>
        <VueDragResizeRotate v-show="showChat"
        class-name="aiChatEdge"
        :min-width="450"
        :min-height="750"
        :w="awidth"
        :h="aheight"
        :x="0"
        :y="0"
        @resizing="onResize"
        @resizestop="onResize"
        @click="aiBoxresizable"
        style="overflow: hidden; position: fixed; top: 1.2vh; left: 20vw;"
        >
          <aiChatbox bc="#ddd" br="25px" @findPost="onFindPost" />
        </VueDragResizeRotate>
  </background>
  
</template>

<script setup>
import sr from './SearchResult.vue'
import VueDragResizeRotate from "@gausszhou/vue3-drag-resize-rotate";
import "@gausszhou/vue3-drag-resize-rotate/lib/bundle.esm.css";
import {defineProps,ref} from 'vue'
import ssb from './SecondSIdeBarOfAi.vue'
import aiChatbox from './AiChatbox.vue'
const pr = defineProps(['widthRatio','list'])
const sidebarRatio=ref(0.175);
let displayIndex = ref(-1);
let awidth = (1-sidebarRatio.value)*pr.widthRatio*window.innerWidth/100;
let aheight = 0.98*window.innerHeight;
console.log(awidth,aheight)

let pages=ref([]);
function del(index){
  pages.value[index].isc = false;
  pages.value.splice(index,1);
}
function connectTo(index){
  console.log(pages.value[index])
  displayIndex.value=index;
}
function cliHide(){
  console.log('hide');
}
function cliLobby(){
  connectTo(-1);
  console.log('lobby');
}
function cliPageSidebar(index){
  connectTo(index);
  console.log('page-sidebar');
}
function cliAdd(){
  connectTo(-2)
  console.log('add');
}
</script>

<script>
export default {
data() {
  return {
      showChat:true,
      minWidth: 200,
      minHeight: 200,
      w: 200,
      h: 200,
      aiBoxresizable: true,
      searchResults: [//{title:'string',link:'https://www.baidu.com/',snippet:'string'},
      ]
  }
},
methods:{
  onFindPost(post){
    console.log('AiWin findPost');
    console.log(post);
    this.searchResults.push(post)
  },
  onTransShowChat() {
    this.showChat=!this.showChat
  },
  onResize: function (x, y, width, height) {
      this.w = width;
      this.h = height;
    },
  changeStateResizable: function() {
    console.log(this.resizable);
      this.resizable=!this.resizable;
    }
}
};
</script>

<style scoped>
::-webkit-scrollbar {
  display: none
}
.background {
  background-color: lightgray;
  display: flex;

}
.sr-box {
  position: relative;
  top:1vh;
  display: flex;
  flex-direction: column;
  gap: 1vh;
  transform-style: preserve-3d;
}



entryBlock {
    box-sizing: border-box;
    position: relative;
    width: 90%;
    margin-left: 5%;
    margin-top: 1%;
    padding: 1%;
    height: 10vw;
    overflow: hidden;
    border-radius: 15px;
    background-color: white;
    white-space: nowrap;
    display: flex;
    scale: 1;
    transition-property: scale,height;
    transition-duration: 0.16s,0.4s;
    transition-timing-function: ease-in-out,ease-in-out;
    transition-delay: 0ms,200ms;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.entryBlockContainer{
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 1vh;
    transform-style: preserve-3d;
}
entryBlock:hover  {
    opacity: 1;
    scale: 1.03;
    height: 50vh;
    filter: drop-shadow(0 0 25px #000)
            drop-shadow(0 0 45px #000);
}
entryBlock:hover subText {
    opacity: 1;
    min-height: 70%;
    max-height: 10%;
    white-space: normal;
    
    filter: drop-shadow(0 0 25px #000)
            drop-shadow(0 0 45px #000);
}
entryBlock:not(:hover)  {
    opacity: 0.5;
    scale: 0.95;
    transform: perspective(500px);
}
subCoverBox {
    position: absolute;
    left: 1%;
    top : 1%;
    width: 60%;
    max-height: 100%;
    overflow: hidden;
    border-radius: 15px;
}
.subCover {
    width: 100%;
    height: 80vh;
}
.subText {
    padding-left: 0.7%;
    padding-right: 0.7%;
    padding-top: 0.4%;
    padding-bottom: 0.8%;
    background-color: bisque;
    border-radius: 15px;
}
subTitle {
    position :absolute;
    height: auto;
    left:63%;
    width: 34.875%;
    align-self: flex-start;
    font-size: 2.5vh;
}

subTags {
    position: absolute;
    width: 100%;
    left:63%;
    display: flex;
    flex-wrap: wrap;
    gap: 2.2%;
}
tagBox {
    position :relative;
    top: 5vh;
    height: 1vh;
    min-width: 3%;
    font-size: 2.3vh;
    background-color: bisque;
    padding-left: 10%;
    padding-right: 10%;
    padding-top: 0.2%;
    padding-bottom: 0.2%;
    border-radius: 15px;
}

subText {
    position :absolute;
    width: 34.6875%;
    font-size: 2.3vh;
    left:63%;
    align-self: self-end;
    overflow: scroll;
    min-height: 0;
    white-space:nowrap;
    transition: min-height 0.4s ease-in-out 450ms;
}
subText::-webkit-scrollbar {
    display: none;
}

</style>