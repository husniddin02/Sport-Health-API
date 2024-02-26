// src/services/workoutService.js

import axios from 'axios';

const API_URL = 'http://api.example.com'; // Замените на ваш URL API

const WorkoutService = {
  getAllWorkouts: async () => {
    const response = await axios.get(`${API_URL}/workouts/`);
    return response.data;
  },
  getWorkoutById: async (workoutId) => {
    const response = await axios.get(`${API_URL}/workouts/${workoutId}/`);
    return response.data;
  },
  createWorkout: async (workoutData) => {
    const response = await axios.post(`${API_URL}/workouts/`, workoutData);
    return response.data;
  },
  updateWorkout: async (workoutId, workoutData) => {
    const response = await axios.put(`${API_URL}/workouts/${workoutId}/`, workoutData);
    return response.data;
  },
  deleteWorkout: async (workoutId) => {
    await axios.delete(`${API_URL}/workouts/${workoutId}/`);
  },
};

export default WorkoutService;
