import axios from 'axios';

const API_URL = 'http://localhost:5000/api/v1';
const AUTH_USERNAME = 'student';
const AUTH_PASSWORD = 'dvfu';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  const credentials = btoa(`${AUTH_USERNAME}:${AUTH_PASSWORD}`);
  config.headers.Authorization = `Basic ${credentials}`;
  return config;
});

export const getCars = async (params?: any) => {
  const response = await api.get('/car-models/', { params });
  return response.data;
};

export const getCarById = async (id: number) => {
  const response = await api.get(`/car-models/${id}`);
  return response.data;
};

export const createCar = async (data: any) => {
  const response = await api.post('/car-models/', data);
  return response.data;
};

export const updateCar = async (id: number, data: any) => {
  const response = await api.put(`/car-models/${id}`, data);
  return response.data;
};

export const deleteCar = async (id: number) => {
  const response = await api.delete(`/car-models/${id}`);
  return response.data;
};

export const getAggregateData = async (type: 'make' | 'transmission' | 'vehicle-type' | 'year') => {
  const response = await api.get(`/aggregate/${type}/`);
  return response.data;
};

export const getQuizData = async () => {
  const response = await api.get('/quiz/');
  return response.data;
};

export const getMakes = async () => {
  const response = await api.get('/car-models/makes');
  return response.data;
};

export const getVehicleTypes = async () => {
  const response = await api.get('/car-models/vehicle-types');
  return response.data;
};

export const getTransmissions = async () => {
  const response = await api.get('/car-models/transmissions');
  return response.data;
};

export const getDrivenWheels = async () => {
  const response = await api.get('/car-models/driven-wheels');
  return response.data;
};

export const getCategories = async () => {
  const response = await api.get('/car-models/categories');
  return response.data;
};