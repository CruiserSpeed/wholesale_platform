<script setup>
</script>

<template>
  <head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Gabarito&family=Montserrat&display=swap" rel="stylesheet">
  </head>
  <body>
      <div class="main_background">
        <div v-for="_ in 4" class="ball"></div>
        <div class="statue"></div>
        <div class="frame"></div>
      </div>
      <div class="container">
        <router-view></router-view>
      </div>
  </body>

</template>


<style scoped lang="scss">
@import "@/scss/globals.scss";

// background
.main_background {
  position: absolute;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  overflow: hidden;

  background: linear-gradient(219.58deg, $background_1_color 0.96%, $background_2_color 24.18%, $background_3_color 82.85%, $background_4_color 100%);
}

@keyframes swaying {
  from {
    translate: 0px 0px;
  }
  to {
    translate: 0px 20px;
  }
}


.ball {
  position: absolute;
  border-radius: 100%;
  background: linear-gradient(40deg, $background_4_color 15%, $background_1_color 85%);
  height: 150px;
  aspect-ratio: 1/1; 
}
.ball:nth-child(1) {
  top: 10%;
  right: 25%;
  scale: 1.3;
  animation: 4s ease-in-out 0s infinite alternate swaying;
  filter: blur(3px);
}
.ball:nth-child(2) {
  top: 50%;
  left: 18%;
  z-index: 4;
  scale: 0.8;
  animation: 3s ease-in-out -1.5s infinite alternate swaying;
  filter: blur(2px);
}
.ball:nth-child(3) {
  top: 10%;
  left: 10%;
  z-index: 1;
  scale: 1.6;
  filter: blur(4px);
}
.ball:nth-child(4) {
  bottom: 15%;
  left: 50%;
  z-index: 1;
  scale: 4;
  filter: blur(3px);
}

.frame {
  position: absolute;
  height: 80%;
  aspect-ratio: 1/2;
  left: 10%;
  top: 10%;
  filter: blur(2px);
  z-index: 2;
  border: 6px solid $background_1_color;
  box-shadow: -6px 6px 0px $background_4_color;
}

.statue {
  position: absolute;
  height: 100%;
  width: auto;
  left: 7%;

  z-index: 3;
  content: url("./assets/statue.png");
  @include debug();
}

.container {
  position: absolute;
  overflow: hidden;
  width: 60%;
  left: 40%;
  height: 100vh;
  z-index: 4;
  @include debug();
}
@media (max-width: 1200px) {
  .container {
    width: 100%;
    left:0%;
  }

  .statue {
    display: none;
  }
  .frame {
    display: none;
  }
}


</style>
