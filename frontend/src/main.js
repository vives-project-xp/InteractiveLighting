import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


const app = createApp(App)
//console.log(process.env.VUE_APP_BACKEND_URL);
app.use(router)

app.mount('#app')
