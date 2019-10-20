<template>
    <header id="header-root">
        <b-nav class="d-flex justify-content-center" >
                <b-nav-item :active="currentActive==link.id?true:false" v-for="link in links" :key="link.id" :href="link.url" class="flex-fill text-center align-self-start" @click="changeActive(link.id)" >
                    {{link.text}}
                </b-nav-item>
        </b-nav>       
  
    </header>
    
</template>

<script>
export default {
    name: 'header',
    props:{
        startId: Number
    },
    data() {
        return {
            links:[
                {id:0, url:'/#mainDiv', text:'Главная'},
                {id:1, url:'/#yakor-rules', text:'Правила'},
                {id:2, url:'/#yakor-nominations', text:'Номинации'},
                {id:3, url:'/#yakor-about', text:'О нас'}
            ],
            currentActive:0
        }
    },
    methods: {
        changeActive(id){
            this.currentActive = id
        }
    },
    mounted(){
        this.currentActive=parseInt(this.startId)
    }
}
</script>
