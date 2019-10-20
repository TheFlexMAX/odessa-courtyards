<template>
  <div class="pb-3">
      <Header startId="-1"/>
      <div class="d-flex">
        <Gallery :images="imagesBefore" title="До реконструкуии" />
        <Gallery :images="imagesBefore" title="После реконструкуии" />
      </div>
      <div style="background:lightgrey">
        <div class="container">
            <h1>{{problems.title}}</h1>
            <p>{{problems.text}}</p>
        </div>
      </div>
      <div>
        <div class="container" >
            <h1>{{solitions.title}}</h1>
            <p>{{solitions.text}}</p>
        </div>
      </div>
      <div style="background:lightgrey">
          <div class="container">
              <h1>Шкала оценивания</h1>
                <label for="formControlRange">{{mark}}</label>
                <input type="range" class="form-control-range" id="formControlRange" v-model="mark">
          </div>
      </div>
      <div class="container d-flex justify-content-between mt-4">
          <b-button class="voting-btn">Предыдущий участник</b-button>
          <b-button class="voting-btn">Оценить участника</b-button>
          <b-button class="voting-btn">Следующий участник</b-button>
      </div>
  </div>
</template>

<script>
import Header from '../components/Header.vue'
import Gallery from '../components/Gallery.vue'

export default {
    name: 'voting',
    components: {
        Header, Gallery
    },
    data() {
        return {
            imagesBefore:[
                {id: 0, image:require('@/assets/images/mrzl.png')},
                {id: 1, image:require('@/assets/images/mnogoet.png')},
                {id: 2, image:require('@/assets/images/green.png')},
                {id: 3, image:require('@/assets/images/sport.png')},
                {id: 4, image:require('@/assets/images/child.png')},
                {id: 5, image:require('@/assets/images/art.png')},
                {id: 6, image:require('@/assets/images/pd.png')},
            ],
            imagesAfter: [

            ],
            problems:{
                title: 'Проблемы обьекта и планы на реконструкцию',
                text: ' Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis sit laudantium ab itaque molestias assumenda temporibus maiores in provident, molestiae ut vero corrupti. Sequi doloremque dignissimos atque officiis illum facilis?'
            },
            solitions:{
                title: 'Описание результатов реконструкции',
                text: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis sit laudantium ab itaque molestias assumenda temporibus maiores in provident, molestiae ut vero corrupti. Sequi doloremque dignissimos atque officiis illum facilis?'
            },
            mark: 50
        }
    },
}
</script>

<style>

</style>