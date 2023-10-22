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
        <router-view class="full_height"></router-view>
      </div>
  </body>

</template>

<style lang="scss">
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
    transform: translateY(0px) scale(1);
  }
  to {
    transform: translateY(20px) scale(1);
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
  background: linear-gradient(400deg, #386376 15.43%, #5DA37E 83.66%);
  height: 250px;
  width: 250px;
}
.ball:nth-child(1) {
  top: 50%;
  left: 60%;
  animation: 3s ease-in-out 1s infinite alternate swaying_1;
}
.ball:nth-child(2) {
  top: 15%;
  left: 15%;
  filter:blur(3px);
  animation: 3s ease-in-out 1s infinite alternate swaying_2;
}
.ball:nth-child(3) {
  top: 10%;
  left: 80%;
  transform: scale(0.4);
  filter:blur(7px);
}

.main_background {
  background: linear-gradient(219.58deg, #4079AD 0.96%, #448199 24.18%, #498C80 82.85%, #4E9767 100%);
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>
