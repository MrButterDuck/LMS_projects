import { useSortable } from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import { ListItem, ListItemText, ListItemButton, ListItemIcon } from '@mui/material';
import DragIndicatorIcon from '@mui/icons-material/DragIndicator';

interface SortableItemProps {
  id: string;
}

export function SortableItem({ id }: SortableItemProps) {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition
  } = useSortable({ id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition
  };

  return (
    <ListItem ref={setNodeRef} style={style} {...attributes} {...listeners}>
      <ListItemButton sx={{ 
        border: '2px solid',
          borderColor: 'secondary.main',
          borderRadius: '8px',
          bgcolor: 'background.paper',
          boxShadow: `0 2px 4px ${'secondary.main'}`,
          '&:hover': {
            bgcolor: 'background.default',
            borderColor: 'primary.main',
          },
      }}>
        <ListItemIcon sx={{ color: 'secondary.main' }}>
          <DragIndicatorIcon />
        </ListItemIcon>
        <ListItemText primary={id} sx={{
          '& .MuiTypography-root': {
              fontWeight: 500,
              color: 'text.primary',
            },
        }}/>
      </ListItemButton>
    </ListItem>
  );
}