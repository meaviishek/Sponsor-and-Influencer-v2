<template>
    <div class="flex min-h-screen">
      <!-- Sidebar -->
      <aside class="w-80 bg-white shadow-lg  h-screen fixed">
        <div class="flex flex-col h-full">
          <!-- Profile Section -->
          <div class="p-6 text-center border-b">
            <h2 class="text-2xl font-bold text-indigo-600 mb-4">Sponsor</h2>
            <div class="relative w-24 h-24 mx-auto mb-4">
              <img
                src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix"
                alt="Profile"
                class="rounded-full w-full h-full object-cover border-2 border-indigo-500"
              />
            </div>
            <h2 class="text-xl font-semibold text-gray-800">{{ userData?.name }}</h2>
            <p class="text-sm text-gray-500">@{{ userData?.username }}</p>
            <div class="text-sm text-gray-700 space-y-2">
            <div class="flex justify-between">
              <span class="font-medium">Company Name :</span>
              <span>{{ userData?.profile.company_name }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-medium">Budget:</span>
              <span>₹ {{ userData?.profile.budget }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-medium">Industry:</span>
              <span>{{ userData?.profile.industry }}</span>
            </div>
          </div>

          <!-- Edit Profile Button -->
          <button
            class="mt-4 w-full bg-indigo-500 text-white py-2 rounded-lg text-sm font-medium hover:bg-indigo-600 transition"
          >
            Edit Profile
          </button>
          </div>
  
          <!-- Navigation -->
          <nav class="flex-1 p-4">
            <div class="space-y-2">
              <!-- Search -->
              <div class="relative mb-6">
                <input
                  type="text"
                  placeholder="Search..."
                  class="w-full pl-10 pr-4 py-2 rounded-lg border focus:outline-none focus:border-indigo-500"
                />
                <svg
                  class="absolute left-3 top-2.5 h-5 w-5 text-gray-400"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                  />
                </svg>
              </div>
  
              <!-- Nav Items -->
              <router-link
                to="/sponsor"
                class="flex items-center space-x-3 text-gray-700 p-2 rounded-lg font-medium hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
                <span>Home</span>
              </router-link>
  
              <router-link
                to="/sponsor/influencers"
                class="flex items-center space-x-3 text-gray-700 p-2 rounded-lg font-medium hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                </svg>
                <span>Influencers</span>
              </router-link>
  
              <router-link
                to="/sponsor/campaigns"
                class="flex items-center space-x-3 text-gray-700 p-2 rounded-lg font-medium hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z" />
                </svg>
                <span>Campaigns</span>
              </router-link>
  
              <router-link
                to="/sponsor/stats"
                class="flex items-center space-x-3 text-gray-700 p-2 rounded-lg font-medium hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
              >
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
                <span>Stats</span>
              </router-link>
            </div>
          </nav>
  
          <!-- Logout Button -->
          <div class="p-4 border-t">
         
            <button
             @click="handleLogout"
              class="flex items-center space-x-3 text-gray-700 p-2 rounded-lg font-medium hover:bg-red-50 hover:text-red-600 transition-colors w-full"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
              </svg>
              <span>Logout</span>
            </button>
          
          </div>
        </div>
      </aside>
  

 
    </div>
  </template>
  
  <script setup>
  // Component logic can be added here

// import {  computed } from 'vue';
import { useUserStore } from '../../stores/user';
import { ref, onMounted } from 'vue';

const userData = ref(null);

onMounted(() => {
  const storedUserData = localStorage.getItem('userData');
  if (storedUserData) {
    userData.value = JSON.parse(storedUserData);
  }
});

const userStore = useUserStore();
// const userData = computed(() => userStore.user);

import { useRouter } from 'vue-router';

import api from '@/services/api';

const router = useRouter();


const handleLogout = async () => {
  try {
    const token = localStorage.getItem('accessToken');
    await api.post('/logout', {}, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    userStore.clearUser();
    localStorage.removeItem('userData');
    localStorage.removeItem('accessToken');

    
    router.push('/');
  } catch (error) {
    console.error('Logout failed:', error.response?.data || error.message);
    alert('Error logging out: ' + (error.response?.data?.error || error.message));
  }
};



  </script>