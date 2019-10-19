<template>
  <div class="nomination p-3 container d-flex flex-column justify-content-center align-items-center">
    <b-img :src="imageSrc" class="nomination-image"/>
    <hr>
    <span class="text-center">{{ name }}</span>
  </div>
</template>

<script>
export default {
    data() {
        return {
        }
    },
    props: {
        name: String,
        image: String
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