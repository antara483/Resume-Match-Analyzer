// import React from 'react';
// import { InboxOutlined } from '@ant-design/icons';
// import { message, Upload } from 'antd';
// const { Dragger } = Upload;
// const props = {
//   name: 'file',
//   multiple: true,
//   action: 'https://660d2bd96ddfa2943b33731c.mockapi.io/api/upload',
//   onChange(info) {
//     const { status } = info.file;
//     if (status !== 'uploading') {
//       console.log(info.file, info.fileList);
//     }
//     if (status === 'done') {
//       message.success(`${info.file.name} file uploaded successfully.`);
//     } else if (status === 'error') {
//       message.error(`${info.file.name} file upload failed.`);
//     }
//   },
//   onDrop(e) {
//     console.log('Dropped files', e.dataTransfer.files);
//   },
// };
// const DropBox = () => (
//   <Dragger {...props}>
//     <p className="ant-upload-drag-icon">
//       <InboxOutlined />
//     </p>
//     <p className="ant-upload-text">Click or drag file to this area to upload</p>
//     <p className="ant-upload-hint">
//       Support for a single or bulk upload. Strictly prohibited from uploading company data or other
//       banned files.
//     </p>
//   </Dragger>
// );
// export default DropBox;
// 1 st try
// import React from 'react';
// import { InboxOutlined } from '@ant-design/icons';
// import { message, Upload } from 'antd';
// const { Dragger } = Upload;

// const DropBox = ({ onUploadComplete }) => {
//   const token = localStorage.getItem('token');

//   const props = {
//     name: 'resumes',
//     multiple: true,
//     customRequest: async ({ file, onSuccess, onError }) => {
//       try {
//         const formData = new FormData();
//         formData.append('resumes', file);

//         const res = await fetch('http://localhost:5000/api/parse-resumes', {
//           method: 'POST',
//           headers: {
//             Authorization: `Bearer ${token}`,
//           },
//           body: formData,
//         });

//         const data = await res.json();
//         if (res.ok) {
//           message.success(`${file.name} uploaded & analyzed successfully`);
//           onUploadComplete(data.results);  // pass results to Parsing.jsx
//           onSuccess();
//         } else {
//           message.error(`${file.name} failed: ${data.error || 'Unknown error'}`);
//           onError();
//         }
//       } catch (err) {
//         console.error(err);
//         message.error('Upload error');
//         onError();
//       }
//     },
//     onDrop(e) {
//       console.log('Dropped files', e.dataTransfer.files);
//     },
//   };

//   return (
//     <Dragger {...props}>
//       <p className="ant-upload-drag-icon">
//         <InboxOutlined />
//       </p>
//       <p className="ant-upload-text">Click or drag file to this area to upload</p>
//       <p className="ant-upload-hint">
//         Upload resume files (PDF/DOCX). JWT-protected.
//       </p>
//     </Dragger>
//   );
// };

// export default DropBox;

// 1st try

// 2nd try
// import React from 'react';
// import { InboxOutlined } from '@ant-design/icons';
// import { Upload } from 'antd';

// const { Dragger } = Upload;

// const DropBox = () => {
//   const props = {
//     multiple: true,
//     beforeUpload: (file) => {
//       const current = JSON.parse(localStorage.getItem('uploadedFiles') || '[]');
//       localStorage.setItem('uploadedFiles', JSON.stringify([...current, file]));
//       return false; // prevent auto-upload
//     },
//     onDrop(e) {
//       console.log('Dropped files', e.dataTransfer.files);
//     }
//   };

//   return (
//     <Dragger {...props}>
//       <p className="ant-upload-drag-icon">
//         <InboxOutlined />
//       </p>
//       <p className="ant-upload-text">Click or drag file to this area to upload</p>
//       <p className="ant-upload-hint">
//         Supports single or bulk upload. Don’t upload sensitive files.
//       </p>
//     </Dragger>
//   );
// };

// export default DropBox;

// 2nd try

// 3rd
// DropBox.jsx
import React from 'react';
import { InboxOutlined } from '@ant-design/icons';
import { Upload } from 'antd';

const { Dragger } = Upload;

const DropBox = ({ onFilesSelected }) => {
  const props = {
    name: 'resumes',
    multiple: true,
    beforeUpload: (file, fileList) => {
      onFilesSelected(fileList); // Pass selected files up
      return false; // Prevent auto upload
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };

  return (
    <Dragger {...props}>
      <p className="ant-upload-drag-icon">
        <InboxOutlined />
      </p>
      <p className="ant-upload-text">Click or drag file to this area to upload</p>
      <p className="ant-upload-hint">
        Support for bulk upload. Don't upload confidential data.
      </p>
    </Dragger>
  );
};

export default DropBox;

// 3rd