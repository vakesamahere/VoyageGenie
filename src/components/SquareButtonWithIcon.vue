<template>
    <a href="#" @click="send" :class="[pr.isClicked?'button-block clicked':'button-block unclicked']" :style="{height:pr.h+'vh'}">
      <div>
        <img v-if="pr.img" :src="pr.imgSrc" class="inner-item" :style="{paddingLeft:pr.padh+'%'}"/>
        <div v-else class="icon-container">
        <div v-html="pr.iconHtml" :style="{fontSize:pr.size+'cqw',marginLeft:pr.marl+'cqw',marginRight:pr.marr+'cqw',marginTop:pr.mart+'cqw',marginBottom:pr.marb+'cqw'}"></div>
        </div>
      </div>
      <p class="inner-item text" :style="{paddingRight:pr.padh+'%', fontSize:pr.fSize+'vh'}">{{ pr.text }}</p>
    </a>
</template>

<script setup>
import {defineProps,defineEmits} from 'vue'
const pr = defineProps(['imgSrc','text','h','isClicked','padh','fSize','withIndex','i','group','size','img','iconHtml','marl','marr','mart','marb'])
const em = defineEmits(['cli'])
function send() {
    if(pr.withIndex){
        em('cli',pr.i,pr.group);
    }else{
        em('cli',pr.isClicked);
    }
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
.button-block {
    padding-top: 2%;
    padding-bottom: 2%;
    width: 100%;
    padding: 0;
    border: none;
    overflow: hidden;
    outline: none;
    display: flex;
}
.clicked {
    filter: drop-shadow(0 0 5px #f50909) drop-shadow(0 0 25px #ff9898);
}
.unclicked {
    background-color: transparent;
}

.button-block img {
    width: auto;
    height: 90%;
    display: block;
}
.inner-item {
    padding-left: 1%;
    padding-right: 1%;
    margin-top: auto;
    margin-bottom: auto;
}
a {
    text-decoration: none;
    color: black;
    font-weight: bold;
}
a:hover {
    filter: drop-shadow(0 0 5px rgb(255, 77, 0));
    transition: all 1s ease;
}
.text {
  white-space: nowrap; /* 文本不换行 */
  overflow: hidden; /* 溢出部分隐藏 */
  text-overflow: ellipsis; /* 显示为省略号 */
  width: 100%; /* 或者设置一个固定宽度 */
  -webkit-user-select: none; /* Safari */
  -moz-user-select: none;    /* Firefox */
  -ms-user-select: none;     /* IE/Edge */
  user-select: none;         /* 标准语法 */
}
.icon-container {
  width: 100%;
  height: 100%;
  display: grid;
}

.icon-container div {
  font-size: 2.5cqw;
  display: grid;
  place-items: center;
}
</style>