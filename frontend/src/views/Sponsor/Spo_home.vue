<script setup>
import { onMounted, ref } from 'vue'
import OngoingCampaign from './OngoingCampaign.vue'
import SponsorRequest from './SponsorRequest.vue'
import api from '@/services/api';
import { fetchUserData } from '@/services/fetchUserData';


const ongoingCampaigns = ref([]);
const incomingRequests = ref([]);
const requestSent=ref([])

onMounted(()=>{
  const storedData = JSON.parse(localStorage.getItem('userData'));

  if (storedData && storedData.profile && storedData.profile.campaigns) {
    const campaigns = storedData.profile.campaigns;

    campaigns.forEach((campaign) => {
      if (campaign.ad_requests) {
        campaign.ad_requests.forEach((request) => {
          const requestDetails = {
            id: request.id,
            influencer: {
              name: storedData.all_influencers.find(
                (influencer) => influencer.id === request.influencer_id
              )?.name || 'Unknown Influencer',
              avatar: 'https://i.pravatar.cc/150',
              followers: storedData.all_influencers.find(
                (influencer) => influencer.id === request.influencer_id
              )?.followers || 'N/A',
            },
            price: request.payment_amount,
            description: campaign.description,
            platform: campaign.niche,
            duration:null, // Customize duration if available
            status: request.status.toLowerCase(),
            by:request.by.toLowerCase()
          };

          if (requestDetails.status === 'pending') {
            if(requestDetails.by === 'sponsor'){
              requestSent.value.push(requestDetails)
            }else{
            incomingRequests.value.push(requestDetails);
          }
          } else if (requestDetails.status === 'accepted') {
            const startDate = new Date(campaign.start_date);
            const endDate = new Date(campaign.end_date);
            ongoingCampaigns.value.push({
              ...requestDetails,
              startDate: startDate.toISOString().split('T')[0],
              endDate: endDate.toISOString().split('T')[0],
            });
          }
        });
      }
    });
  }
})


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
          status: 'ongoing',
          startDate: startDate.toISOString().split('T')[0],
          endDate: endDate.toISOString().split('T')[0]
        };
        ongoingCampaigns.value.push(campaign);
        await fetchUserData()
      }
    }
  } catch (error) {
    console.error('Error accepting request:', error);
    alert('Failed to accept request. Please try again later.');
  }
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


const parseDuration = (duration) => {
  if (duration.includes('month')) return 30;
  if (duration.includes('week')) return 7 * parseInt(duration.match(/\d+/));
  if (duration.includes('day')) return parseInt(duration.match(/\d+/));
  return 0; // Default fallback
};




</script>

<template>
  <div class="min-h-screen ">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

      
      <!-- Ongoing Campaigns -->
      <div class="mb-12">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-4">
          <h2 class="text-xl font-semibold text-gray-900 mb-2 sm:mb-0">
            Ongoing Campaigns
            <span class="ml-2 px-2 py-1 text-sm bg-green-100 text-green-800 rounded-full">
              {{ ongoingCampaigns.length }}
            </span>
          </h2>
          <div class="text-sm text-gray-500">
            Showing all active campaigns
          </div>
        </div>
        
        <div v-if="ongoingCampaigns.length === 0" class="text-gray-500 text-center py-8 bg-white rounded-lg shadow-sm">
          No ongoing campaigns
        </div>
        <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          <OngoingCampaign
            v-for="campaign in ongoingCampaigns"
            :key="campaign.id"
            :campaign="campaign"
          />
        </div>
      </div>
      
      <!-- New Requests -->
      <div>
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-4">
          <h2 class="text-xl font-semibold text-gray-900 mb-2 sm:mb-0">
            New Requests
            <span class="ml-2 px-2 py-1 text-sm bg-blue-100 text-blue-800 rounded-full">
              {{ incomingRequests.length }}
            </span>
          </h2>
        </div>
        
        <div v-if="incomingRequests.length === 0" class="text-gray-500 text-center py-8 bg-white rounded-lg shadow-sm">
          No incoming requests at the moment
        </div>
        <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <SponsorRequest
            v-for="request in incomingRequests"
            :key="request.id"
            :request="request"
            @accept="handleAccept"
            @reject="handleReject"
          />
        </div>
      </div>




      <div>
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-4">
          <h2 class="text-xl font-semibold text-gray-900 mb-2 sm:mb-0">
            Requests Sent
            <span class="ml-2 px-2 py-1 text-sm bg-blue-100 text-blue-800 rounded-full">
              {{ requestSent.length }}
            </span>
          </h2>
        </div>
        
        <div v-if="requestSent.length === 0" class="text-gray-500 text-center py-8 bg-white rounded-lg shadow-sm">
          No requests sent at the moment
        </div>
        <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <!-- <SponsorRequest
            v-for="request in incomingRequests"
            :key="request.id"
            :request="request"
            @accept="handleAccept"
            @reject="handleReject"
          /> -->
      <div v-for="request in requestSent" :key="request.id">
          <div class="bg-white rounded-lg shadow-md p-6 mb-4">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-4">
        <img :src="request.influencer.avatar" :alt="request.influencer.name" class="w-12 h-12 rounded-full">
        <div>
          <h3 class="font-semibold text-lg">{{ request.influencer.name }}</h3>
          <p class="text-gray-600">{{ request.influencer.followers }} followers</p>
        </div>
      </div>
      <div class="text-right">
        <p class="text-2xl font-bold text-gray-900">${{ request.price }}</p>
        <p class="text-sm text-gray-500">Proposed Price</p>
      </div>
    </div>
    
    <div class="mb-4">
      <h4 class="font-medium mb-2">Campaign Details</h4>
      <p class="text-gray-600">{{ request.description }}</p>
    </div>
    
    <div class="flex justify-between items-center">
      <div class="text-sm text-gray-500">
        <span>Platform: {{ request.platform }}</span>
        <span class="mx-2">•</span>
        <span>Duration: {{ request.duration }}</span>
      </div>
      <div class="space-x-3">
        <!-- <button
          @click="emit('reject', request.id)"
          class="px-4 py-2 border border-red-500 text-red-500 rounded-lg hover:bg-red-50 transition-colors"
        >
          Reject
        </button> -->
        <button
          disabled
          class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
        >
          Request sent
        </button>
      </div>
    </div>
  </div>
</div>
        </div>
      </div>
    </div>
  </div>
</template>



