// src/components/Home.js
import React, { useEffect, useState } from 'react';
import './Home.css';

function Home() {
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setLoaded(true);
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className={`header ${loaded ? 'loaded' : ''}`}>
      <video autoPlay muted loop>
        <source src="../assets/videos/header-background.mp4" type="video/mp4" />
      </video>
      <div className="header-content">
        <h1>Welcome to Our App</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla condimentum tortor at libero bibendum, sit amet aliquam lorem accumsan.</p>
        <button className="button-primary">Get Started</button>
      </div>
    </div>
  );
}

export default Home;
