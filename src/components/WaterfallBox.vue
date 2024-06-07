<template>
    <div class="father-box back" :style="{ width: pr.ww + 'px', height: pr.wh + 'px' }">
    <v3-waterfall
      animation="false"
      :list="list"
      :colWidth="Number(pr.ww)*0.94/Number(pr.cols)"
      :virtual-time="0"
      :gap="Number(pr.ww)*0.05/(Number(pr.cols)+1)"
      :bottomGap="Number(pr.ww)*0.05/(Number(pr.cols)+1)"
      scrollBodySelector=".father-box"
      :isMounted="isMounted"
      :isLoading="loading"
      :isOver="over"
      class="waterfall"
      @scrollReachBottom="getNext"
    >
      <template v-slot:default="slotProp">
        <div class="list-item">
          <a href="#" @click="cli(slotProp.item)">
            <div class="cover-wrapper">
              <img v-if="slotProp.item.cover" :src="slotProp.item.cover" data-key="cover" class="cover" />
            </div>
            <div class="brief">
              <p class="card-title">{{ slotProp.item.title }}</p>
            </div>
          </a>
          <div class="outline-bottom">
            <p class="article-tags">
              <span v-for="tag of slotProp.item.tags+''" :key="tag" class="tag">
                {{ tag }}
              </span>
            </p>
          </div>
        </div>
      </template>
    </v3-waterfall>
    </div>
</template>
  
<script setup>
  import { defineProps,defineEmits } from 'vue';
  const pr = defineProps(['ww','wh','cols','list']);
  const em = defineEmits(['cliPage'])
  function cli(item){
    em('cliPage',item);
  }
</script>
<script>
  import {ref,onMounted} from 'vue'
  export default {
    data() {
      return {
        /*
        list: [
          {
            title: '上海会惩罚没有好好做攻略的人|人均500r🎈citywalk旅游攻略',
            cover: './mock/pic/1.jpg',
            tags: [],
          },
          {
            title: '【不可错过】五一小长假，这些隐藏版景点等你探索！',
            cover: './mock/pic/2.jpg',
            tags: [],
          },
          {
            title: '背包客必看：省钱又省心的旅行攻略',
            cover: './mock/pic/3.jpg',
            tags: [],
          },
          {
            title: '艺术与灵魂的邂逅：不可错过的艺术展览！',
            cover: './mock/pic/4.jpg',
            tags: [],
          },
          {
            title: '情侣必游：全球十大最浪漫的地方！',
            cover: './mock/pic/5.jpg',
            tags: [],
          },
          {
            title: '中国最美的十大海岛推荐',
            cover: './mock/pic/6.jpg',
            tags: [],
          },
          {
            title: '度假度假度假🌴',
            cover: './mock/pic/7.jpg',
            tags: [],
          },
          {
            title: '金光穿洞那一刻真的绝了‼️',
            cover: './mock/pic/8.jpg',
            tags: [],
          },
          {
            title: '在南昌电竞酒店被封号',
            cover: './mock/pic/9.jpg',
            tags: [],
          },
          {
            title: '探秘全球最大邮轮！加勒比海8天7夜吃什么？',
            cover: './mock/pic/10.jpg',
            tags: [],
          },
          {
            title: '一万块去日本一个星期够用吗',
            cover: './mock/pic/11.jpg',
            tags: [],
          },
          {
            title: '迄今为止，我最喜欢的城市出现了！',
            cover: './mock/pic/12.jpg',
            tags: [],
          },
          {
            title: '我们杭州的也有属于自己的阿勒泰！',
            cover: './mock/pic/13.jpg',
            tags: [],
          },
          {
            title: '多少人来成都文殊院就是为了这一口。。。',
            cover: './mock/pic/14.jpg',
            tags: [],
          },
          {
            title: '合肥📍这个地方真的太治愈啦',
            cover: './mock/pic/15.jpg',
            tags: [],
          },
          {
            title: '我很少用震撼来形容一个寺庙🙏',
            cover: './mock/pic/16.jpg',
            tags: [],
          },
          {
            title: '这个夏天总要来坐一次豪华游艇吧！',
            cover: './mock/pic/17.jpg',
            tags: [],
          },
          {
            title: '首尔挺有味道的，为什么都说是县城',
            cover: './mock/pic/18.jpg',
            tags: [],
          },
          {
            title: '其实香港人也挺宠大陆游客的',
            cover: './mock/pic/19.jpg',
            tags: [],
          },
          {
            title: '真不在上海！是大阪 出国了吧……好像又没有………',
            cover: './mock/pic/20.jpg',
            tags: [],
          },
          {
            title: '很难想象中国主城区靠海的省会城市居然只有1个，不是广州!!',
            cover: './mock/pic/21.jpg',
            tags: [],
          },
          {
            title: '圣彼得大教堂的惊鸿一瞥',
            cover: './mock/pic/22.jpg',
            tags: [],
          },
          {
            title: '比起西湖，我更喜欢这条杭州小众Citywalk‼️',
            cover: './mock/pic/23.jpg',
            tags: [],
          },
          {
            title: '大理｜去有风的地方躺平放空🕊️',
            cover: './mock/pic/24.jpg',
            tags: [],
          },
          {
            title: '一天一万在曼谷玩的值吗？',
            cover: './mock/pic/25.jpg',
            tags: [],
          },
          {
            title: '东京涩谷日落电梯，我答应带你去看！',
            cover: './mock/pic/26.jpg',
            tags: [],
          }
        ], // 数据列表//*/
        isMounted: true,
        loading: false,
        over: false
      };
    },
    methods: {
      getNext() {
        console.log(1);
        // 滚动到底部时调用的方法，用于加载更多数据
      },
      getColWidth() {
        return 500;
      },
      setup () {
        const isMounted = ref(false)
  
        onMounted(() => {
          isMounted.value = true
        })
  
        return { isMounted }
      }
    }
  };
  </script>
  
<style scoped>
::-webkit-scrollbar {
  display: none
}
  .father-box {
    overflow-y: scroll;
  }
  .list-item {
    border-radius: 15px;
    overflow: hidden;
    background-color: white;
    filter: drop-shadow(0 0 15px #555) drop-shadow(0 0 45px #555);
  }
  .list-item:hover{
    filter: drop-shadow(0 0 5px #000) drop-shadow(0 0 15px #111) drop-shadow(0 0 45px #111);
  }
  .cover {
    max-width: 100%;
    width: 100%;
    max-height: none;
    height: auto;
  }
  .back {
    background-color: lightgray;
  }
  .card-title {
    font-size:larger;
    margin-top: auto;
    margin-left: auto;
  }
  a {
      text-decoration: none;
      color: black;
      font-weight: bold;
  }
  </style>