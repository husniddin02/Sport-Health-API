import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { createSportsFacility } from '../../services/sportsFacilityService'; // Обновленный импорт

function SportsFacilityForm() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  async function handleSubmit(event) {
    event.preventDefault();
    try {
      await createSportsFacility({ name, description }); // Обновленный вызов функции
      navigate('/sports-facilities'); // Используем navigate вместо history.push
    } catch (error) {
      setError(error);
    }
  }

  return (
    <div>
      <h1>Add Sports Facility</h1>
      {error && <div>Error: {error.message}</div>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Description:</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />
        </div>
        <button type="submit">Add Facility</button>
      </form>
    </div>
  );
}

export default SportsFacilityForm;
