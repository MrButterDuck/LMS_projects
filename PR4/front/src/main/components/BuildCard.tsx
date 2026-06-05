import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Link } from 'react-router-dom';

interface BuildCardProps {
  img: string;
  title: string;
  description: string;
  index: number;
  variant?: 'image-top' | 'image-bottom';
}

function BuildCard({ img, title, description, index, variant = 'image-top' }: BuildCardProps) {
  return (
    <Card
      sx={{
        height: '100%',
        display: 'flex',
        flexDirection: 'column',
        borderRadius: 3,
        overflow: 'hidden'
      }}
    >
      {variant === 'image-top' && (
        <Link to={"/building/" + index} style={{ textDecoration: 'none' }}>
          <Box
            sx={{
              mx: 3,
              mt: 3,
              borderRadius: 4,
              overflow: 'hidden',
              height: 160
            }}
          >
            <CardMedia
              component="img"
              height="160"
              image={img}
              alt={title}
              sx={{ width: '100%', height: '100%', objectFit: 'cover' }}
            />
          </Box>
        </Link>
      )}

      <CardContent
        sx={{
          flexGrow: 1,
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between'
        }}
      >
        <Box>
          <Typography
            gutterBottom
            variant="h5"
            component="h2"
            align="center"
            sx={{ minHeight: '40px', fontWeight: 'bold' }}
          >
            {title}
          </Typography>
          <Typography
            variant="body2"
            color="text.secondary"
            sx={{ mb: 2 }}
          >
            {description}
          </Typography>
        </Box>
        {variant === 'image-bottom' && (
          <Link to={"/building/" + index} style={{ textDecoration: 'none', marginBottom: 16 }}>
            <Box
              sx={{
                mx: 1,
                borderRadius: 4,
                overflow: 'hidden',
                height: 140
              }}
            >
              <CardMedia
                component="img"
                height="140"
                image={img}
                alt={title}
                sx={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
            </Box>
          </Link>
        )}

        <Box
          sx={{
            display: 'flex',
            justifyContent: variant === 'image-top' ? 'flex-start' : 'flex-end',
            mt: 2
          }}
        >
          <Button component={Link} to={"/building/" + index} variant="contained" size="small">
            Подробнее
          </Button>
        </Box>
      </CardContent>
    </Card>
  );
}

export default BuildCard;