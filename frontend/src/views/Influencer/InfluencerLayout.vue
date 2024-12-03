<template>
  <div class="flex min-h-screen">
    <!-- Sidebar -->
    <Inf_sidebar />
    <NotificationButton/>
    <!-- Main Content -->
    <div class="flex-1 ml-64 overflow-y-auto p-2">
      <router-view />
    </div>
  </div>
</template>

<script setup>
// Import sidebar
import Inf_sidebar from '@/views/Influencer/Inf_sidebar.vue';
import NotificationButton from '@/components/NotificationButton.vue';
</script>
