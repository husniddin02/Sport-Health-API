// src/services/auth.js
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/v1/user/';

const AuthService = {
  // Авторизация пользователя
  login: async (email, password) => {
    try {
      const response = await axios.post(`${BASE_URL}login/`, { email, password });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  // Выход пользователя из системы
  logout: async () => {
    try {
      const response = await axios.post(`${BASE_URL}logout/`);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  // Регистрация нового пользователя
  signup: async (userData) => {
    try {
      const response = await axios.post(`${BASE_URL}signup/`, userData);
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  // Подтверждение адреса электронной почты
  confirmEmail: async (email) => {
    try {
      const response = await axios.post(`${BASE_URL}email-confirmation/`, { email });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  // Сброс пароля пользователя
  resetPassword: async (email) => {
    try {
      const response = await axios.post(`${BASE_URL}password-reset/`, { email });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },

  // Изменение пароля пользователя
  changePassword: async (oldPassword, newPassword) => {
    try {
      const response = await axios.post(`${BASE_URL}change-password/`, { oldPassword, newPassword });
      return response.data;
    } catch (error) {
      throw error.response.data;
    }
  },
};

export default AuthService;
