import React from 'react';

import './styles.css';
import DrawingBoard from "react-drawing-board";
import {config} from "../../config";

class DrawBoard extends React.Component {
    state = {recognition:''}
    constructor(props) {
        super(props);
    }

    onSave(img) {
        let data_url = img.dataUrl
        const body = {
            data_url: data_url
        }
        const request = {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body),
            mode: 'cors',
        };
        return fetch(config['SERVER_URL'] + "/recognize", request)
            .then(res => res.json())
            .then(data => {
                this.setState({recognition:data.recognition})
            })
            .catch()
    }

    render() {
        return (
            <div className="board-container">
                <DrawingBoard onSave={this.onSave.bind(this)}/>
                <div className="input-container">
                    <h1 id="recognition-text">{this.state.recognition}</h1>
                </div>
            </div>
        );
    }
}

export default DrawBoard;
