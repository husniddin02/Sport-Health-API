// src/services/sportsFacilityService.js

import axios from 'axios';

const API_URL = 'http://api.example.com/sports-facilities'; // Обновленный URL API

export async function getAllSportsFacilities() {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching sports facilities:', error);
    throw error; // Прокидываем ошибку для дальнейшей обработки в компонентах
  }
}

export async function createSportsFacility(data) {
  try {
    const response = await axios.post(API_URL, data);
    return response.data;
  } catch (error) {
    console.error('Error creating sports facility:', error);
    throw error;
  }
}

export async function getSportsFacilityById(id) { // Исправленное имя функции
  try {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching sports facility by ID:', error);
    throw error;
  }
}

export async function updateSportsFacility(id, data) {
  try {
    const response = await axios.put(`${API_URL}/${id}`, data);
    return response.data;
  } catch (error) {
    console.error('Error updating sports facility:', error);
    throw error;
  }
}

export async function deleteSportsFacility(id) {
  try {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting sports facility:', error);
    throw error;
  }
}