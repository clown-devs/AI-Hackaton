<template>
  <header class="header_container">
    <div class="container">
      <logoIcon class="logo_icon" />
    </div>
  </header>
</template>
<script setup>
import logoIcon from 'assets/logo.svg';
</script>
<style scoped>
.header_container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.25);
  position: relative;
  z-index: 2;
}

.container {
  width: 1440px;
  height: 156px;
  padding-inline: 88px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo_icon {
  color: #2f72ff;
  /* color: ; */
  width: 165px;
  height: 99px;
}
</style>
