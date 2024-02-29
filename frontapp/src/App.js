// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import CategoriesList from './components/Categories/CategoriesList';
import CategoryForm from './components/Categories/CategoryForm';
import CategoryDetails from './components/Categories/CategoryDetail';
import NewsList from './components/News/NewsLists';
import NewsForm from './components/News/NewsForm';
import NewsDetails from './components/News/NewsDetail';
import SportsFacilityList from './components/SportFacilities/SportsFacilityList';
import SportsFacilityForm from './components/SportFacilities/SportsFacilityForm';
import SportsFacilityDetails from './components/SportFacilities/SportsFacilityDetails';
import WorkoutList from './components/Workouts/WorkoutList';
import WorkoutForm from './components/Workouts/WorkoutForm';
import WorkoutDetails from './components/Workouts/WorkoutDetail';
import AuthForm from './components/Auth/AuthForm'; // импорт компонента для авторизации
import './App.css'; // импорт стилей для всего приложения

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/login" element={<AuthForm isLoginForm={true} />} />
          <Route path="/signup" element={<AuthForm isLoginForm={false} />} />
          <Route path="/" element={<Home />} />
          <Route path="/categories" element={<CategoriesList />} />
          <Route path="/categories/create" element={<CategoryForm />} />
          <Route path="/categories/:categoryId" element={<CategoryDetails />} />
          <Route path="/news" element={<NewsList />} />
          <Route path="/news/create" element={<NewsForm />} />
          <Route path="/news/:newsId" element={<NewsDetails />} />
          <Route path="/sports-facilities" element={<SportsFacilityList />} />
          <Route path="/sports-facilities/create" element={<SportsFacilityForm />} />
          <Route path="/sports-facilities/:facilityId" element={<SportsFacilityDetails />} />
          <Route path="/workouts" element={<WorkoutList />} />
          <Route path="/workouts/create" element={<WorkoutForm />} />
          <Route path="/workouts/:workoutId" element={<WorkoutDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
