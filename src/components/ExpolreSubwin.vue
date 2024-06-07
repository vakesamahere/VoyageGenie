<template>
    <div class="background">
        <ssb ref="ssbIns" :wid="sidebarRatio*100" v-model:items="pages" @cliPageEv="cliPageSidebar" @cliLobbyEv="cliLobby" @cliAddEv="cliAdd" @cliHideEv="cliHide" @del="del"></ssb>
        <div>
            <addPost @generateNewPost="handleGenerateNewPost" v-show="displayIndex==-2" :ww="wfwidth"></addPost>
            <wf v-if="pr.loadWf&displayIndex==-1" :list="pr.list" :ww="wfwidth" :wh="wfheight" cols="4" @cliPage="cliPage"></wf>
            <div v-for="(item,index) in pages" :key="item">
                <singlePage @delSelf="delPost" v-show="displayIndex==index" :ww="wfwidth" :post="item">{{ index }}</singlePage>
            </div>
        </div>
    </div>
</template>

<script setup>
import {defineProps,ref} from 'vue'
import ssb from './SecondSIdeBarOfSquare.vue'
import addPost from './EditNewPost.vue'
import wf from './WaterfallBox.vue'
import singlePage from './SinglePage.vue'
const pr = defineProps(['widthRatio','list','loadWf'])
const sidebarRatio=ref(0.175);
let wfwidth = (1-sidebarRatio.value)*pr.widthRatio*window.innerWidth/100;
let wfheight = window.innerHeight;


</script>

<script>
import { reactive, onMounted } from 'vue';
export default {
    setup() {
      const state = reactive({
        loaded:false
      });
      onMounted(async () => {
        await loadData();
        state.loaded = true;
      });
      async function loadData() {
        return new Promise((resolve) => {
            console.log(resolve);
          setTimeout((resolve) => {
            resolve();
          },3000);
        });
      }
      return {
        state
      };
    },
  data() {
    return {
      displayIndex:-1,
      pages:[]
    }
  },
  methods:{
    handleGenerateNewPost(postJson) {
        this.$emit('generateNewPost',postJson)
        this.connectTo(-1)
    },

    delPost(post){
            this.pages.splice(this.pages.indexOf(post),1);
            this.$emit('delPost',post)//to App
            this.connectTo(-1)
        },
    del(index){
        this.pages[index].isc = false;
        this.pages.splice(index,1);
        this.connectTo(-1)
    },
    cliPage(page){
        if(!this.pages.includes(page)){
            this.pages.push(page);
        }
        this.pages.forEach(element => {
            element.isc = false;
            if(element==page){
                element.isc = true;
            }
        });
        this.connectTo(this.pages.indexOf(page));
    },
    connectTo(index){
        console.log(this.pages[index])
        this.displayIndex=index;
    },
    cliHide(){
        this.connectTo(-1);
        console.log('hide');
    },
    cliLobby(){
        this.connectTo(-1);
        console.log('lobby');
    },
    cliPageSidebar(index){
        this.connectTo(index);
        console.log('page-sidebar');
    },
    cliAdd() {
        this.connectTo(-2)
        console.log('add');
    }
  }
};
</script>

<style scoped>
.background {
    background-color: lightgray;
    display: flex;
}
</style>