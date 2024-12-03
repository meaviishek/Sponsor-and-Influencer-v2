<script setup>
import { computed } from 'vue';
const props=defineProps({
  campaign: {
    type: Object,
    required: true
  }
});

const daysRemaining = computed(() => {
  const end = new Date(props.campaign.endDate)
  const today = new Date()
  const diff = end - today
  return Math.ceil(diff / (1000 * 60 * 60 * 24))
})
const progressPercentage = computed(() => {
  const start = new Date(props.campaign.startDate)
  const end = new Date(props.campaign.endDate)
  const today = new Date()
  const total = end - start
  const elapsed = today - start
  return Math.min(100, Math.max(0, Math.round((elapsed / total) * 100)))
})
</script>

<template>
  <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-3">
        <img src="https://i.pravatar.cc/150" alt="" class="w-12 h-12 rounded-full object-cover" />
        <div>
          <h3 class="font-semibold text-lg">{{ campaign.name }}</h3>
          <p class="text-gray-600">{{ campaign.description }}</p>
        </div>
      </div>
      <span :class="{
        'bg-green-100 text-green-800': campaign.status === 'accepted',
        'bg-blue-100 text-blue-800': campaign.status === 'pending',
        'bg-gray-100 text-gray-800': campaign.status === 'completed'
      }" class="px-3 py-1 rounded-full text-sm font-medium">
        {{ campaign.status }}
      </span>
    </div>
    
    <p>Price: <span class="text-gray-500">₹{{ campaign.price }}</span></p>

    <div class="space-y-2">
      <div class="flex justify-between text-sm">
        <span class="text-gray-600">Campaign Progress</span>
        <span class="font-medium">{{ progressPercentage }}%</span>
      </div>
      <div class="w-full bg-gray-200 rounded-full h-2">
        <div
          class="bg-green-500 h-2 rounded-full"
          :style="{ width: `${progressPercentage}%` }"
        ></div>
      </div>
      <div class="flex justify-between text-sm">
        <span class="text-gray-500">{{ campaign.startDate }}</span>
        <span class="text-gray-500">{{ campaign.endDate }}</span>
      </div>
      <div class="text-sm font-medium" :class="daysRemaining > 5 ? 'text-green-600' : 'text-orange-500'">
        {{ daysRemaining }} days remaining
      </div>
    </div>
  </div>
</template>