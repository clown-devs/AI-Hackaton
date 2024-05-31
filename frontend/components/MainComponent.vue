<template>
  <div class="main-wrapper">
    <Header class="header" />
    <Main class="main" />
    <Footer class="footer" />
  </div>
</template>
<script setup>
import Header from './Header';
import Footer from './Footer';
import Main from './Main';
</script>

<style scoped>
.main-wrapper {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.header {
  flex-shrink: 0;
}

.main {
  flex-grow: 1;
}

.footer {
  flex-shrink: 0;
}
</style>
