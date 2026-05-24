import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Provider } from 'react-redux';
import store from './store';
import List from "./list/List";
import Main from "./main/Main";
import Chart from "./chart/Chart";
import Building from "./building/Building";
import Testing from "./testing/Testing";

const router = createBrowserRouter([
  {
    path: "",
    element: <Main />,
  },
  {
    path: "/list",
    element: <List />,
  },
  {
    path: "/chart",
    element: <Chart />,
  },
  {
    path: "/building/:id",
    element: <Building />,
  },
  {
    path: "/testing",
    element: <Testing />,
  },
]);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <Provider store={store}>
      <RouterProvider router={router} />
    </Provider>
  </React.StrictMode>
);