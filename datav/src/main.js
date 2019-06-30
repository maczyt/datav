import Vue from 'vue'
import ECharts from 'vue-echarts'
import App from './App'
import 'echarts'
import '@/assets/js/china'
import '@/assets/css/common.css'

Vue.config.productionTip = false
Vue.component('v-chart', ECharts)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App)
})
