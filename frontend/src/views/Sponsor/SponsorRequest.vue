<script setup>
defineProps({
  request: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['accept', 'reject'])
</script>

<template>
  <div class="bg-white rounded-lg shadow-md p-6 mb-4">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-4">
        <img :src="request.influencer.avatar" :alt="request.influencer.name" class="w-12 h-12 rounded-full">
        <div>
          <h3 class="font-semibold text-lg">{{ request.influencer.name }}</h3>
          <p class="text-gray-600">{{ request.influencer.followers }} followers</p>
        </div>
      </div>
      <div class="text-right">
        <p class="text-2xl font-bold text-gray-900">${{ request.price }}</p>
        <p class="text-sm text-gray-500">Proposed Price</p>
      </div>
    </div>
    
    <div class="mb-4">
      <h4 class="font-medium mb-2">Campaign Details</h4>
      <p class="text-gray-600">{{ request.description }}</p>
    </div>
    
    <div class="flex justify-between items-center">
      <div class="text-sm text-gray-500">
        <span>Platform: {{ request.platform }}</span>
        <span class="mx-2">•</span>
        <span>Duration: {{ request.duration }}</span>
      </div>
      <div class="space-x-3">
        <button
          @click="emit('reject', request.id)"
          class="px-4 py-2 border border-red-500 text-red-500 rounded-lg hover:bg-red-50 transition-colors"
        >
          Reject
        </button>
        <button
          @click="emit('accept', request.id)"
          class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
        >
          Accept
        </button>
      </div>
    </div>
  </div>
</template>