<script setup></script>

<template>
  <main>
    <div id="AboutH1">
      <h1 class="AboutH1">Interactive Lighting</h1>
    </div>
     <div class="ledDiv">
      <!-- <div class="col" id="leftCol">
        <h2>Color Picker</h2>
        <table id="colorTable">
          <tr>
            <td id="colorPickerSide">
              <input type="color" id="colorpicker" value="#ffa31a" @input="UpdateColorValue()" />
            </td>
            <td id="fullColorSide">
              <input type="button" class="fullColor" id="fullRed" @click="ChangeColorValue('#ff0000')" />
              <input type="button" class="fullColor" id="fullBlue"  @click="ChangeColorValue('#0000ff')" />
              <input type="button" class="fullColor" id="fullGreen" @click="ChangeColorValue('#00ff00')" />
              <input type="button" class="fullColor" id="fullWhite" @click="ChangeColorValue('#ffffff')" /> 
            </td>
          </tr>
        </table>
      </div> -->
      <div class="container">
    <div class="left-side">
      <input type="color" id="color-picker-button" value="#ffa31a" @input="UpdateColorValue()" />
    </div>
    <div class="right-side">
        <button class="color-button red"   @click="ChangeColorValue('#ff0000')"></button>
        <button class="color-button blue"  @click="ChangeColorValue('#0000ff')"></button>
        <button class="color-button green" @click="ChangeColorValue('#00ff00')"></button>
        <button class="color-button white" @click="ChangeColorValue('#ffffff')"></button>
    </div>
</div>
      <div class="col" id="rightCol">
        <div class="rightSideRows">
          <h2>On/Off</h2>
          <button type="button" id="buttononoff" @click="toggleLed()">
            <i style="font-size:24px" class="fa">&#xf011;</i>
          </button>
        </div>
        <div class="rightSideRows">
          <h2>Brightness</h2>
          <input class="slider" type="range" id="brightness" min="0" max="255" value="50" @input="getBrightnessValue()" />
        </div>
        <div class="rightSideRows">
          <h2>Random Effect</h2>
          <button id="buttonRandomEffect" type="button" class="buttonRandomEffect" @click="setRandomEffect()">
            <i style="font-size: 24px;" class="fa">&#xf6cf</i>
          </button>
        </div>
      </div>
    </div>
  </main>
<footer>
hehe
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
    UpdateColorValue(){
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
    ChangeColorValue(color){
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

.ledDiv {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
  background-color: transparent;
}

.col {
  width: 100%;
  height: 100%;
  overflow: visible;
}

/* #leftCol {
  height: 100%;
  width: 50%;
  margin: 0vh 0vh 0vh 0vh;
} */

#rightCol {
  height: 100%;
  width: 50%;
}

#colorTable{
  width: 100%;
  height: 100%;
  background-color: transparent;
}

.rightSideRows {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  height: 100%;
  width: 100%;
  padding: 2%;
}

#colorTable{
  width: 100%;
  height: 40vh;
  background-color: transparent;
}

#colorPickerSide{
  width: 80%;
  height: 100%;
  background-color: transparent;
}


#fullColorSide{
  width: 30%;
  height: 100%;
  background-color: transparent;
}

.container{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 50%;
  background-color: transparent;
}

.left-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  height: 100%;
  width: 100%;
}

.color-picker-button {
  height: 100%;
  width: 100%;
  padding: 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.right-side {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 20px;
  height: 100%;
  width: 100%;
}

.color-button {
  width: 100px;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.color-button:not(:last-child) {
  margin-bottom: 10px;
}

.red { background-color: red; }
.blue { background-color: blue; }
.green { background-color: green; }
.white { background-color: white; }
    
#colorpicker {
  height: 90%;
  width: 90%;
  border: none;
  background-color: transparent;
  border-radius: 40px;
  overflow: hidden;
}

.fullColor{
  justify-content: left;
  width: 100%;
  height: 20%;
  display: flex;
  flex-direction: column;
  border-radius: 7px;
  border: none;
  margin: 0% 0 10% 0;
  overflow: hidden;
}

#fullRed{
  background-color: red;
}

#fullBlue{
  background-color: blue;
}

#fullGreen{
  background-color: green;
}

#fullWhite{
  background-color: white;
}



#buttononoff {
  background-color: rgb(155, 208, 183);
  width: 50%;
  font-size: x-large;
  border-radius: 50px;
}


#brightness {
  /*Delete the default slider appearance*/
  -webkit-appearance: none;
  appearance: none;

  /*Style*/
  width: 50%;
  cursor: pointer;
  outline: none;
  height: 1vh;
  background-color: rgb(155, 208, 183);
  border-radius: 50px;
  font-size: x-large;
}

#brightness::-webkit-slider-thumb {
  border-radius: 50%;
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  background: wheat;
  cursor: pointer;
}


button:active{
  color:rgb(248, 246, 244);
  box-shadow: 0 5px rgb(28, 46, 38);
  transform: translateY(4px);
}

#buttonRandomEffect {
  background-color: rgb(155, 208, 183);
  width: 50%;
  font-size: x-large;
  border-radius: 50px;
}
footer {
    background-color: rgb(7, 7, 7);
    color: rgb(155, 208, 183);
    text-align: center;
    padding: 20px 0;
    border-radius: 10px;
}
</style>
