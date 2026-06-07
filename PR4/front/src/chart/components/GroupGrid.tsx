import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import { ruRU } from '@mui/x-data-grid/locales';
import Container from '@mui/material/Container';

type tGroup = {
  id: number | string;
  Группа: string;
  'Минимальная мощность': number;
  'Максимальная мощность': number;
  'Средняя мощность': number;
};

type GroupProps = {
  data: tGroup[];
};

function GroupGrid({ data }: GroupProps) {
  const rows: GridRowsProp = data;
  const columns: GridColDef[] = [
    { field: 'Группа', flex: 1 },
    { field: 'Минимальная мощность', flex: 1 },
    { field: 'Максимальная мощность', flex: 1 },
    { field: 'Средняя мощность', flex: 1 }
  ];
  return (
    <Container maxWidth="lg" sx={{ height: '500px', mt: '20px' }}>
      <DataGrid
        localeText={ruRU.components.MuiDataGrid.defaultProps.localeText}
        rows={rows}
        columns={columns}
        showToolbar={false}
      />
    </Container>
  );
}
export default GroupGrid;