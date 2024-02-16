import React, { useState, useEffect } from 'react';
import axios from 'axios';

const WorkoutList = () => {
    const [workouts, setWorkouts] = useState([]);

    useEffect(() => {
        // Получение списка тренировок с сервера
        const fetchWorkouts = async () => {
            try {
                const response = await axios.get('/api/workouts');
                setWorkouts(response.data);
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
                {workouts.map(workout => (
                    <li key={workout.id}>{workout.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default WorkoutList;
