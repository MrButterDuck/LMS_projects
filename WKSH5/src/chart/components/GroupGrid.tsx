import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import { ruRU } from '@mui/x-data-grid/locales';
import Container from '@mui/material/Container';
import { tGroup } from "../groupdata";

type GroupProps = {
  data: tGroup;
};

function GroupGrid({ data }: GroupProps) {
  const rows: GridRowsProp = data;

  const columns: GridColDef[] = [
    { field: 'Группа', flex: 1 },
    { field: 'Минимальная высота', flex: 1 },
    { field: 'Максимальная высота', flex: 1 },
    { field: 'Средняя высота', flex: 1 },
  ];

  return (
    <Container maxWidth="lg" sx={{ height: '500px', mt: '20px' }}>
      <DataGrid
        localeText={ruRU.components.MuiDataGrid.defaultProps.localeText}
        rows={rows}
        columns={columns}
        showToolbar={true}
      />
    </Container>
  );
}

export default GroupGrid;