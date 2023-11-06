
<script setup>

import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useGlobalsStore } from '@/stores/GlobalsStore.js';

const router = useRouter();
const globals_store = useGlobalsStore();
let input_email = ref('');
let input_password = ref('');
let input_confirmation = ref('');

const props = defineProps({
    sign_in: Boolean
});

function validate_email(email) {
    return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email)
}

function validate_password(password) {
    if (password.length < 5) {
        return false;
    }
    return true;
}

function sign_button() {
    if (props.sign_in) {
        router.push({path: "sign_up"});
    } else {
        router.push({path: "sign_in"});
    }
}


function ok_button() {
    const url = props.sign_in ? globals_store.registration_sign_in_url : globals_store.registration_sign_up_url;
    const email = input_email.value;
    const password = input_password.value;
    const confirmation = input_confirmation.value;

    if (email.length === 0 || password.length === 0) {
        alert("Поля не долдны быть пустыми");
        return;
    }

    if (!validate_email(email)) {
        alert(`Проверьте корректность email ${email}`);
        return;
    }
    if (!props.sign_in) {
        if (!validate_password(password)) {
            alert("Ненадежный пароль");
            return;
        }

        if (password !== confirmation) {
            alert("Пароли не совпадают");
            return;
        }
    }

    const data = {email: email, password: password};
    if (props.sign_in) {
        axios.post(url, data).then(
            (response) => {
                const result = response.data[globals_store.JF_RESULT];
                if (result === globals_store.JV_SUCCESS) {
                    router.push({path: "homepage"});
                } else if (result === globals_store.JV_INVALID_CREDENTIALS) {
                    alert("Данные не верны");
                } else if (result === globals_store.JV_ADMIN_NOT_CONFIRMED) {
                    alert("Дождитесь, пока вашу заявку подтвердят");
                } else if (result === globals_store.JV_ADMIN_REFUSED) {
                    alert("Вашу заявку отклонили");
                } else if (result === globals_store.JV_EMAIL_NOT_CONFIRMED) {
                    alert("Подтвердите вашу почту");
                } else {
                    alert("Что-то пошло не так");
                }
            }
        )
    } else {
        axios.post(url, data).then(
            (response) => {
                const result = response.data[globals_store.JF_RESULT];
                if (result === globals_store.JV_SUCCESS) {
                    alert("Ваша заявка рассматривается");
                } else if (result === globals_store.JV_ALREADY_EXISTS) {
                    alert("Вы уже отправили заявку");
                } else {
                    alert("Что-то пошло не так");
                }
            }
        )

    }
}

</script>

<template>

    <div class="root">
        <div class="container">
            <div class="header">
                <div class="header__item">{{ props.sign_in ? "Sign in" : "Sign up" }}</div>
            </div>
            <div class="content">
                <div class="inner_content">
                    <div class="input_with_lable">
                        <div class="input_with_lable__lable">Email</div>
                        <input class="input_with_lable__input" type="email" placeholder="email" v-model="input_email">
                    </div>

                    <div class="input_with_lable">
                        <div class="input_with_lable__lable">Password</div>
                        <input required class="input_with_lable__input"  type="password" placeholder="password" v-model="input_password">
                    </div>

                    <div v-if="!props.sign_in" class="input_with_lable">
                        <div class="input_with_lable__lable">Confirmation</div>
                        <input required class="input_with_lable__input"  type="password" placeholder="password" v-model="input_confirmation">
                    </div>
                </div>
                <div v-if="props.sign_in" class="content__item">
                    Админка для TradeMatch<br><br>
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consectetur nisi non eos quisquam. Illo, a porro possimus, distinctio quasi dolorum, nesciunt quaerat ratione vero adipisci numquam magni. Labore, quia vel!
                </div>
                <div v-else class="content__item">
                    Введите свои данные и дождитесь, пока вашу заявку подтвердят. Уведомление придет на указанную почту
                </div>
            </div>
            <div class="bottom">
                <div @click="sign_button()" class="bottom__item_left">{{ props.sign_in ? "sign up" : "sign in" }}</div>
                <div @click="ok_button()" class="bottom__item_right">OK</div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
@import "@/scss/globals.scss";

.root {
}
.container {
    height: 500px;
    min-width: 400px;

    display: flex;
    flex-direction: column;
    align-items: center;
}


.header {
    @include glass_panel();
    display: flex;
    align-items: center;
    justify-content: center;
    height: 150px;
    width: 100%;
    border-radius: 30px 30px 0px 0px;

    &__item {
        @include text_style(55px);
    }
}

.content {
    display: flex;
    height: 100%;
    width: 100%;
    @include glass_panel();
    border-radius: 0px 0px 0px 0px;
    margin-top: 8px;
    padding-top: 15px;
    padding-bottom: 15px;

    &__item {
        @include text_style(20px);
        padding-top: 50px;
        margin-left: 20px;
        margin-right: 20px;
        height: 100%;
        width: 500px;
    }
}
.inner_content {
    display: flex;
    align-items: start;
    justify-content: space-around;
    flex-direction: column;
    height: 100%;
    width: 100%;
    padding-left: 30px;
    padding-right: 30px;
}

.input_with_lable {
    width: 100%;

    &__lable {
        @include text_style(25px);
        text-align: left;
    }
    &__input {
        @include text_style(15px);
        padding: 10px;
        border-radius: 6px;
        background-color: $cyan_color;
        width: 100%;
    }
    &__input::placeholder {
        @include text_style(15px, $lightblue_color);
    }

}
.bottom {
    margin-top: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 80px;
    width: 100%;

    &__item_left {
        @include glass_panel();
        height: 100%;
        width: 100%;
        margin-right: 4px;
        border-radius: 0px 0px 0px 30px;

        display: flex;
        justify-content: center;
        align-items: center;
        @include text_style();

        &:hover {
            transform: scale(1.01);
        }
    }
    &__item_right {
        @include glass_panel();
        height: 100%;
        width: 100%;
        margin-left: 4px;
        border-radius: 0px 0px 30px 0px;

        display: flex;
        justify-content: center;
        align-items: center;
        @include text_style();

        &:hover {
            transform: scale(1.01);
        }
    }
}

@media (max-width: 800px) {
    .content__item {
        display: none;
    }
}

</style>