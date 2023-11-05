<script setup>
import RegistrationFormSignIn from "@/components/registration/RegistrationFormSignIn.vue"
</script>


<template>
  <div class="container"> 
    <trnasition name="fade" mode="out-in">
    <RegistrationFormSignIn />
    </trnasition>
  </div>
</template>


<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100vh;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s;

}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;

}

</style>

