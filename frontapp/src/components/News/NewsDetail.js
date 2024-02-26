// src/components/News/NewsDetails.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import NewsService from '../../services/newsService';

const NewsDetails = () => {
  const { newsId } = useParams();
  const [news, setNews] = useState(null);

  useEffect(() => {
    const fetchNews = async () => {
      try {
        const data = await NewsService.getNewsById(newsId);
        setNews(data);
      } catch (error) {
        console.error('Error fetching news details:', error);
      }
    };

    fetchNews();
  }, [newsId]);

  if (!news) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{news.title}</h2>
      <p>{news.content}</p>
      <p>Publication Date: {news.publication_date}</p>
      <p>Author: {news.author}</p>
      <p>Category ID: {news.category}</p>
    </div>
  );
};

export default NewsDetails;
