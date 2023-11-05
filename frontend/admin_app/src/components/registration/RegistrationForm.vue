
<script setup>

import axios from 'axios';
import { ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const router = useRouter();
let input_email = ref('');
let input_password = ref('');

const props = defineProps({
    sign_in: Boolean
});

function validate_email() {
    return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(input_email)
}

function toggle_button() {

    console.log(props.sign_in);

    if (props.sign_in) {
        router.push({path: "sign_up"});
    } else {
        router.push({path: "sign_in"});
    }
}

function ok_button() {
    const url = "http://127.0.0.1:5000/ping";

    const data = {email: this.input_email, password: this.input_password};
    axios.get(url).then(
        (response) => {
            alert(response.data);
        }
    )
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
                <div class="content__item">
                    Админка для <b>TradeMatch</b><br><br>
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consectetur nisi non eos quisquam. Illo, a porro possimus, distinctio quasi dolorum, nesciunt quaerat ratione vero adipisci numquam magni. Labore, quia vel!
                </div>
            </div>
            <div class="bottom">
                <div @click="toggle_button()" class="bottom__item_left">{{ props.sign_in ? "sign up" : "sign in" }}</div>
                <div @click="ok_button()" class="bottom__item_right">OK</div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
@import "@/scss/_globals.scss";

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