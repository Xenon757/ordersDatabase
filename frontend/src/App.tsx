import { useState, useEffect } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://127.0.0.1:8000/api/tests/");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const jsonData = await response.json();
      console.log(jsonData);
    };

    fetchData(); // Call the function when the component mounts

    // Optionally, you can include dependencies in the array below
    // to make the effect re-run when certain values change.
  }, []); // Empty dependency array means this effect will run once after the initial render

  return <></>;
}

export default App;
