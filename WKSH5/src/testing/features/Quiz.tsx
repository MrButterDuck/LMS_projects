import * as React from 'react';
import { Box, Button, Container, Typography } from '@mui/material';
import { quiz } from "../quizData";
import Matching from "./Matching";
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '../../store';
import { resetLists } from './quizSlice';

function Quiz() {
  const [results, setResults] = React.useState<string[] | null>(null);
  const [resetKey, setResetKey] = React.useState(0);
  const lists = useSelector((state: RootState) => state.lists.lists);
  const dispatch = useDispatch();

  const handleCheck = () => {
    const res = quiz.map((item, index) => {
      const userAnswers = lists[index] || [];
      let correct = 0;
      if (item.type === "S") {
        const correctOrder = [...item.tasks]
          .sort((a, b) => Number(a.answer) - Number(b.answer))
          .map(t => t.question);
        correct = userAnswers.filter((q, i) => q === correctOrder[i]).length;
      } else {
        const correctAnswers = item.tasks.map(t => t.answer);
        correct = correctAnswers.filter((ans, i) => ans === userAnswers[i]).length;
      }
      if (correct === item.tasks.length) {
        return `Задание ${index + 1}. Все ответы верные.`;
      }
      return `Задание ${index + 1}. Верных ответов: ${correct}.`;
    });
    setResults(res);
  };

  const handleReset = () => {
    setResults(null);
    dispatch(resetLists());
    setResetKey(prev => prev + 1);
  };

  return (
    <Container maxWidth="md">
      {quiz.map((item, index) => (
        <Box key={`${item.id}-${resetKey}`} component="section" sx={{ m: 2, p: 2 }}>
          <Typography variant="h5" gutterBottom>
            {index + 1}. {item.title}
          </Typography>
          <Matching index={index} tasks={item.tasks} type={item.type} />
        </Box>
      ))}
      <Box sx={{ display: 'flex', justifyContent: 'space-around', mt: 2 }}>
        <Button variant="contained" onClick={handleCheck}>Проверить</Button>
        <Button variant="contained" onClick={handleReset}>Начать снова</Button>
      </Box>
      {results && (
        <Box sx={{ mt: 4, textAlign: 'center' }}>
          <Typography variant="h5" gutterBottom>Результаты теста</Typography>
          {results.map((r, i) => (
            <Typography key={i}>{r}</Typography>
          ))}
        </Box>
      )}
    </Container>
  );
}

export default Quiz;