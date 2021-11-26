import './App.css';
import Router from "./Router";
import React from 'react';

class App extends React.Component {
    render() {
        return (
            <div className="App">
                <Router state={this.state}/>
            </div>
        );
    }
}

export default App;
