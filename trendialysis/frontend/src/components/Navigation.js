import React, { Component } from "react";

export class Navigation extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <nav class="navbar navbar-fixed-top navbar-expand-lg navbar-light bg-light">
        <a href="#" class="navbar-brand mb-0 h1">
          <img
            class="d-inline-block align-top"
            src="https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
            width="30"
            height="30"
          />
          Trendialysis
        </a>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li lcass="nav-item active">
              <a href="/" class="nav-link">
                Home
              </a>
            </li>
            <li lcass="nav-item active">
              <a href="/patient" class="nav-link">
                Patient info
              </a>
            </li>
            <li lcass="nav-item active">
              <a href="/qualityofLife" class="nav-link">
                Quality of Life
              </a>
            </li>
          </ul>
        </div>
      </nav>
    );
  }
}
