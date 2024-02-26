// src/components/Health/HealthDetails.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import HealthService from '../../services/healthService';

const HealthDetails = () => {
  const { healthId } = useParams();
  const [healthRecord, setHealthRecord] = useState(null);

  useEffect(() => {
    const fetchHealthRecord = async () => {
      try {
        const data = await HealthService.getHealthRecordById(healthId);
        setHealthRecord(data);
      } catch (error) {
        console.error('Error fetching health record details:', error);
      }
    };

    fetchHealthRecord();
  }, [healthId]);

  if (!healthRecord) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Health Record Details</h2>
      <p>Height: {healthRecord.height} cm</p>
      <p>Weight: {healthRecord.weight} kg</p>
      <p>Heart Rate: {healthRecord.heart_rate} bpm</p>
      <p>BMI: {healthRecord.bmi}</p>
      <p>BMI Category: {healthRecord.bmi_category}</p>
      <p>Additional Notes: {healthRecord.additional_notes}</p>
    </div>
  );
};

export default HealthDetails;
