const fs = require('fs');

const readStream = fs.createReadStream('data.txt', 'utf8');

readStream.on('data', (chunk) => {
  console.log("Received data:", chunk);
});

readStream.on('end', () => {
  console.log("Stream ended.");
});
