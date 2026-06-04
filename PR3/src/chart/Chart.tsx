import * as React from 'react';
import Navbar from "../components/Navbar";
import GroupGrid from "./components/GroupGrid";
import GroupChart from "./components/GroupChart";
import { years, brands, bodyStyles } from "./groupdata";
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Footer from '../components/Footer';

type tSelect = "Марка" | "Год" | "Кузов";

function Chart() {
  const [group, setGroup] = React.useState<tSelect>("Марка");
  const [groupData, setGroupData] = React.useState(brands);

  const handleChange = (event: SelectChangeEvent) => {
    const value = event.target.value as tSelect;
    setGroup(value);
    if (value === "Марка") setGroupData(brands);
    else if (value === "Год") setGroupData(years);
    else if (value === "Кузов") setGroupData(bodyStyles);
  };

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar active="3" />
      <div style={{ flex: 1 }}>
        <Box sx={{ width: "200px", m: "auto", mt: "20px" }}>
          <FormControl fullWidth>
            <InputLabel>Группировать по</InputLabel>
            <Select
              id="select-group"
              value={group}
              label="Группировать по"
              onChange={handleChange}
            >
              <MenuItem value="Страна">Стране</MenuItem>
              <MenuItem value="Год">Году</MenuItem>
              <MenuItem value="Тип">Типу</MenuItem>
            </Select>
          </FormControl>
        </Box>
        <GroupChart data={groupData} />
        <GroupGrid data={groupData} />
      </div>
      <Footer />
    </div>
  );
}

export default Chart;