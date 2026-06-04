import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import { Link } from 'react-router-dom';
import structures from '../../data';

const gallery = structures.slice(0, 4);

const heights = {
  mobile: 200,
  top: 245,
  bottom: 147,
  full: 400,
};

type ImageCardProps = {
  to: string;
  img: string;
  title: string;
  height: any;
  flex?: any;
};

function ImageCard({
  to,
  img,
  title,
  height,
  flex,
}: ImageCardProps) {
  return (
    <Box
      component={Link}
      to={to}
      sx={{
        display: 'block',
        overflow: 'hidden',
        borderRadius: 1,
        transition: 'transform 0.2s',
        '&:hover': {
          transform: 'scale(1.01)',
        },
        height,
        flex,
      }}
    >
      <Box
        component="img"
        src={img}
        alt={title}
        sx={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          display: 'block',
        }}
      />
    </Box>
  );
}

function Gallery() {
  return (
    <Container maxWidth="xl" sx={{ mt: 2, px: { xs: 2, md: 4 } }}>
      <Box
        sx={{
          display: 'flex',
          gap: 1,
          flexDirection: { xs: 'column', md: 'row' },
        }}
      >
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 1,
            flex: {
              xs: '1 1 auto',
              md: '0 0 calc(50% - 4px)',
            }
          }}
        >
          <ImageCard
            to="/building/0"
            img={gallery[0].img}
            title={gallery[0].title}
            height={{ xs: heights.mobile, md: heights.top }}
          />

          <Box
            sx={{
              display: 'flex',
              gap: 1,
              flexDirection: { xs: 'column', md: 'row' },
              height: { md: heights.bottom },
            }}
          >
            {[gallery[1], gallery[2]].map((item, index) => (
              <ImageCard
                key={index}
                to={`/building/${index + 1}`}
                img={item.img}
                title={item.title}
                flex={{ md: 1 }}
                height={{ xs: heights.mobile, md: '100%' }}
              />
            ))}
          </Box>
        </Box>

        <ImageCard
          to="/building/3"
          img={gallery[3].img}
          title={gallery[3].title}
          flex={{
            xs: '1 1 auto',
            md: '0 0 calc(50% - 4px)',
          }}
          height={{ xs: heights.mobile, md: heights.full }}
        />
      </Box>
    </Container>
  );
}

export default Gallery;