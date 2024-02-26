// src/services/userService.js

import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/v1/';

const UserService = {
  // Получение данных профиля пользователя
  getUserProfile: async () => {
    try {
      const response = await axios.get(`${BASE_URL}user/profile/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Обновление данных профиля пользователя
  updateUserProfile: async (userData) => {
    try {
      const response = await axios.patch(`${BASE_URL}user/profile/`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Регистрация нового пользователя
  signUpUser: async (userData) => {
    try {
      const response = await axios.post(`${BASE_URL}user/signup/`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Вход пользователя в систему
  loginUser: async (userData) => {
    try {
      const response = await axios.post(`${BASE_URL}user/login/`, userData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Выход пользователя из системы
  logoutUser: async () => {
    try {
      const response = await axios.post(`${BASE_URL}user/logout/`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Сброс пароля пользователя
  resetUserPassword: async (emailData) => {
    try {
      const response = await axios.post(`${BASE_URL}user/password-reset/`, emailData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Подтверждение адреса электронной почты пользователя
  confirmUserEmail: async (emailData) => {
    try {
      const response = await axios.post(`${BASE_URL}user/email-confirmation/`, emailData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  // Изменение пароля пользователя
  changeUserPassword: async (passwordData) => {
    try {
      const response = await axios.post(`${BASE_URL}user/change-password/`, passwordData);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
};

export default UserService;
