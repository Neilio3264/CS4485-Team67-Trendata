import React, { Component } from "react";
import { table } from "react-bootstrap";
import {
  BrowserRouter as Router,
  Route,
  Link,
  Redirect,
  Switch,
} from "react-router-dom";

export default class patient extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <table class="table">
        <thead>
          <tr>
            <th scope="col"> # </th>
            <th scope="col"> Patient ID </th>
            <th scope="col"> First Name </th>
            <th scope="col"> Last Name </th>
            <th scope="col"> Age </th>
            <th scope="col"> Gender </th>
            <th scope="col"> Phone</th>
          </tr>
        </thead>
      </table>
    );
  }
}
