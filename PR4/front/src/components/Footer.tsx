import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';

function Footer() {
  return (
    <Box
      component="footer"
      sx={{
        mt: 6,
        py: 4,
        bgcolor: 'background.paper',
        borderTop: '2px solid',
        borderColor: 'primary.main',
      }}
    >
      <Container maxWidth="xl">
        <Divider sx={{ mb: 3 }} />
        <Box
          sx={{
            display: 'flex',
            flexDirection: { xs: 'column', md: 'row' },
            justifyContent: 'space-between',
            alignItems: { xs: 'center', md: 'flex-start' },
            gap: 2
          }}
        >
          <Box>
            <Typography variant="h6" sx={{ color: '#5d8aa8', mb: 1 }}>
              Car Features & MSRP
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Каталог автомобилей с характеристиками и ценами
            </Typography>
          </Box>
        </Box>
        <Divider sx={{ mt: 3, mb: 2 }} />
        <Typography variant="body2" color="text.secondary" align="center">
          {'© '}{new Date().getFullYear()}{' Автомобили и их характеристики. Все права защищены.'}
        </Typography>
      </Container>
    </Box>
  );
}

export default Footer;