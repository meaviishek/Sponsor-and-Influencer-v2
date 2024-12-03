<script setup>
import { ref, defineEmits } from 'vue'
import api from '@/services/api';
import axios from 'axios';
import { fetchUserData } from '@/services/fetchUserData';
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'

const emit = defineEmits(['close', 'save'])

const props = defineProps({
  isOpen: Boolean,
  editMode: Boolean,
  campaign: {
    type: Object,
    default: () => ({
      name: '',
      budget: '',
      niche: '',
      description: '',
      startDate: '',
      endDate: ''
    })
  }
})

const formData = ref({ ...props.campaign })

const niches = ['Technology', 'Fashion', 'Food', 'Travel', 'Sports', 'Entertainment']

const handleSubmit = async () => {
  try {
    
    if (!formData.value.name || !formData.value.startDate || !formData.value.endDate || !formData.value.budget) {
      alert('Please fill in all required fields.');
      return;
    }
    const storedUserData=localStorage.getItem('userData');
    const parsedData = JSON.parse(storedUserData)
    const response = await api.post('/createcampaign', {
      sponsor_id: parsedData.id, // Ensure this is set during user login
      name: formData.value.name,
      start_date: formData.value.startDate,
      end_date: formData.value.endDate,
      budget: formData.value.budget,
      niche: formData.value.niche,
      description: formData.value.description
    });

    if (response.status === 201) {
      alert('Campaign created successfully!');
      await fetchUserData();
   
      emit('save', response.data.campaign);

    
      formData.value = {
        name: '',
        budget: '',
        niche: '',
        description: '',
        startDate: '',
        endDate: ''
      };

      // Close dialog
      emit('close');
    }
    await fetchUserData();
    window.location.reload()
  } catch (error) {
    console.error('Error creating campaign:', error.response?.data || error.message);
    alert('Failed to create campaign: ' + (error.response?.data?.error || error.message));
  }
};
</script>

<template>
  <TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" class="relative z-10" @close="$emit('close')">
      <TransitionChild
        enter="ease-out duration-300"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in duration-200"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-black/25" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-y-auto">
        <div class="flex min-h-full items-center justify-center p-4">
          <TransitionChild
            enter="ease-out duration-300"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="ease-in duration-200"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <DialogPanel class="w-full  transform overflow-hidden rounded-2xl bg-gray-50 p-6 text-left align-middle shadow-xl transition-all">
              <div class="flex items-center justify-between mb-4">
                <DialogTitle class="text-xl font-semibold leading-6 text-gray-900">
                  {{ editMode ? 'Edit Campaign' : 'Create New Campaign' }}
                </DialogTitle>
                <button
                  type="button"
                  class="text-gray-400 hover:text-gray-500"
                  @click="$emit('close')"
                >
                  <XMarkIcon class="h-6 w-6" />
                </button>
              </div>

              <form @submit.prevent="handleSubmit" class=" grid grid-cols-2 gap-2">
                <div>
                  <label class="block text-sm font-medium text-gray-700">Campaign Name</label>
                  <input
                    type="text"
                    v-model="formData.name"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border"
                    required
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700">Budget</label>
                  <input
                    type="number"
                    v-model="formData.budget"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border"
                    required
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700">Niche</label>
                  <select
                    v-model="formData.niche"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border"
                    required
                  >
                    <option value="">Select a niche</option>
                    <option v-for="niche in niches" :key="niche" :value="niche">
                      {{ niche }}
                    </option>
                  </select>
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700">Start Date</label>
                  <input
                    type="date"
                    v-model="formData.startDate"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border"
                    required
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700">End Date</label>
                  <input
                    type="date"
                    v-model="formData.endDate"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border"
                    required
                  />
                </div>

                <div>
                  <label class="block text-sm font-medium text-gray-700">Message</label>
                  <textarea
                    v-model="formData.description"
                    rows="3"
                    class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm p-2 border"
                    required
                  ></textarea>
                </div>

                <div class="mt-6">
                  <button
                    type="submit"
                    class="w-full inline-flex justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white hover:bg-indigo-700 focus:outline-none focus-visible:ring-2 focus-visible:ring-indigo-500 focus-visible:ring-offset-2"
                  >
                    {{ editMode ? 'Update Campaign' : 'Create Campaign' }}
                  </button>
                </div>
              </form>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>