<template>
  <MainComponent />
</template>

<script setup>
import MainComponent from './components/MainComponent';
</script>

<style>
@import 'reset-css';
:root {
  --font-title: Montserrat, sans-serif;
  --font-text: Open Sans, sans-serif;

  font-family: var(--font-text);
}

html,
body,
#__nuxt {
  height: 100%;
}
</style>
