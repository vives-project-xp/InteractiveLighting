<template>
  <main>
    <div class="effect">
      <h1 class="AboutH1">Choose your effect</h1>
      <input type="text" v-model="searchQuery" placeholder="Search effects..." class="form-control mb-3" id="searchBar">
      <div class="d-flex flex-wrap justify-content-center">
        <div v-for="(effect, index) in filteredEffects" :key="index">
          <div class="card">
            <div class="d-flex p-1">
              <div class="card-body">
                <h5 class="card-title">{{ effect.effect }}</h5>
                <button type="button" class="btn btn-primary" id="buttonEffect" @click="setEffect(effect.index)">Set {{ effect.effect }}</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EffectView',
  data() {
    return {
      effects: [],
      searchQuery: ''
    }
  },
  mounted() {
    // Call the method to fetch effects list
    this.getEffectList();
  },
  computed: {
    filteredEffects() {
      // Filter the effects based on the search query
      return this.effects.filter(effect =>
        effect.effect.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  methods: {
    getEffectList() {
      // Fetch effects list from the provided URL
      axios
        .get("http://localhost:3000/effect")
        .then((response) => {
          console.log(response.data);
          this.effects = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    setEffect(index) {
      // Set the selected effect
      const selectedEffect = this.effects.find(effect => effect.index === index);
      if (selectedEffect) {
        const request = {
          fx: selectedEffect.index
        };
        axios.post('http://localhost:3000/effect', request)
          .then((response) => {
            console.log(response);
          })
          .catch((error) => {
            console.error(error);
          });
      }
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

#searchBar {
  width: 50%;
  margin: 0 auto;
  background-color: rgb(155, 208, 183);
  border-radius: 7px;
  border: none;
  color: black;
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
  width: 17rem;
  background-color:rgb(0, 15, 44, 0.2);
  border-radius: 10px; 
  box-shadow: 0 0 20px rgba(155, 208, 183); 
  margin: 10px;
  color: wheat;
}

#buttonEffect{
  background-color:rgb(155, 208, 183) ;
  color: black;
}

</style>
