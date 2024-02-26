// src/components/Events/EventForm.js

import React, { useState } from 'react';
import EventService from '../../services/eventService';

const EventForm = ({ onSubmit, initialData }) => {
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
        await EventService.updateEvent(initialData.event_id, formData);
      } else {
        await EventService.createEvent(formData);
      }
      onSubmit();
    } catch (error) {
      console.error('Error submitting event form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="event_name">Event Name:</label>
        <input
          type="text"
          id="event_name"
          name="event_name"
          value={formData.event_name || ''}
          onChange={handleChange}
          required
        />
      </div>
      <div>
        <label htmlFor="event_date">Event Date:</label>
        <input
          type="date"
          id="event_date"
          name="event_date"
          value={formData.event_date || ''}
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
        <label htmlFor="organizer">Organizer:</label>
        <input
          type="text"
          id="organizer"
          name="organizer"
          value={formData.organizer || ''}
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
      <button type="submit">{initialData ? 'Update' : 'Create'} Event</button>
    </form>
  );
};

export default EventForm;
