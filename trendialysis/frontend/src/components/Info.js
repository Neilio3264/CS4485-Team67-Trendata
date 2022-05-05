import React, { Component } from "react";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const data = [
  {
    name: 'Page A',
    uv: 4000,
    pv: 2400,
    amt: 2400,
  },
  {
    name: 'Page B',
    uv: 3000,
    pv: 1398,
    amt: 2210,
  },
  {
    name: 'Page C',
    uv: 2000,
    pv: 9800,
    amt: 2290,
  },
  {
    name: 'Page D',
    uv: 2780,
    pv: 3908,
    amt: 2000,
  },
  {
    name: 'Page E',
    uv: 1890,
    pv: 4800,
    amt: 2181,
  },
  {
    name: 'Page F',
    uv: 2390,
    pv: 3800,
    amt: 2500,
  },
  {
    name: 'Page G',
    uv: 3490,
    pv: 4300,
    amt: 2100,
  },
];

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
        history: []
    };
    this.patientId = this.props.match.params.patientId;
    this.getPatientDetails = this.getPatientDetails.bind(this);
    this.getPatientHistory();
  }

  getPatientHistory() {
    fetch("/api/get-history" + "?patient_id=" + this.patientId)
      .then((response) => response.json())
      .then((data) => {
        this.setState({
          history: data,
      });
    });
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

  updateTable() {
    const data = this.state.history.map((record) => (
      <tr key={record.patient_id} className="row">
        <th className="col">{record.patient_id}</th>
        <td className="col">{record.time}</td>
        <td className="col">{record.inpatient}</td>
        <td className="col">{record.creatinine}</td>
        <td className="col">{record.aki}</td>
      </tr>
    ));
    return data;
  }

  render() {
    return (
      <div>
        <div className="container table-responsive">
          <h3>Patient Health Summary</h3>
          <table className="table table-striped table-bordered table-hover">
            <thead>
              <tr>
                <th>Dias_blood_pressure</th>
                <th>ur_specific_gravity</th>
                <th>ur_albumin</th>
                <th>ur_sugar</th>
                <th>red_blood_cells</th>
                <th>ur_pus_cell</th>
                <th>ur_pus_cell_Clumps</th>
                <th>ur_bacteria</th>
                <th>blood_glucose_random</th>
                <th>blood_urea</th>
                <th>sodium</th>
                <th>potassium</th>
                <th>hemoglobin</th>
                <th>packed_cell_volume</th>
                <th>white_blood_cell_count</th>
                <th>red_blood_cell_count</th>
                <th>hypertension</th>
                <th>diabetes</th>
                <th>coronary_artery_disease</th>
                <th>appetite</th>
                <th>pedal_edema</th>
                <th>anemia</th>
                <th>classification</th>
              </tr>
            </thead>
            <tbody>
                <tr>
                    <th>{this.state.Dias_blood_pressure}</th>
                    <th>{this.state.ur_specific_gravity}</th>
                    <th>{this.state.ur_albumin}</th>
                    <th>{this.state.ur_sugar}</th>
                    <th>{this.state.red_blood_cells}</th>
                    <th>{this.state.ur_pus_cell}</th>
                    <th>{this.state.ur_pus_cell_Clumps}</th>
                    <th>{this.state.ur_bacteria}</th>
                    <th>{this.state.blood_glucose_random}</th>
                    <th>{this.state.blood_urea}</th>
                    <th>{this.state.sodium}</th>
                    <th>{this.state.potassium}</th>
                    <th>{this.state.hemoglobin}</th>
                    <th>{this.state.packed_cell_volume}</th>
                    <th>{this.state.white_blood_cell_count}</th>
                    <th>{this.state.red_blood_cell_count}</th>
                    <th>{this.state.hypertension}</th>
                    <th>{this.state.diabetes}</th>
                    <th>{this.state.coronary_artery_disease}</th>
                    <th>{this.state.appetite}</th>
                    <th>{this.state.pedal_edema}</th>
                    <th>{this.state.anemia}</th>
                    <th>{this.state.classification}</th>
                </tr>
            </tbody>
          </table>
        </div>
        <div className="container table-responsive pad">
          <h3>Patient AKI Level</h3>
          <table className="table table-striped table-bordered table-hover">
            <thead>
              <tr className="row">
                <th className="col">Patient ID</th>
                <th className="col">Time</th>
                <th className="col">Inpatient</th>
                <th className="col">Creatinine</th>
                <th className="col">AKI</th>
              </tr>
            </thead>
            <tbody>{this.updateTable()}</tbody>
          </table>
        </div>
        <div className="container pad">
          <h3>AKI Levels Overtime</h3>
          <ResponsiveContainer width={'100%'} height={500}>
            <LineChart
              width={500}
              height={300}
              data={this.state.history}
              margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
              }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="time" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="aki" stroke="#8884d8" activeDot={{ r: 8 }} />
              <Line type="monotone" dataKey="creatinine" stroke="#82ca9d" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    );
  }
}
