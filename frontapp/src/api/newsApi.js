// src/api/newsApi.js

import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1/news';

const newsApi = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Получение списка новостей
export const getNews = async () => {
  try {
    const response = await newsApi.get('/');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Получение деталей новости по ID
export const getNewsDetails = async (newsId) => {
  try {
    const response = await newsApi.get(`/${newsId}/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Создание новости
export const createNews = async (newsData) => {
  try {
    const response = await newsApi.post('/', newsData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Обновление информации о новости
export const updateNews = async (newsId, updatedNewsData) => {
  try {
    const response = await newsApi.put(`/${newsId}/`, updatedNewsData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Удаление новости по ID
export const deleteNews = async (newsId) => {
  try {
    const response = await newsApi.delete(`/${newsId}/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export default newsApi;
