// src/containers/WorkoutListContainer.js
import React, { useState, useEffect } from 'react';
import WorkoutList from '../components/WorkoutList';

const WorkoutListContainer = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/workouts');
        if (!response.ok) {
          throw new Error('Failed to fetch workouts');
        }
        const data = await response.json();
        setWorkouts(data);
      } catch (error) {
        console.error('Error fetching workouts:', error);
      }
    };

    fetchWorkouts();
  }, []);

  return <WorkoutList workouts={workouts} />;
};

export default WorkoutListContainer;
