import Vue from 'vue'
import Router from 'vue-router'
import Auth from '@/components/Auth'
import DefaultFeedbackForm from '@/components/DefaultFeedbackForm'
import FeedbackStatistics from '@/components/FeedbackStatistics'
import Main from '@/components/Main'
import Login from "../components/Login";

Vue.use(Router)

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
      path: '/feedback/:course_id',
      name: 'dff',
      component: DefaultFeedbackForm,
      props: true
    },
    {
      path: '/stats',
      name: 'stats',
      component: FeedbackStatistics
    },
    {
      path: '/main',
      name: 'main',
      component: Main
    }
  ]
})
