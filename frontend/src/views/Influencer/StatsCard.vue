<template>
    <div class="bg-white rounded-xl shadow-lg p-4 sm:p-6 transition-all duration-300 hover:shadow-xl">
      <div class="flex items-center justify-between mb-3 sm:mb-4">
        <h3 class="text-gray-600 text-xs sm:text-sm font-medium">{{ title }}</h3>
        <component :is="icon" class="w-4 h-4 sm:w-5 sm:h-5 text-indigo-500" />
      </div>
      <p class="text-xl sm:text-2xl font-bold text-gray-900">{{ value }}</p>
      <p :class="['text-xs sm:text-sm mt-2', trend > 0 ? 'text-green-600' : 'text-red-600']">
        {{ trend > 0 ? '+' : '' }}{{ trend }}% from last month
      </p>
    </div>
  </template>
  
  <script setup>
  defineProps({
    title: String,
    value: String,
    trend: Number,
    icon: Object
  })
  </script>