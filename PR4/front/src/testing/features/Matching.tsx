import { useEffect, useState } from 'react';
import { Grid, List, ListItem, ListItemButton, ListItemText, Checkbox, FormControlLabel } from '@mui/material';
import { tTasks } from "../quizData";
import { useDispatch } from 'react-redux';
import { addList, setDraggedItems } from './quizSlice';
import SortableList from './SrtableList';

interface ComponentProps {
  index: number;
  tasks: tTasks;
  type: "M" | "S" | "C";
}

function shuffle<T>(arr: T[]): T[] {
  return [...arr].sort(() => Math.random() - 0.5);
}

function Matching({ index, tasks, type }: ComponentProps) {
  const answers = shuffle(tasks.map(t => type === "S" ? t.question : t.answer));
  const dispatch = useDispatch();
  const [selected, setSelected] = useState<string[]>([]);
  const [shuffledTasks, setShuffledTasks] = useState<tTasks>([]);

  useEffect(() => {
    if (type === "C") {
      dispatch(addList({ index, items: [] }));
      setShuffledTasks(shuffle(tasks));
    } else {
      dispatch(addList({ index, items: answers }));
    }
  }, []);

  if (type === "S") {
    return <SortableList index={index} answers={answers} />;
  }

  if (type === "C") {
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>, question: string) => {
      let newSelected = [...selected];
      if (event.target.checked) {
        newSelected.push(question);
      } else {
        newSelected = newSelected.filter(q => q !== question);
      }
      setSelected(newSelected);
      dispatch(setDraggedItems({ index, items: newSelected }));
    };

    return (
      <List>
        {shuffledTasks.map((item) => (
          <ListItem key={item.question} disablePadding>
            <FormControlLabel
              control={
                <Checkbox
                  checked={selected.includes(item.question)}
                  onChange={(e) => handleChange(e, item.question)}
                  color="primary"
                  sx={{ ml: 1 }}
                />
              }
              label={
                <ListItemText 
                  primary={item.question} 
                  sx={{ 
                    '& .MuiTypography-root': { 
                      fontWeight: 600, 
                      color: 'info.main' 
                    } 
                  }} 
                />
              }
            />
          </ListItem>
        ))}
      </List>
    );
  }

  return (
    <Grid container spacing={2}>
      <Grid size={6}>
        <List>
          {tasks.map((item) => (
            <ListItem key={item.question}>
              <ListItemButton sx={{
                border: '2px solid',
                borderColor: 'info.main',
                borderRadius: '8px',
                bgcolor: 'background.paper',
                textAlign: 'right',
                boxShadow: `0 2px 4px ${'info.main'}`,
                '&:hover': {
                  bgcolor: 'secondary.light',
                },
              }}>
                <ListItemText primary={item.question} sx={{
                  '& .MuiTypography-root': {
                    fontWeight: 600,
                    color: 'info.main',
                  },
                }}/>
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      </Grid>
      <Grid size={6}>
        <SortableList index={index} answers={answers} />
      </Grid>
    </Grid>
  );
}
export default Matching;