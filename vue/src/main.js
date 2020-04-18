// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import router from './router'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'
import axios from 'axios'

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


Vue.prototype.axiosInstance = axiosInstance

new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>',
  vuetify: new Vuetify(vuetifyOptions),
  render: h => h(App)
})
