import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/'; // Замените на ваш URL API

const WorkoutService = {
  getAllWorkouts: async () => {
    try {
      const response = await axios.get(`${API_URL}/workouts/`);
      return response.data;
    } catch (error) {
      console.error('Error fetching all workouts:', error);
      throw error;
    }
  },
  getWorkoutById: async (workoutId) => {
    try {
      const response = await axios.get(`${API_URL}/workouts/${workoutId}/`);
      return response.data;
    } catch (error) {
      console.error(`Error fetching workout with ID ${workoutId}:`, error);
      throw error;
    }
  },
  createWorkout: async (workoutData) => {
    try {
      const response = await axios.post(`${API_URL}/workouts/`, workoutData);
      return response.data;
    } catch (error) {
      console.error('Error creating workout:', error);
      throw error;
    }
  },
  updateWorkout: async (workoutId, workoutData) => {
    try {
      const response = await axios.put(`${API_URL}/workouts/${workoutId}/`, workoutData);
      return response.data;
    } catch (error) {
      console.error(`Error updating workout with ID ${workoutId}:`, error);
      throw error;
    }
  },
  deleteWorkout: async (workoutId) => {
    try {
      await axios.delete(`${API_URL}/workouts/${workoutId}/`);
    } catch (error) {
      console.error(`Error deleting workout with ID ${workoutId}:`, error);
      throw error;
    }
  },
};

export default WorkoutService;
