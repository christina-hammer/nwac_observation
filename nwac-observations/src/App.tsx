import './App.css';
import React from 'react';
import ReactDOM from 'react-dom';
import Map from './Map';

export default class App extends React.Component<any, any> {

  constructor(props: any) {
    super(props);
  }

  render() {
    return (
      <div className="App">
        <header className="page-header">
        <h1>NWAC Observation Map</h1>
          <p style={{ color:'pink'}}>
            This is where a disclaimer belongs.
          </p>
        </header>
        <div>
          <Map/>
        </div>
      </div>
    );
  }
}