import React from 'react';
import './NewsPage.css';
import NewsCard from '../components/news/NewsCard';

function NewsPage() {
  return (
    <div className="news-page">
      <h1>Latest News</h1>
      <div className="news-list">
        <NewsCard />
        {/* Добавьте другие NewsCard здесь */}
      </div>
    </div>
  );
}

export default NewsPage;
