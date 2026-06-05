import React, { useState, useEffect } from 'react';
import {
  Box, Button, Container, Typography, Dialog, DialogTitle, DialogContent,
  DialogActions, TextField, CircularProgress, Alert, FormControl, InputLabel, Select, MenuItem, Chip
} from '@mui/material';
import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { ruRU } from '@mui/x-data-grid/locales';
import { getCars, createCar, updateCar, deleteCar, getMakes, getVehicleTypes, getTransmissions, getDrivenWheels, getCategories } from '../services/api';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

function Crud() {
  const [rows, setRows] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [open, setOpen] = useState(false);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [error, setError] = useState('');
  
  // Справочники
  const [makes, setMakes] = useState<any[]>([]);
  const [vehicleTypes, setVehicleTypes] = useState<any[]>([]);
  const [transmissions, setTransmissions] = useState<any[]>([]);
  const [drivenWheels, setDrivenWheels] = useState<any[]>([]);
  const [categories, setCategories] = useState<any[]>([]);
  
  const [formData, setFormData] = useState({
    make: '', model: '', year: '', engine_hp: '', engine_cylinders: '',
    transmission: '', driven_wheels: '', number_of_doors: '', market_categories: '', vehicle_type: ''
  });

  useEffect(() => {
    const loadReferences = async () => {
      try {
        const [makesRes, vehicleTypesRes, transmissionsRes, drivenWheelsRes, categoriesRes] = await Promise.all([
          getMakes(),
          getVehicleTypes(),
          getTransmissions(),
          getDrivenWheels(),
          getCategories()
        ]);
        
        if (makesRes.success) setMakes(makesRes.makes);
        if (vehicleTypesRes.success) setVehicleTypes(vehicleTypesRes.vehicle_types);
        if (transmissionsRes.success) setTransmissions(transmissionsRes.transmissions);
        if (drivenWheelsRes.success) setDrivenWheels(drivenWheelsRes.driven_wheels);
        if (categoriesRes.success) setCategories(categoriesRes.categories);
      } catch (err) {
        console.error("Failed to load references", err);
      }
    };
    loadReferences();
  }, []);

  const fetchCars = async () => {
    setLoading(true);
    try {
      const response = await getCars({ limit: 1000 });
      if (response.success) {
        const transformed = response.car_models.map((car: any) => ({
          id: car.id,
          make: car.make || '',
          model: car.model || '',
          year: car.year || '',
          engine_hp: car.engine_hp || '',
          engine_cylinders: car.engine_cylinders || '',
          transmission: car.transmission || '',
          driven_wheels: car.driven_wheels || '',
          number_of_doors: car.number_of_doors || '',
          market_categories: car.categories || '',
          vehicle_type: car.vehicle_type || ''
        }));
        setRows(transformed);
      }
    } catch (err) {
      setError('Ошибка загрузки данных');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchCars(); }, []);

  const handleOpen = (row?: any) => {
    if (row) {
      setEditingId(row.id);
      setFormData({
        make: row.make, model: row.model, year: String(row.year),
        engine_hp: String(row.engine_hp), engine_cylinders: String(row.engine_cylinders),
        transmission: row.transmission, driven_wheels: row.driven_wheels,
        number_of_doors: String(row.number_of_doors), market_categories: row.market_categories,
        vehicle_type: row.vehicle_type
      });
    } else {
      setEditingId(null);
      setFormData({ make: '', model: '', year: '', engine_hp: '', engine_cylinders: '', transmission: '', driven_wheels: '', number_of_doors: '', market_categories: '', vehicle_type: '' });
    }
    setOpen(true);
    setError('');
  };

  const handleClose = () => { setOpen(false); setEditingId(null); setError(''); };

  const handleSubmit = async () => {
    try {
      if (editingId) {
        await updateCar(editingId, formData);
      } else {
        await createCar(formData);
      }
      handleClose();
      fetchCars();
    } catch (err: any) {
      setError(err.response?.data?.error || 'Ошибка сохранения');
    }
  };

  const handleDelete = async (id: number) => {
    if (window.confirm('Вы уверены, что хотите удалить эту запись?')) {
      try {
        await deleteCar(id);
        fetchCars();
      } catch (err) {
        setError('Ошибка удаления');
      }
    }
  };

  const columns: GridColDef[] = [
    { field: 'make', headerName: 'Марка', flex: 1 },
    { field: 'model', headerName: 'Модель', flex: 1 },
    { field: 'year', headerName: 'Год', width: 80 },
    { field: 'vehicle_type', headerName: 'Тип кузова', width: 120 },
    { field: 'engine_hp', headerName: 'Мощность', width: 100 },
    { field: 'engine_cylinders', headerName: 'Цилиндры', width: 100 },
    { field: 'transmission', headerName: 'Коробка', width: 120 },
    { field: 'driven_wheels', headerName: 'Привод', width: 120 },
    { field: 'number_of_doors', headerName: 'Двери', width: 80 },
    { field: 'market_categories', headerName: 'Категории', flex: 1 },
    { field: 'actions', headerName: 'Действия', width: 180, renderCell: (params) => (
      <Box sx={{ display: 'flex', gap: 1 }}>
        <Button size="small" variant="outlined" onClick={() => handleOpen(params.row)}>Изм.</Button>
        <Button size="small" variant="outlined" color="error" onClick={() => handleDelete(params.row.id)}>Удал.</Button>
      </Box>
    )}
  ];

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar active="5" />
      <Container maxWidth="xl" sx={{ mt: 4, mb: 4, flex: 1 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
          <Typography variant="h5">Управление автомобилями (CRUD)</Typography>
          <Button variant="contained" onClick={() => handleOpen()}>Добавить</Button>
        </Box>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <div style={{ height: 600, width: '100%' }}>
          <DataGrid
            localeText={ruRU.components.MuiDataGrid.defaultProps.localeText}
            rows={rows}
            columns={columns}
            loading={loading}
            getRowId={(row) => row.id}
          />
        </div>

        <Dialog open={open} onClose={handleClose} maxWidth="md" fullWidth>
          <DialogTitle>{editingId ? 'Редактировать' : 'Добавить'} автомобиль</DialogTitle>
          <DialogContent>
            {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
            <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 2, mt: 1 }}>
              <FormControl fullWidth required>
                <InputLabel>Марка</InputLabel>
                <Select
                  value={formData.make}
                  label="Марка"
                  onChange={e => setFormData({...formData, make: e.target.value})}
                >
                  {makes.map(make => (
                    <MenuItem key={make.id} value={make.name}>{make.name}</MenuItem>
                  ))}
                </Select>
              </FormControl>
              
              <TextField 
                label="Модель" 
                value={formData.model} 
                onChange={e => setFormData({...formData, model: e.target.value})} 
                required 
                fullWidth 
              />
              
              <TextField 
                label="Год" 
                type="number" 
                value={formData.year} 
                onChange={e => setFormData({...formData, year: e.target.value})} 
                required 
                fullWidth 
              />
              
              <FormControl fullWidth required>
                <InputLabel>Тип кузова</InputLabel>
                <Select
                  value={formData.vehicle_type}
                  label="Тип кузова"
                  onChange={e => setFormData({...formData, vehicle_type: e.target.value})}
                >
                  {vehicleTypes.map(type => (
                    <MenuItem key={type.id} value={type.name}>{type.name}</MenuItem>
                  ))}
                </Select>
              </FormControl>
              
              <TextField 
                label="Мощность (л.с.)" 
                type="number" 
                value={formData.engine_hp} 
                onChange={e => setFormData({...formData, engine_hp: e.target.value})} 
                required 
                fullWidth 
              />
              
              <TextField 
                label="Цилиндры" 
                type="number" 
                value={formData.engine_cylinders} 
                onChange={e => setFormData({...formData, engine_cylinders: e.target.value})} 
                required 
                fullWidth 
              />
              
              <FormControl fullWidth required>
                <InputLabel>Коробка</InputLabel>
                <Select
                  value={formData.transmission}
                  label="Коробка"
                  onChange={e => setFormData({...formData, transmission: e.target.value})}
                >
                  {transmissions.map(t => (
                    <MenuItem key={t.id} value={t.name}>{t.name}</MenuItem>
                  ))}
                </Select>
              </FormControl>
              
              <FormControl fullWidth required>
                <InputLabel>Привод</InputLabel>
                <Select
                  value={formData.driven_wheels}
                  label="Привод"
                  onChange={e => setFormData({...formData, driven_wheels: e.target.value})}
                >
                  {drivenWheels.map(w => (
                    <MenuItem key={w.id} value={w.name}>{w.name}</MenuItem>
                  ))}
                </Select>
              </FormControl>
              
              <TextField 
                label="Двери" 
                type="number" 
                value={formData.number_of_doors} 
                onChange={e => setFormData({...formData, number_of_doors: e.target.value})} 
                required 
                fullWidth 
              />
              
              <FormControl fullWidth required>
                <InputLabel>Категории</InputLabel>
                <Select
                  multiple
                  value={formData.market_categories ? formData.market_categories.split(',').map(s => s.trim()) : []}
                  label="Категории"
                  onChange={e => setFormData({...formData, market_categories: (e.target.value as string[]).join(', ')})}
                  renderValue={(selected) => (
                    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                      {selected.map((value) => (
                        <Chip key={value} label={value} size="small" />
                      ))}
                    </Box>
                  )}
                >
                  {categories.map(cat => (
                    <MenuItem key={cat.id} value={cat.name}>{cat.name}</MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Box>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose}>Отмена</Button>
            <Button onClick={handleSubmit} variant="contained">Сохранить</Button>
          </DialogActions>
        </Dialog>
      </Container>
      <Footer />
    </div>
  );
}
export default Crud;