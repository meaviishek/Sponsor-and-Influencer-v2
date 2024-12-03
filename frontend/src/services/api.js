
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // Replace this with your backend URL
  timeout: 5000, // Optional: Set a timeout for requests
});

export default api;
