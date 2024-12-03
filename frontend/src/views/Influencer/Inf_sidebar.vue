<template>
  <div class="flex min-h-screen">
    <!-- Sidebar -->
    <aside class="w-80 bg-white shadow-lg h-screen fixed">
      <div class="flex flex-col h-full">
        <!-- Profile Section -->
        <div class="p-6 text-center border-b">
          <!-- Heading -->
          <h2 class="text-2xl font-bold text-indigo-600 mb-4">Influencer</h2>

          <!-- Profile Picture -->
          <div class="relative w-24 h-24 mx-auto mb-4">
            <img
              src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix"
              alt="Profile"
              class="rounded-full w-full h-full object-cover border-2 border-indigo-500"
            />
          </div>

          <!-- Profile Name -->
          <h2 class="text-xl font-semibold text-gray-800">{{ userData?.name}}</h2>
          <p class="text-sm text-gray-500 mb-4">@{{ userData?.username }}</p>

          <!-- Profile Details -->
          <div class="text-sm text-gray-700 space-y-2">
            <div class="flex justify-between">
              <span class="font-medium">Reach:</span>
              <span>{{ userData?.profile.reach }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-medium">Followers:</span>
              <span>{{ userData?.profile.followers }}</span>
            </div>
            <div class="flex justify-between">
              <span class="font-medium">Category:</span>
              <span>{{ userData?.profile.category }}</span>
            </div>
          </div>

          <!-- Edit Profile Button -->
          <button
         @click="openEditModal"
            class="mt-4 w-full bg-indigo-500 text-white py-2 rounded-lg text-sm font-medium hover:bg-indigo-600 transition"
          >
            Edit Profile
          </button>
        </div>

        <!-- Total Earnings Section -->
        <!-- <div class="p-4 border-b">
          <div class="flex justify-between items-center">
            <h3 class="text-lg font-semibold text-gray-800">Total Earnings</h3>
            <p class="text-xl font-bold text-green-600">$12,345</p>
          </div>
        </div> -->

        <!-- Navigation -->
        <nav class="flex-1 p-4">
          <div class="space-y-2">
            <!-- Nav Items -->
            <router-link
              to="/influencer"
              class="flex items-center space-x-3 text-gray-700 p-2 rounded-lg font-medium hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              <span>Home</span>
            </router-link>

            <router-link
              to="/influencer/campaigns"
              class="flex items-center space-x-3 text-gray-700 p-2 rounded-lg font-medium hover:bg-indigo-50 hover:text-indigo-600 transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5.882V19.24a1.76 1.76 0 01-3.417.592l-2.147-6.15M18 13a3 3 0 100-6M5.436 13.683A4.001 4.001 0 017 6h1.832c4.1 0 7.625-1.234 9.168-3v14c-1.543-1.766-5.067-3-9.168-3H7a3.988 3.988 0 01-1.564-.317z" />
              </svg>
              <span>Campaigns</span>
            </router-link>

            <router-link
              to="/influencer/stats"
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
        Logout
          </button>

        </div>
      </div>
    </aside>
  </div>







  <div
      v-if="isEditModalOpen"
      class="fixed inset-0 bg-gray-800 bg-opacity-50 flex justify-center items-center z-50"
    >
      <div class="bg-white w-96 p-6 rounded-lg shadow-lg">
        <h3 class="text-lg font-semibold text-gray-800 mb-4">Edit Profile</h3>
        <form @submit.prevent="updateProfile">
          <div class="space-y-4">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
              <input
                v-model="editForm.name"
                type="text"
                id="name"
                class="mt-1 p-2 border rounded w-full"
                required
              />
            </div>
            <div>
              <label for="category" class="block text-sm font-medium text-gray-700">Category</label>
              <input
                v-model="editForm.category"
                type="text"
                id="category"
                class="mt-1 p-2 border rounded w-full"
                required
              />
            </div>
            <div>
              <label for="reach" class="block text-sm font-medium text-gray-700">Reach</label>
              <input
                v-model="editForm.reach"
                type="number"
                id="reach"
                class="mt-1 p-2 border rounded w-full"
                required
              />
            </div>
            <div>
              <label for="followers" class="block text-sm font-medium text-gray-700">Followers</label>
              <input
                v-model="editForm.followers"
                type="number"
                id="followers"
                class="mt-1 p-2 border rounded w-full"
                required
              />
            </div>
          </div>
          <div class="mt-6 flex justify-between">
            <button
              type="button"
              @click="closeEditModal"
              class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-600 transition"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="bg-indigo-500 text-white py-2 px-4 rounded hover:bg-indigo-600 transition"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  
</template>

<script setup>
// Component logic can be added here
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
import { fetchUserData } from '@/services/fetchUserData';

const router = useRouter();
const isEditModalOpen = ref(false);
const editForm = ref({
  name: '',
  category: '',
  reach: 0,
  followers: 0,
});

onMounted(() => {
  const storedUserData = localStorage.getItem('userData');
  if (storedUserData) {
    userData.value = JSON.parse(storedUserData);
    Object.assign(editForm.value, {
      name: userData.value.name,
      category: userData.value.profile.category,
      reach: userData.value.profile.reach,
      followers: userData.value.profile.followers,
    });
  }
});

const openEditModal = () => {
  isEditModalOpen.value = true;
};

const closeEditModal = () => {
  isEditModalOpen.value = false;
};


const updateProfile = async () => {
  try {
    const token = localStorage.getItem('accessToken');
    const response = await api.post(
      '/inf/profile',
      {
        name: editForm.value.name,
        category: editForm.value.category,
        reach: editForm.value.reach,
        followers: editForm.value.followers,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );

    userData.value = response.data.user;
    localStorage.setItem('userData', JSON.stringify(userData.value));
    await fetchUserData()
    closeEditModal();
    window.location.reload();
    alert('Profile updated successfully!');
  } catch (error) {
    console.error('Failed to update profile:', error.response?.data || error.message);
    alert('Error updating profile: ' + (error.response?.data?.message || error.message));
  }
};

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
