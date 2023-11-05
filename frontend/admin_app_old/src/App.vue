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
        <div class="frame_1"></div>
        <div class="content_1">
          <router-view class="full_height"></router-view>
        </div>
      </div>
  </body>

</template>

<style lang="scss">
@import "@/scss/_globals.scss";

* {
  padding: 0;
  margin: 0;
  border: 0;
}

*, *:before, *:after {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

:focus, :active {
  outline: none;
}

a:focus, a:active {
  outline: none;
}

nav, footer, header, aside {
  display: block;
}

html, body {
  height: 100%;
  width: 100%;
  font-size: 100%;
  line-height: 1;
  font-size: 14px;
  -ms-text-size-adjust: 100%;
  -moz-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}

input, button, textarea {
  font-family: inherit;
}

input::-ms-clear {
  display: none;
}

button {
  cursor: pointer;
}

button::-moz-focus-inner {
  padding: 0;
  border: 0;
}

a, a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: none;
}

ul li {
  list-style: none;
}

img {
  vertical-align: top;
}

h1, h2, h3, h4, h5, h6 {
  font-size: inherit;
  font-weight: 400;
}

html, body {
  height: 100vh;
}

.full_height {
  height: 100%;
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


.content_1 {
  position: absolute;
  z-index: 4;
  left: 45%;
}
.ball {
  position: absolute;
  border-radius: 1000px;
  background: linear-gradient(400deg, $background_4_color 15.43%, $background_1_color 83.66%);
  height: 150px;
  width: 150px;
  z-index: 3;
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
  filter:blur(2px);
  animation: 3s ease-in-out 1s infinite alternate swaying_2;
}
.ball:nth-child(3) {
  top: 10%;
  left: 10%;
  z-index: 0;
  transform: scale(1.6);
  filter:blur(4px);
}
.ball:nth-child(4) {
  top: 85%;
  left: 50%;
  z-index: 0;
  transform: scale(4);
  filter:blur(3px);
}

.frame_1 {
  position: absolute;
  top:55px;
  left:40px;
  height: 620px;
  width: 300px;
  filter: blur(2px);
  z-index: 1;
  border-style: solid;
  border-color: gray;
  border-color: $background_1_color;
  border-width: 6px;
  margin-left: 5%;
  box-shadow: -6px 6px 0px $background_4_color;
}

.statue {
  position: absolute;
  z-index: 2;
  height: 100%;
  width: 50%;
  margin-left: 5%;
  background-image: url("./images/statue.png");
  background-size: contain;
  background-repeat: no-repeat;
}

.main_background {
  position: relative;
  // background: linear-gradient(219.58deg, #4079AD 0.96%, #448199 24.18%, #498C80 82.85%, #4E9767 100%);
  background: linear-gradient(219.58deg, $background_1_color 0.96%, $background_2_color 24.18%, $background_3_color 82.85%, $background_4_color 100%);
  // background-image: url("./images/statue.png");
  height: 100vh;
  overflow: hidden;
  // display: flex;
  // justify-content: center;
  // align-items: center;
}

</style>
