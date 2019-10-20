<template>
<div class="gallery-root container p-3 mt-3 w-50">
    <h3>{{title}}</h3>
    <div class="container"><b-img :src="mainImage" fluid style="width: 700px; height:400px"></b-img></div>
    
    <div class="row container p-2">
        <div v-for="img in images" :key="img.key" >
            <b-img :src="img.image" class="upimg" @click="changeImg(img.image)"></b-img>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'gallery',
    props: {
     images: Array,
     title: '',
    },
    data() {
        return {
            mainImage: this.images[0].image
        }
    },
    methods:{
        changeImg(newUrl){
            this.mainImage = newUrl
        }
    },
}
</script>

<style>

</style>