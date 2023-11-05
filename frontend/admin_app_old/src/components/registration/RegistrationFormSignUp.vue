
<script>

export default {
    name: "RegistrationFormUp",
    data() {
        return {
            input_email: "",
            input_password: "",
            input_confirmation: ""
        }
    },
    methods: {
        sign_in_button() {
            this.$router.push({path: "sign_in"});
        },
        validate_email() {
            if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.input_email)) {
                return true;
            }
            return false;
        },
        ok_button() {
            const url = "http://127.0.0.1:5000/sign_up";

            if (!this.validate_email(this.input_email)) {
                alert("Please, correct your email");
                return;
            }
            if (this.input_password.length < 5) {
                alert("Password must contains at least 5 symbols");
                return;
            }
            if (this.input_confirmation != this.input_password) {
                alert("Passwords doesnt match");
                return;
            }
            const data = {email: this.input_email, password: this.input_password};
            fetch(url, {
                method: "POST",
                body: JSON.stringify(data),
            });
            this.$router.push({path: "sign_in"});
        }
    }
}
</script>

<template>

    <div class="root">
        <div class="container">
            <div class="header">
                <div class="header__item">Sign up</div>
            </div>
            <div class="content">
                <div class="inner_content">
                    <div class="inner_content__text">Email</div>
                    <input class="inner_content__input" type="email" placeholder="email" v-model="input_email">
                    <div class="inner_content__text">Password</div>
                    <input required class="inner_content__input"  type="password" placeholder="password" v-model="input_password">
                    <div class="inner_content__text">Password confirmation</div>
                    <input required class="inner_content__input"  type="password" placeholder="password" v-model="input_confirmation">
                </div>
                <div class="content__item">
                    Админка для TradeMatch<br><br>
                    После регистрации дождитесь, пока админ подвердит вашу заявку. Подтверждение придет на указанную почту
                </div>
            </div>
            <div class="bottom">
                <div @click="sign_in_button()" class="bottom__item_left">Sign in</div>
                <div @click="ok_button()" class="bottom__item_right">OK</div>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
@import "@/scss/_globals.scss";

.container {
    width: 700px;
    height: 500px;

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
    justify-content: center;
    flex-direction: column;
    height: 100%;
    width: 100%;
    padding-left: 30px;
    padding-right: 30px;

    &__text {
        @include text_style(25px);
    }
    &__input {
        margin-top: 10px;
        margin-bottom: 20px;
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


</style> //