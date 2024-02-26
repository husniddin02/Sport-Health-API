// src/components/News/NewsForm.js

import React, { useState } from 'react';
import NewsService from '../../services/newsService';

const NewsForm = ({ onSubmit, initialData }) => {
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
        await NewsService.updateNews(initialData.news_id, formData);
      } else {
        await NewsService.createNews(formData);
      }
      onSubmit();
    } catch (error) {
      console.error('Error submitting news form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="title">Title:</label>
        <input
          type="text"
          id="title"
          name="title"
          value={formData.title || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="content">Content:</label>
        <textarea
          id="content"
          name="content"
          value={formData.content || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="publication_date">Publication Date:</label>
        <input
          type="date"
          id="publication_date"
          name="publication_date"
          value={formData.publication_date || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="author">Author:</label>
        <input
          type="text"
          id="author"
          name="author"
          value={formData.author || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="category_id">Category ID:</label>
        <input
          type="number"
          id="category_id"
          name="category_id"
          value={formData.category_id || ''}
          onChange={handleChange}
          required
        />
      </div>
      <button type="submit">{initialData ? 'Update' : 'Create'} News</button>
    </form>
  );
};

export default NewsForm;
