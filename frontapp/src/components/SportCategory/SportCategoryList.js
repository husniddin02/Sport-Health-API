import React from 'react';

const SportCategoryList = ({ categories }) => {
  return (
    <div className="category-list">
      <h2>Sport Categories</h2>
      {categories.map((category, index) => (
        <div key={index} className="category-item">
          <h3>{category.name}</h3>
          <p>{category.description}</p>
        </div>
      ))}
    </div>
  );
};

export default SportCategoryList;
