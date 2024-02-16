// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Profile from './components/Profile';
import WorkoutListContainer from './containers/WorkoutListContainer';
import NewsListContainer from './containers/NewsListContainer';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/profile">
            <Profile />
          </Route>
          <Route path="/workouts">
            <WorkoutListContainer />
          </Route>
          <Route path="/news">
            <NewsListContainer />
          </Route>
          {/* Другие маршруты для других страниц */}
        </Switch>
      </div>
    </Router>
  );
};

export default App;
