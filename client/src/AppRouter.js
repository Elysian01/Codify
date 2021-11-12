import React from 'react';
import {  BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from './Home.component.js';
import PageNotFound from '../PageNotFound.component';

const App = () => {
    <BrowserRouter>
        <div>
            <Switch>
                        
                <Route path = "/Home" component = {Home} exact = {true} />
                <Route component={PageNotFound} />
            </Switch>
        </div>
    </BrowserRouter>
}

export default App;