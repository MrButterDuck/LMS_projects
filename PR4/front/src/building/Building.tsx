import { useParams, Link } from 'react-router-dom';
import Navbar from "../components/Navbar";
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Footer from '../components/Footer';
import cars from "../data";

function Building() {
  const { id } = useParams();
  const item = cars[Number(id)];

  if (!item) {
    return (
      <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
        <Navbar active="1" />
        <div style={{ flex: 1 }}>
          <Container maxWidth="lg" sx={{ mt: '20px' }}>
            <Typography>Страница не найдена</Typography>
          </Container>
        </div>
        <Footer />
      </div>
    );
  }

  return (
    <div style={{ minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Navbar active="1" />
      <div style={{ flex: 1 }}>
        <Container maxWidth="lg" sx={{ mt: '20px' }}>
          <Breadcrumbs sx={{ mb: '16px' }}>
            <Link to="/" style={{ color: 'inherit' }}>Главная</Link>
            <Typography color="text.primary">{item.title}</Typography>
          </Breadcrumbs>
          <Typography variant="h4" align="center" sx={{ mb: '20px' }}>
            {item.title}
          </Typography>
          <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2 }}>
            <Box
              component="img"
              src={item.img}
              alt={item.title}
              sx={{ width: { xs: '100%', md: '50%' }, height: 'auto', display: 'block' }}
            />
          </Box>
          <Box sx={{ columns: { xs: 1, md: 2 }, gap: 4 }}>
            {item.description.map((text, index) => (
              <Typography
                key={index}
                variant="body1"
                align="justify"
                sx={{ mb: 2, breakInside: 'avoid' }}
              >
                {text}
              </Typography>
            ))}
          </Box>
        </Container>
      </div>
      <Footer />
    </div>
  );
}

export default Building;