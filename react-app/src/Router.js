import React from "react";
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";

export default class Router extends React.Component {
    constructor(props) {
        super(props);
        this.state = this.props.state;
    }

    render() {
        return (
            <BrowserRouter>
                <h1>TEST</h1>
            </BrowserRouter>
        );
    }
}