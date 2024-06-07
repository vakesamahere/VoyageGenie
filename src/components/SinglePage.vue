<template>
    <background :style="{width: pr.ww + 'px'}">
        <topTitle @dblclick="savePost">{{ pr.post.title }}</topTitle>
        <topTextBox>
            <div v-for="item in pr.post.text.split('\n')" :key="item">
                <topText><pre1>{{ item }}</pre1></topText>
            </div>
        </topTextBox>
        <!-- 遍历 entris 数组 -->
        <div class="entryBlockContainer">
        <div v-for="(entry,entryIndex) in pr.post.entris" :key="entry.id">
        <entryBlock>
            <subCoverBox>
                <img :src="entry.covers[displayIndexes[entryIndex]]" alt="内容图片" @click="nextCover(entryIndex)" class="subCover">  
            </subCoverBox>
          <subTitle class="subText" :style="{'background-color':entry.title.color}">{{ entry.title.text }}</subTitle>
          <subText class="subText horizontal-scroll-container" :style="{'background-color':entry.text.color}">{{ entry.text.text }}</subText>
          <order :style="{'background-color':entry.order.color}">{{ entry.order.text }}</order>
          <subTags>
            <div v-for="tag in entry.tags" :key="tag">
                <tagBox :style="{'background-color':tag.color}">
                    {{ tag.text }}
                </tagBox>
            </div>
          </subTags>
        </entryBlock>
        </div>
        </div>
        <br><br><br><br><br><br><br><br><br>
        <p @dblclick="delSelf" style="align-self: center;font-weight: lighter;opacity: 0.3;">看光了阿</p>
    </background>
  </template>
  
<script setup>
    import {defineProps,ref} from 'vue'
    const pr = defineProps(['post','ww'])
    let entryLength = ref([])
    let displayIndexes = ref([])
    pr.post.entris.forEach(element => {
        entryLength.value.push(element.covers.length);
        displayIndexes.value.push(0);
    });
    function nextCover(entryIndex) {
        displayIndexes.value[entryIndex]=(displayIndexes.value[entryIndex]+1)%entryLength.value[entryIndex];
        console.log(displayIndexes.value[entryIndex]);
    }
</script>

<script>
export default {
    methods: {
        delSelf(){
            console.log(1);
            this.$emit('delSelf',this.post)//to explore subwin
        },
        savePost() {
        console.log('帖子保存:', this.post);
            // 使用Clipboard API复制JSON字符串到剪贴板
        if (navigator.clipboard && navigator.clipboard.writeText) {
        const jsonStr = JSON.stringify(this.post);
        navigator.clipboard.writeText(jsonStr).then(() => {
            console.log('JSON字符串已复制到剪贴板');
            alert('已将帖子数据复制到剪贴板');
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
}
</script>
  
<style scoped>
background {
    user-select: none;
    position: relative;
    padding-left: 4.25%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow-y: scroll;
    overflow-x: hidden;
    padding-top: 1vh;
    padding-bottom: 1vh;
}
topTitle {
    font-size: 4vh;
    font-weight: bold;
    width: 100%;
    white-space: nowrap;
}
topTextBox {
    width: 87%;
    border-radius: 5px;
    margin-top: 2vh;
    margin-bottom: 2vh;
    background-color: bisque;
    padding: 1%;
    border-radius: 5px;
    font-size: 2vh;
    font-weight: lighter;
    word-wrap: break-word;
    padding-left: 2.5%;
    padding-right: 2.5%;
}
topText {
    word-wrap: break-word;
    white-space: break-spaces;
}
entryBlock {
    position: relative;
    width: 90%;
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
}
.entryBlockContainer{
    position: relative;
    top:1vh;
    display: flex;
    flex-direction: column;
    gap: 1vh;
    transform-style: preserve-3d;
}
.entryBlockContainer:hover > :hover entryBlock {
    opacity: 1;
    scale: 1.03;
    height: 40vh;
    filter: drop-shadow(0 0 25px #000)
            drop-shadow(0 0 45px #000);
}
.entryBlockContainer:hover > :hover entryBlock subText {
    opacity: 1;
    min-height: 70%;
    max-height: 10%;
    white-space: normal;
    
    filter: drop-shadow(0 0 25px #000)
            drop-shadow(0 0 45px #000);
}
.entryBlockContainer:hover > :not(:hover) entryBlock {
    opacity: 0.5;
    scale: 0.95;
    transform: perspective(500px);
}
subCoverBox {
    position: absolute;
    left: 1%;
    top : 3%;
    width: 40%;
    max-height: 94%;
    overflow: hidden;
    border-radius: 15px;
}
.subCover {
    width: 100%;
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
    left:43%;
    align-self: flex-start;
    font-size: 2.5vh;
}

subTags {
    position: absolute;
    width: 100%;
    left:43%;
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
    width: 54.6875%;
    font-size: 2.3vh;
    left:43%;
    align-self: self-end;
    overflow: scroll;
    min-height: 0;
    white-space:nowrap;
    transition: min-height 0.4s ease-in-out 450ms;
}
subText::-webkit-scrollbar {
    display: none;
}
order {
    height:min-content;
    margin-left: auto;
    margin-right: 0;
    padding-left: 0.7%;
    padding-right: 0.7%;
    background-color: bisque;
    border-radius: 15px;
}
</style>