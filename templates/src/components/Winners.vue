<template>
  <div class="container">
    <div v-for="winner in winners" :key="winner.id" class="d-flex flex-column mb-5">

      <div class="d-flex justify-content-between">
        <span class="align-self-end">{{winner.adress}}</span>
        <h1 class="align-self-end">{{winner.category}}</h1>
      </div>
      <hr style="border:1px solid black" class="w-100">
      <h1>Описание планов</h1>
      <span class="mb-3">{{winner.planes}}</span>
      <h1>Описание результатов</h1>
      <span>{{winner.results}}</span>
      Фото до рекострукции
      <div v-for="img in winner.images" :key="img.id">
        <b-img :src="img.url"></b-img>
      </div>
    </div>
  </div>
</template>

<script>
import Header from '../components/Header.vue'
export default {
  components: {	},
  data() {
    return {
      winners:[
        {id: 0, 
        category:'Старый город', 
        adress: 'улица Марсельская 44',
         planes:'  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Temporibus facilis iste tempora vel. Repellendus rerum sunt, magnam molestiae assumenda natus, voluptate amet ipsa blanditiis error ab est, cum nihil! Impedit.', 
         results: '  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Temporibus facilis iste tempora vel. Repellendus rerum sunt, magnam molestiae assumenda natus, voluptate amet ipsa blanditiis error ab est, cum nihil! Impedit.', 
         images:[{url:require('@/assets/images/mrzl.png'), id:0},{url:require('@/assets/images/mrzl.png'), id:1},{url:require('@/assets/images/mrzl.png'), id:2}, ,{url:require('@/assets/images/mrzl.png'), id:3},{url:require('@/assets/images/mrzl.png'), id:4},{url:require('@/assets/images/mrzl.png'), id:5},{url:require('@/assets/images/mrzl.png'), id:6},]
        },
        {id: 1, 
        category:'Старый город', 
        adress: 'улица Марсельская 44',
         planes:'  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Temporibus facilis iste tempora vel. Repellendus rerum sunt, magnam molestiae assumenda natus, voluptate amet ipsa blanditiis error ab est, cum nihil! Impedit.', 
         results: '  Lorem ipsum dolor sit amet consectetur, adipisicing elit. Temporibus facilis iste tempora vel. Repellendus rerum sunt, magnam molestiae assumenda natus, voluptate amet ipsa blanditiis error ab est, cum nihil! Impedit.', 
         images:[{url:require('@/assets/images/mrzl.png'), id:0},{url:require('@/assets/images/mrzl.png'), id:1},{url:require('@/assets/images/mrzl.png'), id:2}, ,{url:require('@/assets/images/mrzl.png'), id:3},{url:require('@/assets/images/mrzl.png'), id:4},{url:require('@/assets/images/mrzl.png'), id:5},{url:require('@/assets/images/mrzl.png'), id:6},]
         },
      ]
    }
  },
}
</script>

<style>

</style>