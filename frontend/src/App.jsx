import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import MenuGrid from './components/CashierPOS/MenuGrid';
import HRDashboard from './components/HRDashboard/LedgerTable';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50 flex flex-col">
        <nav className="bg-primary text-primary-foreground p-4 shadow-md flex justify-between items-center">
          <h1 className="text-xl font-bold">FlexiFeast</h1>
          <div className="flex gap-4">
            <Link to="/" className="hover:underline">POS Canteen</Link>
            <Link to="/hr" className="hover:underline">HR Admin</Link>
          </div>
        </nav>
        
        <main className="flex-1 p-4">
          <Routes>
            <Route path="/" element={<MenuGrid />} />
            <Route path="/hr" element={<HRDashboard />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
