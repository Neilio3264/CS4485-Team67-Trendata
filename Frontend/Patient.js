import React, { Component } from "react";
import { Table } from "react-bootstrap";
export class Patient extends Component {
  render() {
    return (
      <div>
        <Table className="mt-4" striped bordered hover size="sm">
          <thead>
            <tr>
              <th>Patient ID</th>
              <th>Patient Name</th>
              <th>Date of Birth</th>
              <th>Address</th>
            </tr>
          </thead>
        </Table>
      </div>
    );
  }
}
