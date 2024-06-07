<template>
    <div @click="send" :class="[pr.isClicked?'circle-button clicked':'circle-button unclicked']" :style="{width:r+'px',height:r+'px'}">
      <img v-if="pr.img" :src="pr.imgSrc"/>
      <div v-else class="icon-container">
        <div v-html="pr.iconHtml" :style="{fontSize:pr.size+'cqw'}"></div>
        </div>
    </div>
</template>

<script setup>
import {defineProps,defineEmits} from 'vue'
const pr = defineProps(['imgSrc','r','h','isClicked','iconHtml','img','size'])
const em = defineEmits(['cli'])
let r = (pr.h?window.innerWidth:window.innerHeight)*pr.r/100;
window.addEventListener('resize', () => {
        r = (pr.h?window.innerWidth:window.innerHeight)*pr.r/100;
    });
function send() {
    em('cli',pr.isClicked);
}
</script>

<script>
</script>

<style scoped>
.circle-button {
    padding: 0;
    border: none;
    border-radius: 50%;
    overflow: hidden;
    cursor: pointer;
    outline: none;
    transition: background-color 0.3s;
}
.clicked {
    filter: drop-shadow(0 0 5px #f50909) drop-shadow(0 0 25px #ff9898);
}
.unclicked {
    background-color: transparent;
}

.circle-button img {
    width: 100%;
    height: auto;
    display: block;
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
  transition: all 0.5s ease 0.05s;
}

.icon-container div:hover {
  filter: invert(0.95) drop-shadow(0 0 10px #000) drop-shadow(0 0 2px #000);
  scale: 1.2;
}
</style>