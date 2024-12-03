<script setup>
import { computed } from 'vue'

const props = defineProps({
  campaign: {
    type: Object,
    required: true
  }
})

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
  <div class="bg-white rounded-lg shadow-md p-6">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-4">
        <img :src="campaign.influencer.avatar" :alt="campaign.influencer.name" class="w-12 h-12 rounded-full">
        <div>
          <h3 class="font-semibold text-lg">{{ campaign.influencer.name }}</h3>
          <p class="text-gray-600">{{ campaign.influencer.followers }} followers</p>
        </div>
      </div>
      <div class="text-right">
        <p class="text-lg font-semibold text-gray-900">₹{{ campaign.price }}</p>
        <p class="text-sm text-gray-500">Campaign Value</p>
      </div>
    </div>
    
    <div class="mb-4">
      <p class="text-gray-600 text-sm mb-2">{{ campaign.name }}</p>

      <p class="text-gray-600 text-sm mb-2">{{ campaign.description }}</p>
      <div class="flex items-center text-sm text-gray-500 space-x-4">
        <span>{{ campaign.platform }}</span>
        <span>•</span>
        <span>{{ campaign.duration }}</span>
      </div>
    </div>
    
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