import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Provider } from 'react-redux';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import store from './store';
import theme from './theme';
import List from "./list/List";
import Main from "./main/Main";
import Chart from "./chart/Chart";
import Building from "./building/Building";
import Testing from "./testing/Testing";
import Crud from "./crud/Crud"

const router = createBrowserRouter([
  { path: "/", element: <Main /> },
  { path: "/list", element: <List /> },
  { path: "/chart", element: <Chart /> },
  { path: "/building/:id", element: <Building /> },
  { path: "/testing", element: <Testing /> },
   { path: "/crud", element: <Crud /> }
]);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <React.StrictMode>
    <Provider store={store}>
      <ThemeProvider theme={theme}>
        <CssBaseline /> 
        <RouterProvider router={router} />
      </ThemeProvider>
    </Provider>
  </React.StrictMode>
);