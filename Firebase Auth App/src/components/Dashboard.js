import React, { useState, useEffect } from "react";
// import { useMqtt } from "react-mqtt";
import { Button } from "react-bootstrap";
import { useAuth } from "../contexts/AuthContext";
import { Link, useNavigate } from "react-router-dom";

export default function Dashboard() {
  const [error, setError] = useState("");
  const { currentUser, logout } = useAuth();
  const navigate = useNavigate();

  async function handleLogout() {
    setError("");

    try {
      await logout();
      navigate("/login");
    } catch {
      setError("Failed to log out");
    }
  }
  return (
    <div>
      <h1>Division Selector</h1>
      <Link to="/division1">Division1</Link>
      <Link to="/division2">Division2</Link>

      {/* <button onClick={handleStatkeeperClick}>Statkeeper</button> */}
      <div className="w-100 text-center mt-2">
        <Button variant="link" onClick={handleLogout}>
          Log Out
        </Button>
      </div>
    </div>
  );
}
