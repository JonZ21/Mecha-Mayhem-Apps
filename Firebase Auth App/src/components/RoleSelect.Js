import React, { useState } from "react";

function RoleSelect() {
  const [role, setRole] = useState(null);

  const handleScorekeeperClick = () => {
    setRole("Scorekeeper");
  };

  const handleStatkeeperClick = () => {
    setRole("Statkeeper");
  };

  return (
    <div>
      <h1>Role Selector</h1>
      {role ? <p>Your role is: {role}</p> : <p>No role selected</p>}
      <button onClick={handleScorekeeperClick}>Scorekeeper</button>
      <button onClick={handleStatkeeperClick}>Statkeeper</button>
    </div>
  );
}

export default RoleSelect;
