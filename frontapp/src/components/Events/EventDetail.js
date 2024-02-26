// src/components/Events/EventDetails.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import EventService from '../../services/eventService';

const EventDetails = () => {
  const { eventId } = useParams();
  const [event, setEvent] = useState(null);

  useEffect(() => {
    const fetchEvent = async () => {
      try {
        const data = await EventService.getEventById(eventId);
        setEvent(data);
      } catch (error) {
        console.error('Error fetching event details:', error);
      }
    };

    fetchEvent();
  }, [eventId]);

  if (!event) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Event Details</h2>
      <h3>{event.event_name}</h3>
      <p>Date: {event.event_date}</p>
      <p>Location: {event.location}</p>
      <p>Organizer: {event.organizer}</p>
      <p>Description: {event.description}</p>
    </div>
  );
};

export default EventDetails;
