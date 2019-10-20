import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import MakeRequest from './views/MakeRequest.vue'
import Nominations from './views/Nominations.vue'
import BeforeForm from './views/BeforeForm.vue'
import AfterForm from './views/AfterForm.vue'

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
    },
    {
      path: '/nominations',
      name: 'nominations',
      component: Nominations
    },
    {
      path: '/before-form/:name',
      name: 'before-form',
      component: BeforeForm
    },
    {
      path: '/after-form/:name',
      name: 'after-form',
      component: AfterForm
    }
  ]
})
