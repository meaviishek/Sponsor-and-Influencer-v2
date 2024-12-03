<template>
    <div class="min-h-screen bg-gray-100 flex items-center justify-center py-10 px-4">
      <div class="bg-white shadow-md rounded-lg max-w-xl w-full p-6">
        <h2 class="text-2xl font-semibold text-gray-800 text-center mb-4">Sponsor Registration</h2>
        <form @submit.prevent="handleSubmit">
          <!-- Name -->

          <div  class="grid lg:grid-cols-2 lg:gap-12">
           <div>
            <div class="mb-4">
            <label for="username" class="block text-gray-700 font-medium mb-1">Username</label>
            <input
              v-model="formData.username"
              id="username"
              type="text"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter your name"
              required
            />
          </div>
          <div class="mb-4">
            <label for="name" class="block text-gray-700 font-medium mb-1">Sponsor Name</label>
            <input
              v-model="formData.name"
              id="name"
              type="text"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter your name"
              required
            />
          </div>
  
          <!-- Email -->
          <div class="mb-4">
            <label for="email" class="block text-gray-700 font-medium mb-1">Email</label>
            <input
              v-model="formData.email"
              id="email"
              type="email"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter your email"
              required
            />
          </div>
  
          <div class="mb-4">
            <label for="budget" class="block text-gray-700 font-medium mb-1">Budget</label>
            <input
              v-model="formData.budget"
              id="budget"
              type="number"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter your budget"
              required
            />
          </div>
        </div>


          <!-- Company Name -->
          <div>
          <div class="mb-4">
            <label for="company" class="block text-gray-700 font-medium mb-1">Company Name</label>
            <input
              v-model="formData.company_name"
              id="company"
              type="text"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter your company name"
              required
            />
          </div>
          <div class="mb-4">
            <label for="industry" class="block text-gray-700 font-medium mb-1">Industry</label>
            <input
              v-model="formData.industry"
              id="industry"
              type="text"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter Industry"
              required
            />
          </div>
          <div class="mb-4">
            <label for="password" class="block text-gray-700 font-medium mb-1">Password</label>
            <input
              v-model="formData.password"
              id="password"
              type="password"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter Password"
              required
            />
          </div>
          <div class="mb-4">
            <label for="passwordc" class="block text-gray-700 font-medium mb-1">Confirm Password</label>
            <input
              v-model="formData.password"
              id="passwordc"
              type="password"
              class="w-full px-4 py-2 border rounded-lg focus:ring focus:ring-blue-300"
              placeholder="Enter Password"
              required
            />
          </div>
      

      

        </div>
    </div>
    <div class="flex items-start mb-4">
                      <div class="flex items-center h-5">
                        <input id="terms" aria-describedby="terms" type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-primary-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-primary-600 dark:ring-offset-gray-800" required="">
                      </div>
                      <div class="ml-3 text-sm">
                        <label for="terms" class="font-light text-gray-900 ">I accept the <a class="font-medium text-primary-600 hover:underline dark:text-primary-500" href="#">Terms and Conditions</a></label>
                      </div>
                  </div>
          <button
            type="submit"
            class="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition"
          >
            Register
          </button>
          <div class="text-center mt-4">
            <router-link to="/" class="text-blue-600  hover:text-blue-800 transition">
                Already have an account? Login here

            </router-link>
            </div>

        </form>
      </div>
    </div>
  </template>
  
  <script>
  import api from '@/services/api';
  export default {
    data() {
      return {
        formData: {
          username: "",
  name:"",
  email: "",
  password: "",
  role: "sponsor",
  company_name: "",
  industry: "",
  budget:0
        },
      };
    },
    methods: {
      async handleSubmit() {
      try {
        const response = await api.post('/register', this.formData);
        console.log("Registration successful:", response.data);
        alert("Registration successful!");
        this.$router.push('/'); // Redirect to login page after success
      } catch (error) {
        console.error("Error during registration:", error.response?.data || error.message);
        alert(error.response?.data?.error || "An error occurred during registration.");
      }
    },
    },
  };
  </script>
  
  <style>
  /* Add custom styles if needed */
  </style>
  