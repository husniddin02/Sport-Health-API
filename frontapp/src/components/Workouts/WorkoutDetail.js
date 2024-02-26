// src/components/Workout/WorkoutDetails.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import WorkoutService from '../../services/workoutService';

const WorkoutDetails = () => {
  const { workoutId } = useParams();
  const [workout, setWorkout] = useState(null);

  useEffect(() => {
    const fetchWorkout = async () => {
      try {
        const data = await WorkoutService.getWorkoutById(workoutId);
        setWorkout(data);
      } catch (error) {
        console.error('Error fetching workout details:', error);
      }
    };

    fetchWorkout();
  }, [workoutId]);

  if (!workout) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>{workout.exercise_type}</h2>
      <p>Date: {workout.workout_date}</p>
      <p>Duration: {workout.duration}</p>
      <p>Notes: {workout.notes}</p>
    </div>
  );
};

export default WorkoutDetails;
