const express = require('express');
const mysql = require('mysql');
const cors = require('cors');
const { computeHeadingLevel } = require('@testing-library/react');

const app = express();
const PORT = 8000;

// MySQL database configuration
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '1111',
  database: 'questiondb',
});

console.log(connection);

// Connect to MySQL database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL database:', err);
  } else {
    console.log('Connected to MySQL database');
  }
});

// Middleware
app.use(cors());
app.use(express.json());

// API endpoint to handle the insertion of student data

  



  app.post('/stud', (req, res) => {
    const { id, password } = req.body;
    console.log(req.body)
  // alert('inside'); 
    // Query the database to check if the provided ID and password match any student record
    const query = 'SELECT * FROM student WHERE id = ? AND password = ?';
    connection.query(query, [id, password], (err, results) => {
      if (err) {
        console.error('Error querying database:', err);
        res.json({ success: false, message: 'Error during login' });
        return;
      }
      if (results.length > 0) {
        const foundstudent = results[0];
        res.json({ success: true, message: 'Login successful', student: foundstudent});
      } else {
        res.json({ success: false, message: 'Invalid ID or password' });
      }
    });
  });

  const bodyParser=require('body-parser');
  app.use(bodyParser.json());

// API endpoint to fetch questions
app.get('/questions', (req, res) => {
  const sql = 'SELECT * FROM questions';

  connection.query(sql, (err, result) => {
    if (err) {
      console.error('Error fetching questions from database:', err);
      res.status(500).send('Internal Server Error');
    } else {
      console.log (result);
      res.json(result);
    }
  });
});

app.post('/quesub', (req, res) => {
  try {
    // Extract selected options from the request body
    const { id, arr } = req.body;

    // Create a SQL query to insert data
    for (let i = 0; i < 5; i++) {
      const insertQuery = 'INSERT INTO answers VALUES (?, ?, ?)';

      // Execute the query with the selected options
      connection.query(insertQuery, [id, i, arr[i]], (err, result) => {
        if (err) {
          console.error('Error inserting selected options:', err);
          res.status(500).json({ error: 'Internal Server Error' });
          return;
        }

        // console.log(`Selected option for question ${i} inserted successfully`);
        
        // Check if this is the last iteration, then send the response
        if (i === 4) {
          // console.log('All selected options inserted successfully');
          res.status(201).json({ message: 'Selected options saved successfully.' });
        }
      });
    }
  } catch (error) {
    console.error('Error saving selected options:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});


// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});







