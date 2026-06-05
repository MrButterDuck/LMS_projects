import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuItem from '@mui/material/MenuItem';
import Drawer from '@mui/material/Drawer';
import MenuIcon from '@mui/icons-material/Menu';
import MenuList from '@mui/material/MenuList';
import CloseRoundedIcon from '@mui/icons-material/CloseRounded';
import { styled } from '@mui/material/styles';
import { Link } from 'react-router-dom';

const StyledToolbar = styled(Toolbar)(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center', 
  flexShrink: 0,
  borderRadius: `calc(${theme.shape.borderRadius}px + 8px)`,
  border: '2px solid',
  borderColor: '#1d3557',
  padding: '8px 12px',
}));

interface ComponentProps {
  active: string;
}

function Navbar({ active }: ComponentProps) {
  const [open, setOpen] = React.useState(false);
  const toggleDrawer = (newOpen: boolean) => () => {
    setOpen(newOpen);
  };

  return (
    <AppBar
      position="static"
      sx={{
        boxShadow: 0,
        bgcolor: 'transparent',
        mt: '28px'
      }}
    >
      <Container maxWidth="xl">
        <StyledToolbar>
          <Box sx={{ display: { xs: 'none', md: 'flex' } }}>
            <Link to="/" style={{ textDecoration: 'none' }}>
              <Button
                variant={active === '1' ? 'contained' : 'text'}
                color="info"
                size="medium"
              >
                Главная
              </Button>
            </Link>
            <Link to="/list" style={{ textDecoration: 'none' }}>
              <Button
                variant={active === '2' ? 'contained' : 'text'}
                color="info"
                size="medium"
              >
                Каталог авто
              </Button>
            </Link>
            <Link to="/chart" style={{ textDecoration: 'none' }}>
              <Button
                variant={active === '3' ? 'contained' : 'text'}
                color="info"
                size="medium"
              >
                Диаграммы
              </Button>
            </Link>
            <Link to="/testing" style={{ textDecoration: 'none' }}>
              <Button
                variant={active === '4' ? 'contained' : 'text'}
                color="info"
                size="medium"
              >
                Проверь себя
              </Button>
            </Link>
            <Link to="/crud" style={{ textDecoration: 'none' }}>
              <Button
                variant={active === '5' ? 'contained' : 'text'}
                color="info"
                size="medium"
              >
                CRUD
              </Button>
            </Link>
          </Box>

          <Box sx={{ display: { xs: 'flex', md: 'none' } }}>
            <IconButton aria-label="Menu button" onClick={toggleDrawer(true)}>
              <MenuIcon />
            </IconButton>
            <Drawer 
              anchor="top" 
              open={open} 
              onClose={toggleDrawer(false)}
              sx={{
                '& .MuiDrawer-paper': {
                  width: '100%',
                  maxWidth: '100vw',
                  height: 'auto',
                  maxHeight: '70vh',
                  borderRadius: '0 0 20px 20px',
                  boxShadow: '0 4px 20px rgba(0,0,0,0.1)',
                }
              }}
            >
              <Box sx={{ px: 2, py: 1 }}>
                <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
                  <IconButton onClick={toggleDrawer(false)} size="small">
                    <CloseRoundedIcon />
                  </IconButton>
                </Box>
                <MenuList sx={{ p: 0 }}>
                  <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
                    <MenuItem
                      onClick={toggleDrawer(false)}
                      sx={{
                        py: 2.5,
                        px: 3,
                        mb: 1,
                        borderRadius: 2,
                        bgcolor: active === '1' ? 'info.main' : 'transparent',
                        color: active === '1' ? 'white' : 'inherit',
                        fontSize: '1.1rem',
                        fontWeight: 500,
                        '&:hover': { 
                          bgcolor: 'info.light', 
                          color: 'white',
                          transform: 'translateX(8px)',
                          transition: 'all 0.2s ease'
                        }
                      }}
                    >
                      Главная
                    </MenuItem>
                  </Link>
                  <Link to="/list" style={{ textDecoration: 'none', color: 'inherit' }}>
                    <MenuItem
                      onClick={toggleDrawer(false)}
                      sx={{
                        py: 2.5,
                        px: 3,
                        mb: 1,
                        borderRadius: 2,
                        bgcolor: active === '2' ? 'info.main' : 'transparent',
                        color: active === '2' ? 'white' : 'inherit',
                        fontSize: '1.1rem',
                        fontWeight: 500,
                        '&:hover': { 
                          bgcolor: 'info.light', 
                          color: 'white',
                          transform: 'translateX(8px)',
                          transition: 'all 0.2s ease'
                        }
                      }}
                    >
                      Каталог авто
                    </MenuItem>
                  </Link>
                  <Link to="/chart" style={{ textDecoration: 'none', color: 'inherit' }}>
                    <MenuItem
                      onClick={toggleDrawer(false)}
                      sx={{
                        py: 2.5,
                        px: 3,
                        mb: 1,
                        borderRadius: 2,
                        bgcolor: active === '3' ? 'info.main' : 'transparent',
                        color: active === '3' ? 'white' : 'inherit',
                        fontSize: '1.1rem',
                        fontWeight: 500,
                        '&:hover': { 
                          bgcolor: 'info.light', 
                          color: 'white',
                          transform: 'translateX(8px)',
                          transition: 'all 0.2s ease'
                        }
                      }}
                    >
                      Диаграммы
                    </MenuItem>
                  </Link>
                  <Link to="/testing" style={{ textDecoration: 'none', color: 'inherit' }}>
                    <MenuItem
                      onClick={toggleDrawer(false)}
                      sx={{
                        py: 2.5,
                        px: 3,
                        mb: 1,
                        borderRadius: 2,
                        bgcolor: active === '4' ? 'info.main' : 'transparent',
                        color: active === '4' ? 'white' : 'inherit',
                        fontSize: '1.1rem',
                        fontWeight: 500,
                        '&:hover': { 
                          bgcolor: 'info.light', 
                          color: 'white',
                          transform: 'translateX(8px)',
                          transition: 'all 0.2s ease'
                        }
                      }}
                    >
                      Проверь себя
                    </MenuItem>
                  </Link>
                  <Link to="/crud" style={{ textDecoration: 'none', color: 'inherit' }}>
                    <MenuItem
                      onClick={toggleDrawer(false)}
                      sx={{
                        py: 2.5,
                        px: 3,
                        mb: 1,
                        borderRadius: 2,
                        bgcolor: active === '5' ? 'info.main' : 'transparent',
                        color: active === '5' ? 'white' : 'inherit',
                        fontSize: '1.1rem',
                        fontWeight: 500,
                        '&:hover': { 
                          bgcolor: 'info.light', 
                          color: 'white',
                          transform: 'translateX(8px)',
                          transition: 'all 0.2s ease'
                        }
                      }}
                    >
                      CRUD
                    </MenuItem>
                  </Link>
                </MenuList>
              </Box>
            </Drawer>
          </Box>
        </StyledToolbar>
      </Container>
    </AppBar>
  );
}

export default Navbar;