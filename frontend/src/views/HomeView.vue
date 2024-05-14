<script setup>
import { RouterLink, RouterView } from "vue-router";

// Load environment variables
import dotenv from "dotenv";

// Access backend URL
//const backendUrl = process.env.VUE_APP_BACKEND_URL;
//console.log("Backend URL:", backendUrl);
</script>

<template>
  <main>
    <h1 class="H1Style">Interactive Lighting</h1>
    <!-- Leds -->
    <div class="leds">
      <!-- ColorSettings -->
      <div class="ledControls" id="colorSettings">
        <h2 class="grid-item-colorSettings" id="titelColor">Color</h2>
        <!-- Colorpicker -->
        <!-- <div class="grid-item-colorSettings" id="colorpickerdiv"> -->
        <input
          type="color"
          class="grid-item-colorSettings"
          id="colorpicker"
          value="#ffa31a"
          @input="UpdateColorValue()"
        />
        <!-- </div> -->
        <!-- primary color buttons -->
        <div class="grid-item-colorSettings">
          <button
            class="primary-color-btn"
            id="primary-btn-red"
            @click="ChangeColorValue('#ff0000')"
          >
            Red
          </button>
        </div>
        <div class="grid-item-colorSettings">
          <button
            class="primary-color-btn"
            id="primary-btn-blue"
            @click="ChangeColorValue('#0000ff')"
          >
            Blue
          </button>
        </div>
        <div class="grid-item-colorSettings">
          <button
            class="primary-color-btn"
            id="primary-btn-green"
            @click="ChangeColorValue('#00ff00')"
          >
            Green
          </button>
        </div>
        <div class="grid-item-colorSettings">
          <button
            class="primary-color-btn"
            id="primary-btn-white"
            @click="ChangeColorValue('#ffffff')"
          >
            White
          </button>
        </div>
      </div>
      <!-- LedSettings -->
      <div class="ledControls" id="ledSettings">
        <h2 class="grid-item-ledControls" id="titelLedSettings">
          Led Settings
        </h2>
        <div class="grid-item-ledControls" id="onOffDiv">
          <h2>On/Off</h2>
          <button
            type="button"
            class="btnLedSettings"
            id="onOffbtn"
            @click="toggleLed()"
          >
            <i id="OnOffIcon" style="font-size: 24px" class="fa">&#xf011;</i>
          </button>
        </div>
        <div class="grid-item-ledControls" id="brightnessDiv">
          <h2>Brightness</h2>
          <input
            type="range"
            id="brightness"
            min="0"
            max="255"
            value="50"
            @input="getBrightnessValue()"
          />
        </div>
        <div class="grid-item-ledControls" id="speedDiv">
          <h2>Speed</h2>
          <input
            type="range"
            id="speed"
            min="0"
            max="255"
            value="50"
            @input="getSpeedValue()"
          />
        </div>
        <div class="grid-item-ledControls" id="randomEffectDiv">
          <h2>Random Effect</h2>
          <br />
          <button
            type="button"
            class="btnLedSettings"
            id="randomEffectbtn"
            @click="setRandomEffect()"
          >
            <i class="gg-dice-6"></i>
          </button>
        </div>
        <br />
      </div>
    </div>
  </main>
  <footer>
    <div class="footer-content">
      <div class="footer-section contact">
        <h2>Contact Us</h2>
        <ul>
          <li>
            <a
              id="footerLink"
              href="https://github.com/vives-project-xp/InteractiveLighting"
              ><i class="fa-brands fa-github"></i> Github</a
            >
          </li>
          <li>
            <i class="fa-solid fa-compass"></i> Vives Brugge Xaverianenstraat
          </li>
        </ul>
      </div>
    </div>
  </footer>
</template>

<script>
import axios from "axios";
export default {
  name: "EffectView",
  data() {
    return {
      backendUrl: import.meta.env.VITE_BACKEND_URL,
      // backendUrl: "localhost:3000",
      state: false,
      effect: {},
    };
  },
  methods: {
    UpdateColorValue() {
      const color = document.getElementById("colorpicker").value;
      const payload = {
        color: color,
      };
      console.log(payload);
      axios
        .post(`${this.backendUrl}/color`, payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    setRandomEffect() {
      axios
        .post(`${this.backendUrl}/random`
        )
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getBrightnessValue() {
      const brightness = document.getElementById("brightness").value;
      const payload = {
        brightness: parseInt(brightness),
      };
      axios
        .post(`${this.backendUrl}/brightness`, payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    getSpeedValue() {
      const brightness = document.getElementById("speed").value;
      const payload = {
        brightness: parseInt(brightness),
      };
      axios
        .post(`${this.backendUrl}/brightness`, payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    toggleLed() {
      this.state = !this.state; // Corrected syntax to toggle the state
      const payload = {
        on: this.state,
      };
      axios
        .post(`${this.backendUrl}/onof`, payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    ChangeColorValue(color) {
      this.updateColorPickerValue(color); // Update color picker value
      const payload = {
        color: color,
      };
      axios
        .post(`${this.backendUrl}/color`, payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateColorPickerValue(color) {
      document.getElementById("colorpicker").value = color;
    },
  },
};
import { onMounted } from "vue";
onMounted(() => {
  methods.getEffectList();
});
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
  font-size: 1vh;
}

main {
  height: 75%;
  width: 100%;
  padding: 2vh 0vh 2vh 0vh;
  margin: 2vh 0vh 2vh 0vh;
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 7px;
}

footer {
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 7px;
  padding: 5px;
}

.footer-section ul {
  list-style: none;
  color: wheat;
  display: flex;
  justify-content: center;
  font-size: medium;
}

.footer-section ul li {
  color: wheat;
  margin-right: 1vw;
}

#footerLink {
  color: wheat;
}

.leds {
  display: flex;
  justify-content: center;
  align-items: center;
}

.ledControls {
  width: 50%;
  height: 55vh;
  justify-content: center;
  align-items: center;
  padding: 0.5%;
}

#colorSettings {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(5, 1fr);
  gap: 5px;
  justify-content: center;
  align-items: center;
  margin-right: 2%;
}

#titelColor {
  grid-area: span 1 / span 4;
}

.grid-item-colorSettings {
  width: 100%;
  height: 100%;
  background-color: transparent;
  justify-content: center;
  align-items: center;
}

#colorpicker {
  width: 100%;
  height: 100%;
  grid-area: span 4 / span 3;
  border-radius: 20px;
  display: block;
}

.primary-color-btn {
  width: 100%;
  height: 100%;
  background-color: transparent;
  border: none;
  border-radius: 5px;
  font-size: 2.5vh;
  color: black;
  font-weight: 900;
}

#primary-btn-red {
  background-color: red;
}

#primary-btn-red:active {
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

#primary-btn-blue {
  background-color: blue;
}

#primary-btn-blue:active {
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

#primary-btn-green {
  background-color: green;
}

#primary-btn-green:active {
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

#primary-btn-white {
  background-color: white;
}

#primary-btn-white:active {
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

#ledSettings {
  display: grid;
  grid-template-rows: repeat(4, 1fr);
  gap: 5%;
  justify-content: center;
  align-items: center;
}

.grid-item-ledControls {
  width: 100%;
  height: 100%;
  background-color: transparent;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
}

.btnLedSettings {
  background-color: transparent;
  border: none;
}

#onOffDiv {
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

#onOffbtn {
  width: 100%;
  height: 50%;
  background-color: rgb(155, 208, 183);
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border: none;
}

#onOffbtn:hover {
  background-color: rgb(217, 151, 116);
  transition: 1000ms;
}

#onOffbtn:active {
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

#brightnessDiv {
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

#brightnessslider {
  width: 100%;
  height: 1.5vh;
  border-radius: 5px;
  background: #d3d3d3;
  outline: none;
  -webkit-transition: 0.2s;
  transition: opacity 0.2s;
}

#brightnessslider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 3.5vh;
  height: 3.5vh;
  border-radius: 50%;
  background: rgb(155, 208, 183);
  cursor: pointer;
}

#brightnessslider::-webkit-slider-thumb:hover {
  background-color: rgb(217, 151, 116);
  transition: 1000ms;
}

#brightnessslider::-moz-range-thumb {
  width: 1vw;
  height: 1vh;
  border-radius: 50%;
  background: rgb(155, 208, 183);
}

#speedDiv{
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

#speedslider {
  width: 100%;
  height: 1.5vh;
  border-radius: 5px;
  background: #d3d3d3;
  outline: none;
  -webkit-transition: 0.2s;
  transition: opacity 0.2s;
}

#speedslider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 3.5vh;
  height: 3.5vh;
  border-radius: 50%;
  background: rgb(155, 208, 183);
  cursor: pointer;
}

#speedslider::-webkit-slider-thumb:hover {
  background-color: rgb(217, 151, 116);
  transition: 1000ms;
}

#speedslider::-moz-range-thumb {
  width: 1vw;
  height: 1vh;
  border-radius: 50%;
  background: rgb(155, 208, 183);
}

#randomEffectDiv {
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

#randomEffectbtn {
  width: 100%;
  height: 50%;
  background-color: rgb(155, 208, 183);
  justify-content: center;
  align-items: center;
  border-radius: 10px;
  border: none;
  display: flex;
}

.gg-dice-6 {
  display: block;
  transform: scale(var(--ggs, 1));
  position: relative;
  box-sizing: border-box;
  width: 22px;
  height: 22px;
  border: 2px solid;
  border-radius: 3px;
}

.gg-dice-6::before {
  content: "";
  display: block;
  box-sizing: border-box;
  background: currentColor;
  position: absolute;
  width: 4px;
  height: 4px;
  border-radius: 4px;
  left: 2px;
  top: 2px;
  box-shadow: 0 5px 0, 0 10px 0, 10px 0 0, 10px 5px 0, 10px 10px 0;
}

#randomEffectbtn:hover {
  background-color: rgb(217, 151, 116);
  transition: 1000ms;
}

#randomEffectbtn:active {
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.2);
  transform: translateY(1px);
}

@media screen and (max-width: 600px) {
  .leds {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .ledControls {
    width: 100%;
    height: 55vh;
    justify-content: center;
    align-items: center;
    padding: 0.5%;
  }
}
</style>
