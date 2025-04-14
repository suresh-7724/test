function applyFunctionToArray(fn, arr) {
  return arr.map(fn);
}

const double = x => x * 2;
console.log(applyFunctionToArray(double, [1, 2, 3])); // [2, 4, 6]
