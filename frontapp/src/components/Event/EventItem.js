import React from 'react';

const EventItem = ({ name, date, location, organizer }) => {
  return (
    <div className="event-item">
      <h3>{name}</h3>
      <p><strong>Date:</strong> {date}</p>
      <p><strong>Location:</strong> {location}</p>
      <p><strong>Organizer:</strong> {organizer}</p>
    </div>
  );
};

export default EventItem;
