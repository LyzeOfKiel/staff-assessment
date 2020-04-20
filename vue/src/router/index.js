import Vue from 'vue'
import Router from 'vue-router'
import Auth from '@/components/Auth'
import DefaultFeedbackForm from '@/components/DefaultFeedbackForm'
import Stats from "@/components/Stats";
import Main from '@/components/Main'
import Login from "../components/Login";
import Survey from "../components/Survey";
// import Courses from '@components/Courses';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/main',
      name: 'main',
      component: Main,
      children: [
        {
          path: 'survey/:course/:type',
          name: 'survey',
          component: Survey,
          props: true
        },
        {
          path: '/stats',
          name: 'stats',
          component: Stats
        },
      ]
    }
  ]
})
