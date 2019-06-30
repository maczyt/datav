<template>
  <div id="app">
    <div class="canvas" style="opacity: .2">
      <bg-canvas />
    </div>
    <div v-if="loading" class="loading">
      <div class="loadbox"><img src="/static/picture/loading.gif"> 页面加载中...</div>
    </div>
    <Head class="head" />

    <div class="mainbox">
    <ul class="clearfix">
      <li class="flex">
        <div class="boxall">
            <div class="alltitle">行业及职位数量</div>
            <div class="allnav">
              <chart1 :prefix="prefix" />
            </div>
            <div class="boxfoot"></div>
        </div>
        <div class="boxall">
            <div class="alltitle">薪酬分布情况</div>
            <div class="allnav">
              <chart2 :prefix="prefix" />
            </div>
            <div class="boxfoot"></div>
        </div>
        <div class="boxall">
            <div style="height:100%; width: 100%;">
                <div class="sy">
                  <chart-fb1 :prefix="prefix" />
                </div>
                <div class="sy">
                  <chart-fb2 :prefix="prefix" />
                </div>
                <div class="sy">
                  <chart-fb3 :prefix="prefix" />
                </div>
            </div>
            <div class="boxfoot"></div>
        </div>
      </li>
      <li class="flex">
          <div class="bar">
              <div class="barbox">
                  <ul class="clearfix">
                      <li class="pulll_left counter">{{all_count}}</li>
                      <li class="pulll_left counter">{{today_count}}</li>
                  </ul>
              </div>
              <div class="barbox2">
                  <ul class="clearfix">
                      <li class="pulll_left">总数据量</li>
                      <li class="pulll_left">今日抓取量</li>
                  </ul>
              </div>
          </div>
          <div class="map">
              <div class="map1"><img src="/static/picture/lbx.png"></div>
              <div class="map2"><img src="/static/picture/jt.png"></div>
              <div class="map3"><img src="/static/picture/map.png"></div>
              <div class="map4">
                <chart-map :prefix="prefix" />
              </div>
          </div>
      </li>
      <li class="flex">
          <div class="boxall">
              <div class="alltitle">岗位数量发布情况</div>
              <div class="allnav">
                <chart3 :prefix="prefix" />
              </div>
              <div class="boxfoot"></div>
          </div>
          <div class="boxall">
              <div class="alltitle">工作经验分布情况</div>
              <div class="allnav">
                <chart4 :prefix="prefix" />
              </div>
              <div class="boxfoot"></div>
          </div>
          <div class="boxall">
              <div class="alltitle">学历要求情况</div>
              <div class="allnav">
                <chart5 :prefix="prefix" />
              </div>
              <div class="boxfoot"></div>
          </div>
      </li>
  </ul>
  </div>
  <div class="back"></div>
  </div>
</template>

<script>
import bgCanvas from "@/components/bg-canvas";
import Head from "@/components/head";

/* charts */
import chart1 from "@/components/charts/chart1";
import chart2 from "@/components/charts/chart2";
import chart3 from "@/components/charts/chart3";
import chart4 from "@/components/charts/chart4";
import chart5 from "@/components/charts/chart5";

import chartFb1 from "@/components/charts/chart-fb1";
import chartFb2 from "@/components/charts/chart-fb2";
import chartFb3 from "@/components/charts/chart-fb3";
import chartMap from "@/components/charts/chart-map";
import axios from "axios";

const PREFIX = process.env.NODE_ENV === "development" ? "" : "/datav";

export default {
  name: "App",
  data() {
    return {
      loading: true,
      all_count: 1000,
      today_count: 200,
      prefix: PREFIX
    };
  },
  components: {
    bgCanvas,
    Head,
    chart1,
    chart2,
    chart3,
    chart4,
    chart5,
    chartFb1,
    chartFb2,
    chartFb3,
    chartMap
  },
  methods: {
    handleSetRem() {
      const html = document.documentElement;
      const whei = html.clientWidth;
      html.style.fontSize = whei / 20 + "px";
    }
  },
  created() {
    this.handleSetRem();
    window.addEventListener("resize", this.handleSetRem, false);
  },
  mounted() {
    this.loading = false;
    axios.get(`${PREFIX}/static/tmp/count.json`).then(res => {
      const data = res.data;
      this.all_count = data.allCount;
      this.today_count = data.todayCount;
      console.log("data", data);
    });
    // this.handleSetRem();
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.handleSetRem, false);
  }
};
</script>