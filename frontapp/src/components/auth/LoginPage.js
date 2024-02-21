// src/components/auth/LoginPage.js

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css';

/**
 * Компонент страницы входа
 * src/components/auth/LoginPage.js
 */
const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  /**
   * Обработчик сабмита формы входа
   * @param {Event} e Событие формы
   */
  const handleLogin = (e) => {
    e.preventDefault();
    // Логика для отправки запроса на сервер для входа пользователя
    console.log('Logging in with:', email, password);
    // После успешного входа перенаправляем пользователя на главную страницу
    navigate('/');
  };

  return (
    <div className="login-container">
      <h1>Login Page</h1>
      <form onSubmit={handleLogin} className="login-form">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;
