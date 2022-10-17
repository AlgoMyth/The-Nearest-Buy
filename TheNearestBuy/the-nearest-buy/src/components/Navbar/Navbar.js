import React, { useState } from "react";
import logo from "../../logo.svg";
import "./navbar.css";
import { Button, Stack } from "@mui/material";
import UserNavigation from "./UserNavigation";
import MenuIcon from "@mui/icons-material/Menu";

const Navbar = () => {
  const [isNavOpen, setIsNavOpen] = useState(0);
  const [isLogin, setIsLogin] = useState(0);
  const login = () => {
    setIsLogin(1);
  };
  const SignUp = () => {
    setIsLogin(1);
  };

  return (
    <>
      <span className="navIcon" onClick={() => setIsNavOpen(!isNavOpen)}>
        <MenuIcon />
      </span>
      {isNavOpen || window.innerWidth > 768 ? (
        <section id="navbar">
          <img src={logo} alt="" />
          <h2>Company Name</h2>
          <div className="loginSignUp">
            {isLogin ? (
              <div>
                <UserNavigation isLogin={isLogin} setIsLogin={setIsLogin} />
              </div>
            ) : (
              <Stack spacing={2} direction={{ xs: "column", sm: "row" }}>
                <Button variant="contained" onClick={() => login()}>
                  Login
                </Button>
                <Button variant="outlined">Sign Up</Button>
              </Stack>
            )}
          </div>
        </section>
      ) : (
        ""
      )}
    </>
  );
};

export default Navbar;
