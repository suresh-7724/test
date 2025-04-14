// Import required modules
const express = require('express');
const fs = require('fs');
const path = require('path');

// Create an instance of express
const app = express();

// Middleware to parse URL-encoded data (for form submission)
app.use(express.urlencoded({ extended: true }));

// Serve static files (e.g., for CSS or JS)
app.use(express.static('public'));

// Route to display the input form
app.get('/', (req, res) => {
  res.send(`
    <html>
      <body>
        <h1>Read File Contents</h1>
        <form action="/read-file" method="POST">
          <label for="filename">Enter file name: </label>
          <input type="text" id="filename" name="filename" required>
          <button type="submit">Submit</button>
        </form>
      </body>
    </html>
  `);
});

// Route to handle file reading based on input
app.post('/read-file', (req, res) => {
  const filename = req.body.filename;
  
  // Define the path to the file (ensure it's in a safe directory)
  const filePath = path.join(__dirname, filename);
  
  // Read the file and send its content as response
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      res.send(`<h1>Error</h1><p>Could not read the file. Please ensure the file exists.</p>`);
      return;
    }
    res.send(`
      <html>
        <body>
          <h1>File Contents of ${filename}</h1>
          <pre>${data}</pre>
        </body>
      </html>
    `);
  });
});

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
