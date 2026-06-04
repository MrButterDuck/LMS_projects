import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    mode: 'dark',

    primary: {
      main: '#ff3b30',
      light: '#ff6b63',
      dark: '#c6281e',
      contrastText: '#ffffff',
    },

    secondary: {
      main: '#00b4d8',
      light: '#48cae4',
      dark: '#0077b6',
      contrastText: '#ffffff',
    },

    info: {
      main: '#90e0ef',
      light: '#caf0f8',
      dark: '#0077b6',
      contrastText: '#000000',
    },

    background: {
      default: '#0f1115',
      paper: '#1a1d24',
    },

    text: {
      primary: '#f5f7fa',
      secondary: '#a9b0bb',
    },

    divider: '#2b2f38',
  },

  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',

    h4: {
      fontWeight: 700,
      color: '#ffffff',
    },

    h5: {
      fontWeight: 600,
      color: '#f5f7fa',
    },

    h6: {
      fontWeight: 600,
      color: '#f5f7fa',
    },
  },

  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: {
          backgroundColor: '#0f1115',
          color: '#f5f7fa',
        },
      },
    },

    MuiCard: {
      styleOverrides: {
        root: {
          backgroundColor: '#1a1d24',
          borderRadius: 14,
          border: '1px solid #2b2f38',
          boxShadow: '0 4px 16px rgba(0,0,0,0.35)',
        },
      },
    },

    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          borderRadius: 10,
          fontWeight: 600,
        },
      },
    },

    MuiAppBar: {
      styleOverrides: {
        root: {
          backgroundColor: '#111318',
          color: '#ffffff',
          borderBottom: '1px solid #2b2f38',
        },
      },
    },
  },
});

export default theme;