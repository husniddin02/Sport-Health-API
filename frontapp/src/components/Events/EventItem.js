// src/components/Events/EventItem.js

import React from 'react';

function EventItem({ event }) {
  const { title, date, time, location, description } = event;

  return (
    <div className="event-item">
      <h3>{title}</h3>
      <p>Date: {date}</p>
      <p>Time: {time}</p>
      <p>Location: {location}</p>
      <p>Description: {description}</p>
      <button>Register</button>
    </div>
  );
}

export default EventItem;
