const express = require('express');
const axios = require('axios');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
const port = 3001;
const TARGET_URL = 'http://localhost:8080';

// Enable CORS
app.use(cors({
  origin: 'http://localhost:3000',
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Accept', 'Authorization'],
  credentials: true
}));

// Parse JSON request bodies
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Handle all methods
app.all('*', async (req, res) => {
  try {
    // Log the incoming request
    console.log(`${req.method} ${req.path}`);
    
    // Skip actual request for OPTIONS
    if (req.method === 'OPTIONS') {
      return res.status(200).end();
    }
    
    // Forward the request to the target server
    const response = await axios({
      method: req.method,
      url: `${TARGET_URL}${req.url}`,
      data: req.body,
      headers: {
        ...req.headers,
        host: new URL(TARGET_URL).host
      },
      validateStatus: () => true, // Don't throw on non-2xx responses
    });
    
    // Send the response back to the client
    res.status(response.status);
    Object.entries(response.headers).forEach(([key, value]) => {
      res.setHeader(key, value);
    });
    
    // Ensure CORS headers are set
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:3000');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Accept, Authorization');
    res.setHeader('Access-Control-Allow-Credentials', 'true');
    
    res.send(response.data);
  } catch (error) {
    console.error('Proxy error:', error.message);
    res.status(500).send('Proxy error');
  }
});

app.listen(port, () => {
  console.log(`CORS Proxy server running at http://localhost:${port}`);
});
