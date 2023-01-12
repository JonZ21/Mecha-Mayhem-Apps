import React from "react";
import { Route, Navigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";
import { Outlet } from "react-router";
import Signup from "./Signup";
import Login from "./Login";
import Dashboard from "./Dashboard";

const PrivateRoute = () => {
  const { isAuth } = useAuth();
  return isAuth ? <Outlet /> : <Login />;
};

export default PrivateRoute;

// export default function PrivateRoute({ component: Component, ...rest }) {
//   const { currentUser } = useAuth();

//   return (
//     <Route
//       {...rest}
//       render={(props) => {
//         return currentUser ? (
//           <Navigate to={...props} />
//         ) : (
//           <Navigate to="/login" />
//         );
//       }}
//     ></Route>
//   );
// }
