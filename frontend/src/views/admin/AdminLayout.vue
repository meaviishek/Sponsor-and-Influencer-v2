<template>
    <div class="flex min-h-screen">
      <!-- Sidebar -->
      <Adm_sidebar />
      <NotificationButton/>
      <!-- Main Content -->
      <div class="flex ml-64 overflow-y-auto p-2">
        <router-view />
      </div>
    </div>
  </template>
  
  <script setup>
  // Import sidebar
  import Adm_sidebar from './Adm_sidebar.vue';
  import NotificationButton from '@/components/NotificationButton.vue';
  </script>
  