import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { getAllSportsFacilities } from '../../services/sportsFacilityService'; // Обновленный импорт

function SportsFacilityList() {
  const [sportsFacilities, setSportsFacilities] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchSportsFacilities();
  }, []);

  async function fetchSportsFacilities() {
    try {
      const data = await getAllSportsFacilities(); // Обновленный вызов функции
      setSportsFacilities(data);
    } catch (error) {
      setError(error);
    }
  }

  if (error) {
    return <div>Error fetching sports facilities: {error.message}</div>;
  }

  return (
    <div>
      <h1>Sports Facilities</h1>
      <ul>
        {sportsFacilities.map((facility) => (
          <li key={facility.id}>
            <Link to={`/sports-facilities/${facility.id}`}>{facility.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default SportsFacilityList;
