import React, { Component } from "react";

export default class patient extends Component {
  constructor(props) {
    super(props);
    this.state = {
      patients: [],
    };
    this.getPatientDetails();

    this.print = this.print.bind(this);
  }

  print() {
    document.addEventListener("DOMContentLoaded", () => {
      const rows = document.querySelectorAll("tr[data-href]");
      console.log(rows);
    })
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
  }

  updateTable() {
    const data = this.state.patients.map((patient) => (
      <tr key={patient.patient_id} className="row" data-href="https://www.google.com/">
        <th className="col">{patient.patient_id}</th>
        <td className="col" data-href="/qualityofLife">{patient.first_name}</td>
        <td className="col">{patient.last_name}</td>
        <td className="col">{patient.age}</td>
        <td className="col">{patient.gender}</td>
        <td className="col">{patient.phone}</td>
      </tr>
    ));
    return data;
  }

  render() {
    return (
      <div className="container table-responsive">
        <table className="table table-striped table-bordered table-hover">
          <thead>
            <tr className="row">
              <th className="col">Patient ID</th>
              <th className="col">First</th>
              <th className="col">Last</th>
              <th className="col">Age</th>
              <th className="col">Gender</th>
              <th className="col">Phone</th>
            </tr>
          </thead>
          <tbody>{this.updateTable()}</tbody>
        </table>
      </div>
    );
  }
}
