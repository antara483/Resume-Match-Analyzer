// import React from 'react'
// import DropBox from './DropBox'
// import { useNavigate } from 'react-router-dom';

// const Parsing = () => {
//     const navigate = useNavigate();

//     const handleAnalyze = () => {
//     // Example: Navigate to a results page or show an alert
//     navigate('/results'); // Change to your actual path if needed
//     // OR perform some logic here
//   };

// //   return (
// //     <div>Parsing
// //     <DropBox/>
// //     </div>
// //   )
// // }
//     return (
//     <div style={{ textAlign: 'center', padding: '20px' }}>
//       <h2>Resume Match Analyzer</h2>
//       <DropBox />
      
//       <button
//         onClick={handleAnalyze}
//         style={{
//           marginTop: '20px',
//           padding: '10px 20px',
//           fontSize: '16px',
//           backgroundColor: '#2196F3',
//           color: 'white',
//           border: 'none',
//           borderRadius: '5px',
//           cursor: 'pointer'
//         }}
//       >
//         Analyze Results
//       </button>
//     </div>
//   );
// };

// export default Parsing;


// import React, { useState } from 'react';
// import DropBox from './DropBox';
// import ChartComponent from './ChartComponent'; // Adjust path as needed
// import { useNavigate } from 'react-router-dom';
// import { Space, Table, Tag } from 'antd';
// import './Parsing.css';

// const Parsing = () => {
//   const [showTable, setShowTable] = useState(false);
//   const navigate = useNavigate();

//   const handleAnalyze = () => {
//     // Show table on Analyze button click
//     setShowTable(true);

//     // Optional: Navigate if needed
//     // navigate('/results');
//   };

//   const columns = [
//     {
//       title: 'Resume',
//       dataIndex: 'name',
//       key: 'name',
//       render: text => <a>{text}</a>,
//     },
//     {
//       title: 'Best Job Match',
//       dataIndex: 'age',
//       key: 'age',
//     },
//     {
//       title: 'Match %',
//       dataIndex: 'address',
//       key: 'address',
//     },
//     {
//     title: 'Chart',
//       key: 'chart',
//       render: () => <ChartComponent />,
      

//     },
//     {
//       title: 'Status',
//       key: 'tags',
//       dataIndex: 'tags',
//       render: (_, { tags }) => (
//         <>
//           {tags.map(tag => {
//             let color = tag.length > 5 ? 'geekblue' : 'green';
//             if (tag === 'loser') {
//               color = 'volcano';
//             }
//             return (
//               <Tag color={color} key={tag}>
//                 {tag.toUpperCase()}
//               </Tag>
//             );
//           })}
//         </>
//       ),
//     },
//     // {
//       // title: 'Chart',
//       // key: 'action',
//       // render: (_, record) => (
//       //   <Space size="middle">
//       //     <a>Invite {record.name}</a>
//       //     <a>Delete</a>
//       //   </Space>
//       // ),
      
//     //   title: 'Chart',
//     //   key: 'chart',
//     //   render: () => <ChartComponent />,
      

//     // },
//   ];

//   const data = [
//     {
//       key: '1',
//       name: 'John Brown',
//       age: 32,
//       address: 'New York No. 1 Lake Park',
//       tags: ['nice', 'developer'],
//     },
//     {
//       key: '2',
//       name: 'Jim Green',
//       age: 42,
//       address: 'London No. 1 Lake Park',
//       tags: ['loser'],
//     },
//     {
//       key: '3',
//       name: 'Joe Black',
//       age: 32,
//       address: 'Sydney No. 1 Lake Park',
//       tags: ['cool', 'teacher'],
//     },
//   ];

//   return (
//     <div style={{ textAlign: 'center', padding: '20px',marginLeft: '55px',
//       marginRight: '55px',
//       marginBottom: '40px',backgroundColor: '#ecece2', }}>
//       <h2>Resume Match Analyzer</h2>
//       <DropBox />

//       <button
//         onClick={handleAnalyze}
//         style={{
//           marginTop: '20px',
//           padding: '10px 20px',
//           fontSize: '16px',
//           backgroundColor: '#2196F3',
//           color: 'white',
//           border: 'none',
//           borderRadius: '5px',
//           cursor: 'pointer'
//         }}
//       >
//         Analyze Results
//       </button>

//       {showTable && (
//         <div style={{ marginTop: '40px',backgroundColor: '#FFF9DB', }}>
//           <Table columns={columns} dataSource={data} bordered
//     style={{ backgroundColor: '#FFF9DB', color: '#FFF9DB' }} />
//         </div>
//       )}
//     </div>
//   );
// };

// export default Parsing;

// 1 try
// import React, { useEffect, useState } from 'react';
// import DropBox from './DropBox';
// import ChartComponent from './ChartComponent'; // Adjust path as needed
// import { Table, Tag, Button } from 'antd';
// import { useNavigate } from 'react-router-dom';

// const Parsing = () => {
//   const [results, setResults] = useState([]);
//   const [showTable, setShowTable] = useState(false);
//   const navigate = useNavigate();

//   useEffect(() => {
//     const token = localStorage.getItem('token');
//     if (!token) {
//       alert('You must log in first!');
//       navigate('/login');
//     }
//   }, [navigate]);

//   const handleResults = (parsedResults) => {
//     setResults(parsedResults);
//     setShowTable(true);
//   };

//   const handleLogout = () => {
//     localStorage.removeItem('token');
//     navigate('/login');
//   };

//   const columns = [
//     {
//       title: 'Resume',
//       dataIndex: 'name',
//       key: 'name',
//     },
//     {
//       title: 'Job Title',
//       dataIndex: 'job_title',
//       key: 'job_title',
//     },
//     {
//       title: 'Match %',
//       dataIndex: 'match',
//       key: 'match',
//       render: (text) => `${text}%`,
//     },
//     {
//       title: 'Status',
//       dataIndex: 'status',
//       key: 'status',
//       render: (status) => (
//         <Tag color={status === 'Selected' ? 'green' : 'red'}>
//           {status}
//         </Tag>
//       ),
//     },
//     {
//       title: 'Match Chart',
//       key: 'chart',
//       render: (_, record) => (
//         <ChartComponent score={record.match} />
//       ),
//     },
//   ];

//   const tableData = results.map((r, index) => ({
//     key: index,
//     name: r.filename || `Resume ${index + 1}`,
//     job_title: r.job_title || 'N/A',
//     match: r.match || 0,
//     status: r.status || 'Rejected',
//   }));

//   return (
//     <div style={{ padding: '20px', backgroundColor: '#FFF9DB', minHeight: '100vh' }}>
//       <h1 style={{ color: '#333' }}>Resume Match Analyzer</h1>

//       <Button type="primary" danger onClick={handleLogout} style={{ float: 'right', marginBottom: 16 }}>
//         Logout
//       </Button>

//       <DropBox onUploadComplete={handleResults} />

//       {showTable && (
//         <div style={{ marginTop: '40px' }}>
//           <Table
//             columns={columns}
//             dataSource={tableData}
//             bordered
//             pagination={{ pageSize: 5 }}
//           />
//         </div>
//       )}
//     </div>
//   );
// };

// export default Parsing;
// 1 try

// 2 try
// import React, { useState } from 'react';
// import DropBox from './DropBox';
// import ChartComponent from './ChartComponent';
// import { Table, Tag, message } from 'antd';
// import { useNavigate } from 'react-router-dom';
// import './Parsing.css';

// const Parsing = () => {
//   const [showTable, setShowTable] = useState(false);
//   const [results, setResults] = useState([]);
//   const navigate = useNavigate();

//   const handleAnalyze = async () => {
//     const token = localStorage.getItem('token');
//     const uploadedFiles = JSON.parse(localStorage.getItem('uploadedFiles') || '[]');

//     if (!token) {
//       message.error("You must be logged in.");
//       navigate("/login");
//       return;
//     }

//     if (!uploadedFiles.length) {
//       message.error("No resumes uploaded.");
//       return;
//     }

//     const formData = new FormData();
//     uploadedFiles.forEach(file => formData.append("resumes", file));

//     try {
//       const response = await fetch("http://localhost:5000/api/parse-resumes", {
//         method: "POST",
//         headers: {
//           Authorization: `Bearer ${token}`
//         },
//         body: formData
//       });

//       const data = await response.json();

//       if (response.ok) {
//         const formatted = data.results.map((item, index) => ({
//           key: index,
//           name: item.filename,
//           age: item.job_title,
//           address: `${item.match}%`,
//           tags: [item.status]
//         }));

//         setResults(formatted);
//         setShowTable(true);
//       } else {
//         message.error(data.error || "Parsing failed.");
//       }

//     } catch (err) {
//       console.error(err);
//       message.error("Server error.");
//     }
//   };

//   const columns = [
//     {
//       title: 'Resume',
//       dataIndex: 'name',
//       key: 'name',
//     },
//     {
//       title: 'Best Job Match',
//       dataIndex: 'age',
//       key: 'age',
//     },
//     {
//       title: 'Match %',
//       dataIndex: 'address',
//       key: 'address',
//     },
//     {
//       title: 'Chart',
//       key: 'chart',
//       render: () => <ChartComponent />,
//     },
//     {
//       title: 'Status',
//       key: 'tags',
//       dataIndex: 'tags',
//       render: (_, { tags }) => (
//         <>
//           {tags.map(tag => {
//             let color = tag === 'Highly Qualified' ? 'green' : tag === 'Qualified' ? 'geekblue' : 'volcano';
//             return <Tag color={color} key={tag}>{tag.toUpperCase()}</Tag>;
//           })}
//         </>
//       ),
//     }
//   ];

//   return (
//     <div style={{ textAlign: 'center', padding: '20px', margin: '0 55px 40px', backgroundColor: '#ecece2' }}>
//       <h2>Resume Match Analyzer</h2>
//       <DropBox />

//       <button
//         onClick={handleAnalyze}
//         style={{
//           marginTop: '20px',
//           padding: '10px 20px',
//           fontSize: '16px',
//           backgroundColor: '#2196F3',
//           color: 'white',
//           border: 'none',
//           borderRadius: '5px',
//           cursor: 'pointer'
//         }}
//       >
//         Analyze Results
//       </button>

//       {showTable && (
//         <div style={{ marginTop: '40px', backgroundColor: '#FFF9DB' }}>
//           <Table
//             columns={columns}
//             dataSource={results}
//             bordered
//             style={{ backgroundColor: '#FFF9DB' }}
//           />
//         </div>
//       )}
//     </div>
//   );
// };

// export default Parsing;
// 2 try

// 3rd
import React, { useState } from 'react';
import DropBox from './DropBox';
import ChartComponent from './ChartComponent';
import { Table, Tag, message } from 'antd';
import { useNavigate } from 'react-router-dom';
import './Parsing.css';

const Parsing = () => {
  const [showTable, setShowTable] = useState(false);
  const [results, setResults] = useState([]);
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const navigate = useNavigate();

  const handleAnalyze = async () => {
    const token = localStorage.getItem('token');

    if (!token) {
      message.error("You must be logged in.");
      navigate("/login");
      return;
    }

    if (!uploadedFiles.length) {
      message.error("No resumes uploaded.");
      return;
    }

    const formData = new FormData();
    uploadedFiles.forEach(file => formData.append("resumes", file));

    try {
      const response = await fetch("http://localhost:5000/api/parse-resumes", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`
        },
        body: formData
      });

      const data = await response.json();

      if (response.ok) {
        const formatted = data.results.map((item, index) => ({
          key: index,
          name: item.filename,
          age: item.job_title,
          address: `${item.match}%`,
          matchPercent: item.match, // for chart
          tags: [item.status]
        }));

        setResults(formatted);
        setShowTable(true);
      } else {
        message.error(data.error || "Parsing failed.");
      }

    } catch (err) {
      console.error(err);
      message.error("Server error.");
    }
  };

  const columns = [
    {
      title: 'Resume',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Best Job Match',
      dataIndex: 'age',
      key: 'age',
    },
    {
      title: 'Match %',
      dataIndex: 'address',
      key: 'address',
    },
    {
      title: 'Chart',
      key: 'chart',
      render: (_, record) => <ChartComponent matchPercentage={record.matchPercent} />,
    },
    {
      title: 'Status',
      key: 'tags',
      dataIndex: 'tags',
      render: (_, { tags }) => (
        <>
          {tags.map(tag => {
            let color = tag === 'Highly Qualified' ? 'green' : tag === 'Qualified' ? 'geekblue' : 'volcano';
            return <Tag color={color} key={tag}>{tag.toUpperCase()}</Tag>;
          })}
        </>
      ),
    }
  ];

  return (
    <div style={{ textAlign: 'center', padding: '20px', margin: '0 55px 40px', backgroundColor: '#ecece2' }}>
      <h2>Resume Match Analyzer</h2>
      <DropBox onFilesSelected={setUploadedFiles} />

      <button
        onClick={handleAnalyze}
        style={{
          marginTop: '20px',
          padding: '10px 20px',
          fontSize: '16px',
          backgroundColor: '#2196F3',
          color: 'white',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer'
        }}
      >
        Analyze Results
      </button>

      {showTable && (
        <div style={{ marginTop: '40px', backgroundColor: '#FFF9DB' }}>
          <Table
            columns={columns}
            dataSource={results}
            bordered
            style={{ backgroundColor: '#FFF9DB' }}
          />
        </div>
      )}
    </div>
  );
};

export default Parsing;

// 3rd