import './App.css';
import React, { useRef, useEffect, useState } from 'react';

import mapboxgl from '!mapbox-gl'; // eslint-disable-line import/no-webpack-loader-syntax

//TODO add secure storage solution for this token
mapboxgl.accessToken = '';


export default class App extends React.PureComponent {

  constructor(props) {
    super(props);
    this.state = {
    lng: -70.9,
    lat: 42.35,
    zoom: 9
    };
    this.mapContainer = React.createRef();
  }

  componentDidMount() {
    const { lng, lat, zoom } = this.state;
    const map = new mapboxgl.Map({
    container: this.mapContainer.current,
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [lng, lat],
    zoom: zoom
    });
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
        <div ref={this.mapContainer} className="map-container" />
        </div>
      </div>
    );
  }
}