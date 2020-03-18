import Vue from 'vue'
import Router from 'vue-router'
import Auth from '@/components/Auth'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: Auth
    }
  ]
})
