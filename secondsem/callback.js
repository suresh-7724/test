function applyCallback(num, callback) {
  return callback(num);
}

const square = x => x * x;

console.log(applyCallback(5, square)); // 25
