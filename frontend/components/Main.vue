<template>
  <main class="main">
    <div class="container">
      <div class="drag_n_drop">
        <form method="post" enctype="multipart/form-data">
          <label class="input-file">
            <input type="file" name="file" @change="uploadFile" />
            <span class="input-file-btn">Выберите файл</span>
            <span class="input-file-text">{{ fileName }}</span>
          </label>
        </form>
        <div
          class="dropzone"
          @dragover.prevent="dragOverHandler"
          @drop.prevent="dropHandler"
        >
          Перетащите файлы сюда
        </div>
      </div>
      <div class="table_data">
        <div v-if="response">
          <table class="table">
            <thead>
              <tr>
                <th>№ эпизода НРД</th>
                <th>Время начала регистрации эпизода НРД, с</th>
                <th>Время завершения регистрации НРД, c</th>
                <th>Длительность эпизода НДР</th>
                <th>Тип эпизода НРД*</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="row in response" :key="row.episode">
                <td>{{ row.episode }}</td>
                <td>{{ row.start }}</td>
                <td>{{ row.end }}</td>
                <td>{{ row.duration }}</td>
                <td>{{ row.type }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div v-else></div>
      </div>
    </div>
  </main>
</template>
<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';

let fileName = ref('Максимум 10мб');

const response = ref(null);

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
  fileName.value = file ? file.name : 'Выберите файл';

  const formData = new FormData();
  formData.append('file', file);

  try {
    const res = await axios.post('http://v0d14ka.ddns.net:99/', formData);
    response.value = res.data;
  } catch (error) {
    console.error('Ошибка при отправке файлов:', error);
  }
};

const uploadFile = async (event) => {
  const file = event.target.files[0];
  fileName.value = file ? file.name : 'Выберите файл';

  if (!file) {
    console.error('Файл не выбран.');
    return;
  }

  const formData = new FormData();
  formData.append('file', file);

  try {
    const res = await axios.post('http://v0d14ka.ddns.net:99/', formData);
    response.value = res.data;
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
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.input-file {
  position: relative;
  display: inline-block;
}
.input-file-btn {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  text-decoration: none;
  font-size: 14px;
  vertical-align: middle;
  color: rgb(255 255 255);
  text-align: center;
  border-radius: 4px;
  background-color: #419152;
  line-height: 22px;
  height: 40px;
  padding: 10px 20px;
  box-sizing: border-box;
  border: none;
  margin: 0;
  transition: background-color 0.2s;
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

/* Focus */
.input-file input[type='file']:focus + .input-file-btn {
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

/* Hover/active */
.input-file:hover .input-file-btn {
  background-color: #59be6e;
}
.input-file:active .input-file-btn {
  background-color: #2e703a;
}

/* Disabled */
.input-file input[type='file']:disabled + .input-file-btn {
  background-color: #eee;
}

/* Table styles */
.table {
  width: 100%;
  border: none;
  margin-bottom: 20px;
  border-collapse: separate;
}
.table thead th {
  font-weight: bold;
  text-align: left;
  border: none;
  padding: 10px 15px;
  background: #ededed;
  font-size: 14px;
  border-top: 1px solid #ddd;
}
.table tr th:first-child,
.table tr td:first-child {
  border-left: 1px solid #ddd;
}
.table tr th:last-child,
.table tr td:last-child {
  border-right: 1px solid #ddd;
}
.table thead tr th:first-child {
  border-radius: 20px 0 0 0;
}
.table thead tr th:last-child {
  border-radius: 0 20px 0 0;
}
.table tbody td {
  text-align: left;
  border: none;
  padding: 10px 15px;
  font-size: 14px;
  vertical-align: top;
}
.table tbody tr:nth-child(even) {
  background: #f8f8f8;
}
.table tbody tr:last-child td {
  border-bottom: 1px solid #ddd;
}
.table tbody tr:last-child td:first-child {
  border-radius: 0 0 0 20px;
}
.table tbody tr:last-child td:last-child {
  border-radius: 0 0 20px 0;
}

.dropzone {
  border: 2px dashed #007bff;
  border-radius: 5px;
  padding: 20px;
  text-align: center;
  color: #007bff;
  cursor: pointer;
}
</style>
