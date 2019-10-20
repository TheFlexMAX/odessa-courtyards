<template>
  <div id="nominations-root" >
      <Header startId = "2" />
      <div class="mt-4" >
        <div v-for="nom in noms" :key="nom.id" :class="{'bg-grey':nom.id%2!=0, 'd-flex':true}" style="padding: 40px" :id="'y'+nom.id">
            <b-img :src="nom.imgSrc" class="nom-img"></b-img>
            <div class="d-flex flex-column ml-4">
                <h3>{{nom.title}}</h3>
                <p>{{nom.text}}</p>
                <b-button id="make-request" class="align-self-end" to="make-request">Подать заявку</b-button>
            </div>           
        </div>
      </div>
  </div>
</template>

<script>

import Header from '../components/Header'

export default {
    data() {
        return {
            noms: [
                {id: 0, title: 'lorem ipsum', text: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, repellat unde, molestiae soluta earum perferendis reiciendis ex, autem reprehenderit mollitia nulla iusto? Doloremque est cum architecto, saepe quibusdam reiciendis iure.',imgSrc: require('@/assets/images/art.png')},
                {id: 1, title: 'lorem', text: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, repellat unde, molestiae soluta earum perferendis reiciendis ex, autem reprehenderit mollitia nulla iusto? Doloremque est cum architecto, saepe quibusdam reiciendis iure.',imgSrc: require('@/assets/images/art.png')},
                {id: 2, title: 'lorem', text: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, repellat unde, molestiae soluta earum perferendis reiciendis ex, autem reprehenderit mollitia nulla iusto? Doloremque est cum architecto, saepe quibusdam reiciendis iure.',imgSrc: require('@/assets/images/art.png')},
                {id: 3, title: 'lorem', text: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, repellat unde, molestiae soluta earum perferendis reiciendis ex, autem reprehenderit mollitia nulla iusto? Doloremque est cum architecto, saepe quibusdam reiciendis iure.',imgSrc: require('@/assets/images/art.png')},
                {id: 4, title: 'lorem', text: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, repellat unde, molestiae soluta earum perferendis reiciendis ex, autem reprehenderit mollitia nulla iusto? Doloremque est cum architecto, saepe quibusdam reiciendis iure.',imgSrc: require('@/assets/images/art.png')},
                {id: 5, title: 'lorem', text: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, repellat unde, molestiae soluta earum perferendis reiciendis ex, autem reprehenderit mollitia nulla iusto? Doloremque est cum architecto, saepe quibusdam reiciendis iure.',imgSrc: require('@/assets/images/art.png')},
                {id: 6, title: 'lorem', text: 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dolore, repellat unde, molestiae soluta earum perferendis reiciendis ex, autem reprehenderit mollitia nulla iusto? Doloremque est cum architecto, saepe quibusdam reiciendis iure.',imgSrc: require('@/assets/images/art.png')},
            ]
        }
    },
    components: {
        Header
    }
}
</script>

<style>

</style>