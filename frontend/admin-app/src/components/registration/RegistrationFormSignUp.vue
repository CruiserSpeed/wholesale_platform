
<script>

export default {
    name: "RegistrationFormUp",
    data() {
        return {
        }
    },
    methods: {
        sign_in_button() {
            this.$router.push({path: "sign_in"});
        },
        ok_button() {
            alert("Заявка подана");
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
                    <input class="inner_content__input" type="email" placeholder="email">
                    <div class="inner_content__text">Password</div>
                    <input required class="inner_content__input"  type="password" placeholder="password">
                    <div class="inner_content__text">Password confirmation</div>
                    <input required class="inner_content__input"  type="password" placeholder="password">
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