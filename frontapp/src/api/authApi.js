// src/api/authApi.js

import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1/auth';

const authApi = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Регистрация
export const register = async (userData) => {
  try {
    const response = await authApi.post('/register/', userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Вход
export const login = async (userData) => {
  try {
    const response = await authApi.post('/login/', userData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Сброс пароля
export const resetPassword = async (email) => {
  try {
    const response = await authApi.post('/reset-password/', { email });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Изменение пароля
export const changePassword = async (passwords) => {
  try {
    const response = await authApi.post('/change-password/', passwords);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export default authApi;
