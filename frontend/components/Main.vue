<template>
  <main class="main">
    <div v-if="!upload" class="container">
      <div class="drag_n_drop">
        <div
          class="dropzone"
          @dragover.prevent="dragOverHandler"
          @drop.prevent="dropHandler"
        >
          <Upload class="upload_logo" />
          <h4>Перетащите сюда файлы для загрузки</h4>
          <span class="or">или</span>
          <div class="button_send">
            <form method="post" enctype="multipart/form-data">
              <label class="input-file">
                <input type="file" name="file" @change="uploadFile" />
                <span class="input-file-btn">Выберите файл</span>
              </label>
            </form>
          </div>
        </div>
      </div>
      <div class="image_main">
        <img class="image" src="../assets/image.png" alt="" />
      </div>
    </div>
    <FinishedComponent
      v-else
      :filePath="word_url"
      :tableItems="response"
      basePath="http://v0d14ka.ddns.net:99/"
    />
  </main>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import Upload from 'assets/upload.svg';
import FinishedComponent from './FinishedComponent.vue';

let fileName = ref('Максимум 10мб');
const word_url = ref('');

const response = ref(null);
const upload = ref(false);

const dragOverHandler = (event) => {
  event.dataTransfer.dropEffect = 'copy';
};

const dropHandler = async (event) => {
  const files = event.dataTransfer.files;
  if (files.length) {
    await uploadFiles(files[0]);
  }
};

const uploadFiles = async (file) => {
  console.log(file);
  fileName.value = file ? file.name : 'Выберите файл';
  const formData = new FormData();
  formData.append('file', file);
  console.log(formData);
  try {
    const res = await axios.post('http://v0d14ka.ddns.net:99/', formData);
    response.value = res.data.items;
    word_url.value = res.data.word_url;
  } catch (error) {
    console.error('Ошибка при отправке файлов:', error);
  }

  setTimeout(() => {
    upload.value = true;
  }, 3000);
};

const uploadFile = async (event) => {
  const file = event.target.files[0];
  fileName.value = file ? file.name : 'Выберите файл';
  upload.value = true;
  if (!file) {
    console.error('Файл не выбран.');
    return;
  }

  const formData = new FormData();
  formData.append('file', file);

  try {
    const res = await axios.post('http://v0d14ka.ddns.net:99/', formData);
    response.value = res.data.items;
    word_url.value = res.data.word_url;
  } catch (error) {
    console.error('Ошибка при отправке файла:', error);
  }
};
</script>
<style scoped>
.main {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  background-color: #f9f9f9;
}

.container {
  padding-inline: 88px;
  min-height: 246px;
  width: 1440px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.input-file {
  position: relative;
  display: inline-block;
}

.input-file-text {
  padding: 0 10px;
  line-height: 40px;
  display: inline-block;
}
.input-file input[type='file'] {
  position: absolute;
  z-index: -1;
  opacity: 0;
  display: block;
  width: 0;
  height: 0;
}

.input-file-btn {
  padding: 25px;
  cursor: pointer;
}

.dropzone {
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  width: 336px;
  height: 207px;
  border: 5px solid #2f72ff;
  border-radius: 20px;
  flex-direction: column;
  color: #2f72ff;
  height: auto;
  max-width: 100%;
  padding: 20px;
}

.upload_logo {
  color: #2f72ff;
  width: 60px;
  height: 52px;
  margin-bottom: 21px;
}

.or {
  color: gray;
  margin-bottom: 27px;
  margin-top: 23px;
}

.drag_n_drop {
  position: relative;
}
.button_send {
  position: absolute; /* Позиционируем кнопку абсолютно относительно блока */
  bottom: -20px; /* Сдвигаем кнопку вверх, чтобы она выходила за границы блока */
  left: 50%; /* Размещаем по центру блока */
  transform: translateX(
    -50%
  ); /* Сдвигаем кнопку обратно, чтобы она точно центрировалась по горизонтали */
  /* Стили кнопки */
  padding: 5px 10px;
  width: 223px;
  height: 36px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  background-color: #2f72ff;
  border-radius: 50px;
}

.image {
  max-width: 100%;
  height: auto;
}

.image_main {
  @media screen and (max-width: 1000px) {
    display: none;
  }
}
</style>
