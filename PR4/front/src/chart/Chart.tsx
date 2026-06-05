import * as React from 'react';
import Navbar from "../components/Navbar";
import GroupGrid from "./components/GroupGrid";
import GroupChart from "./components/GroupChart";
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Footer from '../components/Footer';
import { getAggregateData } from '../services/api';

type tSelect = "Марка" | "Год" | "Кузов";

function Chart() {
  const [group, setGroup] = React.useState<tSelect>("Марка");
  const [groupData, setGroupData] = React.useState<any[]>([]);
  const [loading, setLoading] = React.useState(false);

  React.useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        let endpoint: 'make' | 'year' | 'vehicle-type' = 'make';
        if (group === "Год") endpoint = 'year';
        else if (group === "Кузов") endpoint = 'vehicle-type';

        const response = await getAggregateData(endpoint);
        if (response.success) {
          const transformed = response.stat.map((item: any) => ({
            id: item.id || item.year,
            Группа: item.make || item.year || item.vehicle_type || item.transmission,
            'Минимальная мощность': item.min_hp,
            'Максимальная мощность': item.max_hp,
            'Средняя мощность': item.avg_hp
          }));
          setGroupData(transformed);
        }
      } catch (error) {
        console.error("Failed to fetch aggregate data", error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [group]);

  const handleChange = (event: SelectChangeEvent) => {
    setGroup(event.target.value as tSelect);
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
              disabled={loading}
            >
              <MenuItem value="Марка">Марке</MenuItem>
              <MenuItem value="Год">Году</MenuItem>
              <MenuItem value="Кузов">Типу кузова</MenuItem>
            </Select>
          </FormControl>
        </Box>
        {loading ? <Box sx={{ textAlign: 'center', mt: 4 }}>Загрузка...</Box> : (
          <>
            <GroupChart data={groupData} />
            <GroupGrid data={groupData} />
          </>
        )}
      </div>
      <Footer />
    </div>
  );
}
export default Chart;