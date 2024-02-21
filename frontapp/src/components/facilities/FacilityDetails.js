// src/components/facilities/FacilityDetails.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getFacilityById } from '../api/facilityApi';
import './FacilityDetails.css';

/**
 * Компонент для отображения деталей спортивного объекта
 */
const FacilityDetails = () => {
  const { facilityId } = useParams();
  const [facility, setFacility] = useState(null);

  useEffect(() => {
    // Загружаем детали спортивного объекта по facilityId при монтировании компонента
    const fetchFacilityDetails = async () => {
      try {
        const facilityData = await getFacilityById(facilityId);
        setFacility(facilityData);
      } catch (error) {
        console.error('Error fetching facility details:', error);
      }
    };
    fetchFacilityDetails();
  }, [facilityId]);

  return (
    <div className="facility-details">
      {facility ? (
        <div>
          <h2>{facility.name}</h2>
          <p>Location: {facility.location}</p>
          <p>Capacity: {facility.capacity}</p>
          {/* Другие детали спортивного объекта */}
        </div>
      ) : (
        <p>Loading facility details...</p>
      )}
    </div>
  );
};

export default FacilityDetails;
