<template>
    <box style="height: 100vh;overflow: auto;">
    <div v-for="(result, index) in searchResults" :key="index">
    <entryBlock>
    <subCoverBox>
        <iframe :src="result.link" class="subCover"></iframe>
    </subCoverBox>
    <subTitle class="subText">{{ result.title }}</subTitle>
    <subText class="subText horizontal-scroll-container">{{ result.snippet }}</subText>
    </entryBlock>
    </div></box>
</template>
  
  <script>
  export default {
    name: 'SearchResult',
    props: {
      searchResults: {
        type: Object,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>

  entryBlock {
    box-sizing: border-box;
    position: relative;
    width: 90%;
    margin-left: 5%;
    margin-top: 1%;
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
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}
.entryBlockContainer{
    position: relative;
    top:1vh;
    display: flex;
    flex-direction: column;
    gap: 1vh;
    transform-style: preserve-3d;
}
entryBlock:hover  {
    opacity: 1;
    scale: 1.03;
    height: 50vh;
    filter: drop-shadow(0 0 25px #000)
            drop-shadow(0 0 45px #000);
}
entryBlock:hover subText {
    opacity: 1;
    min-height: 70%;
    max-height: 10%;
    white-space: normal;
    
    filter: drop-shadow(0 0 25px #000)
            drop-shadow(0 0 45px #000);
}
entryBlock:not(:hover)  {
    opacity: 0.5;
    scale: 0.95;
    transform: perspective(500px);
}
subCoverBox {
    position: absolute;
    left: 1%;
    top : 1%;
    width: 60%;
    max-height: 100%;
    overflow: hidden;
    border-radius: 15px;
}
.subCover {
    width: 100%;
    height: 80vh;
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
    left:63%;
    width: 34.875%;
    align-self: flex-start;
    font-size: 2.5vh;
}

subTags {
    position: absolute;
    width: 100%;
    left:63%;
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
    width: 34.6875%;
    font-size: 2.3vh;
    left:63%;
    align-self: self-end;
    overflow: scroll;
    min-height: 0;
    white-space:nowrap;
    transition: min-height 0.4s ease-in-out 450ms;
}
subText::-webkit-scrollbar {
    display: none;
}

  </style>
  