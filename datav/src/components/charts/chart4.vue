<template>
  <v-chart :options="option" />
</template>

<script>
// 工作经验分布情况
import axios from "axios";

function setOption(name_data = [], value_data = []) {
  return {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        type: "shadow"
      }
    },

    grid: {
      left: "0%",
      top: "10px",
      right: "0%",
      bottom: "2%",
      containLabel: true
    },
    xAxis: [
      {
        type: "category",
        data: name_data,
        axisLine: {
          show: true,
          lineStyle: {
            color: "rgba(255,255,255,.1)",
            width: 1,
            type: "solid"
          }
        },

        axisTick: {
          show: false
        },
        axisLabel: {
          interval: 0,
          show: true,
          splitNumber: 15,
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        }
      }
    ],
    yAxis: [
      {
        type: "value",
        axisLabel: {
          show: true,
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: "12"
          }
        },
        axisTick: {
          show: false
        },
        axisLine: {
          show: true,
          lineStyle: {
            color: "rgba(255,255,255,.1	)",
            width: 1,
            type: "solid"
          }
        },
        splitLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        }
      }
    ],
    series: [
      {
        type: "bar",
        data: value_data,
        barWidth: "35%", //柱子宽度
        itemStyle: {
          color: "#2f89cf",
          opacity: 1,
          barBorderRadius: 5
        }
      }
    ]
  };
}

export default {
  data() {
    return {
      option: {}
    };
  },
  props: {
    prefix: {
      type: String
    }
  },
  created() {
    this.option = setOption();

    axios.get(`${this.prefix}/static/tmp/workYear.json`).then(res => {
      let data = res.data;
      data = data.sort((a, b) => b.value - a.value).slice(0, 6);
      const name_data = data.map(item => item.name);
      const series_data = data.map(item => item.value);
      this.option = setOption(name_data, series_data);
    });
  }
};
</script>
