<template>
  <div class="nomination p-3 container d-flex flex-column justify-content-center align-items-center">
    <b-img :src="imageSrc" class="nomination-image"/>
    <hr>
    <a :href="'/nominations#y'+id" class="text-center">{{ name }}</a>
  </div>
</template>

<script>
export default {
    name: 'nomination',
    data() {
        return {
        }
    },
    props: {
        name: String,
        image: String,
        id: Number
    },
    computed:{
        imageSrc(){
            const imageSrc = require('@/assets/images/'+this.image);
            return imageSrc
        }
        
    }
}
</script>

<style>

</style>