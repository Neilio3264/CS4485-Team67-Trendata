import React, { Component } from "react";
import { Link } from 'react-router-dom';

export default class qualityofLife extends Component {
  constructor(props) {
    super(props);
    this.state = {

    }
    this.onInputchange = this.onInputchange.bind(this);
  }

  onInputchange(event) {
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  onSubmitForm(id) {
    console.log(id)
    if (id != '')
    {
      this.props.history.push('/patient/' + id);
    }
    else
      return;
  }

  render() {
    const { items } = this.state;

    return (
      <div className="container">
        <div className="row"></div>
        <div className="row">
          <label htmlFor="patient_id" className="form-label" aria-describedby="formHelpBlock"><b>Patient ID</b></label>
          <input name="patient_id" type="text" className="form-control" id="patient_id" value={this.state.patient_id} onChange={this.onInputchange}></input>
          <div id="passwordHelpBlock" className="form-text">
            The id should be a 5 integer whole number, and must not contain test, spaces, special characters, or emoji.
          </div>
        </div>
        <div>
          <Link to={"/patient/" + this.state.patient_id}>
            <button className="btn btn-primary">Enter</button>
          </Link>
        </div>
      </div>
    );
  }
}
