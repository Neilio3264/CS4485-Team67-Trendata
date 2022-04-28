import React, { Component } from "react";
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
    this.state = {
      patients: [],
    };
    this.getPatientDetails();
  }
  jqueryPart() {
    this.jqueryPart(document).ready(function ($) {
      $("*[data-href]").on("click", function () {
        window.location = $(this).data("/qualityofLife");
      });
    });
  }
  getPatientDetails() {
    fetch("/api/get-patients")
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          patients: data,
        });
      });
    console.log("This is the patient array: " + this.state.patients);
  }

  updateTable() {
    const data = this.state.patients.map((patient) => (
      <tr key={patient.patient_id}>
        <th scope="row">{patient.patient_id}</th>
        <td data-href="/qualityofLife">{patient.first_name}</td>
        <td>{patient.last_name}</td>
        <td>{patient.age}</td>
        <td>{patient.gender}</td>
        <td>{patient.phone}</td>
      </tr>
    ));
    return data;
  }

  render() {
    return (
      <table class="table table-responsive table-striped table-bordered table-hover">
        <thead>
          <tr>
            <th scope="col">Patient ID</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Age</th>
            <th scope="col">Gender</th>
            <th scope="col">Phone</th>
            <th scope="col">$$$</th>
            <th scope="col">$$$</th>
          </tr>
        </thead>
        <tbody>{this.updateTable()}</tbody>
      </table>
    );
  }
}
