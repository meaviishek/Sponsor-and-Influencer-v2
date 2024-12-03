<script setup>
import { ref, computed,onMounted } from 'vue'
import CardGrid from './CardGrid.vue'
import ActionButton from './ActionButton.vue'
import SearchBar from './SearchBar.vue'
import { FlagIcon, TrashIcon } from '@heroicons/vue/24/outline'
import { fetchUserData } from '@/services/fetchUserData'
import api from '@/services/api'

const searchQuery = ref('')
const sponsors=ref([])
onMounted(() => {
  const userData = JSON.parse(localStorage.getItem('userData'))
  sponsors.value = userData?.all_sponsors || []
})

const filteredSponsors = computed(() => {
  const query = searchQuery.value.toLowerCase()
  return sponsors.value.filter(sponsor => 
    sponsor.name.toLowerCase().includes(query) ||
    sponsor.username.toLowerCase().includes(query) ||
    (sponsor.company_name && sponsor.company_name.toLowerCase().includes(query)) ||
    sponsor.industry.toLowerCase().includes(query)
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
    const sponsor = sponsors.value.find(inf => inf.id === id)
    if (sponsor) {
      sponsor.approved = !sponsor.approved
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
    sponsors.value = sponsors.value.filter(sponsor => sponsor.id !== id)
    alert(response.data.message || 'User deleted successfully')
  } catch (error) {
    console.error('Failed to delete user:', error.response?.data || error.message)
    alert('Error deleting user: ' + (error.response?.data?.error || error.message))
  }}
</script>

<template>
  <CardGrid title="All Sponsors">
    <template #search>
      <SearchBar 
        v-model="searchQuery"
        placeholder="Search by name, company, or industry..."
      />
    </template>

    <div v-for="sponsor in filteredSponsors" :key="sponsor.id"
      class="bg-white rounded-xl shadow-lg overflow-hidden transform transition-all duration-300 hover:shadow-xl hover:-translate-y-1">
      <div class="p-6 space-y-4">
        <div class="flex justify-between items-start">
          <div>
            <h3 class="text-xl font-bold text-gray-900">{{ sponsor.name }}</h3>
            <p class="text-sm text-blue-600 font-medium">@{{ sponsor.username }}</p>
          </div>
          <div class="flex space-x-2">
            <ActionButton variant="warning" @click="handleFlag(sponsor.user_id)">
              <FlagIcon class="h-4 w-4 mr-1" />
              {{ sponsor.approved ? 'Flag' : 'Flagged' }}
            </ActionButton>
            <ActionButton variant="danger" @click="handleDelete(sponsor.user_id)">
              <TrashIcon class="h-4 w-4 mr-1" />
              Delete
            </ActionButton>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Company</span>
            <span class="font-semibold text-gray-900">{{ sponsor.company_name || 'Not specified' }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg">
            <span class="text-sm text-gray-600 block">Industry</span>
            <span class="font-semibold text-gray-900">{{ sponsor.industry }}</span>
          </div>
          <div class="bg-gray-50 p-3 rounded-lg col-span-2">
            <span class="text-sm text-gray-600 block">Budget</span>
            <span class="font-semibold text-gray-900">${{ sponsor.budget.toLocaleString() }}</span>
          </div>
        </div>
      </div>
    </div>
  </CardGrid>
</template>