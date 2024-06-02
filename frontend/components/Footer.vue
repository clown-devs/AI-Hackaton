<template>
  <footer class="footer_container">
    <div class="container">
      <a target="_blank" href="https://t.me/Clown_devs_AI_bot"><Telergam class="telegram_logo" /></a>
      <a target="_blank" href="https://github.com/clown-devs"><GitHub class="github_logo" /></a>
    </div>
  </footer>
</template>
<script setup>
import Telergam from 'assets/Telegram.svg';
import GitHub from 'assets/GitHub.svg';
</script>
<style scoped>
.footer_container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.25);
  position: relative;
  z-index: 2;
}

.container {
  padding-inline: 88px;
  min-height: 115px;
  width: 1440px;
  display: flex;
  align-items: center;
}

.telegram_logo {
  width: 137px;
  height: 30px;
  color: #2f72ff;
  margin-right: 100px;
}

.github_logo {
  width: 110px;
  height: 30px;
  color: #2f72ff;
}
</style>
