<template>
  <div class="container">
    <div class="table_data">
      <div v-if="response">
        <div class="arrow" style="margin-block: 20px">
          <button
            @click="reloadPage"
            style="cursor: pointer; border: none; color: #2f72ff; padding: 15px"
          >
            Назад
          </button>
        </div>
        <div class="description">
          <h3 v-if="anomaleData" class="true_anomale">
            У данного пациента найдена аномалия
          </h3>
          <h3 v-else class="false_anomale">
            У данного пациента не найдена аномалия
          </h3>
        </div>
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
            <tr v-for="row in tableItems" :key="row.episode">
              <td>{{ row.episode }}</td>
              <td>{{ row.start }}</td>
              <td>{{ row.end }}</td>
              <td>{{ row.duration }}</td>
              <td>{{ row.type }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="finish">
        <div class="container_buttons">
          <a :href="completeFilePath" download="example">
            <button class="download_button">
              <div class="cont_but">
                <span class="title_but">Скачать файл</span>
                <Download class="download_logo" />
              </div>
            </button>
          </a>
          <button @click="watchResult" class="watch_button">
            <span class="title_watch__but">Посмотреть результат</span>
          </button>
        </div>
        <div class="image_container">
          <img class="image" src="../assets/finished_logo.png" alt="" />
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { defineProps, computed } from 'vue';
import Download from 'assets/download.svg';

const props = defineProps({
  filePath: String,
  tableItems: Array,
  anomaleData: Boolean,
  basePath: String,
});
const response = ref(false);

const completeFilePath = computed(() => {
  return props.basePath + props.filePath;
});

const watchResult = () => {
  console.log(123);
  response.value = true;
};

function reloadPage() {
  window.location.reload();
}
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
  cursor: pointer;
  margin-top: 26px;
}

.title_but {
  margin-right: 18px;
}

.link_watch {
  margin-top: 26px;
}

.image {
  max-width: 100%;
  height: auto;

  @media screen and (max-width: 1000px) {
    display: none;
  }
}

.container_buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.container {
  padding-inline: 88px;
  min-height: 246px;
  width: 1440px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.download_logo {
  color: white;
  width: 20px;
  height: 20px;
}

.finish {
  display: flex;
  align-items: center;
}

.table {
  width: 100%;
  border: none;
  margin-bottom: 20px;
  border-collapse: separate;
  /* color: #2f72ff; */
}
.table thead th {
  font-weight: bold;
  text-align: left;
  border: none;
  padding: 10px 15px;
  background: #ededed;
  font-size: 14px;
  border-top: 1px solid #ddd;
  color: #2f72ff;
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

.true_anomale {
  text-align: center;
  margin-block: 30px;
  padding: 20px;
  font-size: 25px;
  border: 2px solid rgb(220, 116, 116);
  color: #2f72ff;
  background-color: rgb(235, 164, 164);
}

.false_anomale {
  text-align: center;
  margin-block: 30px;
  padding: 20px;
  font-size: 25px;
  border: 2px solid rgb(17, 167, 107);
  color: #2f72ff;
  background-color: rgb(132, 218, 142);
}
</style>
