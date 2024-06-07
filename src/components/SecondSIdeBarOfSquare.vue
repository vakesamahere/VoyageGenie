<template>
  <div class="bar-background" :style="{width:pr.wid + 'vw'}">
  <titleBox v-model:isClicked="iscTitle" @cli="cliTitle" iconHtml='<i class="fa-solid fa-earth-americas"></i>' size="1.6" marr="0.1" marl="0.4" mart="0.4" marb="0.1" h='7' text="广场" padh="0" fSize='3.5'>广场</titleBox>
  <div style="height: 3vh"></div>
  <lobbyButton v-model:isClicked="iscLobby" @cli="cliLobby" iconHtml='<i class="fa-solid fa-magnifying-glass"></i>' size="1.3" marl="0.5" marr="0.15" h='5' text="发现" padh="2" fSize='2.3'>发现</lobbyButton>
  <div style="height: 1vh"></div>
  <svg width="100%" height="2">
    <line x1="2%" y1="1" x2="98%" y2="1" style="stroke:black;stroke-width:1" />
  </svg>
  <pages style="margin-left: 7%;margin-right: 7%;margin-top: 4%;margin-bottom: 4%;">
    <div v-for="(item,index) in pr.items" :key='item'>
      <pageBox class="clickable" iconHtml='<i class="fa-solid fa-diamond"></i>' size="0.5" marr="0.2" mart="0.2" v-model:isClicked="item.isc" :withIndex='1' :i="index" :group="pr.items" :text="item.title" @cli="cliButtonInGroup" @dblclick='del(index)' imgSrc="./mock/pic/button.png" h='5' padh="2" fSize='2.3'></pageBox>
    </div>
  </pages>
  <addButton v-model:isClicked="iscAdd" @click="cliAdd" icon-html='<i class="fa-solid fa-marker"></i>' size="1.7" :r="pr.wid*0.2" h="1" style="position: absolute;bottom:0.6vh">+</addButton>
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
    try {
      element.isc=false;
    } catch (error) {
      console.log(error);
    }
  });
  try {
    iscAdd.value=false;
  } catch (error) {
    console.log(error);
  }
}
function cliTitle() {
  shine(iscTitle,450);
  em('cliHideEv');
}
function cliLobby() {
  resetButton();
  shine(iscLobby,75)
  em('cliLobbyEv');
}
//*
function cliAdd(){
  resetButton();
  try {
    iscAdd.value=true;
  } catch (error) {
    console.log(error);
  }
  em('cliAddEv');
}//*/
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