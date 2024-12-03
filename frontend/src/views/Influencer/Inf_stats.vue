<template>
  <div class="min-h-screen ">

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <header class="mb-6 sm:mb-8">
      <h1 class="text-2xl sm:text-3xl font-bold text-gray-900">Your Stats</h1>
      <p class="text-gray-600">Welcome back, Sarah!</p>
    </header>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6 mb-6 sm:mb-8">
      <StatsCard 
      title="Total Followers"
          :value="userData?.profile.followers"
          :trend="5"
          :icon="TrendingUp"
      />
      <StatsCard 
      title="Reach"
          :value="userData?.profile.reach"
          :trend="8"
          :icon="TrendingUp"
      />
      <StatsCard 
      title="Campaigns"
          :value="userData?.all_campaigns.length"
          :trend="2"
          :icon="Target"
      />
      <StatsCard 
      title="Ad Requests"
          :value="userData?.profile.ad_requests.length"
          :trend="10"
          :icon="Clock"
      />
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-4 sm:gap-6 mb-6 sm:mb-8">
      <div class="lg:col-span-2">
        <EarningChart />
      </div>
      <div>
        <CampaignList />
      </div>
    </div>

    <!-- <div class="grid grid-cols-1">
      <RequestsTable />
    </div> -->
    </main>
  </div>
</template>

<script setup>
import { Target, TrendingUp, Clock } from 'lucide-vue-next'
import StatsCard from './StatsCard.vue'
import EarningChart from './EarningChart.vue'
import CampaignList from './CampaignList.vue'
// import RequestsTable from './components/RequestsTable.vue'
import { ref,onMounted } from 'vue'

const userData=ref(null)

onMounted(()=>{
  const storedUserData=localStorage.getItem('userData');
  if(storedUserData){
    userData.value=JSON.parse(storedUserData) 
 

  }
  console.log(userData.value)
 
});


</script>