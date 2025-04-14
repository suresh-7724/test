function addElement(arr, element) {
  return [...arr, element];
}

const original = [1, 2, 3];
const newArr = addElement(original, 4);

console.log("Original:", original); // [1, 2, 3]
console.log("New:", newArr);       // [1, 2, 3, 4]
