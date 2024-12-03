

<template>
  <div class="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center space-x-3">
        <img src="https://i.pravatar.cc/150" alt="" class="w-12 h-12 rounded-full object-cover" />
        <div>
          <h3 class="font-semibold text-lg">{{ campaign.name }}</h3>
          <!-- <p class="text-gray-600">{{ campaign.description }}</p> -->
        </div>
      </div>
      <span class="px-3 py-1 rounded-full text-sm font-medium bg-indigo-100 text-indigo-800">
        {{ campaign.niche }}
      </span>
    </div>
    
    <p class="text-gray-600 mb-4">{{ campaign.description }}</p>
    
    <!-- <div class="mb-4">
      <h4 class="font-medium text-gray-900 mb-2">Requirements:</h4>
      <ul class="list-disc list-inside text-gray-600">
        <li v-for="requirement in campaign.requirements" :key="requirement">
          {{ requirement }}
        </li>
      </ul>
    </div> -->

    <div class="flex justify-between items-center text-sm text-gray-600 mb-4">
      <div>
        <p>Pay: <span class="font-medium">₹ {{ campaign.budget.toLocaleString() }}</span></p>
        <p>Start Date: <span class="font-medium">{{ new Date(campaign.start_date).toLocaleDateString() }} </span></p>
        <p>End Date: <span class="font-medium">{{ new Date(campaign.start_date).toLocaleDateString() }} </span></p>
      </div>
    </div>

    <button
      @click="isRequestMade ? cancelRequest() : applyToCampaign()"
      :class="isRequestMade 
                ? 'bg-red-600 hover:bg-red-700' 
                : 'bg-indigo-600 hover:bg-indigo-700'"
      class="w-full text-white px-4 py-2 rounded-md transition-colors"
    >
      {{ isRequestMade ? "Cancel Request" : "Apply Now" }}
    </button> 

    <p v-if="successMessage" class="text-green-600 mt-3">{{ successMessage }}</p>

    <!-- Error Message -->
    <p v-if="errorMessage" class="text-red-600 mt-3">{{ errorMessage }}</p>
  </div>
</template>



<script setup>
import { ref,defineProps,onMounted } from 'vue';
import api from '@/services/api';
import { fetchUserData } from '@/services/fetchUserData';

const props=defineProps({
  campaign: {
    type: Object,
    required: true
  },
});

const isLoading = ref(false);
const successMessage = ref("");
const errorMessage = ref("");
const isRequestMade = ref(false);
const inf_id=ref(null)

const applyToCampaign = async () => {
  isLoading.value = true;
  successMessage.value = "";
  errorMessage.value = "";
 
  const storedUserData=localStorage.getItem('userData')
if(storedUserData){
  const userData = JSON.parse(storedUserData);
  inf_id.value=userData.id
}

console.log(inf_id.value)
console.log("Campaign Prop: ", props.campaign);


  try {
    const response = await api.post("/adr_inf", {
      influencer_id: inf_id.value, 
      campaign_id: props.campaign.id,
      payment_amount: props.campaign.budget,
      by: "Influencer" 
    });

    if(response){
      isRequestMade.value = true;

    successMessage.value = "Application sent successfully!";}

    await fetchUserData()

    
  } catch (error) {
    errorMessage.value = error.response?.data?.error || "Failed to apply for the campaign.";
  } finally {
    isLoading.value = false;
  }

};


const checkRequestStatus = async () => {
  const storedUserData = localStorage.getItem('userData');
  if (storedUserData) {
    const userData = JSON.parse(storedUserData);
    inf_id.value = userData.id;

    try {
      const response = await api.get(`/adr_infch/${inf_id.value}/${props.campaign.id}`);
      isRequestMade.value = response.data.exists;
      await fetchUserData()
    } catch (error) {
      console.error("Error checking request status:", error);
    }
  }
};

const cancelRequest = async () => {
  

  try {
    const response = await api.delete(`/adr_infdel/${inf_id.value}/${props.campaign.id}`);
    successMessage.value = 'Request canceled successfully!';
    isRequestMade.value = false;
    await fetchUserData()
    console.log(response.data);
  } catch (error) {
    errorMessage.value = error.response?.data?.error || 'Failed to cancel the request.';
  } finally {
    isLoading.value = false;
  }
};
onMounted(() => {
  checkRequestStatus();
});
</script>