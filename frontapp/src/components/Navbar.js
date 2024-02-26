// src/components/Navbar.js

import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/categories">Categories</Link>
        </li>
        <li>
          <Link to="/news">News</Link>
        </li>
        <li>
          <Link to="/sport-facilities">Sport Facilities</Link>
        </li>
        <li>
          <Link to="/workouts">Workouts</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
