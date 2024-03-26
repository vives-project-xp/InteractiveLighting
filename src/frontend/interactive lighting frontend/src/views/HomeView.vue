<script setup></script>
<template>
  <main>
    <div id="AboutH1">
      <h1 class="AboutH1">Interactive Lighting</h1>
    </div>
    <div class="ledSettings">
        <div class="grid-container">
          <input type="color" class="grid-item" id="colorpicker">
          <div class="right-side-colorpicker">
            <div class="grid-item"><button class="color-button red" @click="ChangeColorValue('#ff0000')"></button></div>
            <div class="grid-item"><button class="color-button blue" @click="ChangeColorValue('#0000ff')"></button></div>
            <div class="grid-item"><button class="color-button green" @click="ChangeColorValue('#00ff00')"></button></div>
            <div class="grid-item"><button class="color-button white" @click="ChangeColorValue('#ffffff')"></button></div>
        </div>
      </div>
      <div class="col" id="LedControlButtons">
        <div class="LedControlButtons">
          <h2>On/Off</h2>
          <button type="button" id="btnOnOff" @click="toggleLed()">
            <i style="font-size:24px" class="fa">&#xf011;</i>
          </button>
        </div>
        <div class="LedControlButtons">
          <h2>Brightness</h2>
          <input class="slider" type="range" id="brightness" min="0" max="255" value="50"
            @input="getBrightnessValue()" />
        </div>
        <div class="LedControlButtons">
          <h2>Random Effect</h2>
          <div id="buttonRandomEffect" >
            <button type="button" class="buttonRandomEffect" @click="setRandomEffect()">
              <i style="font-size: 24px;" class="fa">&#xf6cf</i>
            </button>
          </div>
        </div>
      </div>
    </div>
    
  </main>
  <footer>
    <div class="footer-content">
        <div class="footer-section contact">
            <h2>Contact Us</h2>
            <ul>
                <li><i class="fa fa-envelope"></i> info@example.com</li>
                <li><i class="fa-solid fa-phone-volume"></i> +32 33 56 63</li>
                <li><i class="fa-solid fa-location-dot"></i> Vives Brugge Xaverianenstraat</li>
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
      axios
        .post("http://localhost:3000/color", payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    setRandomEffect() {
      axios
        .post("http://localhost:3000/random")
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
        .post("http://localhost:3000/brightness", payload)
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
        .post("http://localhost:3000/onof", payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    ChangeColorValue(color) {
      const payload = {
        color: color,
      };
      axios
        .post("http://localhost:3000/color", payload)
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
};
import { onMounted } from "vue";
onMounted(() => {
  methods.getEffectList();
})
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
  height: 100%;
  width: 100%;
  padding: 2vh 0vh 2vh 0vh;
  margin: 2vh 0vh 2vh 0vh;
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 7px;
}

#btnOnOff{
  background-color:rgb(155, 208, 183);
  width: 25%;
}

#buttonRandomEffect{
  background-color:rgb(155, 208, 183);
  width: 25%;
  
}

footer{
    background-color: black;
    padding: 5px;
    border-radius: 10px;
}

.footer-section ul{
    list-style: none;
    padding:0;
}
.grid-container {
  display: grid;
  width: 50%;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: repeat(4, 100px);
  height: 100%;
  gap: 0;
}
.grid-item {
  background-color: #ddd; /* Background color */
  border: 1px solid #999; /* Border */
  display: flex; /* Center content horizontally and vertically */
  justify-content: center;
  align-items: center;
  font-size: 1.2rem; /* Font size */
}
.ledDiv {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  background-color: transparent;
}
</style>
