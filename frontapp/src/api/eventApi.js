// src/api/eventApi.js

import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1/events';

const eventApi = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Получение списка мероприятий
export const getEvents = async () => {
  try {
    const response = await eventApi.get('/');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Получение деталей мероприятия по ID
export const getEventDetails = async (eventId) => {
  try {
    const response = await eventApi.get(`/${eventId}/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Создание нового мероприятия
export const createEvent = async (eventData) => {
  try {
    const response = await eventApi.post('/', eventData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Обновление информации о мероприятии
export const updateEvent = async (eventId, updatedEventData) => {
  try {
    const response = await eventApi.put(`/${eventId}/`, updatedEventData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Удаление мероприятия по ID
export const deleteEvent = async (eventId) => {
  try {
    const response = await eventApi.delete(`/${eventId}/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export default eventApi;
