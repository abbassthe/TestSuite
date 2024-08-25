import React, { useState, FormEvent } from 'react';
import "./Cover.scss";

export default function Cover() {
  // State for storing input text and the API response
  const [inputText, setInputText] = useState<string>('');
  const [responseText, setResponseText] = useState<string>('');

  // Function to handle the form submission
  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault(); // Prevents page reload on form submission

    try {
      const response = await fetch('https://testsuite-1.onrender.com/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: inputText }), // Send the input text in the body of the request
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json(); // Assuming the API returns JSON
      setResponseText(data.response); // Update the response text
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
      setResponseText('Error: Failed to fetch data'); // Handle any errors
    }
  };

  return (
    <div className="Wrapper">
      <div className='WrapperCover'>
        <form onSubmit={handleSubmit} id="Form">
          <label style={{display : "flex"}}>
            <textarea
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              rows={10} // Adjust this value to control the height
              placeholder="Enter your code here..."
            />
          </label>
          <button className='button' type="submit">Send</button>
        </form>

        <div className='table' style={{height : "100vh"}}>
          <h3>Response:</h3>
          <pre>{responseText}</pre> {/* Display the API response in a preformatted block */}
        </div>
      </div>
    </div>
  );
}
