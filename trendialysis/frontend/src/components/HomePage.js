import React, { Component } from "react";
import Patient from "./Patient";
import qualityofLife from "./qualityofLife";
import info from "./Info";

import {
  BrowserRouter as Router,
  Route,
  Link,
  Redirect,
  Switch,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <p> This is the home page</p>
          </Route>
          <Route exact path="/patient" component={Patient}></Route>
          <Route path="/patient/:patientId" component={info}></Route>
          <Route exact path="/qualityofLife" component={qualityofLife}></Route>
        </Switch>
      </Router>
    );
  }
}
