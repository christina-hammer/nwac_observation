import './App.css';
import React from 'react';
import ReactDOM from 'react-dom';
import mapboxgl from "mapbox-gl";

export default class App extends React.Component<any, any> {

  private mapContainer: HTMLElement | null | undefined = undefined;

  constructor(props: any) {
    super(props);
    this.state = {
    lng: -121.9,
    lat: 47.35,
    zoom: 5.5
    };
  }

  componentDidMount() {
    const { lng, lat, zoom } = this.state;
    const map = new mapboxgl.Map({
    accessToken:'',
    container: this.mapContainer === undefined || this.mapContainer === null ? "" : this.mapContainer,
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
        <div 
          style={{ marginLeft:'24px', marginRight:'24px'}} 
          ref={(el): void => {
            this.mapContainer = el;
          }} 
        className="map-container" />
        </div>
      </div>
    );
  }
}