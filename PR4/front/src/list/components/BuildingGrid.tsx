import React, { useState, useEffect } from 'react';
import {
  DataGrid,
  GridRowsProp,
  GridColDef,
  GridPaginationModel,
  GridSortModel,
  GridFilterModel
} from "@mui/x-data-grid";
import { ruRU } from '@mui/x-data-grid/locales';
import Container from '@mui/material/Container';
import { getCars } from '../../services/api';

function BuildingsGrid() {
  const [rows, setRows] = useState<GridRowsProp>([]);
  const [rowCount, setRowCount] = useState(0);
  const [loading, setLoading] = useState(false);

  const [paginationModel, setPaginationModel] = useState<GridPaginationModel>({
    page: 0,
    pageSize: 10
  });

  const [sortModel, setSortModel] = useState<GridSortModel>([]);
  const [filterModel, setFilterModel] = useState<GridFilterModel>({ items: [] });

  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const params: any = {
          page: paginationModel.page + 1,
          limit: paginationModel.pageSize,
        };

        if (sortModel.length > 0) {
          params.sort_by = sortModel[0].field;
          params.sort_dir = sortModel[0].sort === 'asc' ? 'asc' : 'desc';
        }

        if (filterModel.items.length > 0) {
          filterModel.items.forEach((item: any) => {
            if (item.field && item.value != null) {
              params[`filter[${item.field}]`] = item.value;

              if (item.operator) {
                params[`op[${item.field}]`] = item.operator;
              }
            }
          });
        }

        if (search) {
          params.search = search;
        }

        console.log(params);

        const response = await getCars(params);

        if (response.success) {
          const transformedRows = response.car_models.map((car: any, index: number) => ({
            id: car.id || index,
            make: car.make || '',
            model: car.model || '',
            year: car.year || '',
            vehicle_type: car.vehicle_type || '',
            engine_hp: car.engine_hp || '',
            engine_cylinders: car.engine_cylinders || '',
            transmission: car.transmission || '',
            driven_wheels: car.driven_wheels || '',
            number_of_doors: car.number_of_doors || '',
            categories: car.categories || ''
          }));

          setRows(transformedRows);
          setRowCount(response.total || transformedRows.length);
        }
      } catch (error) {
        console.error("Failed to fetch cars", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [paginationModel, sortModel, filterModel, search]);

  const columns: GridColDef[] = [
    { field: 'make', headerName: 'Марка', flex: 1, minWidth: 100 },
    { field: 'model', headerName: 'Модель', flex: 1, minWidth: 120 },
    { field: 'year', headerName: 'Год', width: 80 },
    { field: 'vehicle_type', headerName: 'Тип двигателя', flex: 1, minWidth: 100 },
    { field: 'engine_hp', headerName: 'Мощность', width: 100 },
    { field: 'engine_cylinders', headerName: 'Цилиндры', width: 90 },
    { field: 'transmission', headerName: 'Коробка', flex: 1, minWidth: 110 },
    { field: 'driven_wheels', headerName: 'Привод', flex: 1, minWidth: 100 },
    { field: 'number_of_doors', headerName: 'Двери', width: 70 },
    { field: 'categories', headerName: 'Категория', flex: 1, minWidth: 150 }
  ];

  return (
    <Container maxWidth="xl" sx={{ height: '700px', mt: '20px' }}>
      <DataGrid
        localeText={ruRU.components.MuiDataGrid.defaultProps.localeText}
        rows={rows}
        columns={columns}
        loading={loading}
        rowCount={rowCount}
        paginationMode="server"
        paginationModel={paginationModel}
        onPaginationModelChange={setPaginationModel}
        sortingMode="server"
        sortModel={sortModel}
        onSortModelChange={setSortModel}
        filterMode="server"
        filterModel={filterModel}
        onFilterModelChange={(model: any) => {
          setFilterModel(model);

          const quick = model.quickFilterValues?.[0] || "";
          setSearch(quick);
        }}
        showToolbar={true}
      />
    </Container>
  );
}

export default BuildingsGrid;