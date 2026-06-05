import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import { Link } from 'react-router-dom';

interface SideCardProps {
  img: string;
  title: string;
  description: string;
  index: number;
}

function SideCard({ img, title, description, index }: SideCardProps) {
  return (
    <Link to={"/building/" + index} style={{ textDecoration: 'none' }}>
      <Card
        sx={{
          transition: 'transform 0.2s',
          '&:hover': { transform: 'scale(1.03)' }
        }}
      >
        <Box sx={{ mx: 1, mt: 1, borderRadius: 1, overflow: 'hidden' }}>
          <CardMedia
            component="img"
            height="100"
            image={img}
            alt={title}
          />
        </Box>
        <CardContent sx={{ py: 1, '&:last-child': { pb: 1 } }}>
          <Typography variant="subtitle2" sx={{ fontWeight: 'bold' }}>
            {title}
          </Typography>
          <Typography variant="caption" color="text.secondary">
            {description}
          </Typography>
        </CardContent>
      </Card>
    </Link>
  );
}

export default SideCard;