<script setup>
import api from '@/services/api';
import { fetchUserData } from '@/services/fetchUserData';
import { ref } from 'vue';
const props=defineProps({
  influencer: {
    type: Object,
    required: true
  }
})

const isModalOpen = ref(false)
const selectedCampaign = ref(null)
const successMessage = ref("");
const errorMessage = ref("");
const isRequestMade = ref(false);
const paymentAmount = ref('')
const campaigns = ref([]) // List of campaigns
const openModal = async () => {
  try {
    isModalOpen.value = true
    const userData = JSON.parse(localStorage.getItem('userData'))
    campaigns.value = userData.profile.campaigns || []
  } catch (error) {
    console.error('Failed to fetch campaigns:', error)
    alert('Error fetching campaigns. Please try again later.')
  }
}

// console.log(props.influencer.id)

const closeModal = () => {
  isModalOpen.value = false
  selectedCampaign.value = null
  paymentAmount.value = ''
}

const sendAdRequest = async () => {
  try {
    if (!selectedCampaign.value) {
      alert('Please select a campaign.')
      return
    }
    const campaign = campaigns.value.find(c => c.id === selectedCampaign.value);
    const budget = campaign ? campaign.budget : 0;
    const response = await api.post(
      '/adr_inf',
      {
        influencer_id: props.influencer.id,
        campaign_id: selectedCampaign.value,
        payment_amount: paymentAmount.value || budget,
        by: 'Sponsor' 
      })
      if(response){
      isRequestMade.value = true;

    successMessage.value = "Application sent successfully!";}

    await fetchUserData()
    window.location.reload()

    alert(response.data.message || 'Ad request created successfully!')
    closeModal()
  } catch (error) {
    console.error('Failed to send ad request:', error.response?.data || error.message)
    alert('Error sending ad request: ' + (error.response?.data?.error || error.message))
  }
}
</script>

<template>
  <div class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
    <div class="p-6">
      <div class="flex items-center space-x-4">
        <img src="https://i.pravatar.cc/150?img=1" class="w-16 h-16 rounded-full object-cover" />
        <div>
          <h3 class="text-lg font-semibold text-gray-800">{{ influencer.name }}</h3>
          <p class="text-sm text-gray-600">{{ influencer.user_name }}</p>
        </div>
      </div>
      
      <div class="mt-4">
        <div class="flex items-center space-x-2">
          <span class="px-3 py-1 bg-purple-100 text-purple-800 rounded-full text-sm">
            {{ influencer.niche }}
          </span>
        </div>
        
        <div class="mt-4 grid grid-cols-2 gap-4">
          <div>
            <p class="text-sm text-gray-600">Followers</p>
            <p class="text-lg font-semibold">{{ influencer.followers.toLocaleString() }}</p>
          </div>
          <div>
            <p class="text-sm text-gray-600">Reach</p>
            <p class="text-lg font-semibold">{{ influencer.reach.toLocaleString() }}</p>
          </div>
        </div>

        <div class="mt-4">
          <p class="text-sm text-gray-600">Category</p>
          <p class="text-lg font-semibold">{{ influencer.category }}</p>
        </div>
      </div>

      <button @click="openModal" class="mt-6 w-full bg-purple-600 text-white py-2 px-4 rounded-lg hover:bg-purple-700 transition-colors duration-300">
        Send Ad Request

      </button>
    </div>
  </div>



  <div v-if="isModalOpen" class="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center">
    <div class="bg-white p-6 rounded-lg w-96">
      <h2 class="text-lg font-bold mb-4">Select a Campaign</h2>
      <div class="space-y-4">
        <select v-model="selectedCampaign" class="w-full border rounded-lg p-2">
          <option disabled value="">-- Select Campaign --</option>
          <option v-for="campaign in campaigns" :key="campaign.id" :value="campaign.id">
            {{ campaign.description }}
          </option>
        </select>

        <input
          type="number"
          v-model="paymentAmount"
       
          class="w-full border rounded-lg p-2"
          placeholder="Enter payment amount (optional)"
        />
      </div>

      <div class="flex justify-end mt-4 space-x-2">
        <button @click="closeModal" class="bg-gray-300 text-gray-800 px-4 py-2 rounded-lg hover:bg-gray-400">
          Cancel
        </button>
        <button @click="sendAdRequest" class="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700">
          Submit
        </button>
      </div>
    </div>
  </div>
</template>