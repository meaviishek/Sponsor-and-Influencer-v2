<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user';
import api from '@/services/api';
import { useRouter } from 'vue-router';
import { 
  HomeIcon, 
  UsersIcon, 
  MegaphoneIcon, 
  ChartBarIcon,
  BuildingOfficeIcon,
  ArrowLeftOnRectangleIcon 
} from '@heroicons/vue/24/outline'

const userStore = useUserStore();
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

<template>
  <div class="h-screen fixed w-64 bg-gray-900 text-white flex flex-col">
    <!-- Logo -->
    <div class="px-4 py-6">
      <h1 class="text-xl font-bold">Admin Dashboard</h1>
    </div>

    <!-- Navigation Links -->
    <nav class="flex-1 px-2 py-4 space-y-2">
        <router-link to="/admin" 
     class="flex items-center px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors rounded-lg"
     :class="{ 'bg-gray-800 text-white': active }">
    <component :is="HomeIcon" class="w-5 h-5 mr-3" />
    <span class="text-sm font-medium">Home</span>
  </router-link>
  <router-link to="/admin/influencers" 
     class="flex items-center px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors rounded-lg"
     :class="{ 'bg-gray-800 text-white': active }">
    <component :is="UsersIcon" class="w-5 h-5 mr-3" />
    <span class="text-sm font-medium">Influencers</span>
  </router-link>
  <router-link to="/admin/sponsors" 
     class="flex items-center px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors rounded-lg"
     :class="{ 'bg-gray-800 text-white': active }">
    <component :is="BuildingOfficeIcon" class="w-5 h-5 mr-3" />
    <span class="text-sm font-medium">Sponsors</span>
  </router-link>
  <router-link to="/admin/campaigns" 
     class="flex items-center px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors rounded-lg"
     :class="{ 'bg-gray-800 text-white': active }">
    <component :is="MegaphoneIcon" class="w-5 h-5 mr-3" />
    <span class="text-sm font-medium">Campaigns</span>
  </router-link>
  <router-link to="/admin/stats" 
     class="flex items-center px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors rounded-lg"
     :class="{ 'bg-gray-800 text-white': active }">
    <component :is="ChartBarIcon" class="w-5 h-5 mr-3" />
    <span class="text-sm font-medium">Stats</span>
  </router-link>
    
     
    </nav>

    <!-- Logout Button -->
    <div class="px-4 py-4 border-t border-gray-800">
      <button 
        @click="handleLogout"
        class="flex items-center w-full px-4 py-3 text-gray-300 hover:bg-gray-800 hover:text-white transition-colors rounded-lg">
        <ArrowLeftOnRectangleIcon class="w-5 h-5 mr-3" />
        <span class="text-sm font-medium">Logout</span>
      </button>
    </div>
  </div>
</template>
