import React from 'react';
import './App.css';
import AppointmentCards from './components/AppointmentCards';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Clinic Patient Portal</h1>
        <p>Welcome to your healthcare management system.</p>
      </header>
      <AppointmentCards />
    </div>
  );
}

export default App;
