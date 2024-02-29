// src/components/Auth/AuthForm.js
import React, { useState } from 'react';
import './authForms.css'; // импортируем наши стили

function AuthForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [action, setAction] = useState('signin');

  const handleRadioChange = (e) => {
    setAction(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (action === 'signin') {
      // Здесь будет логика для входа
      console.log('Sign in with:', email, password);
    } else if (action === 'signup') {
      // Здесь будет логика для регистрации
      console.log('Sign up with:', email, password);
    } else {
      // Здесь будет логика для сброса пароля
      console.log('Reset password for:', email);
    }
  };

  return (
    <div className="auth-form">
      <form onSubmit={handleSubmit}>
        <input
          id="signin"
          name="action"
          type="radio"
          value="signin"
          checked={action === 'signin'}
          onChange={handleRadioChange}
        />
        <label htmlFor="signin">Sign in</label>

        <input
          id="signup"
          name="action"
          type="radio"
          value="signup"
          checked={action === 'signup'}
          onChange={handleRadioChange}
        />
        <label htmlFor="signup">Sign up</label>

        <input
          id="reset"
          name="action"
          type="radio"
          value="reset"
          checked={action === 'reset'}
          onChange={handleRadioChange}
        />
        <label htmlFor="reset">Reset</label>

        <div id="wrapper">
          <div id="arrow"></div>
          <input
            id="email"
            placeholder="Email"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            id="pass"
            placeholder="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          {action === 'signup' && (
            <input
              id="repass"
              placeholder="Repeat password"
              type="password"
              required
            />
          )}
        </div>

        <button type="submit">
          <span>
            {action === 'reset' ? 'Reset password' : action === 'signin' ? 'Sign in' : 'Sign up'}
          </span>
        </button>
      </form>
      <div id="hint">Click on the tabs</div>
    </div>
  );
}

export default AuthForm;
