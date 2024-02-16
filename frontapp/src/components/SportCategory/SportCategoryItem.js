import React from 'react';

const SportCategoryItem = ({ name, description }) => {
  return (
    <div className="category-item">
      <h2>{name}</h2>
      <p>{description}</p>
    </div>
  );
};

export default SportCategoryItem;
