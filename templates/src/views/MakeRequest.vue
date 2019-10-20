<template>
  <div>
        <Header startId="-1"/>
        <b-form class="container text-left mt-4 p-5 d-flex flex-column" id="form-wrapper" @submit="onSubmit" @submit.prevent="onSubmit">
            <h2 class="mb-3 align-self-center">Заполнение анкеты на участие в фестивале</h2>
            <p>Ваше ФИО</p>
            <b-form-group label="Фамилия:" label-for="surname">
                <b-form-input
                    id="surname"
                    type="text"
                    required
                    v-model="formData.first_name"
                ></b-form-input>
            </b-form-group>
            <b-form-group label="Имя:" label-for="name">
                <b-form-input
                    id="name"
                    type="text"
                    required
                    v-model="formData.middle_name"
                ></b-form-input>
            </b-form-group><b-form-group label="Отчетсво:" label-for="patronymic">
                <b-form-input
                    id="patronymic"
                    type="text"
                    required
                    v-model="formData.last_name"
                ></b-form-input>
            </b-form-group>
            <b-form-group label="Номер телефона:" label-for="tel">
                <b-form-input
                    id="tel"
                    type="text"
                    required
                    v-model="formData.phone_number"
                ></b-form-input>
            </b-form-group>
            <b-form-group label="Email:" label-for="email">
                <b-form-input
                    id="email"
                    type="email"
                    required
                    v-model="formData.email"
                ></b-form-input>
            </b-form-group>
            <b-form-group label="Ввыберите категорию" label-for="category"
                id="category"
                type="text"
                required
                placeholder="Ввыберите категорию"
            >
                <b-form-select :options="categoryOptions" v-model="formData.nomination">
                    <template v-slot:first>
                        <option :value="null" disabled>Выберите категрию</option>
                    </template>
                </b-form-select>
            </b-form-group>
            <b-form-group label="Адрес обьекта номинации:" label-for="address">
                <b-form-input
                    id="address"
                    type="text"
                    required
                    v-model="formData.adress"
                ></b-form-input>
            </b-form-group>
            <b-form-group label-for="addInfotextarea" label="Дополнительная информация">
                <b-form-textarea
                    id="addInfotextarea"
                    rows="3"
                    max-rows="6"
                    v-model="formData.additional_information"
                ></b-form-textarea>
            </b-form-group>
            <b-button type="submit" class="form-submit-btn align-self-center pt-2 pb-2 pl-5 pr-5 mt-3">Отправить заявку</b-button>
        </b-form>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import axios from 'axios'

export default {
    name: 'make-request',
    components: {
        Header
    },
    data() {
        return {
            categoryOptions: [
                {value: 0, text: 'Старый город'},
                {value: 1, text: 'Многоэтажки'},
                {value: 2, text: 'Самый зеленый двор'},
                {value: 3, text: 'Самый спортивный'},
                {value: 4, text: 'Лучший двор для детей'},
                {value: 5, text: 'Лучший стрит-арт'},
                {value: 6, text: 'Лучший подъезд'},
            ],
            formData: {             
                first_name: '',
                middle_name: '',
                last_name:'',
                email:'',
                phone_number: '',
                adress: '',
                additional_information: '',
                nomination: ''
            }
        }
    },
    methods: {
        onSubmit(e){
            let nomId = this.formData.nomination
            this.formData.nomination = Object.entries(this.categoryOptions)[0][1].text
            e.preventDefault()
            axios.post('/localhost:8000/form', {
                ...formData
            })
            .then(function (response) {
            })
            .catch(function (error) {
            });
        }
    }
}
</script>

<style>

</style>