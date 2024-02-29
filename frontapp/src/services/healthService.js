// src/services/healthService.js

const API_URL = 'http://127.0.0.1:8000/health/';

const headers = {
  'Content-Type': 'application/json',
};

const HealthService = {
  getAllHealthRecords: async () => {
    const response = await fetch(API_URL, { headers });
    const data = await response.json();
    return data;
  },

  getHealthRecordById: async (healthId) => {
    const response = await fetch(`${API_URL}${healthId}/`, { headers });
    const data = await response.json();
    return data;
  },

  createHealthRecord: async (formData) => {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers,
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    return data;
  },

  updateHealthRecord: async (healthId, formData) => {
    const response = await fetch(`${API_URL}${healthId}/`, {
      method: 'PUT',
      headers,
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    return data;
  },

  deleteHealthRecord: async (healthId) => {
    await fetch(`${API_URL}${healthId}/`, {
      method: 'DELETE',
      headers,
    });
  },
};

export default HealthService;
