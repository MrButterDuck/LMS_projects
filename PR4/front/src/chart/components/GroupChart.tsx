import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';
import { LineChart } from '@mui/x-charts/LineChart';
import Container from '@mui/material/Container';
import SettingChart from './SettingChart';

type tGroup = {
  id: number | string;
  Группа: string;
  'Минимальная мощность': number;
  'Максимальная мощность': number;
  'Средняя мощность': number;
};

type GroupChartProps = {
  data: tGroup[];
};

type tSeries = {
  'Максимальная мощность': boolean;
  'Средняя мощность': boolean;
  'Минимальная мощность': boolean;
};

function GroupChart({ data }: GroupChartProps) {
  const [series, setSeries] = React.useState<tSeries>({
    'Максимальная мощность': true,
    'Средняя мощность': false,
    'Минимальная мощность': false
  });
  const [isBar, setIsBar] = React.useState(true);
  const activeCount = Object.values(series).filter(Boolean).length;
  const seriesY = Object.entries(series)
    .filter(item => item[1] === true)
    .map(item => ({ dataKey: item[0], label: item[0] }));
  const chartSetting = {
    yAxis: [{ label: 'Мощность (л.с.)' }],
    height: 400
  };
  return (
    <Container maxWidth="lg">
      {isBar ? (
        <BarChart
          dataset={data}
          xAxis={[{ scaleType: 'band', dataKey: 'Группа' }]}
          series={seriesY}
          {...(activeCount === 1 ? { barLabel: "value" } as any : {})}
          slotProps={{
            legend: {
              position: { vertical: 'bottom', horizontal: 'center' }
            }
          }}
          {...chartSetting}
        />
      ) : (
        <LineChart
          dataset={data}
          xAxis={[{ scaleType: 'band', dataKey: 'Группа' }]}
          series={seriesY}
          slotProps={{
            legend: {
              position: { vertical: 'bottom', horizontal: 'center' }
            }
          }}
          {...chartSetting}
        />
      )}
      <SettingChart series={series} setSeries={setSeries} isBar={isBar} setIsBar={setIsBar} />
    </Container>
  );
}
export default GroupChart;