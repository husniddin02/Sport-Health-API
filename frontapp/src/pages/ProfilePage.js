import React from 'react';
import './ProfilePage.css';
import ProfileStatus from '../components/profile/ProfileStatus';
import ProfileAchievements from '../components/profile/ProfileAchievements';

function ProfilePage() {
  return (
    <div className="profile-page">
      <h1>Profile</h1>
      <div className="profile-content">
        <ProfileStatus />
        <ProfileAchievements />
      </div>
    </div>
  );
}

export default ProfilePage;
