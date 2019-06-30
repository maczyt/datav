<template>
  <v-chart :options="option" />
</template>

<script>
// 行业及职位数量
import axios from "axios";

function setOption(name_data = [], data = []) {
  return {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        // 柱形图阴影样式
        type: "shadow"
      }
    },
    // 柱形图与外容器间距
    grid: {
      left: "0%",
      top: "10px",
      right: "0%",
      bottom: "2%",
      // x,y轴是否显示
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
            // 横坐标线宽
            width: 1,
            type: "solid"
          }
        },

        axisTick: {
          // 是否显示X轴刻度
          show: false
        },
        axisLabel: {
          // x轴数据标签显示样式
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
        data: data,
        barWidth: "35%", //柱子宽度
        itemStyle: {
          color: "#2f89cf",
          // 数值为0时不绘制该柱形
          opacity: 1,
          // 柱形图圆角
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

    axios.get(`${this.prefix}/static/tmp/industryField.json`).then(res => {
      let data = res.data;
      data = data.sort((a, b) => b.value - a.value).slice(0, 6);
      const name_data = data.map(item => item.name);
      const series_data = data.map(item => item.value);
      this.option = setOption(name_data, series_data);
    });
  }
};
</script>
