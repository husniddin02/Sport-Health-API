import React, { useState } from 'react';

const WorkoutForm = ({ onSubmit }) => {
  const [exerciseType, setExerciseType] = useState('');
  const [duration, setDuration] = useState('');
  const [notes, setNotes] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ exerciseType, duration, notes });
    setExerciseType('');
    setDuration('');
    setNotes('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Workout</h2>
      <label>
        Exercise Type:
        <input type="text" value={exerciseType} onChange={(e) => setExerciseType(e.target.value)} />
      </label>
      <label>
        Duration:
        <input type="text" value={duration} onChange={(e) => setDuration(e.target.value)} />
      </label>
      <label>
        Notes:
        <textarea value={notes} onChange={(e) => setNotes(e.target.value)} />
      </label>
      <button type="submit">Add Workout</button>
    </form>
  );
};

export default WorkoutForm;
