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
        bgcolor: 'grey.100',
        borderTop: '1px solid',
        borderColor: 'divider',
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
            gap: 2,
          }}
        >
          <Box>
            <Typography variant="h6" sx={{ color: '#5d8aa8', mb: 1 }}>
              ТИТЛЕ
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Бла-бла-бла
            </Typography>
          </Box>

        </Box>

        <Divider sx={{ mt: 3, mb: 2 }} />

        <Typography variant="body2" color="text.secondary" align="center">
          {'© '}
          {new Date().getFullYear()}
          {' Самые высокие здания и сооружения. Ваши права не защищены.'}
        </Typography>
      </Container>
    </Box>
  );
}

export default Footer;
