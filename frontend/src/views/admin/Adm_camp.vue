<script setup>
import { ref, computed } from 'vue'
import CardGrid from './CardGrid.vue'
import ActionButton from './ActionButton.vue'
import SearchBar from './SearchBar.vue'
import { FlagIcon, TrashIcon } from '@heroicons/vue/24/outline'

const searchQuery = ref('')

const campaigns = ref([
  {
    id: 2,
    name: "Samsung Campaign",
    description: "Exciting Samsung deals",
    goals: "Increase brand awareness",
    budget: 18500,
    niche: "Tech",
    start_date: "2024-06-01T00:00:00",
    end_date: "2024-08-31T00:00:00",
    sponsor: {
      id: 1,
      name: "abhi",
      username: "sponsor_user"
    }
  }
])

const filteredCampaigns = computed(() => {
  const query = searchQuery.value.toLowerCase()
  return campaigns.value.filter(campaign => 
    campaign.name.toLowerCase().includes(query) ||
    campaign.description.toLowerCase().includes(query) ||
    campaign.niche.toLowerCase().includes(query) ||
    campaign.sponsor.name.toLowerCase().includes(query)
  )
})

const handleFlag = (id) => {
  console.log('Flag campaign:', id)
}

const handleDelete = (id) => {
  console.log('Delete campaign:', id)
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString()
}
</script>

<template>
  <CardGrid title="All Campaigns">
    <template #search>
      <SearchBar 
        v-model="searchQuery"
        placeholder="Search campaigns..."
      />
    </template>

    <div v-for="campaign in filteredCampaigns" :key="campaign.id"
      class="bg-white rounded-xl shadow-lg overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
      <div class="p-6 space-y-4">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-xl font-bold text-gray-900">{{ campaign.name }}</h3>
            <p class="text-sm text-blue-600 font-medium">
              by {{ campaign.sponsor.name }} (@{{ campaign.sponsor.username }})
            </p>
          </div>
          <div class="flex space-x-2">
            <ActionButton variant="warning" @click="handleFlag(campaign.id)">
              <FlagIcon class="h-4 w-4 mr-1" />
              Flag
            </ActionButton>
            <ActionButton variant="danger" @click="handleDelete(campaign.id)">
              <TrashIcon class="h-4 w-4 mr-1" />
              Delete
            </ActionButton>
          </div>
        </div>

        <p class="text-gray-700">{{ campaign.description }}</p>

        <div class="grid grid-cols-2 gap-4">
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Goals</span>
            <span class="font-semibold text-gray-900">{{ campaign.goals }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Budget</span>
            <span class="font-semibold text-gray-900">${{ campaign.budget.toLocaleString() }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Niche</span>
            <span class="font-semibold text-gray-900">{{ campaign.niche }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Duration</span>
            <span class="font-semibold text-gray-900">{{ formatDate(campaign.start_date) }} - {{ formatDate(campaign.end_date) }}</span>
          </div>
        </div>
      </div>
    </div>
  </CardGrid>
</template>