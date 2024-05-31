<template>
  <div
    class="dropzone"
    @dragover.prevent="dragOverHandler"
    @drop.prevent="dropHandler"
    @dragleave.prevent="dragLeaveHandler"
  >
    Перетащите файлы сюда
  </div>
</template>
<script setup>
import { ref } from 'vue';
import axios from 'axios';

const apiUrl = 'адрес_вашего_бекенда'; // Замените это на ваш API URL

// Drag and Drop обработчики
const dragOverHandler = (event) => {
  event.dataTransfer.dropEffect = 'copy'; // Визуально показываем, что копируем
};

const dropHandler = async (event) => {
  const files = event.dataTransfer.files;
  if (files.length) {
    await uploadFiles(files);
  }
};

const dragLeaveHandler = (event) => {
  // При необходимости можно добавить обработку ухода файлов из зоны
};

const uploadFiles = async (files) => {
  const formData = new FormData();
  for (let file of files) {
    formData.append('files', file); // Добавляем каждый файл в formData
  }

  try {
    const response = await axios.post(apiUrl, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    console.log('Файлы были успешно отправлены:', response.data);
  } catch (error) {
    console.error('Ошибка при отправке файлов:', error);
  }
};
</script>
<style scoped>
.dropzone {
  border: 2px dashed #007bff;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
  color: #007bff;
  cursor: pointer;
}
</style>
