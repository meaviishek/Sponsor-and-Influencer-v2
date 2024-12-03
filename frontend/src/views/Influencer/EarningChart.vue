<template>
    <div class="bg-white rounded-xl shadow-lg p-4 sm:p-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-6 gap-4">
        <h2 class="text-lg sm:text-xl font-bold text-gray-900">Earnings Overview</h2>
        <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center">
          <div class="text-sm text-gray-500">
            Total: <span class="font-bold text-gray-900">${{ totalEarnings.toLocaleString() }}</span>
          </div>
          <select v-model="timeframe" 
                  class="w-full sm:w-auto bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-indigo-500 focus:border-indigo-500 p-2">
            <option value="24h">Last 24 Hours</option>
            <option value="7d">Last 7 Days</option>
            <option value="30d">Last 30 Days</option>
            <option value="1y">Last Year</option>
          </select>
        </div>
      </div>
      <div class="h-[250px] sm:h-[300px]">
        <Line :data="chartData" :options="chartOptions" />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue'
  import { Line } from 'vue-chartjs'
  import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
  } from 'chart.js'
  
  ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
  )
  
  const timeframe = ref('30d')
  
  const earningsData = {
    '24h': {
      labels: ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'],
      data: [1200, 1500, 2000, 1800, 2200, 2500],
    },
    '7d': {
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      data: [5000, 4500, 6000, 5500, 7000, 6500, 7500],
    },
    '30d': {
      labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
      data: [20000, 25000, 22000, 28000],
    },
    '1y': {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      data: [65000, 70000, 80000, 75000, 85000, 90000, 88000, 92000, 95000, 98000, 100000, 105000],
    },
  }
  
  const chartData = computed(() => ({
    labels: earningsData[timeframe.value].labels,
    datasets: [
      {
        label: 'Earnings',
        data: earningsData[timeframe.value].data,
        fill: true,
        borderColor: '#6366f1',
        backgroundColor: 'rgba(99, 102, 241, 0.1)',
        tension: 0.4,
      },
    ],
  }))
  
  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        mode: 'index',
        intersect: false,
        callbacks: {
          label: (context) => `$${context.raw.toLocaleString()}`,
        },
      },
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: (value) => `$${value.toLocaleString()}`,
        },
      },
    },
  }
  
  const totalEarnings = computed(() => {
    return earningsData[timeframe.value].data.reduce((sum, value) => sum + value, 0)
  })
  </script>