import React, { useState, useEffect } from 'react';
import eventService from '../../services/eventService';
import EventItem from './EventItem';

function EventList() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const data = await eventService.getAllEvents();
        setEvents(data);
      } catch (error) {
        console.error('Error fetching events', error);
      }
    };
    fetchEvents();
  }, []);

  return (
    <div className="event-list">
      <h2>Upcoming Events</h2>
      {events.map((event) => (
        <EventItem key={event.id} event={event} />
      ))}
    </div>
  );
}

export default EventList;
