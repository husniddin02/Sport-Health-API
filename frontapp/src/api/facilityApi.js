// src/api/facilityApi.js

import axios from 'axios';

const BASE_URL = 'http://localhost:8000/api/v1/facilities';

const facilityApi = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Получение списка объектов спорта
export const getFacilities = async () => {
  try {
    const response = await facilityApi.get('/');
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Получение информации об объекте спорта по ID
export const getFacilityDetails = async (facilityId) => {
  try {
    const response = await facilityApi.get(`/${facilityId}/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Создание нового объекта спорта
export const createFacility = async (facilityData) => {
  try {
    const response = await facilityApi.post('/', facilityData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Обновление информации об объекте спорта
export const updateFacility = async (facilityId, updatedFacilityData) => {
  try {
    const response = await facilityApi.put(`/${facilityId}/`, updatedFacilityData);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

// Удаление объекта спорта по ID
export const deleteFacility = async (facilityId) => {
  try {
    const response = await facilityApi.delete(`/${facilityId}/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export default facilityApi;
