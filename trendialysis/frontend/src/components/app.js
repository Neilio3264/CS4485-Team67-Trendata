import React, { Component, StrictMode } from "react";
import { createRoot } from "react-dom/client";
import HomePage from "./HomePage";
import { Navigation } from "./Navigation";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="container">
        <Navigation />
        <HomePage />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
const app = createRoot(appDiv);
app.render(
  <StrictMode>
    <App />
  </StrictMode>
)
