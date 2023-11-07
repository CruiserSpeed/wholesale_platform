<script>
</script>

<template>
    <div class="root_homepage">
        <div class="container_2">
            <div class="navbar">
                <div class="navbar__user">
                </div>
                <div class="menu">
                    <div class="menu__item">statistics</div>
                    <div class="menu__item">admins</div>
                    <div class="menu__item">admins</div>
                    <div class="menu__item">admins</div>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped lang="scss">
@import "@/scss/globals.scss";
.root_homepage {
    height: 100vh;
    width: 100vw;
}

.container_2 {
    height: 100%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    z-index: 4;
    @include text_style(50px);
}

.navbar {
    display: flex;
    align-items: center;
    padding: 50px;
    position: fixed;
    width: 100%;
    height: 30px;
    background-color: $background_4_color;

    &__user {
        height: 70px;
        aspect-ratio: 1/1;
        border-radius: 100%;
        background-color: red;

    }

}

</style>