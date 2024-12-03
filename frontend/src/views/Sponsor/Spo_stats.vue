<script setup>
import StatsCard from './StatsCard.vue'
import CampaignChart from './CampaignChart.vue'
</script>

<template>
  <div class="min-h-screen p-8">
    <div class="max-w-7xl mx-auto">
      <h1 class="text-3xl font-bold text-gray-900 mb-8">Sponsor Dashboard</h1>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <StatsCard 
          title="Active Campaigns"
          value="25"
          icon="i-heroicons-chart-bar"
          :trend="15"
        />
        <StatsCard 
          title="Total Campaigns"
          value="142"
          icon="i-heroicons-document-text"
          :trend="8"
        />
        <StatsCard 
          title="Total Investment"
          value="$847,235"
          icon="i-heroicons-currency-dollar"
          :trend="12"
        />
        <StatsCard 
          title="Average ROI"
          value="24.5%"
          icon="i-heroicons-arrow-trending-up"
          :trend="5"
        />
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <CampaignChart />
        
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-lg font-semibold mb-4">Recent Campaigns</h3>
          <div class="space-y-4">
            <div v-for="i in 4" :key="i" class="flex items-center justify-between border-b pb-4 last:border-0">
              <div>
                <p class="font-medium">Campaign {{ i }}</p>
                <p class="text-sm text-gray-500">Started {{ i }} days ago</p>
              </div>
              <div class="text-right">
                <p class="font-medium">${{ Math.floor(Math.random() * 10000) }}</p>
                <p class="text-sm" :class="Math.random() > 0.5 ? 'text-green-500' : 'text-red-500'">
                  {{ Math.floor(Math.random() * 20) }}% ROI
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>