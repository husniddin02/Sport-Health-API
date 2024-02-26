// src/components/Categories/CategoriesList.js

import React, { useState, useEffect } from 'react';
import categoryService from '../../services/сategoryService';


const CategoriesList = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const data = await categoryService.getAllCategories();
        setCategories(data);
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    fetchCategories();
  }, []);

  return (
    <div>
      <h2>Categories</h2>
      <ul>
        {categories.map((category) => (
          <li key={category.category_id}>
            <h3>{category.category_name}</h3>
            <p>{category.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CategoriesList;
