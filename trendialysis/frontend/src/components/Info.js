import React, { Component } from "react";

export default class info extends Component {
  constructor(props) {
    super(props);
    this.state = {
        Dias_blood_pressure: 80.0,
        ur_specific_gravity: 1.02,
        ur_albumin: 1.0,
        ur_sugar: 0.0,
        red_blood_cells: null,
        ur_pus_cell: "normal",
        ur_pus_cell_Clumps: "notpresent",
        ur_bacteria: "notpresent",
        blood_glucose_random: 121.0,
        blood_urea: 36.0,
        sodium: null,
        potassium: null,
        hemoglobin: 15.4,
        packed_cell_volume: 44,
        white_blood_cell_count: 7800,
        red_blood_cell_count: 5.2,
        hypertension: "yes",
        diabetes: "yes",
        coronary_artery_disease: "no",
        appetite: "good",
        pedal_edema: "no",
        anemia: "no",
        classification: "ckd",
    };
    this.patientId = this.props.match.params.patientId;
    this.getPatientDetails();
  }

  getPatientDetails() {
    fetch("/api/get-metrics" + "?patient_id=" + this.patientId)
      .then((response) => response.json())
      .then((data) => {
          console.log(data);
        this.setState({
            Dias_blood_pressure: data.Dias_blood_pressure,
            ur_specific_gravity: data.ur_specific_gravity,
            ur_albumin: data.ur_albumin,
            ur_sugar: data.ur_sugar,
            red_blood_cells: data.red_blood_cells,
            ur_pus_cell: data.ur_pus_cell,
            ur_pus_cell_Clumps: data.ur_pus_cell_Clumps,
            ur_bacteria: data.ur_bacteria,
            blood_glucose_random: data.blood_glucose_random,
            blood_urea: data.blood_urea,
            sodium: data.sodium,
            potassium: data.potassium,
            hemoglobin: data.hemoglobin,
            packed_cell_volume: data.packed_cell_volume,
            white_blood_cell_count: data.white_blood_cell_count,
            red_blood_cell_count: data.red_blood_cell_count,
            hypertension: data.hypertension,
            diabetes: data.diabetes,
            coronary_artery_disease: data.coronary_artery_disease,
            appetite: data.appetite,
            pedal_edema: data.pedal_edema,
            anemia: data.anemia,
            classification: data.classification,
        });
      });
  }

  render() {
    return (
      <div className="container">
        <table className="table table-responsive table-striped table-bordered table-hover">
          <thead>
            <tr className="row">
              <th className="col">Dias_blood_pressure</th>
              <th className="col">ur_specific_gravity</th>
              <th className="col">ur_albumin</th>
              <th className="col">ur_sugar</th>
              <th className="col">red_blood_cells</th>
              <th className="col">ur_pus_cell</th>
              <th className="col">ur_pus_cell_Clumps</th>
              <th className="col">ur_bacteria</th>
            </tr>
          </thead>
          <tbody>
              <tr className="row">
                  <th className="col">{this.state.Dias_blood_pressure}</th>
                  <th className="col">{this.state.ur_specific_gravity}</th>
                  <th className="col">{this.state.ur_albumin}</th>
                  <th className="col">{this.state.ur_sugar}</th>
                  <th className="col">{this.state.red_blood_cells}</th>
                  <th className="col">{this.state.ur_pus_cell}</th>
                  <th className="col">{this.state.ur_pus_cell_Clumps}</th>
                  <th className="col">{this.state.ur_bacteria}</th>
              </tr>
          </tbody>
        </table>
      </div>
    );
  }
}
