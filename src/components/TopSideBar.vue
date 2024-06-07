<template>
  <div class="background" :style="{width:pr.wid + 'vw'}">
    <cb @cli="sub1on" v-model:isClicked="isc1" imgSrc="./mock/pic/1.jpg" img="true" :r="pr.wid*0.65" h="1" class="inner-button user-info"></cb>
    <div style="padding-top:2vh"></div>
    <cb @cli="sub2on" v-model:isClicked="isc2" iconHtml='<i class="fa-solid fa-earth-americas"></i>' size="1.6" :r="pr.wid*0.9" h="1" class="inner-button explore" style="padding-top: 0.2vw"></cb>
    <cb @cli="sub3on" v-model:isClicked="isc3" iconHtml='<i class="fa-solid fa-comment"></i>' size="1.5" :r="pr.wid*0.9" h="1" class="inner-button ai" style="padding-top: 0.2vw"></cb>
    <cb @cli="sub4on" v-model:isClicked="isc4" iconHtml='<i class="fa-solid fa-plane"></i>' size="1.5" :r="pr.wid*0.9" h="1" class="inner-button user-plan" style="padding-top: 0.2vw"></cb>
    <cb @cli="sub5on" v-model:isClicked="isc5" iconHtml='<i class="fa-solid fa-house"></i>' size="1.6" :r="pr.wid*0.9" h="1" class="inner-button user-space" style="padding-top: 0.2vw"></cb>
    <cb @cli="sub6on" v-model:isClicked="isc6" iconHtml='<i class="fa-solid fa-gear"></i>' size="1.9" :r="pr.wid*0.9" h="1" class="inner-button setting" style="position: absolute;bottom:1vh;align-self: center;"></cb>
  </div>
</template>

<script setup>
import cb from './CircleButton.vue'
import {defineProps,defineEmits,ref} from 'vue'
const pr = defineProps(['wid'])
const em = defineEmits(['s1','s2','s3','s4','s5','s6'])
let isc1=ref(false);
let isc2=ref(false);
let isc3=ref(false);
let isc4=ref(false);
let isc5=ref(false);
let isc6=ref(false);

function resetButton(){
  isc1.value=false;
  isc2.value=false;
  isc3.value=false;
  isc4.value=false;
  isc5.value=false;
  isc6.value=false;
}
function sub1on(){
  resetButton();
  isc1.value=true;
  em('s1');
}
function sub2on(c){
  resetButton();
  isc2.value=true;
  em('s2');
}
function sub3on(){
  resetButton();
  isc3.value=true;
  em('s3');
}
function sub4on(){
  resetButton();
  isc4.value=true;
  em('s4');
}
function sub5on(){
  resetButton();
  isc5.value=true;
  em('s5');
}
function sub6on(){
  resetButton();
  isc6.value=true;
  em('s6');
}
</script>

<script>
</script>

<style scoped>
.background {
  background-color: #FFC297;
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
</style>