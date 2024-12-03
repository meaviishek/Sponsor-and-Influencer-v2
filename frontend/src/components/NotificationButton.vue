<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { BellIcon } from '@heroicons/vue/24/outline';

const showNotifications = ref(false);
const notifications = ref([
  {
    id: 1,
    title: 'Campaign Deadline',
    message: 'Nike campaign content due in 2 days',
    time: '2 hours ago',
    isRead: false,
    type: 'reminder'
  },
  {
    id: 2,
    title: 'New Campaign Request',
    message: 'Samsung wants to collaborate with you',
    time: '1 day ago',
    isRead: false,
    type: 'campaign'
  },
  {
    id: 3,
    title: 'Content Approval',
    message: 'Your draft for Sephora has been approved',
    time: '2 days ago',
    isRead: true,
    type: 'message'
  }
]);

const unreadCount = computed(() => 
  notifications.value.filter(n => !n.isRead).length
);

const markAsRead = (notificationId) => {
  const notification = notifications.value.find(n => n.id === notificationId);
  if (notification) {
    notification.isRead = true;
  }
};

const closeNotifications = (event) => {
  if (!event.target.closest('.notification-container')) {
    showNotifications.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', closeNotifications);
});

onUnmounted(() => {
  document.removeEventListener('click', closeNotifications);
});
</script>

<template>
  <div class="notification-container fixed top-4 right-4 z-50">
    <button
      @click.stop="showNotifications = !showNotifications"
      class="relative p-2 text-gray-600 hover:text-gray-900 bg-white rounded-full shadow-lg hover:shadow-xl transition-all duration-200"
    >
      <BellIcon class="w-6 h-6" />
      <span
        v-if="unreadCount > 0"
        class="absolute -top-1 -right-1 bg-red-500 text-white text-xs w-5 h-5 flex items-center justify-center rounded-full"
      >
        {{ unreadCount }}
      </span>
    </button>

    <div
      v-if="showNotifications"
      class="absolute right-0 mt-2 w-80 bg-white rounded-lg shadow-xl border border-gray-100 overflow-hidden"
    >
      <div class="p-4 border-b border-gray-100">
        <h3 class="text-lg font-semibold text-gray-900">Notifications</h3>
      </div>

      <div class="max-h-96 overflow-y-auto">
        <template v-if="notifications.length">
          <div
            v-for="notification in notifications"
            :key="notification.id"
            @click="markAsRead(notification.id)"
            :class="[
              'p-4 border-b border-gray-100 cursor-pointer hover:bg-gray-50 transition-colors',
              { 'bg-blue-50': !notification.isRead }
            ]"
          >
            <div class="flex items-center justify-between mb-1">
              <h4 class="font-medium text-gray-900">{{ notification.title }}</h4>
              <span class="text-xs text-gray-500">{{ notification.time }}</span>
            </div>
            <p class="text-sm text-gray-600">{{ notification.message }}</p>
          </div>
        </template>
        <div v-else class="p-4 text-center text-gray-500">
          No notifications
        </div>
      </div>

      <div class="p-3 bg-gray-50 text-center">
        <button class="text-sm text-indigo-600 hover:text-indigo-800">
          View all notifications
        </button>
      </div>
    </div>
  </div>
</template>