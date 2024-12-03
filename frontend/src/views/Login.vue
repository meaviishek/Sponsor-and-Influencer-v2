

<template>
    <div class="flex h-screen flex-col lg:flex-row">
      <!-- Left Side: Login Form (1/3 of the screen on large screens, full width on small screens) -->
      <div class="flex-1 flex justify-center items-center bg-gray-50 p-4 lg:p-8">
        <div class="w-full max-w-sm p-6 bg-white shadow-md rounded-lg">
          <h2 class="text-2xl font-bold mb-1 text-center">Login</h2>
          <p class="text-center text-gray-600">
          Welcome to InfluencerSpot
          </p>
  
          <form @submit.prevent="handleLogin">
            <div class="mb-6">
              <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
              <input
                id="email"
                type="email"
                v-model="email"
                placeholder="Enter Your Email"
                required
                class="w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
  
            <div class="mb-6">
              <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
              <input
                id="password"
                type="password"
                v-model="password"
                required
                placeholder="Enter Your Password"
                class="w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
         
  
            <button
              type="submit"
              class="w-full py-2 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition duration-300"
            >
         
              Login
            
              
            </button>
            
            <div class="mt-6 text-center text-blue-600 ">
              <div>
                Don't have an account? Register 
              </div>
              <div class="space-x-4 ">

              <router-link to="/sponsor_reg" class="text-blue-600 hover:underline">
               Sponsor
              </router-link>
              <router-link to="/influencer_reg" class="text-blue-600 hover:underline">
               Influencer
              </router-link>
               </div>
            </div>
          </form>
        </div>
      </div>
  
      <!-- Right Side: Image (2/3 of the screen on large screens, full width on small screens) -->
      <div class="flex-1 bg-blue-500 text-white flex justify-center items-center hidden lg:block">
        <img src="/src/assets/social-media.png" alt="Login Image" class="h-full w-full object-cover" />
      </div>
    </div>
  </template>
  
  <script setup>
  import api from '@/services/api';
import { useRouter } from 'vue-router';
import { fetchUserData } from '@/services/fetchUserData';



const router = useRouter();


let email = '';
let password = '';

const handleLogin = async () => {
  try {
    const response = await api.post('/login', {
      email: email,
      password: password,
   
    });
    const accessToken = response.data.access_token
    // console.log(accessToken)
    localStorage.setItem('accessToken', accessToken);
    const userData = await fetchUserData();
    // const userData = response.data.user;
    

    // userStore.setUser({...userData,accessToken});

    if (userData.role === 'influencer') {
      router.push('/influencer');
    } else if (userData.role === 'sponsor') {
      router.push('/sponsor');
    }else if (userData.role === 'admin'){
      router.push('/admin')
    }

    // Save role and user data to localStorage for persistence
 
  } catch (error) {
    console.error('Login failed:', error.response?.data || error.message);
    alert('Login failed: ' + (error.response?.data?.error || error.message));
  }
};
  </script>
  
  <style scoped>
  /* Custom styles */
  </style>
  