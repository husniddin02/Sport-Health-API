// src/components/Workout/WorkoutList.js

import React, { useState, useEffect } from 'react';
import WorkoutService from '../../services/workoutService';

const WorkoutList = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const data = await WorkoutService.getAllWorkouts();
        setWorkouts(data);
      } catch (error) {
        console.error('Error fetching workouts:', error);
      }
    };

    fetchWorkouts();
  }, []);

  return (
    <div>
      <h2>Workouts</h2>
      <ul>
        {workouts.map((workout) => (
          <li key={workout.workout_id}>
            <h3>{workout.exercise_type}</h3>
            <p>Date: {workout.workout_date}</p>
            <p>Duration: {workout.duration}</p>
            <p>Notes: {workout.notes}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default WorkoutList;
