import React from 'react';
import {  BrowserRouter, Route, Routes  } from 'react-router-dom';
import Home from './Home.js';
import App from './App.js';

const PageNotFound = () => (
    <div>
        test
    </div>
)

const AppRouter = () => (
    <BrowserRouter>
        <div>
            <Routes >
                <Route path = "/" element = {<App />} exact = {true}  />
                <Route path = "/Home" element = {<Home /> } exact = {true} />
                <Route element={<PageNotFound />} />
            </Routes >
        </div>
    </BrowserRouter>
);
export default AppRouter;