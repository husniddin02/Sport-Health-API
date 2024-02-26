// src/services/newsService.js

const API_URL = 'http://127.0.0.1:8000/api/v1/news/';

const headers = {
  'Content-Type': 'application/json',
};

const NewsService = {
  getAllNews: async () => {
    const response = await fetch(API_URL, { headers });
    const data = await response.json();
    return data;
  },

  getNewsById: async (newsId) => {
    const response = await fetch(`${API_URL}${newsId}/`, { headers });
    const data = await response.json();
    return data;
  },

  createNews: async (formData) => {
    const response = await fetch(API_URL, {
      method: 'POST',
      headers,
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    return data;
  },

  updateNews: async (newsId, formData) => {
    const response = await fetch(`${API_URL}${newsId}/`, {
      method: 'PUT',
      headers,
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    return data;
  },

  deleteNews: async (newsId) => {
    await fetch(`${API_URL}${newsId}/`, {
      method: 'DELETE',
      headers,
    });
  },
};

export default NewsService;
