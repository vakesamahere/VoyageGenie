<template>
    <background :style="{width: pr.ww + 'px'}">
      <topTitle>发帖</topTitle>
      <div>
        <button @click="pasteFromClipboard" class="custom-button">从剪贴板导入</button>
      </div>
        <!-- 标题输入 -->
        <div>
          <input v-model="post.title" type="text" placeholder="帖子标题" style="width: 40%;font-size: 3vh" />
        </div>
<br>
        <CoverBox>
          <img :src="post.cover" alt="封面" class="subCover">
        </CoverBox>
        <input type="file" id="fileInputCover" @change="handleCoverUpload" style="display: none;" />
        <label for="fileInputCover" class="custom-button" style="background-color:green;width: 89%;">选择封面</label>

        <button @click="addTextLine" style="width: 15%" class="custom-button">添加正文段落</button>
      <topTextBox>
        <!-- 正文输入，按行分隔 -->
        <div v-for="(item, index) in tempTopText" :key="index">
            <div style="display: flex;flex-direction: row;">
          <button @click="removeParagraph(index)" style="height: 2%;" class="custom-button">x</button>
          <textarea v-model="tempTopText[index]" type="text" @input="updateText(index, $event.target.value)" placeholder="正文内容" style="width: 100%;font-size: 2vh;background-color: transparent;border: none;word-wrap: break-word;height: auto;" ></textarea>
            </div>
        </div>
      </topTextBox>
<br>
        <button @click="addEntry" style="width: 91%;" class="custom-button">添加条目</button>
      <!-- 遍历 entris 数组 -->
      <div>
        <div v-for="(entry, entryIndex) in post.entris" :key="entry.id">
          <entryBlock class="need-border" style="margin-bottom: 2vh;filter: drop-shadow(0 0 15px #666)">
            <!-- 条目标题 -->
            <subTitle class="subText need-border" :style="{'background-color': entry.title.color,'filter': 'drop-shadow(0 0 15px #666)','border-radius':15+'px'}">
              <input v-model="entry.title.text" type="text" placeholder="条目标题" class="inputBox" />
              <input type="color" v-model="entry.title.color" class="colorPanel"/>
            </subTitle>
            <!-- 条目正文 -->
            <subText class="subText need-border horizontal-scroll-container" :style="{'background-color': entry.text.color,'margin-top': 2+'vh','filter': 'drop-shadow(0 0 15px #666)','border-radius':15+'px'}">
              <textarea v-model="entry.text.text" placeholder="条目内容" class="inputBox"></textarea>
              <input type="color" v-model="entry.text.color" class="colorPanel"/>
            </subText>
            <!-- 条目顺序 -->
            <order :style="{'background-color': entry.order.color,'margin-top': 2+'vh','filter': 'drop-shadow(0 0 15px #666)','border-radius':15+'px'}">
              <input v-model="entry.order.text" type="text" placeholder="条目顺序" class="inputBox" />
              <input type="color" v-model="entry.order.color" class="colorPanel"/>
            </order>
            <!-- 条目标签 -->
            <subTags style="display: flex;flex-direction: row;flex-wrap: wrap;">
              <div v-for="(tag, tagIndex) in entry.tags" :key="tagIndex" >
                <tagBox :style="{'background-color': tag.color,'border-radius':15+'px'}">
                  <input v-model="tag.text" type="text" placeholder="标签" style="width: 8vw;height: 2vh;background-color: transparent; border: none;font-size: 1.5vh" />
                  <input type="color" v-model="entry.tags[tagIndex].color" class="colorPanel" style="width: 1vw;height: 2vh"/>
                  <button @click="removeTag(entryIndex, tagIndex)" style="height: 2vh;background-color: transparent;border:2vh solid transparent" >X</button>
                </tagBox>
              </div>
            </subTags>
              <button @click="addTag(entryIndex)" style="width: 8%;background-color:green;" class="custom-button">New tag</button>

            <!-- 图片 -->
            <div style="display: flex;flex-wrap: wrap; ">
            <div v-for="(cover, index) in entry.covers" :key="cover" class="need-border" >
              <subCoverBox>
                <img :src="cover" alt="内容图片" @click="delSubCover(entryIndex,index)" class="subCover">
              </subCoverBox>
            </div>
            </div>
              <input type="file" :id="'fileInputSub'+entryIndex" @change="(event) => handleFileUpload(event, entryIndex)" style="display: none;" multiple />
              <label :for="'fileInputSub'+entryIndex" class="custom-button" style="background-color:green;">选择图片</label>
              <button @click="removeEntry(entryIndex)" class="custom-button" style="background-color:#000;">删除条目{{entryIndex+1}}</button>
          </entryBlock>
    </div>
</div>
<br>
    <!-- 保存按钮 -->
    <button @click="savePost" style="width: 91%;" class='custom-button'>保存帖子</button>
    <br><br><br><br><br><br><br><br>
    </background>
  </template>
  
  <script>
  export default {
    
    data() {
      return {
        tempTopText:[],
        post: {
          title: '',
          text: '',
          cover: 'favicon.ico',
          tags:[],
          entris: [
            // 初始条目数据，可以根据需要添加更多字段
            {
              id: 1,
              title: { text: '', color: '#fff6a6' },
              covers: [],
              order: { text: '', color: '#fff6a6' },
              tags: [{ text: '', color: '#fff6a6' }],
              text: { text: '', color: '#fff6a6' }
            }
          ]
        },
        postDefault: {
          title: '',
          text: '',
          cover: 'favicon.ico',
          tags:[],
          entris: [
            // 初始条目数据，可以根据需要添加更多字段
            {
              id: 1,
              title: { text: '', color: '#fff6a6' },
              covers: [],
              order: { text: '', color: '#fff6a6' },
              tags: [{ text: '', color: '#fff6a6' }],
              text: { text: '', color: '#fff6a6' }
            }
          ]
        },
        displayIndexes: {}, // 用于控制封面图片显示的索引
      };
    },
    methods: {
      async pasteFromClipboard() {
      try {
        const clipboardText = await navigator.clipboard.readText();
        this.post = JSON.parse(clipboardText);
        console.log(this.post);
      } catch (error) {
        alert('读取剪贴板失败:', error);
      }
    },
      // 更新帖子正文的某行文本
      updateText(index, value) {
        this.post.text = this.post.text.split('\n').map((v, i) => {
          return i === index ? value : v;
        }).join('\n');
      },
      // 添加新的正文行
      addTextLine() {
        this.tempTopText.push('')
      },
      // 添加新的条目
      addEntry() {
        this.post.entris.push({
          id: this.post.entris.length + 1,
          title: { text: '', color: '#fff6a6' },
          covers: [],
          order: { text: '', color: '#fff6a6' },
          tags: [{ text: '', color: '#fff6a6' }],
          text: { text: '', color: '#fff6a6' }
        });
      },
      // 添加新的标签到指定条目
      addTag(entryIndex) {
        this.post.entris[entryIndex].tags.push({ text: '', color: '#fff6a6' });
      },
      // 删除一段正文
      removeParagraph(index) {
        this.tempTopText.splice(index, 1);
      },
      // 从指定条目中删除标签
      removeTag(entryIndex, tagIndex) {
        this.post.entris[entryIndex].tags.splice(tagIndex, 1);
      },
      // 删除标签
      removeEntry(index) {
        this.post.entris.splice(index, 1);
      },
      // 切换封面图片显示
      nextCover(entryIndex) {
        // 简单的逻辑，实际应用中可能需要更复杂的状态管理
        if (this.displayIndexes[entryIndex] === undefined) {
          this.displayIndexes[entryIndex] = 0;
        } else {
          this.displayIndexes[entryIndex]++;
        }
      },
      // 保存帖子
      savePost() {
        this.post.text=this.tempTopText.join('\n');
        console.log('帖子保存:', this.post);
            // 使用Clipboard API复制JSON字符串到剪贴板
        if (navigator.clipboard && navigator.clipboard.writeText) {
        const jsonStr = JSON.stringify(this.post);
        navigator.clipboard.writeText(jsonStr).then(() => {
            console.log('JSON字符串已复制到剪贴板');
            alert('导出成功!');
            // 复制成功的操作
            this.post=this.postDefault;
            this.$emit('generateNewPost',this.post);//to explore subwin
        }).catch(err => {
            console.error('复制到剪贴板时出错：', err);
            alert('SomethongWrong');
            // 复制失败的操作
        });
        } else {
        console.error('Clipboard API 不支持');
            alert('Clipboard API 不支持');
        // Clipboard API 不支持时的操作
        }
      },
      handleFileUpload(event,entryIndex) {
        const files = event.target.files;
        if (!files.length) {
          return;
        }
        // 循环处理每张图片
        for (let i = 0; i < files.length; i++) {
          const file = files[i];
          const reader = new FileReader();
          reader.onload = (e) => {
            const base64Image = e.target.result;
            this.post.entris[entryIndex].covers.push(base64Image);
          };
          reader.readAsDataURL(file);
        }
      },
      handleCoverUpload(event) {
        const files = event.target.files;
        if (!files.length) {
          return;
        }
        
        // 读取文件并转换为base64
        const file = files[0];
        const reader = new FileReader();
        reader.onload = (e) => {
          const base64Image = e.target.result;
          this.post.cover=base64Image; // 将base64编码添加到列表中
        };
        reader.readAsDataURL(file);
      },
      delSubCover(entryIndex,index){
        this.post.entris[entryIndex].covers.splice(index,1)
      }
    }
  };
  </script>
  <script setup>
import {defineProps} from 'vue'
const pr = defineProps(['ww'])

</script>
<style scoped>
.need-border {
    border: 1px solid #ccc
}
background {
    position: relative;
    padding-left: 5%;
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow-y: scroll;
    overflow-x: hidden;
    padding-top: 1vh;
    padding-bottom: 1vh;
    gap:'1.5%'
}
topTitle {
    font-size: 4vh;
    font-weight: bold;
    width: 100%;
    white-space: nowrap;
}
topTextBox {
    width: 87.5%;
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
    width: 90%;
    padding: 1%;
    height: auto;
    border-radius: 15px;
    background-color: white;
    white-space: nowrap;
    display: flex;
    flex-direction: column;
}
.subCover {
  max-height: 20cqh;
  max-width: 20cqh;
  width: auto;
  height: auto;
}
.custom-button {
  cursor: pointer;
  display: inline-block;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  transition: background-color 0.3s;
  text-align: center;
  margin: 1cqh;
  font-size: 2vh;
  filter: drop-shadow(0 0 15px #666)
}

.custom-button:hover {
  filter: drop-shadow(0 0 15px #000);
}

input {
  font-size: 2vh;
}
textarea {
  font-size: 2vh;
}
.colorPanel {
  width: 5%;height: 3vh;padding: 0;margin: 0;background-color: transparent;border: none;opacity: 0.5;
}
.inputBox {
  height: 5vh;
  width: 95%;background-color: transparent;border: none;
}

tagBox {
  z-index: 100;
  filter: drop-shadow(0 0 15px #666);
}

</style>