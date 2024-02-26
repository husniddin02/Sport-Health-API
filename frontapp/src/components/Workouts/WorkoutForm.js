// src/components/Workout/WorkoutForm.js

import React, { useState } from 'react';
import WorkoutService from '../../services/workoutService';

const WorkoutForm = ({ onSubmit, initialData }) => {
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
        await WorkoutService.updateWorkout(initialData.workout_id, formData);
      } else {
        await WorkoutService.createWorkout(formData);
      }
      onSubmit();
    } catch (error) {
      console.error('Error submitting workout form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="exercise_type">Exercise Type:</label>
        <input
          type="text"
          id="exercise_type"
          name="exercise_type"
          value={formData.exercise_type || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="workout_date">Workout Date:</label>
        <input
          type="date"
          id="workout_date"
          name="workout_date"
          value={formData.workout_date || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="duration">Duration (minutes):</label>
        <input
          type="number"
          id="duration"
          name="duration"
          value={formData.duration || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="notes">Notes:</label>
        <textarea
          id="notes"
          name="notes"
          value={formData.notes || ''}
          onChange={handleChange}
        />
      </div>
      <button type="submit">{initialData ? 'Update' : 'Create'} Workout</button>
    </form>
  );
};

export default WorkoutForm;
