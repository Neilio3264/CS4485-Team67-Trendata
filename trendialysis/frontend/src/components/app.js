import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";
import { Navigation } from "./Navigation";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Navigation />
        <HomePage />
      </div>
    );
  }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);
