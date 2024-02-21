// src/api/userApi.js

import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1/user';

const userApi = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Получение профиля пользователя
export const getUserProfile = async () => {
  try {
    const response = await userApi.get('/profile/');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Обновление профиля пользователя
export const updateProfile = async (updatedProfile) => {
  try {
    const response = await userApi.patch('/profile/', updatedProfile);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Удаление профиля пользователя
export const deleteProfile = async () => {
  try {
    const response = await userApi.delete('/profile/');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export default userApi;
