<script setup>
import { ref } from 'vue'

const emit = defineEmits(['update:filters'])

const niches = ['Fashion', 'Tech', 'Food', 'Travel', 'Fitness', 'Beauty', 'Gaming', 'Lifestyle']


const filters = ref({
  search: '',
  niche: '',
  
  minFollowers: '',
  maxFollowers: '',
  
})

const updateFilters = () => {
  emit('update:filters', filters.value)
}
</script>

<template>
  <div class="bg-white rounded-lg shadow-md p-6 mb-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <!-- Search -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">Search</label>
        <input
          type="text"
          v-model="filters.search"
          @input="updateFilters"
          placeholder="Search influencers..."
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-purple-500 focus:border-purple-500"
        />
      </div>

      <!-- Niche -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">Niche</label>
        <select
          v-model="filters.niche"
          @change="updateFilters"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-purple-500 focus:border-purple-500"
        >
          <option value="">All Niches</option>
          <option v-for="niche in niches" :key="niche" :value="niche">
            {{ niche }}
          </option>
        </select>
      </div>

   


      <div>
        <label class="block text-sm font-medium text-gray-700 mb-2">Max Followers</label>
        <input
          type="number"
          v-model="filters.maxFollowers"
          @input="updateFilters"
          placeholder="Max followers"
          class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-purple-500 focus:border-purple-500"
        />
      </div>

    
   
    </div>
  </div>
</template>