// src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { BrowserRouter as Router } from 'react-router-dom';
import { setupAxiosInterceptors } from './utils/apiUtils';

// Установка перехватчика axios для добавления токена в запросы
setupAxiosInterceptors();

ReactDOM.render(
  <Router>
    <App />
  </Router>,
  document.getElementById('root')
);
