<template>
  <div class="bar-background" :style="{width:pr.wid + 'vw'}">
  <titleBox v-model:isClicked="iscTitle" @cli="cliTitle" iconHtml='<i class="fa-solid fa-map-location-dot"></i>' size="1.4" mart="0.3" marr="0.25" marl="0.55" h='7' text="AI向导" padh="0" fSize='3.5'>AI向导</titleBox>
  <div style="height: 3vh"></div>
  <lobbyButton v-model:isClicked="iscLobby" @cli="transShowChat" iconHtml='<i class="fa-solid fa-user-check"></i>' size="1.1" mart="0.1" marr="0.2" marl="0.55" h='5' text="Chat" padh="2" fSize='2.3'>chat</lobbyButton>
  <div style="height: 1vh"></div>
  <svg width="100%" height="2">
    <line x1="2%" y1="1" x2="98%" y2="1" style="stroke:black;stroke-width:1" />
  </svg>
  <pages style="margin-left: 7%;margin-right: 7%;margin-top: 4%;margin-bottom: 4%;">
    <div v-for="(item,index) in pr.items" :key='item'>
      <pageBox class="clickable" v-model:isClicked="item.isc" :withIndex='1' :i="index" :group="pr.items" :text="item.title" @cli="cliButtonInGroup" @dblclick='del(index)' imgSrc="./mock/pic/button.png" h='5' padh="2" fSize='2.3'></pageBox>
    </div>
  </pages>
  <addButton v-model:isClicked="iscAdd" @cli="cliAdd" imgSrc="./mock/pic/button.png" :r="pr.wid*0.2" h="1" style="position: absolute;bottom:1vh">+</addButton>
  </div>
</template>

<script setup>
import {defineProps,defineEmits,ref} from 'vue'
import lobbyButton from './SquareButtonWithIcon.vue'
import titleBox from './SquareButtonWithIcon.vue'
import pageBox from './SquareButtonWithIcon.vue'
import addButton from './CircleButton.vue'
const pr = defineProps(['wid','items'])
const em = defineEmits(['cliPageEv','cliLobbyEv','cliAddEv','cliHideEv','del'])
let iscTitle=ref(false);
let iscLobby=ref(false);
let iscAdd=ref(false);

function del(index){
  em('del',index);
}

function resetButton() {
  pr.items.forEach(element => {
    element.isc=false;
  });
  iscAdd.value=false;
}
function cliTitle() {
  shine(iscTitle,450);
  em('cliHideEv');
}
function cliAdd(){
  resetButton();
  iscAdd.value=true;
  em('cliAddEv');
}
function cliButtonInGroup(index,group){
  resetButton();
  group[index].isc=true;
  em('cliPageEv',index);
}
function shine(variable,time){
  variable.value=true;
  setTimeout(() => {
    variable.value=false;
      }, time);
}

</script>

<script>
export default {
  data() {
    return {
    };
  },
  methods:{
    transShowChat(){
      this.$emit('transShowChat')
    }
  }
};
</script>

<style scoped>
.bar-background {
  background-color: white;
  height: 100vw;
  width: auto;
  padding-top: 1vh;
  padding-bottom: 1vh;
  display: flex;
  flex-direction: column;
  height: 100vh; /* 确保父容器有高度 */
  overflow: hidden;
}
.inner-button {
  margin-left: auto;
  margin-right: auto;
}
pageBox:hover {
    filter: drop-shadow(0 0 5px #f50909) drop-shadow(0 0 25px #ff9898);
}
</style>