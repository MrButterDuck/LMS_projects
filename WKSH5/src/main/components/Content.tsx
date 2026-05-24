import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import structures from '../../data';
import BuildCard from './BuildCard';

const cardData = [structures[3], structures[6], structures[9], structures[7]];

function Content() {
  return (
    <Container maxWidth="xl" sx={{ mt: 4, mb: 4 }}>
      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: { xs: 3, md: 6 } }}>
        {cardData.map((item, index) => (
          <Box key={index} sx={{ width: { xs: '100%', md: 'calc(50% - 24px)' } }}>
            <BuildCard building={item} index={index} />
          </Box>
        ))}
      </Box>
    </Container>
  );
}

export default Content;
