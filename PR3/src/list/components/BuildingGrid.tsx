import cars from "../table";
import { DataGrid, GridRowsProp, GridColDef } from "@mui/x-data-grid";
import { ruRU } from '@mui/x-data-grid/locales';
import Container from '@mui/material/Container';

function BuildingsGrid() {
  const rows: GridRowsProp = cars;
  const columns: GridColDef[] = [
    { field: 'Марка', flex: 1 },
    { field: 'Модель', flex: 1 },
    { field: 'Год', width: 80 },
    { field: 'Тип двигателя', flex: 1 },
    { field: 'Мощность', width: 100 },
    { field: 'Цилиндры', width: 90 },
    { field: 'Коробка', width: 110 },
    { field: 'Привод', flex: 1 },
    { field: 'Двери', width: 70 },
    { field: 'Категория', flex: 1 },
    { field: 'Размер', width: 100 },
    { field: 'Стиль', width: 110 },
    { field: 'Трасса MPG', width: 100 },
    { field: 'Город MPG', width: 100 },
    { field: 'Популярность', width: 110 },
    { field: 'MSRP', width: 100 }
  ];

  return (
    <Container maxWidth="xl" sx={{ height: '700px', mt: '20px' }}>
      <DataGrid
        localeText={ruRU.components.MuiDataGrid.defaultProps.localeText}
        rows={rows}
        columns={columns}
        showToolbar={true}
      />
    </Container>
  );
}

export default BuildingsGrid;