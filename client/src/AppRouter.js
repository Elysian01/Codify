import React from 'react';
import {  BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from './Home.component.js';

const App = () => {
    <BrowserRouter>
        <div>
            <Switch>
                <Route path = "/Home" component = {Home} exact = {true} />
            </Switch>
        </div>
    </BrowserRouter>
}

export default App;