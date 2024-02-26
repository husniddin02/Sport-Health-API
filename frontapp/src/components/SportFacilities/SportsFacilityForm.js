// src/components/SportsFacility/SportsFacilityForm.js

import React, { useState } from 'react';
import SportsFacilityService from '../../services/sportsFacilityService';

const SportsFacilityForm = ({ onSubmit, initialData }) => {
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
        await SportsFacilityService.updateFacility(initialData.facility_id, formData);
      } else {
        await SportsFacilityService.createFacility(formData);
      }
      onSubmit();
    } catch (error) {
      console.error('Error submitting facility form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="facility_name">Facility Name:</label>
        <input
          type="text"
          id="facility_name"
          name="facility_name"
          value={formData.facility_name || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="location">Location:</label>
        <input
          type="text"
          id="location"
          name="location"
          value={formData.location || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="capacity">Capacity:</label>
        <input
          type="number"
          id="capacity"
          name="capacity"
          value={formData.capacity || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            name="equipment_available"
            checked={formData.equipment_available || false}
            onChange={handleChange}
          />
          Equipment Available
        </label>
      </div>
      <div>
        <label>
          <input
            type="checkbox"
            name="trainer_available"
            checked={formData.trainer_available || false}
            onChange={handleChange}
          />
          Trainer Available
        </label>
      </div>
      <button type="submit">{initialData ? 'Update' : 'Create'} Facility</button>
    </form>
  );
};

export default SportsFacilityForm;
