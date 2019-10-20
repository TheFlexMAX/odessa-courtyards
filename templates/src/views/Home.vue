<template>
  <div class="home-root">
    <div :style="{'background':'url('+require('@/assets/images/main.png')+')','background-size':'cover'}" id="mainDiv" class="d-inline-flex align-items-center flex-column justify-content-center">
      <div id="title" class="m-4  text-uppercase">{{title}}</div>
      <div id="text" class="container align-center m-4" >{{text}}</div>
      <div class="align-items-center m-4">
        <div id="btn-wrapper">
          <b-button id="make-request-btn" to="/make-request">Подать заявку</b-button>
        </div>
      </div>  
    </div>
    <Header :startId="0" />
    <div style="height:10vh" id="yakor-rules"></div>
    <div id="rules" class="container text-center" v-if="stage=='start'">
      <h1 class="mb-4">Правила</h1>
      <p class="alert alert-danger">
        Предупреждение! Перед участием в конкурсе нужно убедиться, что все планы по реконструкции будут одобрены на законодательном уровне, во избежании неприятных ситуаций на этапе реконструкции. 
      </p>
      <ol>
        <li v-for="rule in rules" :key="rule.id" class="text-justify mt-4">
          {{rule.text}}
        </li>
      </ol>
    </div>
    <div>
    <Winners v-if="stage=='finished'" />
    </div>
    <div id="nominations" class="container">
      <div style="height:10vh" id="yakor-nominations"></div>
      <h1 class="text-center">Номинации</h1>
      <div class="row">
        <div v-for="nomination in nominations" :key="nomination.id" class="col-4">
        <Nomination :name="nomination.text" :image="nomination.image" :id="nomination.id" />
      </div>
    </div>
    </div>
    <div style="height:10vh" id="yakor-about"></div>
    <div id="about" class="container d-flex flex-column justify-content-center align-items-center">
      <h1 class="text-center mb-4">О нас</h1>
      <div class="text-center">
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt ut placeat officia assumenda eligendi eos reprehenderit magni. Tempora earum odio nesciunt, perspiciatis rerum at, cupiditate quis aut harum eaque modi.
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt ut placeat officia assumenda eligendi eos reprehenderit magni. Tempora earum odio nesciunt, perspiciatis rerum at, cupiditate quis aut harum eaque modi.
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nesciunt ut placeat officia assumenda eligendi eos reprehenderit magni. Tempora earum odio nesciunt, perspiciatis rerum at, cupiditate quis aut harum eaque modi.
      </div>
    </div>
  </div>
</template>

<script>

import Header from '@/components/Header.vue'
import Nomination from '@/components/Nomination.vue'
import Winners from '@/components/Winners'

export default {
  name: 'home',
  data() {
    return {
      title: 'дворики одессы',
      text: 'Ежегодный конкурсный проект среди одесских дворов, которые своими силами украшают их жители. Чтобы подать заявку на участие в конкурсе, присылается фото двора до благоустройства/реконструкции/ремонта, а затем после проделанной работы вместе с кратким описанием всех усовершенствований',
      rules: [
        {text: 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et distinctio veritatis repudiandae, perspiciatis commodi id eius libero ab porro similique ipsum vero eos minus omnis dolores perferendis non aut! A?', id:0},
        {text: 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et distinctio veritatis repudiandae, perspiciatis commodi id eius libero ab porro similique ipsum vero eos minus omnis dolores perferendis non aut! A?', id:1},
        {text: 'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Et distinctio veritatis repudiandae, perspiciatis commodi id eius libero ab porro similique ipsum vero eos minus omnis dolores perferendis non aut! A?', id:2}
      ],
      nominations: [
        { id: 0, image:'mrzl.png', text: 'Старый город' },
        { id: 1, image:'mnogoet.png', text: 'Многоэтажки' },
        { id: 2, image:'green.png', text: 'Самый зеленый двор' },
        { id: 3, image:'sport.png', text: 'Самый спортивнй двор' },
        { id: 4, image:'child.png', text: 'Лучший детский двор' },
        { id: 5, image:'art.png', text: 'Лучший стрит арт' },
        { id: 6, image:'pd.png', text: 'Лучший подьезд' },
      ],
      stage: 'start',//in-progress, //finished //
    }
  },
  components: {
    Header,
    Nomination,
    Winners
  }
}
</script>
