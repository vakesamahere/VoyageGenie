<template>
    <div>ATTRIBUTES_ABOVE</div>
    <wf ww='1400' wh='700' cols='4'></wf>
    <div>ATTRIBUTES_BELOW</div>
  </template>
  
  <script setup>
  import wf from './WaterfallBox.vue'
  </script>
  <script>
  export default {
    components: {
      wf
    },
    data() {
      return {
        wfWidth: 1600,
      };
    }
  };
  </script>
  
  <style>
  </style>