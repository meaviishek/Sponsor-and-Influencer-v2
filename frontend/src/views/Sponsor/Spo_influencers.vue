<script setup>
import { ref, computed,onMounted } from 'vue';


import InfluencerCard from './InfluencerCard.vue';
import SearchFilters from './SearchFilters.vue';



const influencers=ref([]);

onMounted(()=>{
  const storedUserData=localStorage.getItem('userData');
  // console.log(storedUserData)
  if(storedUserData){
    const parsedData = JSON.parse(storedUserData)
    influencers.value=parsedData.all_influencers || []
  }
})


const filters = ref({
  search: '',
  niche: '',
  minFollowers: 0,
  
});

const filteredInfluencers = computed(() => {
  return influencers.value.filter(influencer => {
    const matchesSearch = !filters.value.search || 
      influencer.name.toLowerCase().includes(filters.value.search.toLowerCase()) ||
      influencer.handle.toLowerCase().includes(filters.value.search.toLowerCase());
    
    const matchesNiche = !filters.value.niche || 
      influencer.niche === filters.value.niche;
    
    const matchesFollowers = influencer.followers >= filters.value.minFollowers;


    return matchesSearch && matchesNiche && matchesFollowers;
  });
});



</script>

<template>
  <div class="min-h-screen bg-gray-100 py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <h1 class="text-3xl font-bold text-gray-900 mb-8">Find Influencers</h1>
      
      <SearchFilters @update:filters="filters = $event" />

      <div v-if="filteredInfluencers.length === 0" class="text-center py-12">
        <p class="text-gray-500 text-lg">No influencers found matching your criteria.</p>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <InfluencerCard
          v-for="influencer in filteredInfluencers"
          :key="influencer.id"
          :influencer="influencer"
        />
      </div>
    </div>
  </div>
</template>