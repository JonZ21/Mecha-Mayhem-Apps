import Signup from "./Signup";
import Login from "./Login";
import RoleSelect from "./RoleSelect.Js";
import Dashboard from "./Dashboard";
import { Container } from "react-bootstrap";
import { AuthProvider } from "../contexts/AuthContext";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Division from "./Divisions";
import PrivateRoute from "./PrivateRoute";
// import { AuthProvider } from "../contexts/AuthContext";
// import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
  return (
    <AuthProvider>
      <Container
        className="d-flex align-items-center justify-content-center"
        style={{ minHeight: "100vh" }}
      >
        <div className="w-100" style={{ maxWidth: "400px" }}>
          <Router>
            <AuthProvider>
              <Routes>
                <Route path="/" element={<Login />} />
                {/* <Route path="/signup" element={<Signup />} /> */}
                <Route path="/login" element={<Login />} />
                {/* <Route element={<PrivateRoute />}> */}
                <Route path="/home" element={<Dashboard />} />
                <Route path="/division1" element={<Division />} />
                <Route path="/division2" element={<Division />} />
                {/* </Route> */}
              </Routes>
            </AuthProvider>
          </Router>
        </div>
      </Container>
    </AuthProvider>
  );
}

export default App;
