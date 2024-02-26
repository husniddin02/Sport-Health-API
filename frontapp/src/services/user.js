// src/services/user.js

import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/v1/user/';

const UserService = {
  // Получение данных профиля пользователя
  getProfile: async () => {
    try {
      const response = await axios.get(`${BASE_URL}profile/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Обновление данных профиля пользователя
  updateProfile: async (userData) => {
    try {
      const response = await axios.patch(`${BASE_URL}profile/`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Удаление профиля пользователя
  deleteProfile: async () => {
    try {
      const response = await axios.delete(`${BASE_URL}profile/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default UserService;
