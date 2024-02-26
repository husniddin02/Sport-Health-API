// src/components/News/NewsList.js

import React, { useState, useEffect } from 'react';
import NewsService from '../../services/newsService';

const NewsList = () => {
  const [newsList, setNewsList] = useState([]);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const data = await NewsService.getAllNews();
        setNewsList(data);
      } catch (error) {
        console.error('Error fetching news:', error);
      }
    };

    fetchNews();
  }, []);

  return (
    <div>
      <h2>News</h2>
      <ul>
        {newsList.map((news) => (
          <li key={news.news_id}>
            <h3>{news.title}</h3>
            <p>{news.content}</p>
            <p>Publication Date: {news.publication_date}</p>
            <p>Author: {news.author}</p>
            <p>Category ID: {news.category}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default NewsList;
