<script setup lang="ts">
import { ref,onMounted } from 'vue';

import CampaignCard from '@/views/Influencer/CampaignCard.vue';
import RequestCard from '@/views/Influencer/RequestCard.vue';
import { fetchUserData } from '@/services/fetchUserData';
import api from '@/services/api';

const ongoingCampaigns = ref([]);
const incomingRequests = ref([]);

onMounted(() => {
  const storedData = JSON.parse(localStorage.getItem('userData'));

  if (storedData && storedData.profile && storedData.profile.ad_requests) {
    const adRequests = storedData.profile.ad_requests;
    const allCampaigns = storedData.all_campaigns;

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
          sponsor_name:request.sponsor_name,
          by:request.by.toLowerCase()
        };

        if (requestDetails.status === 'pending' && requestDetails.by === 'sponsor') {
          incomingRequests.value.push(requestDetails);
        } else if (requestDetails.status === 'accepted') {
          ongoingCampaigns.value.push(requestDetails);
        }
      }
    });
  }
});
const handleAccept = async (requestId) => {
  try {
    const response = await api.post(`/ad_request/${requestId}/accept`, {
      // by: 'sponsor', // Change this value based on the user role
      message: 'Accepted request'
    });

    if (response.status === 200) {
      const request = incomingRequests.value.find(r => r.id === requestId);
      if (request) {
        incomingRequests.value = incomingRequests.value.filter(r => r.id !== requestId);
        const startDate = new Date();
        const endDate = new Date();
        endDate.setDate(endDate.getDate() + 
          (request.duration.includes('month') ? 30 : 
          request.duration.includes('week') ? 7 * parseInt(request.duration) : 
          parseInt(request.duration)));
        
        const campaign = {
          ...request,
          
          startDate: startDate.toISOString().split('T')[0],
          endDate: endDate.toISOString().split('T')[0]
        };
        ongoingCampaigns.value.push(campaign);
       
      }
    }
  } catch (error) {
    console.error('Error accepting request:', error);
    alert('Failed to accept request. Please try again later.');
  }
  await fetchUserData()
  window.location.reload()
};

const handleReject = async (requestId) => {
  try {
    const response = await api.post(`/ad_request/${requestId}/reject`, {
      // by: 'sponsor', // Change this value based on the user role
      message: 'Rejected request'
    });

    if (response.status === 200) {
      incomingRequests.value = incomingRequests.value.filter(r => r.id !== requestId);
    }
    await fetchUserData()
  } catch (error) {
    console.error('Error rejecting request:', error);
    alert('Failed to reject request. Please try again later.');
  }
};
</script>

<template>
  <div class="min-h-screen">
  

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Ongoing Campaigns Section -->
      <section class="mb-12">
        <h2 class="text-xl font-semibold text-gray-900 mb-6">Ongoing Campaigns</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <CampaignCard v-for="campaign in ongoingCampaigns" :key="campaign.id" :campaign="campaign" />
        </div>
      </section>

      <!-- Incoming Requests Section -->
      <section>
        <h2 class="text-xl font-semibold text-gray-900 mb-6">Incoming Requests</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <RequestCard v-for="request in incomingRequests" :key="request.id" :request="request" @accept="handleAccept" @reject="handleReject" />
        </div>
      </section>
    </main>
  </div>
</template>