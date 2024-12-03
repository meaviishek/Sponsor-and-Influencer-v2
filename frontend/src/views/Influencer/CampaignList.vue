<template>
    <div class="bg-white rounded-xl shadow-lg p-4 sm:p-6">
      <h2 class="text-lg sm:text-xl font-bold text-gray-900 mb-4 sm:mb-6">Active Campaigns</h2>
      <div class="space-y-3 sm:space-y-4">
        <div v-for="campaign in campaigns" :key="campaign.id" 
             class="flex flex-col sm:flex-row sm:items-center justify-between p-3 sm:p-4 rounded-lg hover:bg-gray-50 transition-colors duration-200 gap-3 sm:gap-4">
          <div class="flex items-center space-x-3 sm:space-x-4">
            <img src="https://i.pravatar.cc/300" alt="" class="w-10 h-10 sm:w-12 sm:h-12 rounded-full object-cover"/>
            <div>
              <h3 class="font-semibold text-gray-900">{{ campaign.name }}</h3>
              <p class="text-xs sm:text-sm text-gray-500">{{ campaign.description }}</p>
            </div>
          </div>
          <div class="flex sm:flex-col items-center sm:items-end justify-between sm:text-right">
            <p class="font-bold text-gray-900">₹{{ campaign.price.toLocaleString() }}</p>
            <p :class="['text-xs sm:text-sm', campaign.status === 'In Progress' ? 'text-yellow-600' : 'text-green-600']">
              {{ campaign.status }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
import { ref,onMounted } from 'vue'


const campaigns = ref([]);
onMounted(()=>{
  const storedUserData=JSON.parse(localStorage.getItem('userData'));
  if(storedUserData){ 
    const allCampaigns = storedUserData.all_campaigns;
    const adRequests = storedUserData.profile.ad_requests;
    adRequests.forEach((request) => {
      const campaign = allCampaigns.find((c) => c.id === request.campaign_id);
      if (campaign) {
        const requestDetails = {
          id: request.id,
          name: campaign.name,
          description: campaign.description,
          platform: campaign.niche,
          price: request.payment_amount,
          startDate: campaign.start_date.split('T')[0],
          endDate: campaign.end_date.split('T')[0],
          status: request.status.toLowerCase(),
        };

        if (requestDetails.status === 'pending') {
          // incomingRequests.value.push(requestDetails);
        } else if (requestDetails.status === 'accepted') {
          campaigns.value.push(requestDetails);
        }
      }
    });

  }

 
});
  </script>