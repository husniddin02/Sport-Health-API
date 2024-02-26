// src/services/EventService.js

const API_URL = 'http://127.0.0.1:8000/api/v1';

const EventService = {
  getAllEvents: async () => {
    const response = await fetch(`${API_URL}/events/`);
    if (!response.ok) {
      throw new Error('Failed to fetch events');
    }
    return response.json();
  },

  getEventById: async (eventId) => {
    const response = await fetch(`${API_URL}/events/${eventId}/`);
    if (!response.ok) {
      throw new Error('Failed to fetch event');
    }
    return response.json();
  },

  createEvent: async (eventData) => {
    const response = await fetch(`${API_URL}/events/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(eventData),
    });
    if (!response.ok) {
      throw new Error('Failed to create event');
    }
    return response.json();
  },

  updateEvent: async (eventId, eventData) => {
    const response = await fetch(`${API_URL}/events/${eventId}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(eventData),
    });
    if (!response.ok) {
      throw new Error('Failed to update event');
    }
    return response.json();
  },

  deleteEvent: async (eventId) => {
    const response = await fetch(`${API_URL}/events/${eventId}/`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error('Failed to delete event');
    }
  },
};

export default EventService;
