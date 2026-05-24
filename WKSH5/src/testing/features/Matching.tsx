import { useEffect } from 'react';
import { Grid, List, ListItem, ListItemButton, ListItemText } from '@mui/material';
import { tTasks } from "../quizData";
import { useDispatch } from 'react-redux';
import { addList } from './quizSlice';
import SortableList from './SrtableList';

interface ComponentProps {
  index: number;
  tasks: tTasks;
  type: "M" | "S";
}

function shuffle(arr: string[]): string[] {
  return [...arr].sort(() => Math.random() - 0.5);
}

function Matching({ index, tasks, type }: ComponentProps) {
  const answers = shuffle(tasks.map(t => type === "S" ? t.question : t.answer));
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(addList({ index, items: answers }));
  }, []);

  if (type === "S") {
    return (
      <SortableList index={index} answers={answers} />
    );
  }

  return (
    <Grid container spacing={2}>
      <Grid {...{ size: 6 } as any}>
        <List>
          {tasks.map((item, i) => (
            <ListItem key={i}>
              <ListItemButton sx={{ border: '1px solid gray', borderRadius: '5px', textAlign: 'right' }}>
                <ListItemText primary={item.question} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
      </Grid>
      <Grid {...{ size: 6 } as any}>
        <SortableList index={index} answers={answers} />
      </Grid>
    </Grid>
  );
}

export default Matching;