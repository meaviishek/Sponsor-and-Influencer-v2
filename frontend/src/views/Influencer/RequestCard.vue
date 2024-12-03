<script setup>
import { ref } from 'vue';

defineProps({
  request: {
    type: Object,
    required: true
  }
});

const emit = defineEmits(['accept', 'reject'])

const showNegotiateModal = ref(false);
</script>

<template>
  <div class="bg-white rounded-lg shadow-md p-6">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-3">
        <img src="https://i.pravatar.cc/150" alt="" class="w-12 h-12 rounded-full object-cover" />
        <div>
          <h3 class="font-semibold text-lg">{{ request.name }}</h3>
          <p class="text-gray-600">{{ request.description }}</p>
        </div>
        <div class="text-right">
        <p class="text-2xl font-bold text-gray-900">${{ request.price }}</p>
        <p class="text-sm text-gray-500">Proposed Price</p>
      </div>
      </div>
    </div>
    <p class="text-gray-600 mb-4">Sponsor: {{ request.sponsor_name }}</p>
    <div class="flex justify-between items-center text-sm text-gray-600 mb-4">
      <div>
        <p>Offered Budget: <span class="font-medium">Rs. {{ request?.price }}</span></p>
        <p>Deadline: <span class="font-medium">{{ request.startDate }} to {{ request.endDate }}</span></p>
      </div>
    </div>
    <div class="flex space-x-3">
      <button @click="emit('accept',request.id)" class="bg-green-600 text-white px-4 py-2 rounded-md hover:bg-green-700 transition-colors">
        Accept
      </button>
      <button @click="showNegotiateModal = true" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition-colors">
        Negotiate
      </button>
      <button @click="emit('reject',request.id)" class="bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700 transition-colors">
        Reject
      </button>
    </div>
  </div>
</template>