import Vue from 'vue'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import Home from '../views/Home.vue'
import Nomination from '../views/Nomination.vue'
import Members from '../views/Members.vue'
import Member from '../views/Member.vue'
import Results from '../views/Results.vue'
import Result from '../views/Result.vue'

Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [
  {
    // Главная страница
    path: '/',
    name: 'home',
    component: Home
  },
  {
    // Станица для каждой номинации
    path: '/nomination/:name',
    name: 'nomination',
    component: Nomination
  },
  {
    // Страница со списком участников
    path: '/members',
    name: 'members',
    component: Members
  },
  {
    // Страница отдельного участника
    path: '/members/:name',
    name: 'member',
    component: Member
  },
  {
    // Страница результатов конкурса(вердикт жюри)
    path: '/results',
    name: 'results',
    component: Results
  },
  {
    // Страница отдельного результат
    path: '/results/:name',
    name: 'result',
    component: Result
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
