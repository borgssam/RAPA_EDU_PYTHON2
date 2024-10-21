<template>
  <!-- 1번 컨테이너 - 제목과 현재 시간 -->
  <transition name="fade">
    <div class="container" v-if="currentStep === 1">
      <div class="header">
        <h1 class="title">지하철 혼잡도</h1>
        <div class="time">현재시간 : {{ currentTime }}</div>
      </div>
      <button @click="nextStep">시작</button>
    </div>
  </transition>

  <!-- 2번 컨테이너 - 호선 선택 -->
  <transition name="bounce">
    <div class="container" v-if="currentStep >= 2 && currentStep != 5">
      <div class="form-group">
        <label for="line">호선 선택 :</label>
        <select
          id="line"
          v-model="selectedLine"
          @change="updateStations"
          class="input"
        >
          <option
            v-for="(stations, line) in subwayLines"
            :key="line"
            :value="line"
          >
            {{ line }}
          </option>
        </select>
      </div>
      <button @click="nextStep" :disabled="!selectedLine || currentStep != 2">
        다음
      </button>
    </div>
  </transition>

  <!-- 3번 컨테이너 - 역명 선택 -->
  <transition name="bounce">
    <div class="container" v-if="currentStep >= 3 && currentStep != 5">
      <div class="form-group">
        <label for="station">역명 선택 :</label>
        <select id="station" v-model="departureStation" class="input">
          <option v-for="station in stations" :key="station" :value="station">
            {{ station }}
          </option>
        </select>
      </div>
      <button
        @click="nextStep"
        :disabled="!departureStation || currentStep != 3"
      >
        다음
      </button>
    </div>
  </transition>

  <!-- 4번 컨테이너 - 시간 선택 -->
  <transition name="bounce">
    <div class="container" v-if="currentStep >= 4 && currentStep != 5">
      <div class="form-group">
        <label for="time">출발 시간:</label>
        <select id="time" v-model="desiredTime" class="input">
          <option v-for="time in timeOptions" :key="time" :value="time">
            {{ time }}
          </option>
        </select>
      </div>
      <button @click="fetchSchedule" :disabled="!desiredTime">결과 보기</button>
    </div>
  </transition>

  <!-- 5번 컨테이너 - 결과 표시 -->
  <transition name="fade">
    <div class="container" v-if="currentStep === 5">
      <div class="status-box">
        <h3>[ {{ departureStation }}역 혼잡도 현황 ]</h3>
        <div class="status-row">
          <div class="status-col">
            <strong>현재</strong><br />
            상행 : {{ currentStatus.up }}<br />
          </div>
          <div class="status-col">
            <strong>30분 후</strong><br />
            상행 : {{ futureStatus.up }}<br />
          </div>
        </div>
      </div>
      <button @click="reset">다시 하기</button>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import subwayData from "./subway.json";

// 상태 변수
const subwayLines = ref(subwayData);
const selectedLine = ref("");
const stations = ref([]);
const departureStation = ref("");
const desiredTime = ref("");
const currentTime = ref("");
const currentStep = ref(1);

const currentStatus = ref({ up: "정보 없음", down: "정보 없음" });
const futureStatus = ref({ up: "정보 없음", down: "정보 없음" });

const timeOptions = ref([]);

// 시간 옵션 생성
const generateTimeOptions = () => {
  let hour = 5;
  let minute = 30;
  while (hour < 24 || (hour === 24 && minute === 30)) {
    const time = `${String(hour).padStart(2, "0")}:${String(minute).padStart(
      2,
      "0"
    )}`;
    timeOptions.value.push(time);
    minute += 30;
    if (minute === 60) {
      minute = 0;
      hour++;
    }
  }
};

// Flask 서버로부터 혼잡도 데이터 가져오기
const formatTime = (time) => {
  const [hour, minute] = time.split(":");
  return `${parseInt(hour)}시${minute}분`;
};

const fetchSchedule = async () => {
  try {
    const formattedTime = formatTime(desiredTime.value);
    console.log(formattedTime);
    console.log(formattedTime.value);
    const response = await axios.get("http://127.0.0.1:5001/get_schedule", {
      params: {
        departure_station: departureStation.value,
        line_number: selectedLine.value,
        desired_time: formattedTime, // 변환된 시간 전달
      },
    });

    const result = response.data;
    console.log(result);
    currentStatus.value.up = result.comp || "정보 없음";
    futureStatus.value.up = result.af_comp || "정보 없음";
    currentStatus.value.down = result.bf_comp || "정보 없음";

    nextStep();
  } catch (error) {
    console.error("혼잡도 조회 실패:", error);
  }
};

// 단계 전환 함수
const nextStep = () => {
  if (currentStep.value < 5) {
    currentStep.value++;
  }
};

// 초기화 함수
const reset = () => {
  selectedLine.value = "";
  stations.value = [];
  departureStation.value = "";
  desiredTime.value = "";
  currentStep.value = 1;
};

// 호선 선택 시 역 목록 업데이트
const updateStations = () => {
  stations.value = (subwayLines.value[selectedLine.value] || []).sort((a, b) =>
    a.localeCompare(b, "ko-KR")
  );
};

// 현재 시간 업데이트
onMounted(() => {
  const updateTime = () => {
    const now = new Date();
    currentTime.value = now.toLocaleTimeString("ko-KR", {
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  updateTime();
  setInterval(updateTime, 1000);

  generateTimeOptions(); // 시간 옵션 생성
});
</script>

<style scoped>
h1 {
  font-size: 44px;
  margin: 20px;
}
.time {
  margin: 20px;
}
label {
  color: black;
}
.container {
  width: 500px;
  margin: 20px auto;
  padding: 20px;
  border: 3px solid #616161;
  background-color: #d9d9d9;
  border-radius: 20px;
  margin-bottom: 20px;
}
.input {
  width: 160px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.status-box {
  border: 1px solid #ccc;
  padding: 10px;
  margin-top: 20px;
  background-color: #f9f9f9;
}
.form-group {
  margin: 16px;
}
label {
  padding: 8px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.bounce-enter-active {
  animation: bounce-in 0.6s;
}
.bounce-leave-active {
  animation: bounce-out 0.6s;
}
@keyframes bounce-in {
  0% {
    transform: scale(0.9);
    opacity: 0;
  }
  60% {
    transform: scale(1.05);
    opacity: 1;
  }
  100% {
    transform: scale(1);
  }
}
@keyframes bounce-out {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  100% {
    transform: scale(0.9);
    opacity: 0;
  }
}
</style>
