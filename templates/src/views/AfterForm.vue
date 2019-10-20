<template>
  <div>

    <Header startId   ="-1"/>
      <b-form class="container text-left mt-4 p-5 d-flex flex-column" id="form-wrapper"  @submit="onSubmit" @submit.prevent="onSubmit">
            <h2>Здраствуйте, {{ formData.members }}</h2>
            <div>
                <b-form-group required label="Фотографии">
                    <b-form-file
                        required
                        v-model="formData.photo"
                        multiple
                    ></b-form-file>
                </b-form-group>
            </div>
            <div>
                <b-form-group required label="Дополнительная информация">
                    <b-form-input
                        required
                        type="text"
                        v-model="formData.info"
                    ></b-form-input>
                </b-form-group>
            </div>
            <b-button type="submit" class="form-submit-btn align-self-center pt-2 pb-2 pl-5 pr-5 mt-3">Отправить заявку</b-button>
        </b-form>
  </div>
</template>

<script>

import Header from '@/components/Header.vue'
import axios from 'axios'

export default {
    name: 'before-form',
    data() {
        return {
            formData: {
                photo: [],
                info: ''
            }
        }
    },
    mounted(){
        this.formData.members = location.href.split('/')[4]
    },
    methods: {
        onSubmit(e){
            e.preventDefault();
            axios.post('http://localhost:8000/form-after-create', {
                ...this.formData
            })
            .then(function (response) {
            })
            .catch(function (error) {
            });
        }
    },
    components: {
        Header
    }
}
</script>

<style>

</style>
