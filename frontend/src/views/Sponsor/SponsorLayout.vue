<template>
    <div class="flex min-h-screen">
      <!-- Sidebar -->
      <Spo_sidebar />
      <NotificationButton/>
      <!-- Main Content -->
      <div class="flex-1 ml-64 overflow-y-auto p-2">
        <router-view />
      </div>
    </div>
  </template>
  
  <script setup>
  // Import sidebar
  import Spo_sidebar from '@/views/Sponsor/Spo_sidebar.vue';
  import NotificationButton from '@/components/NotificationButton.vue';
  </script>
  