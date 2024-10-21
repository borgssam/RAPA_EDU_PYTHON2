<template>
  <div id="app">
    <SubwayCongestion />
  </div>
</template>

<script setup>
import { ref } from "vue";
import SubwayCongestion from "./views/SubwayCongestion.vue";

// 선택된 블로그 내용을 저장할 변수
const selectedBlog = ref(null);

// 블로그 링크를 클릭하면 해당 데이터를 BlogView에 전달
const openBlog = (blog) => {
  selectedBlog.value = blog;
};
</script>

<style scoped>
#app {
  text-align: center;
}
</style>
