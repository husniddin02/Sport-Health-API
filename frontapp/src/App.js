// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import CategoriesList from './components/Categories/CategoriesList';
import CategoryForm from './components/Categories/CategoryForm';
import CategoryDetails from './components/Categories/CategoryDetail';
import NewsList from './components/News/NewsLists';
import NewsForm from './components/News/NewsForm';
import NewsDetails from './components/News/NewsDetail';
import SportFacilityList from './components/SportFacilities/SportsFacilityList';
import SportFacilityForm from './components/SportFacilities/SportsFacilityForm';
import SportFacilityDetails from './components/SportFacilities/SportsFacilityDetails';
import WorkoutList from './components/Workouts/WorkoutList';
import WorkoutForm from './components/Workouts/WorkoutForm';
import WorkoutDetails from './components/Workouts/WorkoutDetail';

function App() {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" exact component={Home} />
          <Route path="/categories" exact component={CategoriesList} />
          <Route path="/categories/create" exact component={CategoryForm} />
          <Route path="/categories/:categoryId" exact component={CategoryDetails} />
          <Route path="/news" exact component={NewsList} />
          <Route path="/news/create" exact component={NewsForm} />
          <Route path="/news/:newsId" exact component={NewsDetails} />
          <Route path="/sport-facilities" exact component={SportFacilityList} />
          <Route path="/sport-facilities/create" exact component={SportFacilityForm} />
          <Route path="/sport-facilities/:facilityId" exact component={SportFacilityDetails} />
          <Route path="/workouts" exact component={WorkoutList} />
          <Route path="/workouts/create" exact component={WorkoutForm} />
          <Route path="/workouts/:workoutId" exact component={WorkoutDetails} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
