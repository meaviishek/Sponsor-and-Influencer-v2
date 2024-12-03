import api  from './api'; // Adjust the path to your API configuration
import { useUserStore } from '@/stores/user'; // Adjust the path to your user store


export const fetchUserData = async () => {
    
  try {
    const userStore = useUserStore();
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) throw new Error('No access token found');

    const response = await api.get('/user/data', {
      headers: { Authorization: `Bearer ${accessToken}` },
    });

    const updatedUserData = response.data.user;

  
    userStore.setUser(updatedUserData);

    
    localStorage.setItem('userData', JSON.stringify(updatedUserData));

    return updatedUserData;
  } catch (error) {
    console.error('Failed to fetch user data:', error.response?.data || error.message);
    alert('Failed to fetch user data: ' + (error.response?.data?.error || error.message));
    throw error;
  }
};
