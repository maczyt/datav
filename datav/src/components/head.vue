<template>
  <div>
    <h1>Web前端岗位数据可视化分析<sup>拉勾网</sup></h1>
    <div class="weather">
      <!--<img src="picture/weather.png"><span>多云转小雨</span>-->
      <span>{{showTime}}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showTime: ""
    };
  },
  created() {
    var t = null;
    t = setTimeout(time, 1000); //開始运行
    function time() {
      clearTimeout(t); //清除定时器
      const dt = new Date();
      var y = dt.getFullYear();
      var mt = dt.getMonth() + 1;
      var day = dt.getDate();
      var h = dt.getHours(); //获取时
      var m = dt.getMinutes(); //获取分
      var s = dt.getSeconds(); //获取秒
      this.showTime =
        y + "年" + mt + "月" + day + "-" + h + "时" + m + "分" + s + "秒";
      t = setTimeout(time, 1000); //设定定时器，循环运行
    }
  }
};
</script>

<style scoped>
sup {
  color: #fff;
}
</style>


