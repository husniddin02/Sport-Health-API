import React from 'react';

const NewsItem = ({ title, content, publicationDate, author, category }) => {
  return (
    <div className="news-item">
      <h2>{title}</h2>
      <p>{content}</p>
      <p><strong>Published Date:</strong> {publicationDate}</p>
      <p><strong>Author:</strong> {author}</p>
      <p><strong>Category:</strong> {category}</p>
    </div>
  );
};

export default NewsItem;
