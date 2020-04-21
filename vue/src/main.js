// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import router from './router'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
import axios from 'axios'
import VueApexCharts from 'vue-apexcharts'

Vue.component('apexchart', VueApexCharts)

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
  }
});

Vue.config.productionTip = false

const vuetifyOptions = {}
Vue.use(Vuetify)
export default new Vuetify({
  icons: {
    iconfont: 'mdi'
  },
})

const ignoreWarnMessage = 'The .native modifier for v-on is only valid on components but it was used on <div>.';
Vue.config.warnHandler = function (msg, vm, trace) {
  // `trace` is the component hierarchy trace
  if (msg === ignoreWarnMessage) {
    msg = null;
    vm = null;
    trace = null;
  }
}

Vue.prototype.axiosInstance = axiosInstance

new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>',
  vuetify: new Vuetify(vuetifyOptions),
  render: h => h(App)
})
