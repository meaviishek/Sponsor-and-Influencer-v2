<script setup>
import { ref, computed,onMounted } from 'vue'
import CardGrid from './CardGrid.vue'
import ActionButton from './ActionButton.vue'
import SearchBar from './SearchBar.vue'
import { FlagIcon, TrashIcon } from '@heroicons/vue/24/outline'
import api from '@/services/api'
import { fetchUserData } from '@/services/fetchUserData'

const searchQuery = ref('')

const influencers = ref([])

// Fetch influencers from local storage on load
onMounted(() => {
  const userData = JSON.parse(localStorage.getItem('userData'))
  influencers.value = userData?.all_influencers || []
})

const filteredInfluencers = computed(() => {
  const query = searchQuery.value.toLowerCase()
  return influencers.value.filter(influencer => 
    influencer.name.toLowerCase().includes(query) ||
    influencer.username.toLowerCase().includes(query) ||
    influencer.category.toLowerCase().includes(query) ||
    influencer.niche.toLowerCase().includes(query)
  )
})

const handleFlag = async (id) => {
  try {
    const token = localStorage.getItem('accessToken');
    const response = await api.post(
      `/users/${id}/flag`,
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )
    const influencer = influencers.value.find(inf => inf.id === id)
    if (influencer) {
      influencer.approved = !influencer.approved
    }
    alert(response.data.message || 'User flagged/unflagged successfully')
    await fetchUserData()
    window.location.reload()
  } catch (error) {
    console.error('Failed to flag user:', error.response?.data || error.message)
    alert('Error flagging user: ' + (error.response?.data?.error || error.message))
  }
}

const handleDelete = async (id) => {
  try {
    const token = localStorage.getItem('accessToken');
    const response = await api.delete(`/users/${id}`, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
    influencers.value = influencers.value.filter(influencer => influencer.id !== id)
    alert(response.data.message || 'User deleted successfully')
  } catch (error) {
    console.error('Failed to delete user:', error.response?.data || error.message)
    alert('Error deleting user: ' + (error.response?.data?.error || error.message))
  }
}
</script>

<template>
  <CardGrid title="All Influencers">
    <template #search>
      <SearchBar 
        v-model="searchQuery"
        placeholder="Search by name, username, category, or niche..."
      />
    </template>

    <div v-for="influencer in filteredInfluencers" :key="influencer.id"
      class="bg-white rounded-xl shadow-lg overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
      <div class="p-6 space-y-4">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-xl font-bold text-gray-900">{{ influencer.name }}</h3>
            <p class="text-sm text-blue-600 font-medium">@{{ influencer.username }}</p>
          </div>
          <div class="flex space-x-2">
            <ActionButton variant="warning" @click="handleFlag(influencer.user_id)">
              <FlagIcon class="h-4 w-4 mr-1" />
              {{ influencer.approved ? 'Flag' : 'Flagged' }}

            </ActionButton>
            <ActionButton variant="danger" @click="handleDelete(influencer.user_id)">
              <TrashIcon class="h-4 w-4 mr-1" />
              Delete
            </ActionButton>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Category</span>
            <span class="font-semibold text-gray-900">{{ influencer.category }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Niche</span>
            <span class="font-semibold text-gray-900">{{ influencer.niche }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Followers</span>
            <span class="font-semibold text-gray-900">{{ influencer.followers.toLocaleString() }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Reach</span>
            <span class="font-semibold text-gray-900">{{ influencer.reach.toLocaleString() }}</span>
          </div>
        </div>
      </div>
    </div>
  </CardGrid>
</template>