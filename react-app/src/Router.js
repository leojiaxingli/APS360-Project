import React from "react";
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";
import DrawBoard from "./react-components/drawingboard";

export default class Router extends React.Component {
    constructor(props) {
        super(props);
        this.state = this.props.state;
    }

    render() {
        return (
            <BrowserRouter>
                <Switch>
                    <Route exact path='/' render={() =>
                        (<DrawBoard appState={this.state}/>)}/>
                </Switch>);
            </BrowserRouter>
        );
    }
}