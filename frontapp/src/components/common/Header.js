// src/components/common/Header.js

import React from 'react';
import { Link } from 'react-router-dom';
import { isAuthenticated, removeAccessToken } from '../../utils/authUtils';

const Header = () => {
  const handleLogout = () => {
    removeAccessToken();
    // Дополнительные действия после выхода, например, перенаправление на страницу входа
  };

  return (
    <header>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          {isAuthenticated() ? (
            <>
              <li>
                <Link to="/profile">Profile</Link>
              </li>
              <li>
                <button onClick={handleLogout}>Logout</button>
              </li>
            </>
          ) : (
            <>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/register">Register</Link>
              </li>
            </>
          )}
        </ul>
      </nav>
    </header>
  );
};

export default Header;
