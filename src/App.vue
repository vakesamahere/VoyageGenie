<template>
  <div class="parent-frame" v-if="!testing">
    <div class="top-sidebar sub-div" :style="{width:wTsb+'vw'}">
      <tsb :wid="wTsb" @s1=sub1on @s2=sub2on @s3=sub3on @s4=sub4on @s5=sub5on @s6=sub6on ></tsb>
    </div>
    <div class="sub-window sub-div" :style="{width:wSwin+'vw'}">
      <subwinUserInfo v-show="sub1"></subwinUserInfo>
      <subwinExplore @delPost="delPost" @generateNewPost="handleGenerateNewPost" v-show="sub2" v-model:list="posts" v-model:loadWf="loadWf" :widthRatio="wSwin"></subwinExplore>
      <subwinAi v-show="sub3" :list="posts" :widthRatio="wSwin"></subwinAi>
      <subwinUserPlan v-show="sub4"></subwinUserPlan>
      <subwinUserSpace v-show="sub5"></subwinUserSpace>
      <subwinSetting v-show="sub6"></subwinSetting>
    </div>
  </div>
  <div v-if="testing">
    <test></test>
  </div>
</template>

<script setup>
const testing = ref(false);
import test from './components/EditNewPost.vue'

import {ref} from 'vue'
import tsb from './components/TopSideBar.vue'

import subwinUserInfo from './components/UserInfoSubwin.vue'
import subwinExplore from './components/ExpolreSubwin.vue'
import subwinAi from './components/AiSubwin.vue'
import subwinUserPlan from './components/UserPlanSubwin.vue'
import subwinUserSpace from './components/UserSpaceSubwin.vue'
import subwinSetting from './components/SettingSubwin.vue'

const wTsb = ref(3.5);
const wSwin = ref(100-wTsb.value);

</script>

<script>
import data from './assets/posts.json';
export default {
  data() {
  return {
    posts:data,
    loadWf:false,

    sub1: false,
    sub2: false,
    sub3: false,
    sub4: false,
    sub5: false,
    sub6: false
    }
  },
  methods: {
    delPost(post){
      console.log("old",this.posts.length);
      this.posts.splice(this.posts.indexOf(post),1);
      console.log("new",this.posts.length);
    },
    handleGenerateNewPost(postJson){
      this.posts.push(postJson)
    },
    off() {
      this.sub1=false;
      this.sub2=false;
      this.sub3=false;
      this.sub4=false;
      this.sub5=false;
      this.sub6=false;
      this.loadWf=false;
    },
    sub1on() {
      this.off();
      this.sub1=true;
    },
    sub2on() {
      this.off();
      this.sub2=true;
      this.loadWf=true;
    },
    sub3on() {
      this.off();
      this.sub3=true;
    },
    sub4on() {
      this.off();
      this.sub4=true;
    },
    sub5on() {
      this.off();
      this.sub5=true;
    },
    sub6on() {
      this.off();
      this.sub6=true;
    }
  }
}

</script>

<style>
.parent-frame {
  display: flex;
}
.sub-div{
  height: 100vh;
}
body {
  position: fixed; /* 固定位置，防止滚动 */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: auto; /* 允许内部滚动 */
  margin: 0; /* 移除默认边距 */
  width: 100vw;
  height: 100vh;
}
</style>