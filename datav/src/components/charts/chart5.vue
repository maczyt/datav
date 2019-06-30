<template>
  <v-chart :options="option" />
</template>

<script>
// 学历要求情况
import axios from "axios";

function setOption(name_data = [], value_data = []) {
  return {
    color: ["#0f63d6", "#0f78d6", "#0f8cd6", "#0fa0d6", "#0fb4d6"],
    tooltip: {},
    legend: {
      data: name_data,
      textStyle: {
        color: "rgba(255,255,255,.5)"
      }
    },
    series: [
      {
        type: "pie",
        radius: "55%",
        center: ["50%", "70%"],
        data: value_data,
        roseType: "radius"
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

    axios.get(`${this.prefix}/static/tmp/education.json`).then(res => {
      let data = res.data;
      data = data.sort((a, b) => b.value - a.value).slice(0, 6);
      const name_data = data.map(item => item.name);
      this.option = setOption(name_data, data);
    });
  }
};
</script>
