import Navbar from "../components/Navbar";
import BuildingsGrid from "./components/BuildingGrid";
import Footer from '../components/Footer';

function List() {
  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar active="2" />
      <div style={{ flex: 1 }}>
        <BuildingsGrid />
      </div>
      <Footer />
    </div>
  );
}

export default List;