// src/components/SportsFacility/SportsFacilityDetails.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import SportsFacilityService from '../../services/sportsFacilityService';

const SportsFacilityDetails = () => {
  const { facilityId } = useParams();
  const [facility, setFacility] = useState(null);

  useEffect(() => {
    const fetchFacility = async () => {
      try {
        const data = await SportsFacilityService.getFacilityById(facilityId);
        setFacility(data);
      } catch (error) {
        console.error('Error fetching facility details:', error);
      }
    };

    fetchFacility();
  }, [facilityId]);

  if (!facility) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{facility.facility_name}</h2>
      <p>Location: {facility.location}</p>
      <p>Capacity: {facility.capacity}</p>
      <p>Equipment Available: {facility.equipment_available ? 'Yes' : 'No'}</p>
      <p>Trainer Available: {facility.trainer_available ? 'Yes' : 'No'}</p>
    </div>
  );
};

export default SportsFacilityDetails;