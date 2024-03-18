<script setup></script>

<template>
  <main>
    <div id="header">
      <h1 class="AboutH1">Interactive Lighting</h1>
    </div>
    <div class="container text-center">
      <div class="row">
        <div class="col">
          <h1>Color Picker</h1>
          <input type="color" id="colorpicker" value="#ffa31a" />
        </div>
        <div class="col">
          <div class="vstack gap-3">
            <div class="p-2">
              <h1>On/Off</h1>
              <button type="button" id="buttononoff" @click="toggleLed()">
                <i class="fa-regular fa-lightbulb"></i>
              </button>
            </div>
            <div class="p-2">
              <h1>Brightness</h1>
              <input
                type="range"
                id="brightness"
                min="0"
                max="100"
                value="50"
              />
            </div>
            <div class="p-2">
              <h1>Random Effect</h1>
              <button type="button" class="buttonRandomEffect">
                Effect Color
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import axios from "axios";
export default {
  name: "EffectView",
  data() {
    return {
      state: false,
      effect: {},
    };
  },
  methods: {
    toggleLed() {
      this.state = !this.state; // Corrected syntax to toggle the state
      const payload = {
        on: this.state,
      };
      axios
        .post("http://localhost:3000/onof", payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
body {
  background-color: #000f2c;
  color: wheat;
  text-align: center;
  justify-content: center;
  background-image: url("../assets/Images/image.png");
  background-size: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-attachment: fixed;
}

main {
  height: 100%;
  width: 100%;
  padding: 2vh 0vh 2vh 0vh;
  margin: 2vh 0vh 2vh 0vh;
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 7px;
}

#header {
  width: 100%;
  margin: auto;
}

#colorpicker {
  height: 50vh;
  width: auto;
  border: none;
  background-color: transparent;
}
#colorpicker::-webkit-color-swatch {
  border-radius: 50%;
  border: none;
}

.vstack gap-3 {
  width: 100%;
}

#buttononoff {
  background-color: rgb(155, 208, 183);
  width: 50%;
  border-radius: 7px;
  font-size: x-large;
  border-radius: 50px;
}

#buttonRandomEffect{
  
}
</style>
