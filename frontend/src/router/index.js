// /src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Sponsor_Reg from '../views/Sponsor_Reg.vue';
import Influencer_Reg from '@/views/Influencer_Reg.vue';
import Inf_home from '@/views/Influencer/Inf_home.vue';
// import HomePage from '../views/HomePage.vue';
import InfluencerLayout from '@/views/Influencer/InfluencerLayout.vue';
import Inf_campaigns from '@/views/Influencer/Inf_campaigns.vue';
import Inf_stats from '@/views/Influencer/Inf_stats.vue';

import SponsorLayout from '@/views/Sponsor/SponsorLayout.vue';
import Spo_influencers from '@/views/Sponsor/Spo_influencers.vue';
import Spo_campaigns from '@/views/Sponsor/Spo_campaigns.vue';
import Spo_home from '@/views/Sponsor/Spo_home.vue';
import Spo_stats from '@/views/Sponsor/Spo_stats.vue';
import AdminLayout from '@/views/admin/AdminLayout.vue';
import Adm_home from '@/views/admin/Adm_home.vue';
import Adm_camp from '@/views/admin/Adm_camp.vue';
import Adm_stats from '@/views/admin/Adm_stats.vue';
import Adm_infl from '@/views/admin/Adm_infl.vue';
import Adm_spon from '@/views/admin/Adm_spon.vue';

// Define your routes
const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path:'/sponsor_reg',
    name:'sponsor_reg',
    component:Sponsor_Reg
  },
  {  path:'/influencer_reg',
    name:'influencer_reg',
    component:Influencer_Reg

  },
  
    {
      path: '/influencer',
      name: 'Influencer',
      component: InfluencerLayout,
      children: [
        {
          path: '',
          name: 'Inf_Home',
          component: Inf_home,
        },
        {
          path: 'campaigns',
          name: 'Inf_Campaigns',
          component: Inf_campaigns,
        },
        {
          path: 'stats',
          name: 'Inf_Stats',
          component: Inf_stats,
        },
      ],
  
  },


  {
    path: '/sponsor',
    name: 'Sponsor',
    component: SponsorLayout,
    children: [
      {
        path: '',
        name: 'Spo_Home',
        component: Spo_home,
      },
      {
        path: 'campaigns',
        name: 'Spo_Campaigns',
        component: Spo_campaigns,
      },
      {
        path: 'influencers',
        name: 'Spo_Influencers',
        component: Spo_influencers,
      },
      {
        path: 'stats',
        name: 'Spo_Stats',
        component: Spo_stats,
      },
    ],

},
{
  path: '/admin',
  name: 'Admin',
  component: AdminLayout,
  children: [
    {
      path: '',
      name: 'Adm_home',
      component: Adm_home,
    },
    {
      path: 'influencers',
      name: 'Adm_infl',
      component: Adm_infl,
    },
    {
      path: 'campaigns',
      name: 'Adm_camp',
      component: Adm_camp,
    },
    {
      path: 'stats',
      name: 'Adm_Stats',
      component: Adm_stats,
    },
    {
      path:'sponsors',
      name: 'Adm_Sponsors',
      component: Adm_spon,
    }
  ],

},
 


];

// Create the router instance
const router = createRouter({
  history: createWebHistory(), // This uses the HTML5 history mode
  routes, // short for `routes: routes`
});



export default router;
