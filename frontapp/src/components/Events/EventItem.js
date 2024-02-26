// src/components/Events/EventItem.js

import React from 'react';

const EventItem = ({ event }) => {
  return (
    <div>
      <h3>{event.event_name}</h3>
      <p>Date: {event.event_date}</p>
      <p>Location: {event.location}</p>
      <p>Description: {event.description}</p>
      <p>Organizer: {event.organizer}</p>
    </div>
  );
};

export default EventItem;
