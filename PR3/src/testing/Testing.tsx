import Navbar from "../components/Navbar";
import Quiz from "./features/Quiz";
import Footer from '../components/Footer';

function Testing() {
  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar active="4" />
      <div style={{ flex: 1 }}>
        <Quiz />
      </div>
      <Footer />
    </div>
  );
}

export default Testing;