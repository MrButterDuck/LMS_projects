export type tTasks = {
  question: string;
  answer: string;
}[];

export type tQuizzes = {
  id: number;
  type: "M" | "S";
  title: string;
  tasks: tTasks;
}[];

export const quiz: tQuizzes = [
  {
    id: 1,
    type: "M",
    title: "Сопоставьте марку автомобиля и страну производства.",
    tasks: [
      { question: "BMW", answer: "Германия" },
      { question: "Toyota", answer: "Япония" },
      { question: "Ford", answer: "США" },
      { question: "Ferrari", answer: "Италия" }
    ]
  },
  {
    id: 2,
    type: "M",
    title: "Сопоставьте модель автомобиля и тип кузова.",
    tasks: [
      { question: "Mustang", answer: "Coupe" },
      { question: "Camry", answer: "Sedan" },
      { question: "Golf", answer: "Hatchback" },
      { question: "F-150", answer: "Pickup" },
      { question: "CR-V", answer: "SUV" }
    ]
  },
  {
    id: 3,
    type: "M",
    title: "Сопоставьте марку и тип двигателя.",
    tasks: [
      { question: "Tesla", answer: "electric" },
      { question: "Porsche 911", answer: "premium unleaded" },
      { question: "Toyota Prius", answer: "regular unleaded" }
    ]
  },
  {
    id: 4,
    type: "S",
    title: "Отсортируйте автомобили по возрастанию мощности двигателя (л.с.).",
    tasks: [
      { question: "Toyota Prius (121 л.с.)", answer: "1" },
      { question: "Honda Civic (158 л.с.)", answer: "2" },
      { question: "BMW 1 Series M (335 л.с.)", answer: "3" },
      { question: "Porsche 911 (400 л.с.)", answer: "4" },
      { question: "Tesla Model S (518 л.с.)", answer: "5" },
      { question: "Ferrari 488 GTB (661 л.с.)", answer: "6" }
    ]
  },
  {
    id: 5,
    type: "S",
    title: "Отсортируйте марки по возрастанию года появления модели в датасете.",
    tasks: [
      { question: "BMW 1 Series M (2011)", answer: "1" },
      { question: "Audi A4 (2012)", answer: "2" },
      { question: "Mercedes-Benz C-Class (2013)", answer: "3" },
      { question: "Porsche 911 (2014)", answer: "4" },
      { question: "Tesla Model S (2017)", answer: "5" },
      { question: "Tesla Model 3 (2018)", answer: "6" }
    ]
  },
  {
    id: 6,
    type: "M",
    title: "Сопоставьте автомобиль и его цену MSRP (долл.).",
    tasks: [
      { question: "Honda Civic", answer: "19500" },
      { question: "Tesla Model S", answer: "75000" },
      { question: "Porsche 911", answer: "95000" },
      { question: "Ferrari 488 GTB", answer: "245000" }
    ]
  }
];