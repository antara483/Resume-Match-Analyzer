// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route,  } from 'react-router-dom';
import Signup from './components/Signup';
import Login from './components/Login';
import Parsing from './components/Parsing';

// function AnalyzeButton() {
//   const navigate = useNavigate();

//   return (
//     <div style={{ textAlign: 'center', marginTop: '20px' }}>
//       <button
//         onClick={() => navigate('/parsing-analysis')}
//         style={{
//           padding: '10px 20px',
//           fontSize: '16px',
//           backgroundColor: '#4CAF50',
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
// }
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
         <Route path="/parsing-analysis" element={<Parsing />} />
      </Routes>
    </Router>
  );
}

export default App;
