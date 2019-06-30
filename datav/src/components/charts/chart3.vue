<template>
  <v-chart :options="option" />
</template>

<script>
// 岗位数量发布情况
import echarts from "echarts";
import axios from "axios";

function setOption(name_data = [], value_data = []) {
  return {
    tooltip: {
      trigger: "axis",
      axisPointer: {
        lineStyle: {
          color: "#dddc6b"
        }
      }
    },
    legend: {
      top: "0%",
      data: ["Web前端"],
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    grid: {
      left: "10",
      top: "30",
      right: "10",
      bottom: "10",
      containLabel: true
    },

    xAxis: [
      {
        type: "category",
        boundaryGap: false,
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12
          }
        },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.2)"
          }
        },

        data: name_data
      }
    ],

    yAxis: [
      {
        type: "value",
        axisTick: { show: false },
        axisLine: {
          lineStyle: {
            color: "rgba(255,255,255,.1)"
          }
        },
        axisLabel: {
          textStyle: {
            color: "rgba(255,255,255,.6)",
            fontSize: 12
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
        name: "Web前端",
        type: "line",
        // 是否平滑显示
        smooth: true,
        // 是否在曲线上显示标记点
        showSymbol: false,
        // 曲线样式,颜色和宽度
        lineStyle: {
          color: "#0184d5",
          width: 2
        },
        // 曲线覆盖区域的颜色样式
        areaStyle: {
          color: new echarts.graphic.LinearGradient(
            0,
            0,
            0,
            1,
            [
              {
                offset: 0,
                color: "rgba(1, 132, 213, 0.4)"
              },
              {
                offset: 0.8,
                color: "rgba(1, 132, 213, 0.1)"
              }
            ],
            false
          ),
          shadowColor: "rgba(0, 0, 0, 0.1)"
        },
        itemStyle: {
          color: "#0184d5",
          borderColor: "rgba(221, 220, 107, .1)",
          borderWidth: 12
        },
        data: value_data
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
    axios.get(`${this.prefix}/static/tmp/job.json`).then(res => {
      let data = res.data;
      const name_data = data.map(item => item.name);
      const series_data = data.map(item => item.value);
      this.option = setOption(name_data, series_data);
    });
  }
};
</script>
