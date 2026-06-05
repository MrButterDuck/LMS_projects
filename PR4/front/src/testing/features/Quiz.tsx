import * as React from 'react';
import { Box, Button, Container, Typography, CircularProgress } from '@mui/material';
import Matching from "./Matching";
import { useSelector, useDispatch } from 'react-redux';
import { RootState } from '../../store';
import { resetLists } from './quizSlice';
import { getQuizData } from '../../services/api';

type tTasks = { question: string; answer: string; order: number }[];
type tQuizzes = { id: number; type: "M" | "S"; title: string; tasks: tTasks }[];

function Quiz() {
  const [quizzes, setQuizzes] = React.useState<tQuizzes>([]);
  const [results, setResults] = React.useState<string[] | null>(null);
  const [resetKey, setResetKey] = React.useState(0);
  const [loading, setLoading] = React.useState(true);
  const lists = useSelector((state: RootState) => state.lists.lists);
  const dispatch = useDispatch();

  React.useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await getQuizData();
        if (response.success) {
          const formattedQuizzes = response.quizzes.map((q: any) => ({
            ...q,
            tasks: q.tasks.sort((a: any, b: any) => a.order - b.order)
          }));
          setQuizzes(formattedQuizzes);
        }
      } catch (error) {
        console.error("Failed to fetch quiz data", error);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const handleCheck = () => {
    const res = quizzes.map((item, index) => {
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

  if (loading) {
    return (
      <Container maxWidth="md" sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Container>
    );
  }

  return (
    <Container maxWidth="md">
      {quizzes.map((item, index) => (
        <Box
          key={`${item.id}-${resetKey}`}
          component="section"
          sx={{
            m: 3,
            p: 3,
            bgcolor: 'background.paper',
            borderRadius: '12px',
            border: '2px solid',
            borderColor: 'primary.main',
            boxShadow: `0 4px 8px rgba(0,0,0,0.1)`,
          }}
        >
          <Typography
            variant="h5"
            gutterBottom
            sx={{
              fontWeight: 'bold',
              color: 'info.main',
              borderBottom: '2px solid',
              borderColor: 'primary.main',
              pb: 1,
              mb: 2,
            }}
          >
            {index + 1}. {item.title}
          </Typography>
          <Matching index={index} tasks={item.tasks} type={item.type} />
        </Box>
      ))}
      <Box sx={{ display: 'flex', justifyContent: 'space-around', mt: 2 }}>
        <Button
          variant="contained"
          onClick={handleCheck}
          sx={{ px: 4, py: 1.5, fontWeight: 'bold', fontSize: '1.1rem' }}
        >
          Проверить
        </Button>
        <Button
          variant="outlined"
          onClick={handleReset}
          sx={{ px: 4, py: 1.5, fontWeight: 'bold', fontSize: '1.1rem' }}
        >
          Начать снова
        </Button>
      </Box>
      {results && (
        <Box
          sx={{
            mt: 4,
            p: 3,
            textAlign: 'center',
            bgcolor: 'background.paper',
            borderRadius: '12px',
            border: '2px solid',
            borderColor: 'primary.main',
            boxShadow: `0 4px 8px rgba(0,0,0,0.1)`,
          }}
        >
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