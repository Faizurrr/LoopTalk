import "./App.css";
import { Routes, Route } from "react-router-dom";
import Home from "./Pages/Home";
import Navbar from "./Components/Common/Navbar";
import Footer from "./Components/Common/Footer";
import Signuppage from "./Pages/Signuppage";
import Signinpage from "./Pages/SinginPage";
import Profile from "./Pages/Profile";

function App() {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/SigninPage" element={<Signinpage />} /> 
        <Route path="/SignupPage" element={<Signuppage />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>

      <Footer />
    </>
  );
}

export default App;