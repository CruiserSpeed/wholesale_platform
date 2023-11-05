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
        <div class="ball"></div>
        <div class="ball"></div>
        <div class="ball"></div>
        <div class="ball"></div>
        <div class="statue"></div>
        <div class="frame"></div>
      </div>
      <div class="container">
        <router-view></router-view>
      </div>
  </body>

</template>


<style scoped lang="scss">
@import "@/scss/_globals.scss";

// background
.main_background {
  position: absolute;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  overflow: hidden;

  background: linear-gradient(219.58deg, $background_1_color 0.96%, $background_2_color 24.18%, $background_3_color 82.85%, $background_4_color 100%);
}

@keyframes swaying_1 {
  from {
    transform: translateY(0px) scale(1.3);
  }
  to {
    transform: translateY(20px) scale(1.3);
  }
}
@keyframes swaying_2 {
  from {
    transform: translateY(15px) scale(0.8);
  }
  to {
    transform: translateY(0px) scale(0.8);
  }
}


.ball {
  position: absolute;
  border-radius: 1000px;
  background: linear-gradient(400deg, $background_4_color 15.43%, $background_1_color 83.66%);
  height: 150px;
  width: 150px;
}
.ball:nth-child(1) {
  top: 10%;
  left: 75%;
  animation: 3s ease-in-out 1s infinite alternate swaying_1;
  filter:blur(3px);
}
.ball:nth-child(2) {
  top: 50%;
  left: 18%;
  z-index: 4;
  animation: 3s ease-in-out 1s infinite alternate swaying_2;
  filter:blur(2px);
}
.ball:nth-child(3) {
  top: 10%;
  left: 10%;
  z-index: 1;
  transform: scale(1.6);
  filter:blur(4px);
}
.ball:nth-child(4) {
  top: 85%;
  left: 50%;
  z-index: 1;
  transform: scale(4);
  filter:blur(3px);
}

.frame {
  position: absolute;
  height: 80%;
  width: 330px;
  left: 10%;
  top: 10%;
  filter: blur(2px);
  z-index: 2;
  border-style: solid;
  border-color: $background_1_color;
  border-width: 6px;
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
