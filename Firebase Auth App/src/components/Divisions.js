import React from "react";
import { useLocation } from "react-router-dom";
// import { Connector } from "mqtt-react-hooks";
// import Status from "./Status";

const Division = () => {
  const location = useLocation();

  return (
    <div>
      {location.pathname === "/division1" ? (
        <div>
          <h1>Division 1</h1>
          <p>Welcome to Division 1!</p>
        </div>
      ) : (
        <div>
          <h1>Division 2</h1>
          <p>Welcome to Division 2!</p>
        </div>
      )}
    </div>
  );
};

export default Division;
