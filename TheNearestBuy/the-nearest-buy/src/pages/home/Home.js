import React from "react";
import axios from "axios";
import Product from "../../components/Products/Product";
import "./home.css";

const Home = () => {
  fetch("http://127.0.0.1:8000/wel/?format=api", {
    mode: "no-cors",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    });

  return (
    <section id="home">
      <div className="products">
        <Product />
        <Product />
        <Product />
        <Product />
        <Product />
        <Product />
      </div>
    </section>
  );
};

export default Home;
