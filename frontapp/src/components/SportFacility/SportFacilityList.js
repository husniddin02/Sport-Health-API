import React from 'react';

const SportFacilityList = ({ facilities }) => {
  return (
    <div className="facility-list">
      <h2>Sport Facilities</h2>
      {facilities.map((facility, index) => (
        <div key={index} className="facility-item">
          <h3>{facility.name}</h3>
          <p><strong>Location:</strong> {facility.location}</p>
          <p><strong>Capacity:</strong> {facility.capacity}</p>
          <p><strong>Equipment Available:</strong> {facility.equipmentAvailable ? 'Yes' : 'No'}</p>
          <p><strong>Trainer Available:</strong> {facility.trainerAvailable ? 'Yes' : 'No'}</p>
        </div>
      ))}
    </div>
  );
};

export default SportFacilityList;
