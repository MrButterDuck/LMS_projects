import Navbar from "../components/Navbar";
import BuildingsGrid from "./components/BuildingGrid";

function List() {
  return (
    <div>
      <Navbar active="2"/>
      <BuildingsGrid/>
    </div>
  );
}

export default List;