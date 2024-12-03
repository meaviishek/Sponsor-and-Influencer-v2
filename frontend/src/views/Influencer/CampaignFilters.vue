<script setup>
import { ref } from 'vue';

const emit = defineEmits(['filter']);

const categories = [
  'Tech', 'Fashion', 'Beauty', 'Gaming', 'Fitness', 
  'Food', 'Travel', 'Lifestyle', 'Education', 'Entertainment'
];

const budgetRanges = [
  { label: 'Under $1,000', value: '0-1000' },
  { label: '$1,000 - $5,000', value: '1000-5000' },
  { label: '$5,000 - $10,000', value: '5000-10000' },
  { label: 'Over $10,000', value: '10000-plus' }
];

const selectedCategories = ref([]);
const selectedBudgetRange = ref('');
const searchQuery = ref('');

const updateFilters = () => {
  emit('filter', {
    categories: selectedCategories.value,
    budgetRange: selectedBudgetRange.value,
    search: searchQuery.value
  });
};
</script>

<template>
  <div class="bg-white p-6 rounded-lg shadow-md mb-6">
    <div class="mb-6">
      <label class="block text-sm font-medium text-gray-700 mb-2">Search Campaigns</label>
      <input
        type="text"
        v-model="searchQuery"
        @input="updateFilters"
        placeholder="Search by brand, product, or description..."
        class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
      />
    </div>

    <div class="mb-6">
      <label class="block text-sm font-medium text-gray-700 mb-2">Categories</label>
      <div class="flex flex-wrap gap-2">
        <button
          v-for="category in categories"
          :key="category"
          @click="() => {
            const index = selectedCategories.indexOf(category);
            if (index === -1) {
              selectedCategories.push(category);
            } else {
              selectedCategories.splice(index, 1);
            }
            updateFilters();
          }"
          :class="[
            'px-3 py-1 rounded-full text-sm font-medium transition-colors',
            selectedCategories.includes(category)
              ? 'bg-indigo-100 text-indigo-800'
              : 'bg-gray-100 text-gray-800 hover:bg-gray-200'
          ]"
        >
          {{ category }}
        </button>
      </div>
    </div>

    <div>
      <label class="block text-sm font-medium text-gray-700 mb-2">Budget Range</label>
      <select
        v-model="selectedBudgetRange"
        @change="updateFilters"
        class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
      >
        <option value="">All Budgets</option>
        <option v-for="range in budgetRanges" :key="range.value" :value="range.value">
          {{ range.label }}
        </option>
      </select>
    </div>
  </div>
</template>