import React from 'react';

const SportFacilityItem = ({ name, location, capacity, equipmentAvailable, trainerAvailable }) => {
  return (
    <div className="facility-item">
      <h2>{name}</h2>
      <p><strong>Location:</strong> {location}</p>
      <p><strong>Capacity:</strong> {capacity}</p>
      <p><strong>Equipment Available:</strong> {equipmentAvailable ? 'Yes' : 'No'}</p>
      <p><strong>Trainer Available:</strong> {trainerAvailable ? 'Yes' : 'No'}</p>
    </div>
  );
};

export default SportFacilityItem;
