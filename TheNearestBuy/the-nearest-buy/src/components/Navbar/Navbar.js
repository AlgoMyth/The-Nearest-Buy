import React, { useState } from "react";
import logo from "../../logo.svg";
import "./navbar.css";
import { Button, Stack } from "@mui/material";
import UserNavigation from "./UserNavigation";

const Navbar = () => {
  const [isLogin, setIsLogin] = useState(0);
  const login = () => {
    setIsLogin(1);
  };
  const SignUp = () => {
    setIsLogin(1);
  };

  return (
    <section id="navbar">
      <img src={logo} alt="" />
      <h2>Company Name</h2>
      <div className="loginSignUp">
        {isLogin ? (
          <>
            <UserNavigation isLogin={isLogin} setIsLogin={setIsLogin} />
          </>
        ) : (
          <Stack spacing={2} direction="row">
            <Button variant="contained" onClick={() => login()}>
              Login
            </Button>
            <Button variant="outlined">Sign Up</Button>
          </Stack>
        )}
      </div>
    </section>
  );
};

export default Navbar;
