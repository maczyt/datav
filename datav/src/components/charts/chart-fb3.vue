<template>
  <v-chart :options="option" />
</template>

<script>
import axios from "axios";

function setOption(name_data = [], value_data = []) {
  return {
    title: [
      {
        text: "岗位要求",
        left: "center",
        textStyle: {
          color: "#fff",
          fontSize: "16"
        }
      }
    ],
    tooltip: {
      trigger: "item",
      formatter: "{a} <br/>{b}: {c} ({d}%)",
      position: function(p) {
        //其中p为当前鼠标的位置
        return [p[0] + 10, p[1] - 10];
      }
    },
    legend: {
      top: "70%",
      itemWidth: 10,
      itemHeight: 10,
      data: name_data,
      textStyle: {
        color: "rgba(255,255,255,.5)",
        fontSize: "12"
      }
    },
    series: [
      {
        name: "岗位要求",
        type: "pie",
        center: ["50%", "42%"],
        radius: ["40%", "60%"],
        color: [
          "#065aab",
          "#066eab",
          "#0682ab",
          "#0696ab",
          "#06a0ab",
          "#06b4ab",
          "#06c8ab",
          "#06dcab",
          "#06f0ab"
        ],
        label: { show: false },
        labelLine: { show: false },
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

    axios.get(`${this.prefix}/static/tmp/jobNature.json`).then(res => {
      let data = res.data;
      data = data.sort((a, b) => b.value - a.value).slice(0, 3);
      const name_data = data.map(item => item.name);
      this.option = setOption(name_data, data);
    });
  }
};
</script>


