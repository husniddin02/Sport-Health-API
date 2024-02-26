// src/components/Events/EventsList.js

import React, { useState, useEffect } from 'react';
import EventService from '../../services/eventService';

const EventsList = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const data = await EventService.getAllEvents();
        setEvents(data);
      } catch (error) {
        console.error('Error fetching events:', error);
      }
    };

    fetchEvents();
  }, []);

  return (
    <div>
      <h2>Events List</h2>
      {events.map(event => (
        <div key={event.event_id} className="event">
          <h3>{event.event_name}</h3>
          <p>Date: {event.event_date}</p>
          <p>Location: {event.location}</p>
          <p>Organizer: {event.organizer}</p>
        </div>
      ))}
    </div>
  );
};

export default EventsList;
