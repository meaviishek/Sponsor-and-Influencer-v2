<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary'
  }
})
</script>

<template>
  <button
    class="inline-flex items-center px-3 py-1.5 text-sm font-medium rounded-md transition-colors"
    :class="{
      'bg-red-100 text-red-700 hover:bg-red-200': variant === 'danger',
      'bg-blue-100 text-blue-700 hover:bg-blue-200': variant === 'primary',
      'bg-yellow-100 text-yellow-700 hover:bg-yellow-200': variant === 'warning'
    }"
  >
    <slot></slot>
  </button>
</template>