// src/services/categoryService.js

const API_URL = 'http://127.0.0.1:8000/categories/';

const headers = {
  'Content-Type': 'application/json',
};

const categoryService = {
  getAllCategories: async () => {
    const response = await fetch(API_URL, { headers });
    const data = await response.json();
    return data;
  },

  getCategoryById: async (categoryId) => {
    const response = await fetch(`${API_URL}${categoryId}/`, { headers });
    const data = await response.json();
    return data;
  },

  createCategory: async (formData) => {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers,
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    return data;
  },

  updateCategory: async (categoryId, formData) => {
    const response = await fetch(`${API_URL}${categoryId}/`, {
      method: 'PUT',
      headers,
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    return data;
  },

  deleteCategory: async (categoryId) => {
    await fetch(`${API_URL}${categoryId}/`, {
      method: 'DELETE',
      headers,
    });
  },
};

export default categoryService;
