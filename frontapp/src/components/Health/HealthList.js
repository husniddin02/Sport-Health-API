// src/components/Health/HealthList.js

import React, { useState, useEffect } from 'react';
import HealthService from '../../services/healthService';

const HealthList = () => {
  const [healthRecords, setHealthRecords] = useState([]);

  useEffect(() => {
    const fetchHealthRecords = async () => {
      try {
        const data = await HealthService.getAllHealthRecords();
        setHealthRecords(data);
      } catch (error) {
        console.error('Error fetching health records:', error);
      }
    };

    fetchHealthRecords();
  }, []);

  return (
    <div>
      <h2>Health Records</h2>
      <ul>
        {healthRecords.map((record) => (
          <li key={record.health_id}>
            <h3>Health Record #{record.health_id}</h3>
            <p>Height: {record.height} cm</p>
            <p>Weight: {record.weight} kg</p>
            <p>Heart Rate: {record.heart_rate} bpm</p>
            <p>BMI: {record.bmi}</p>
            <p>BMI Category: {record.bmi_category}</p>
            <p>Additional Notes: {record.additional_notes}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HealthList;
