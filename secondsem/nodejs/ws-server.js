const WebSocket = require('ws');

const server = new WebSocket.Server({ port: 8080 });

server.on('connection', (ws) => {
  console.log("Client connected");

  ws.on('message', (message) => {
    console.log("Received from client:", message);
  });

  ws.on('close', () => {
    console.log("Client disconnected");
  });

  ws.send("Hello from server!");
});
