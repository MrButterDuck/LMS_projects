import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';
import structures from '../../data';
import BuildCard from './BuildCard';
import SideCard from './SideCard';

// 4 карточки для левой колонки
const leftCars = [structures[0], structures[2], structures[4], structures[6]];
// 4 карточки для правой колонки
const rightCars = [structures[1], structures[3], structures[5], structures[7]];
// 2 карточки для центральных больших карточек
const centerCars = [structures[8], structures[9]];
// Карточка для широкой нижней карточки
const bottomCar = structures[0];

function Content() {
  return (
    <Container maxWidth="xl" sx={{ mt: 4, mb: 4 }}>
      <Box
        sx={{
          display: 'grid',
          gridTemplateColumns: { xs: '1fr', md: '13% 1fr 13%' },
          gap: { xs: 2, md: 2 }
        }}
      >

        {/* ЛЕВАЯ КОЛОНКА */}
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 2
          }}
        >
          {leftCars.map((item, index) => (
            <SideCard
              key={index}
              img={item.img}
              title={item.title}
              description="Текст ..."
              index={structures.indexOf(item)}
            />
          ))}
        </Box>

        {/* ЦЕНТРАЛЬНАЯ ЧАСТЬ */}
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 3,
            order: { xs: -1, md: 0 }
          }}
        >
          {/* Ряд из двух больших карточек */}
          <Box
            sx={{
              display: 'grid',
              gridTemplateColumns: { xs: '1fr', md: '1fr 1fr' },
              gap: 2
            }}
          >
            {centerCars.map((item, index) => (
              <BuildCard
                key={index}
                img={item.img}
                title={item.title}
                description={item.description[0].substring(0, 200) + '...'}
                index={structures.indexOf(item)}
                variant={index === 0 ? 'image-top' : 'image-bottom'}
              />
            ))}
          </Box>

          {/* Нижняя широкая карточка: текст слева, изображение справа */}
          <Card
            sx={{
              display: 'flex',
              flexDirection: { xs: 'column', md: 'row' },
              borderRadius: 3,
              overflow: 'hidden'
            }}
          >
            <CardContent
              sx={{
                flexGrow: 1,
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                p: 3
              }}
            >
              <Box>
                <Typography
                  variant="h5"
                  component="h2"
                  gutterBottom
                  sx={{ fontWeight: 'bold' }}
                >
                  {bottomCar.title}
                </Typography>
                <Typography variant="body1" sx={{ mb: 2 }}>
                  {bottomCar.description[0]}
                </Typography>
              </Box>
              <Box sx={{ display: 'flex', justifyContent: 'flex-end' }}>
                <Button
                  component={Link}
                  to={"/building/" + structures.indexOf(bottomCar)}
                  variant="contained"
                >
                  Подробнее
                </Button>
              </Box>
            </CardContent>

            {/* Изображение справа в закруглённом блоке */}
            <Box
              sx={{
                width: { xs: '100%', md: 280 },
                flexShrink: 0,
                m: { xs: 2, md: 2 },
                borderRadius: 4,
                overflow: 'hidden',
                alignSelf: 'center'
              }}
            >
              <CardMedia
                component="img"
                image={bottomCar.img}
                alt={bottomCar.title}
                sx={{
                  width: '100%',
                  height: { xs: 200, md: 180 },
                  objectFit: 'cover',
                  display: 'block'
                }}
              />
            </Box>
          </Card>
        </Box>

        {/* ПРАВАЯ КОЛОНКА */}
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 2
          }}
        >
          {rightCars.map((item, index) => (
            <SideCard
              key={index}
              img={item.img}
              title={item.title}
              description="Текст ..."
              index={structures.indexOf(item)}
            />
          ))}
        </Box>

      </Box>
    </Container>
  );
}

export default Content;