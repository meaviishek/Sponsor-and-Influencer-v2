<script setup>
defineProps({
  title: String,
  value: [String, Number],
  icon: String,
  trend: Number,
})
</script>

<template>
  <div class="bg-white rounded-lg shadow p-6">
    <div class="flex items-center justify-between">
      <div>
        <p class="text-sm text-gray-600">{{ title }}</p>
        <h3 class="text-2xl font-bold mt-2">{{ value }}</h3>
      </div>
      <div :class="'text-2xl ' + icon"></div>
    </div>
    <div class="mt-4">
      <span :class="trend > 0 ? 'text-green-500' : 'text-red-500'" class="text-sm font-semibold">
        {{ trend > 0 ? '+' : '' }}{{ trend }}%
      </span>
      <span class="text-gray-500 text-sm ml-2">vs last month</span>
    </div>
  </div>
</template>