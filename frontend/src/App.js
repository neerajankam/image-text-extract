import React, { useState } from 'react';
import './App.css';

function App() {
  const [image, setImage] = useState(null);
  const [text, setText] = useState('');
  const [results, setResults] = useState('');

  const handleImageChange = (event) => {
    const selectedImage = event.target.files[0];
    setImage(selectedImage);
  };

  const handleImageUpload = async () => {
    if (!image) {
      return;
    }

    const formData = new FormData();
    formData.append('image', image);

    try {
      const response = await fetch('http://0.0.0.0:5000/extract', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      setText(data.text);
      setResults(''); // Clear previous results when uploading new image
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  const handleFetchResults = async () => {
    try {
      const response = await fetch('http://0.0.0.0:5000/extract');
      const data = await response.json();
      setResults(data);
      console.log(data)
      setText(''); // Clear previous text when fetching results
    } catch (error) {
      console.error('Error fetching results:', error);
    }
  };

  return (
    <div className="App">
      <h1>Image Text Extraction</h1>
      <input type="file" accept="image/*" onChange={handleImageChange} />
      <button onClick={handleImageUpload}>Upload</button>
      <button onClick={handleFetchResults}>Fetch Results</button>
      {text && <div className="text">{text}</div>}
      {results && (
        <div className="results">
          <h2>Results from Database:</h2>
          <p>{JSON.stringify(results)}</p>
        </div>
      )}
    </div>
  );
}

export default App;
