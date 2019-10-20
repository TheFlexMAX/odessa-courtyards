import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import MakeRequest from './views/MakeRequest.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/make-request',
      name: 'make-request',
      component: MakeRequest
    }
  ]
})
