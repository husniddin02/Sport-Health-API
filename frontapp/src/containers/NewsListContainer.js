// src/containers/NewsListContainer.js
import React, { useState, useEffect } from 'react';
import NewsList from '../components/NewsList';

const NewsListContainer = () => {
  const [news, setNews] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/news');
        if (!response.ok) {
          throw new Error('Failed to fetch news');
        }
        const data = await response.json();
        setNews(data);
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    };

    fetchNews();
  }, []);

  return <NewsList news={news} />;
};

export default NewsListContainer;
