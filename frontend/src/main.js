// /src/main.js
import { createApp } from 'vue';
import { createPinia } from 'pinia'; 
import App from './App.vue';
import router from './router';
import './assets/main.css';
import { initializeUser } from './services/initializeUser';

const app = createApp(App);


const pinia = createPinia();
app.use(pinia);


app.use(router);

initializeUser();

app.mount('#app');