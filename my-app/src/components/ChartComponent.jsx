// import React from 'react';
// import { PieChart } from '@mui/x-charts/PieChart';

// // Sample chart data for demo
// const chartData = [
//   { id: 0, value: 40, label: 'JavaScript' },
//   { id: 1, value: 30, label: 'Python' },
//   { id: 2, value: 20, label: 'Java' },
//   { id: 3, value: 10, label: 'C++' },
// ];

// const ChartComponent = () => {
//   return (
//     <PieChart
//       height={200}
//       width={200}
//       series={[
//         {
//           data: chartData,
//           innerRadius: 30,
//           outerRadius: 80,
//           arcLabel: (params) => `${params.label}`,
//           arcLabelMinAngle: 15,
//         },
//       ]}
//       slotProps={{
//         legend: { hidden: true },
//       }}
//     />
//   );
// };

// export default ChartComponent;


import React from 'react';
import { PieChart } from '@mui/x-charts/PieChart';

const ChartComponent = ({ matchPercentage }) => {
  const match = matchPercentage || 0; // fallback to 0 if undefined
  const remaining = 100 - match;

  const chartData = [
    { id: 0, value: match, label: 'Match' },
    { id: 1, value: remaining, label: 'Remaining' },
  ];

  return (
    <PieChart
      height={200}
      width={200}
      series={[
        {
          data: chartData,
          innerRadius: 30,
          outerRadius: 80,
          arcLabel: (params) => `${params.label} (${params.value}%)`,
          arcLabelMinAngle: 10,
        },
      ]}
      slotProps={{
        legend: { hidden: true },
      }}
    />
  );
};

export default ChartComponent;
