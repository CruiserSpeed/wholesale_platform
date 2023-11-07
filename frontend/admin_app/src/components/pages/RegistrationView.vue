<script setup>
import RegistrationForm from "@/components/registration/RegistrationForm.vue"

const props = defineProps({
    sign_in: Boolean
});

</script>


<template>
  <div class="root_registration_view">
    <div class="container_2">
      <RegistrationForm :sign_in="sign_in" />
    </div>
  </div>
</template>


<style scoped lang="scss">
@import "@/scss/globals.scss";
.root_registration_view {
  height: 100%;
  width: 100%;
}
.container_2 {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  margin-left: 45%;
  width: 40%;
  height: 100%;
  @include debug;
}

@media (max-width: 1200px) {

  .container_2 {
    margin-left: 30%;
  }
}

</style>

