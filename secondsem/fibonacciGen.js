function* fibonacci() {
  let a = 0, b = 1;
  yield a;
  yield b;
  yield a + b;
}

const fibGen = fibonacci();
console.log(fibGen.next().value); // 0
console.log(fibGen.next().value); // 1
console.log(fibGen.next().value); // 1
