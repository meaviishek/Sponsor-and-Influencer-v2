<script setup>
import { MagnifyingGlassIcon } from '@heroicons/vue/24/outline'

defineProps({
  modelValue: String,
  placeholder: {
    type: String,
    default: 'Search...'
  }
})

defineEmits(['update:modelValue'])
</script>

<template>
  <div class="relative mb-6">
    <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
      <MagnifyingGlassIcon class="h-5 w-5 text-gray-400" />
    </div>
    <input
      type="text"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :placeholder="placeholder"
      class="block w-full pl-10 pr-4 py-2 border border-gray-200 rounded-xl 
             focus:ring-2 focus:ring-blue-500 focus:border-blue-500 
             bg-white shadow-sm transition-all duration-200
             placeholder-gray-400 text-gray-900"
    />
  </div>
</template>