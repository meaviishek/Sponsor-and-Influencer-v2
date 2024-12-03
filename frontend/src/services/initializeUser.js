import  {useUserStore}  from '@/stores/user'; // Import the user store

export const initializeUser = () => {
  try {
    const userStore = useUserStore();
    // Retrieve user data and access token from localStorage
    const storedUserData = localStorage.getItem('userData');
    const storedAccessToken = localStorage.getItem('accessToken');

    // If both user data and token exist, parse the data and update the store
    if (storedUserData && storedAccessToken) {
      const userData = JSON.parse(storedUserData);

      // Update the store with user data and token
      userStore.setUser({
        ...userData,
        accessToken: storedAccessToken,
      });

      console.log('User initialized from localStorage:', userData);
    } else {
      console.log('No user data found in localStorage. User is not logged in.');
    }
  } catch (error) {
    console.error('Error initializing user from localStorage:', error);
  }
};
