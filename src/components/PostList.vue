<template>
  <div>
    <!-- 遍历 posts 数组 -->
    <div v-for="post in posts" :key="post.id">
      <!-- 引用 post 对象的属性 -->
      <h2>{{ post.title }}</h2>
      <img :src="post.cover" alt="封面">
      <ul>
        <li v-for="tag in post.tags" :key="tag">
          {{ tag }}
        </li>
      </ul>
      <!-- 遍历 entris 数组 -->
      <div v-for="entry in post.entris" :key="entry.id">
        <h3>{{ entry.title }}</h3>
        <div v-for="cover in entry.covers" :key="cover">
          <img :src="cover" alt="内容图片">
        </div>
        <p>{{ entry.text }}</p>
        <ul>
          <li v-for="tag in entry.tags" :key="tag">
            {{ tag }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import data from '../assets/posts.json';
export default {
  data() {
    return {
      posts: data
    };
  }
  // ...
};
</script>

<style>

</style>