// src/utils/apiUtils.js

import axios from 'axios';
import { getAccessToken } from './authUtils';

// Функция для настройки axios с токеном доступа
export const setupAxiosInterceptors = () => {
  axios.interceptors.request.use(
    (config) => {
      const token = getAccessToken();
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => {
      Promise.reject(error);
    }
  );
};
