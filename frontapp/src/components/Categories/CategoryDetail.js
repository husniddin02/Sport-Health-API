// src/components/Categories/CategoryDetails.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import categoryService from '../../services/сategoryService';

const CategoryDetails = () => {
  const { categoryId } = useParams();
  const [category, setCategory] = useState(null);

  useEffect(() => {
    const fetchCategory = async () => {
      try {
        const data = await categoryService.getCategoryById(categoryId);
        setCategory(data);
      } catch (error) {
        console.error('Error fetching category details:', error);
      }
    };

    fetchCategory();
  }, [categoryId]);

  if (!category) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Category Details</h2>
      <h3>{category.category_name}</h3>
      <p>{category.description}</p>
    </div>
  );
};

export default CategoryDetails;
