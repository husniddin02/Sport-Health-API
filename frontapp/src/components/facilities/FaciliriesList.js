// src/components/facilities/FacilitiesList.js

import React, { useState, useEffect } from 'react';
import { getAllFacilities } from '../api/facilityApi';
import FacilityItem from './FacilityItem';
import './FacilitiesList.css';

/**
 * Компонент для отображения списка спортивных объектов
 */
const FacilitiesList = () => {
  const [facilities, setFacilities] = useState([]);

  useEffect(() => {
    // Загружаем список всех спортивных объектов при монтировании компонента
    const fetchFacilities = async () => {
      try {
        const facilitiesData = await getAllFacilities();
        setFacilities(facilitiesData);
      } catch (error) {
        console.error('Error fetching facilities:', error);
      }
    };
    fetchFacilities();
  }, []);

  return (
    <div className="facilities-list">
      <h2>Sport Facilities</h2>
      {facilities.map(facility => (
        <FacilityItem key={facility.id} facility={facility} />
      ))}
    </div>
  );
};

export default FacilitiesList;
