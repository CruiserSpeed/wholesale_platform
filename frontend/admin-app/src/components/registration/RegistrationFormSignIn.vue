
<script>

export default {
    name: "RegistrationFormIn",
    data() {
        return {
        }
    },
    methods: {
        sign_up_button() {
            this.$router.push({path: "sign_up"});
        },
        ok_button() {
            this.$router.push({path: "/"});
        }
    }
}
</script>

<template>

    <div class="root">
        <div class="container">
            <div class="header">
                <div class="header__item">Sign in</div>
            </div>
            <div class="content">
                <div class="inner_content">
                    <div class="inner_content__text">Email</div>
                    <input class="inner_content__input" type="email" placeholder="email">
                    <div class="inner_content__text">Password</div>
                    <input required class="inner_content__input"  type="password" placeholder="password">
                </div>
                <div class="content__item">
                    Админка для TradeMatch
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consectetur nisi non eos quisquam. Illo, a porro possimus, distinctio quasi dolorum, nesciunt quaerat ratione vero adipisci numquam magni. Labore, quia vel!
                </div>
            </div>
            <div class="bottom">
                <div @click="sign_up_button()" class="bottom__item_left">Sign up</div>
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
        margin-bottom: 40px;
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