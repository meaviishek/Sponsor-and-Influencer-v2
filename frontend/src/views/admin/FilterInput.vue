<script setup>
defineProps({
  placeholder: {
    type: String,
    default: 'Search...'
  },
  modelValue: String
})

defineEmits(['update:modelValue'])
</script>

<template>
  <div class="relative">
    <input
      type="text"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      :placeholder="placeholder"
      class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
    />
  </div>
</template>