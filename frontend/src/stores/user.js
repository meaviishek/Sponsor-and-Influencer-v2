import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    user: JSON.parse(localStorage.getItem('userData')) || null, // Load user from localStorage
    accessToken: localStorage.getItem('accessToken') || null,
  }),
  actions: {
    setUser(userData) {
      this.user = userData;
      this.accessToken = userData?.accessToken || null;

      // Save user and token to localStorage
      localStorage.setItem('userData', JSON.stringify(userData));
      if (userData?.accessToken) {
        localStorage.setItem('accessToken', userData.accessToken);
      }
    },
  
  initializeUser() {
    const storedUser = localStorage.getItem('userData');
    if (storedUser) {
      this.user = JSON.parse(storedUser);
    }
  },
    clearUser() {
      this.user = null;
      this.isAuthenticated = false;
      this.accessToken = null;
      localStorage.removeItem('userData');
      localStorage.removeItem('accessToken');
    },
  },
});
