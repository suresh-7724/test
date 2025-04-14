function getFirstElement<T>(arr: T[]): T | undefined {
    return arr[0];
}

console.log(getFirstElement<number>([10, 20, 30])); // 10
console.log(getFirstElement<string>(["a", "b", "c"])); // "a"
