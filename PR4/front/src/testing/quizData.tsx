export type tTasks = {
  question: string;
  answer: string;
  order?: number;
}[];

export type tQuizzes = {
  id: number;
  type: "M" | "S" | "C";
  title: string;
  tasks: tTasks;
}[];