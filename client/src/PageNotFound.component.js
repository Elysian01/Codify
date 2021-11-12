import React from "react";
// import "../styles/common.css";
import { Link } from "react-router-dom";

const PageNotFound = () => (
  <div class="not-found-container">
    <div class="boo-wrapper">
      <div class="boo">
        <div class="face"></div>
      </div>
      <div class="shadow"></div>
      <h1>Whoops!</h1>
      <p>
        We couldn't find the page you
        <br />
        were looking for.
      </p>
      <br />
      <Link to="/cashier/home">
        <button class="not-found-btn">Back to Homepage</button>
      </Link>
    </div>
  </div>
);

export default PageNotFound;
