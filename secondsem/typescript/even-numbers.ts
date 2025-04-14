function getEvenNumbers(numbers: number[]): number[] {
    return numbers.filter(num => num % 2 === 0);
}

console.log(getEvenNumbers([1, 2, 3, 4, 5, 6])); // [2, 4, 6]
