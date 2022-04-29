import React, { Component } from "react";

export class Navigation extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <a href="#" className="navbar-brand mb-0 h1">
          <img
            className="d-inline-block align-top"
            src="https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg"
            width="30"
            height="30"
          />
          Trendialysis
        </a>
        <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <a href="/" className="nav-link">
                Home
              </a>
            </li>
            <li className="nav-item active">
              <a href="/patient" className="nav-link">
                Patient info
              </a>
            </li>
            <li className="nav-item active">
              <a href="/qualityofLife" className="nav-link">
                Quality of Life
              </a>
            </li>
          </ul>
        </div>
      </nav>
    );
  }
}
