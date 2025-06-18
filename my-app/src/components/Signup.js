// import React, { useState } from 'react';
// import axios from 'axios';
// import './auth.css';

// const Signup = () => {
//   const [formData, setFormData] = useState({ name: '', email: '', password: '' });

//   const handleChange = (e) => {
//     setFormData({ ...formData, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       await axios.post('http://localhost:5000/signup', formData);
//       alert('Signup successful!');
//     } catch (err) {
//       alert('Signup failed');
//     }
//   };

//   return (
//     <div className="auth-container">
//       <h2>Signup</h2>
//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           name="name"
//           placeholder="Name"
//           onChange={handleChange}
//           required
//         />
//         <input
//           type="email"
//           name="email"
//           placeholder="Email"
//           onChange={handleChange}
//           required
//         />
//         <input
//           type="password"
//           name="password"
//           placeholder="Password"
//           onChange={handleChange}
//           required
//         />
//         <button type="submit">Signup</button>
//       </form>
//     </div>
//   );
// };

// export default Signup;
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './auth.css';

const Signup = () => {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const navigate = useNavigate();
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/api/auth/signup', formData);
      alert('Signup successful!');
      navigate('/login'); 
    } catch (err)
    //  {
    //   alert('Signup failed');
    // }
  //   {
  //   if (err.response) {
  //     if (err.response.status === 409) {
  //       alert('User already exists');
  //     } else if (err.response.data?.message) {
  //       alert(err.response.data.message);
  //     } else {
  //       alert('Signup failed');
  //     }
  //   } else {
  //     alert('Signup failed. Server not reachable.');
  //   }
  // }
     {
    console.error('Signup error:', err); // 🔍 debug
    if (err.response) {
      if (err.response.status === 409) {
        alert('User already exists');
      } else if (err.response.data?.message) {
        alert(err.response.data.message);
      } else {
        alert('Signup failed');
      }
    } else {
      alert('Signup failed. Server not reachable.');
    }
  }
  };

  return (
    <div className="page-container">
      <div
        className="image-side"
        style={{
          backgroundImage: "url('/resume.jpg')",
          backgroundSize: 'cover',
          backgroundPosition: 'center',
        }}
      ></div>
      <div className="form-side">
        <form className="auth-form" onSubmit={handleSubmit}>
          <h2>SignUp</h2>
          <input type="text" name="username" placeholder="Username" onChange={handleChange} required />
          <input type="email" name="email" placeholder="Email" onChange={handleChange} required />
          <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
          <button type="submit">Signup</button>
        </form>
      </div>
    </div>
  );
};

export default Signup;
