

<template>
  <div  >
    <div id="app">
    <!-- Router View to render the current route -->
    <router-view />
  </div>
  </div>
</template>

<script >
export default {
  name: "App",

};
// import { useUserStore } from './stores/user';

// const userStore = useUserStore();

// // Restore user from localStorage on app load
// if (!userStore.user) {
//   const userData = JSON.parse(localStorage.getItem('userData'));
//   if (userData) {
//     userStore.setUser(userData);
//   }
// }

</script>

<style>

/* Add global styles if necessary */
</style>
