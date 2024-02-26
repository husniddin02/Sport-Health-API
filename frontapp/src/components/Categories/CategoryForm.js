// src/components/Categories/CategoryForm.js

import React, { useState } from 'react';
import categoryService from '../../services/сategoryService';

const CategoryForm = ({ onSubmit, initialData }) => {
  const [formData, setFormData] = useState(initialData || {});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (initialData) {
        await categoryService.updateCategory(initialData.category_id, formData);
      } else {
        await categoryService.createCategory(formData);
      }
      onSubmit();
    } catch (error) {
      console.error('Error submitting category form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="category_name">Category Name:</label>
        <input
          type="text"
          id="category_name"
          name="category_name"
          value={formData.category_name || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="description">Description:</label>
        <textarea
          id="description"
          name="description"
          value={formData.description || ''}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">{initialData ? 'Update' : 'Create'} Category</button>
    </form>
  );
};

export default CategoryForm;
