// src/components/SportsFacility/SportsFacilityList.js

import React, { useState, useEffect } from 'react';
import SportsFacilityService from '../../services/sportsFacilityService';

const SportsFacilityList = () => {
  const [facilities, setFacilities] = useState([]);

  useEffect(() => {
    const fetchFacilities = async () => {
      try {
        const data = await SportsFacilityService.getAllFacilities();
        setFacilities(data);
      } catch (error) {
        console.error('Error fetching facilities:', error);
      }
    };

    fetchFacilities();
  }, []);

  return (
    <div>
      <h2>Sports Facilities</h2>
      <ul>
        {facilities.map((facility) => (
          <li key={facility.facility_id}>
            <h3>{facility.facility_name}</h3>
            <p>Location: {facility.location}</p>
            <p>Capacity: {facility.capacity}</p>
            <p>Equipment Available: {facility.equipment_available ? 'Yes' : 'No'}</p>
            <p>Trainer Available: {facility.trainer_available ? 'Yes' : 'No'}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SportsFacilityList;
