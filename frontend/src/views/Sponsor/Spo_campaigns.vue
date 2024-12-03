<script setup>
import { ref,onMounted } from 'vue'
import api from '@/services/api';
import CampaignModal from './CampaignModal.vue'
import { PlusIcon, PencilSquareIcon, TrashIcon } from '@heroicons/vue/24/outline'
import { fetchUserData } from '@/services/fetchUserData';

const isModalOpen = ref(false)
const editMode = ref(false)
const selectedCampaign = ref(null)



const campaigns=ref([])
onMounted(()=>{
  const storedUserData=localStorage.getItem('userData');
  // console.log(storedUserData)
  if(storedUserData){
    const parsedData = JSON.parse(storedUserData)
    campaigns.value=parsedData.profile.campaigns || []
  }
})


const openCreateModal = () => {
  editMode.value = false
  selectedCampaign.value = null
  isModalOpen.value = true
}

const openEditModal = (campaign) => {
  editMode.value = true
  selectedCampaign.value = { ...campaign }
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
  selectedCampaign.value = null
}

const saveCampaign = (campaignData) => {
  if (editMode.value) {
    const index = campaigns.value.findIndex(c => c.id === selectedCampaign.value.id)
    campaigns.value[index] = { ...campaigns.value[index], ...campaignData }
  } else {
    campaigns.value.push({
      id: campaigns.value.length + 1,
      ...campaignData,
      status: 'Pending'
    })
  }
  closeModal()
}

// const deleteCampaign = (id) => {
//   if (confirm('Are you sure you want to delete this campaign?')) {
//     campaigns.value = campaigns.value.filter(c => c.id !== id)
//   }
// }
const deleteCampaign = async (id) => {
  if (confirm('Are you sure you want to delete this campaign?')) {
    try {
      // Call delete API
      const response = await api.delete(`/delcampaign/${id}`)

      if (response.status === 200) {
        // Update local state after successful API response
        campaigns.value = campaigns.value.filter(c => c.id !== id)
        await fetchUserData();
        alert('Campaign deleted successfully.')
      } else {
        const error = await response.json()
        alert(`Failed to delete campaign: ${error.message}`)
      }
    } catch (error) {
      console.error('Error deleting campaign:', error)
      alert('An error occurred while deleting the campaign.')
    }
  }
}
const getStatusColor = (status) => {
  return {
    'Active': 'bg-green-100 text-green-800',
    'Pending': 'bg-yellow-100 text-yellow-800',
    'Completed': 'bg-gray-100 text-gray-800'
  }[status] || 'bg-gray-100 text-gray-800'
}
</script>

<template>
  <div class="min-h-screen bg-gray-50 p-6">
    <div class="max-w-7xl mx-auto">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold text-gray-900">Campaign Management</h1>
        <button
          @click="openCreateModal"
          class="inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          <PlusIcon class="h-5 w-5 mr-2" />
          Create Campaign
        </button>
      </div>

      <div class="bg-white shadow-sm rounded-lg overflow-hidden">
        <div class="grid grid-cols-3 gap-4 sm:gap-6 p-6">
          <template v-if="campaigns.length">
            <div v-for="campaign in campaigns" :key="campaign.id" 
                 class="bg-white border rounded-lg p-6 shadow-sm hover:shadow-md transition-shadow">
              <div class="flex justify-between items-start">
                <div>
                  <h3 class="text-xl font-semibold text-gray-900">{{ campaign.name }}</h3>
                  <span :class="['inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium mt-2', getStatusColor(campaign.status)]">
                    {{ campaign.status }}
                  </span>
                </div>
                <div class="flex space-x-2">
                  <button
                    @click="openEditModal(campaign)"
                    class="p-2 text-gray-400 hover:text-gray-500 rounded-full hover:bg-gray-100"
                  >
                    <PencilSquareIcon class="h-5 w-5" />
                  </button>
                  <button
                    @click="deleteCampaign(campaign.id)"
                    class="p-2 text-red-400 hover:text-red-500 rounded-full hover:bg-red-50"
                  >
                    <TrashIcon class="h-5 w-5" />
                  </button>
                </div>
              </div>

              <div class="mt-4 grid grid-cols-2 gap-4">
                <div>
                  <p class="text-sm font-medium text-gray-500">Budget</p>
                  <p class="mt-1 text-sm text-gray-900">₹ {{ campaign.budget }}</p>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-500">Niche</p>
                  <p class="mt-1 text-sm text-gray-900">{{ campaign.niche }}</p>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-500">Start Date</p>
                  <p class="mt-1 text-sm text-gray-900">{{ new Date(campaign.start_date).toLocaleDateString() }}</p>
                </div>
                <div>
                  <p class="text-sm font-medium text-gray-500">End Date</p>
                  <p class="mt-1 text-sm text-gray-900">{{ new Date(campaign.end_date).toLocaleDateString() }}</p>
                </div>
              </div>

              <div class="mt-4">
                <p class="text-sm font-medium text-gray-500">Message</p>
                <p class="mt-1 text-sm text-gray-900">{{ campaign.description }}</p>
              </div>
            </div>
          </template>
          <div v-else class="text-center py-12">
            <p class="text-gray-500">No campaigns found. Create your first campaign!</p>
          </div>
        </div>
      </div>
    </div>

    <CampaignModal
      :is-open="isModalOpen"
      :edit-mode="editMode"
      :campaign="selectedCampaign"
      @close="closeModal"
      @save="saveCampaign"
    />
  </div>
</template>
