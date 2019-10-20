<template>
  <div>
      <Header startId   ="-1"/>
      <b-form class="container text-left mt-4 p-5 d-flex flex-column" id="form-wrapper"  @submit="onSubmit" @submit.prevent="onSubmit">
            <h2>Здраствуйте, {{ formData.members }}</h2>
            <div>
                <b-form-group required label="Описание проблемы">
                    <b-form-textarea
                        rows="3"
                        max-rows="6"
                        v-model="formData.problem_description"
                    ></b-form-textarea>
                </b-form-group>
            </div>
            <div>
                <b-form-group required label="План решения">
                    <b-form-input
                        required
                        type="text"
                        v-model="formData.plan_description"
                    ></b-form-input>
                </b-form-group>  
            </div>  
            <div>
                <b-form-group required label="Главное фото">
                    <b-form-file
                        required
                        type="text"
                        v-model="formData.general_view"
                    ></b-form-file>
                </b-form-group>
            </div>
            <div>

                <b-form-group required label="Фотографии">
                    <b-form-file
                        required
                        type="text"
                        v-model="formData.photo"
                        multiple
                    ></b-form-file>
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
                problem_description: '',
                members: '',
                plan_description: '',
                general_view: null,
                photo: []
            }
        }
    },
    mounted(){
        this.formData.members = location.href.split('/')[4]
    },
    methods: {  
        onSubmit(e){
            e.preventDefault();
            axios.post('http://localhost:8000/', {
                ...formData
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