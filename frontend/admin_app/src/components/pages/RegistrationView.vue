<script setup>
import RegistrationForm from "@/components/registration/RegistrationForm.vue"

const props = defineProps({
    sign_in: Boolean
});

</script>


<template>
  <div class="root">
    <div class="container"> 
      <trnasition name="fade" mode="out-in">
        <RegistrationForm :sign_in="sign_in" />
      </trnasition>
    </div>
  </div>
</template>


<style scoped lang="scss">
@import "@/scss/globals.scss";
.root {
  height: 100%;
  width: 100%;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  @include debug;
}

</style>

