import logo from "./logo.svg";
import "./App.css";

import { Home } from "./Home";
import { Patient } from "./Patient";
import { Navigation } from "./Navigation";

import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <div className="container">
        <h3 className="m-3 d-flex justify-content-center">
          Patient Infomation
        </h3>
        <Navigation />

        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/patient" element={<Patient />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
