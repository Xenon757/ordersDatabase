import logo from "./logo.svg";
import "./App.css";
import { useEffect } from "react";

function App() {
  const apiCall = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/tests/");
    const data = await response.json();
    console.log(data);
  };
  useEffect(() => {
    apiCall();
  }, []);
  return (
    <>
      <div>Hello there!</div>
    </>
  );
}

export default App;
