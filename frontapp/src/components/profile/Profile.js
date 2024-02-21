// src/components/profile/Profile.js

import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getUserProfile } from '../../api/userApi';

import './Profile.css';

/**
 * Компонент страницы профиля пользователя
 */
const Profile = () => {
  const { userId } = useParams();
  const [userProfile, setUserProfile] = useState(null);

  useEffect(() => {
    // Здесь будет логика для загрузки профиля пользователя по userId
    const fetchUserProfile = async () => {
      try {
        const profileData = await getUserProfile(userId);
        setUserProfile(profileData);
      } catch (error) {
        console.error('Error fetching user profile:', error);
      }
    };
    fetchUserProfile();
  }, [userId]);

  return (
    <div className="profile-container">
      {userProfile ? (
        <div>
          <h2>{userProfile.name}</h2>
          <p>Email: {userProfile.email}</p>
          {/* Другие данные профиля, которые нужно отобразить */}
        </div>
      ) : (
        <p>Loading profile...</p>
      )}
    </div>
  );
};

export default Profile;
