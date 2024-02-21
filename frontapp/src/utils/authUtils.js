// src/utils/authUtils.js

// Функция для сохранения токена доступа в локальное хранилище
export const saveAccessToken = (token) => {
    localStorage.setItem('accessToken', token);
  };
  
  // Функция для получения токена доступа из локального хранилища
  export const getAccessToken = () => {
    return localStorage.getItem('accessToken');
  };
  
  // Функция для удаления токена доступа из локального хранилища
  export const removeAccessToken = () => {
    localStorage.removeItem('accessToken');
  };
  
  // Функция для проверки, аутентифицирован ли пользователь
  export const isAuthenticated = () => {
    const token = getAccessToken();
    return !!token;
  };
  