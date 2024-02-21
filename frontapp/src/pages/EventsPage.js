import React from 'react';
import './EventsPage.css';
import EventCard from '../components/events/EventCard';
import EventFilter from '../components/events/EventFilter';

function EventsPage() {
  return (
    <div className="events-page">
      <h1>Upcoming Events</h1>
      <EventFilter />
      <div className="event-list">
        <EventCard />
        {/* Добавьте другие EventCard здесь */}
      </div>
    </div>
  );
}

export default EventsPage;
