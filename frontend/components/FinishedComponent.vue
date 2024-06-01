<template>
  <div class="container">
    <div class="container_buttons">
      <a href="URL_ВАШЕГО_ФАЙЛА" download="example">
        <button class="download_button">
          <div class="cont_but">
            <span class="title_but">Скачать файл</span>
            <Download class="download_logo" />
          </div>
        </button>
      </a>
      <a href="URL_ВАШЕГО_ФАЙЛА" download="example" class="link_watch">
        <button class="watch_button">
          <span class="title_watch__but">Посмотреть результат</span>
        </button>
      </a>
    </div>
    <img src="../assets/finished_logo.png" alt="" />
  </div>
</template>
<script setup>
import { defineProps } from 'vue';
import Download from 'assets/download.svg';
const props = defineProps({
  valueWordUrl: String,
});
console.log(props.valueWordUrl);
</script>
<style scoped>
.download_button {
  background-color: #2f72ff;
  color: white;
  width: 293px;
  height: 78px;
  border-radius: 50px;
  border: none;
}

.watch_button {
  width: 380px;
  height: 76px;
  color: #2f72ff;
  background-color: #f9f9f9;
  border-radius: 50px;
  border: 1px solid #2f72ff;
}

.title_but {
  margin-right: 18px;
}

.link_watch {
  margin-top: 26px;
}

.cont_but {
}

.container_buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.download_logo {
  color: white;
  width: 20px;
  height: 20px;
}
</style>
