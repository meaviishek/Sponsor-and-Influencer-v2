<script setup>
import { ref, computed,onMounted } from 'vue';
import CampaignFilters from '@/views/Influencer/CampaignFilters.vue';
// import CampaignCard from './CampaignCard.vue';
import PublicCampaignCard from '@/views/Influencer/PublicCampaignCard.vue';

const campaigns=ref([])

onMounted(()=>{
  const storedUserData=localStorage.getItem('userData')

  if(storedUserData){
    const userData=JSON.parse(storedUserData)
    
    campaigns.value=userData.all_campaigns || []
  }
})


const filters = ref({
  categories: [],
  budgetRange: '',
  search: ''
});

const filteredCampaigns = computed(() => {
  return campaigns.value.filter(campaign => {
    // Category filter
    if (filters.value.categories.length > 0 && 
        !filters.value.categories.includes(campaign.niche)) {
      return false;
    }

  
    if (filters.value.budgetRange) {
      const [min, max] = filters.value.budgetRange.split('-').map(Number);
      if (max === undefined) { // For '10000-plus' case
        if (campaign.budget <= min) return false;
      } else {
        if (campaign.budget < min || campaign.budget > max) return false;
      }
    }

    
    if (filters.value.search) {
      const search = filters.value.search.toLowerCase();
      return campaign.name.toLowerCase().includes(search) ||
             campaign.sponsor.name.toLowerCase().includes(search) ||
             campaign.description.toLowerCase().includes(search);
    }

    return true;
  });
});

const updateFilters = (newFilters) => {
  filters.value = { ...filters.value, ...newFilters };
};
</script>

<template>
  <div class="min-h-screen  py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900">Discover Campaigns</h1>
        <p class="mt-2 text-gray-600">Find and apply to campaigns that match your niche and audience.</p>
      </div>

      <CampaignFilters @filter="updateFilters" />

      <div v-if="filteredCampaigns.length > 0" class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <PublicCampaignCard
          v-for="campaign in filteredCampaigns"
          :key="campaign.id"
          :campaign="campaign"
        />
      </div>

      <div v-else class="text-center py-12">
        <h3 class="text-lg font-medium text-gray-900 mb-2">No campaigns found</h3>
        <p class="text-gray-600">Try adjusting your filters or search criteria</p>
      </div>
    </div>
  </div>
</template>