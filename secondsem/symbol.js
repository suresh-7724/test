const id = Symbol("id");

const user = {
  name: "Bob",
  age: 40,
  [id]: 12345
};

console.log("User ID (symbol):", user[id]); // Accessing using the symbol
console.log("User object:", user);

// Symbol property is not shown in JSON or Object.keys()
console.log("Keys:", Object.keys(user)); // name, age only
