import React from 'react';
import mapboxgl from "mapbox-gl";

type MapState = {
	latitude: number;
	longitude: number;
	zoom: number;
}

export default class Map extends React.Component<any, MapState> {

	private mapContainer: HTMLElement | null | undefined = undefined;

	constructor(props: any) {
		super(props);
		this.state = {
		    longitude: -121.9,
		    latitude: 47.35,
		    zoom: 5.5
	    };
	}

	componentDidMount() {
	    const map = new mapboxgl.Map({
		    accessToken:'pk.eyJ1Ijoia2l0aGFtbWVyIiwiYSI6ImNrdGtrNTZocDFtb2Uyb25temNoZGJ3eW4ifQ.2mOqsQ-QTu-ZceUWwOM5ZA',
		    container: this.mapContainer === undefined || this.mapContainer === null ? "" : this.mapContainer,
		    style: 'mapbox://styles/mapbox/streets-v11',
		    center: [this.state.longitude, this.state.latitude],
		    zoom: this.state.zoom
	    });
  	}

  	render() {
  		return (
  			<div 
          	ref={(el): void => {this.mapContainer = el;}} 
        	className="map-container" />
        );
  	}
}