// src/components/Navbar.js
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

function Navbar() {
  const [isMobile, setIsMobile] = useState(false);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 992);
    };

    handleResize();

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <Link to="/" className="navbar-caption">Your App</Link>
      </div>

      {isMobile ? (
        <button className={`navbar-toggler ${isOpen ? 'open' : ''}`} onClick={toggleMenu}>
          <div className="hamburger">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </button>
      ) : (
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link to="/categories" className="nav-link">Categories</Link>
          </li>
          <li className="nav-item">
            <Link to="/news" className="nav-link">News</Link>
          </li>
          <li className="nav-item">
            <Link to="/sports-facilities" className="nav-link">Sports Facilities</Link>
          </li>
          <li className="nav-item">
            <Link to="/workouts" className="nav-link">Workouts</Link>
          </li>
        </ul>
      )}

      <div className={`navbar-collapse ${isOpen ? 'show' : ''}`}>
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link to="/categories" className="nav-link" onClick={toggleMenu}>Categories</Link>
          </li>
          <li className="nav-item">
            <Link to="/news" className="nav-link" onClick={toggleMenu}>News</Link>
          </li>
          <li className="nav-item">
            <Link to="/sports-facilities" className="nav-link" onClick={toggleMenu}>Sports Facilities</Link>
          </li>
          <li className="nav-item">
            <Link to="/workouts" className="nav-link" onClick={toggleMenu}>Workouts</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Navbar;
