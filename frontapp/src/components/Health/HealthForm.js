// src/components/Health/HealthForm.js

import React, { useState } from 'react';
import HealthService from '../../services/healthService';

const HealthForm = ({ onSubmit, initialData }) => {
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
        await HealthService.updateHealthRecord(initialData.health_id, formData);
      } else {
        await HealthService.createHealthRecord(formData);
      }
      onSubmit();
    } catch (error) {
      console.error('Error submitting health record form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="height">Height (cm):</label>
        <input
          type="number"
          id="height"
          name="height"
          value={formData.height || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="weight">Weight (kg):</label>
        <input
          type="number"
          id="weight"
          name="weight"
          value={formData.weight || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="heart_rate">Heart Rate (bpm):</label>
        <input
          type="number"
          id="heart_rate"
          name="heart_rate"
          value={formData.heart_rate || ''}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="bmi">BMI:</label>
        <input
          type="number"
          id="bmi"
          name="bmi"
          value={formData.bmi || ''}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="bmi_category">BMI Category:</label>
        <input
          type="text"
          id="bmi_category"
          name="bmi_category"
          value={formData.bmi_category || ''}
          onChange={handleChange}
        />
      </div>
      <div>
        <label htmlFor="additional_notes">Additional Notes:</label>
        <textarea
          id="additional_notes"
          name="additional_notes"
          value={formData.additional_notes || ''}
          onChange={handleChange}
        />
      </div>
      <button type="submit">{initialData ? 'Update' : 'Create'} Health Record</button>
    </form>
  );
};

export default HealthForm;
