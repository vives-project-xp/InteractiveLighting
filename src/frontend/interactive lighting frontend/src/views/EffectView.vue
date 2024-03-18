<template>
  
<div class="effect">
 <h1 class="AboutH1">This is the effect page. Here you can choose effects for the ledstrip</h1>
</div>
  <table>
      <tr>
        <td>
          <div class="card" style="width: 18rem">
            <img src="..." class="card-img-top" alt="no image yet" />
            <div class="card-body">
              <h5 class="card-title">Effect</h5>
              <p class="card-text">This is the first Effect</p>
              <button type="button btn-danger" class="btn btn-primary" @click="setEffect('test')" >test</button>
            </div>
          </div>
        </td>
        <td>
          <div class="card" style="width: 18rem">
            <img src="..." class="card-img-top" alt="no image yet" />
            <div class="card-body">
              <h5 class="card-title">Effect</h5>
              <p class="card-text">This is the first Effect</p>
              <button type="button btn-danger" class="btn btn-primary" @click="setEffect('test')" >test</button>
            </div>
          </div>
        </td>
        <td>
          <div class="card" style="width: 18rem">
            <img src="..." class="card-img-top" alt="no image yet" />
            <div class="card-body">
              <h5 class="card-title">Effect</h5>
              <p class="card-text">This is the first Effect</p>
              <button type="button btn-danger" class="btn btn-primary" @click="setEffect('test')" >test</button>
            </div>
          </div>
        </td>
      </tr>
      <tr>
        <td>
          <div class="card" style="width: 18rem">
            <img src="..." class="card-img-top" alt="no image yet" />
            <div class="card-body">
              <h5 class="card-title">Effect</h5>
              <p class="card-text">This is the first Effect</p>
              <button type="button btn-danger" class="btn btn-primary" @click="setEffect('test')" >test</button>
            </div>
          </div>
        </td>
        <td>
          <div class="card" style="width: 18rem">
            <img src="..." class="card-img-top" alt="no image yet" />
            <div class="card-body">
              <h5 class="card-title">Effect</h5>
              <p class="card-text">This is the first Effect</p>
              <button type="button btn-danger" class="btn btn-primary" @click="setEffect('test')" >test</button>
            </div>
          </div>
        </td>
        <td>
          <div class="card" style="width: 18rem">
            <img src="..." class="card-img-top" alt="no image yet" />
            <div class="card-body">
              <h5 class="card-title">Effect</h5>
              <p class="card-text">This is the first Effect</p>
              <button type="button btn-danger" class="btn btn-primary" @click="setEffect('test')" >test</button>
            </div>
          </div>
        </td>
      </tr>
  </table>
    
</template>

<script>
import axios from 'axios'
export default {
  name: 'EffectView',
  data() {
    return {
      effect: {}
    }
  },
  methods: {
    setEffect(effect) {
      const request = {
        effect: "test"
      }
      axios.post('http://localhost:3000/effect',request).then((response) => {console.log(response)})
    }
  } 
}
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
.effect{
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('your-image.jpg');
  background-size: cover;
  background-position: center;
  font-family: Arial, sans-serif;
  
}
td{
  padding:50px;
}
table{
  background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('your-image.jpg');
  background-size: cover;
  background-position: center;
  font-family: Arial, sans-serif;
}
.card{
  width: 18rem;
    background-color: #fff;
    border-radius: 10px; 
    box-shadow: 0 0 20px rgba(155, 208, 183); 
    margin: 10px;
}
</style>
