const WebSocket = require('ws');

const client = new WebSocket('ws://localhost:8080');

client.on('open', () => {
  console.log("Connected to server");
  client.send("Hello Server!");
});

client.on('message', (data) => {
  console.log("Received from server:", data);
});
