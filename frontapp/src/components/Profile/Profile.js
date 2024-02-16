import React, { useEffect, useState } from 'react';
import axios from 'axios'; // Подключаем axios для выполнения запросов на сервер

const Profile = () => {
    // Состояние для хранения данных о пользователе
    const [userData, setUserData] = useState(null);

    // Функция для загрузки данных о пользователе с сервера
    const loadUserData = async () => {
        try {
            const response = await axios.get('/api/user/profile'); // Отправляем GET запрос на сервер для получения данных профиля
            setUserData(response.data); // Обновляем состояние данными о пользователе
        } catch (error) {
            console.error('Error loading user data:', error);
        }
    };

    // Загружаем данные пользователя при загрузке компонента
    useEffect(() => {
        loadUserData();
    }, []);

    // Если данные о пользователе еще не загружены, отобразим сообщение о загрузке
    if (!userData) {
        return <div>Loading...</div>;
    }

    // Рендеринг данных профиля пользователя
    return (
        <div className="profile">
            <h2>User Profile</h2>
            <p><strong>Username:</strong> {userData.username}</p>
            <p><strong>Email:</strong> {userData.email}</p>
            <p><strong>Height:</strong> {userData.height} cm</p>
            <p><strong>Weight:</strong> {userData.weight} kg</p>
            {/* Добавьте другие поля профиля, если необходимо */}
        </div>
    );
};

export default Profile;
