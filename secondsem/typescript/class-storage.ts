class Storage<T> {
    private data: T;

    set(value: T): void {
        this.data = value;
    }

    get(): T {
        return this.data;
    }
}

const numberStorage = new Storage<number>();
numberStorage.set(42);
console.log(numberStorage.get()); // 42

const stringStorage = new Storage<string>();
stringStorage.set("Hello");
console.log(stringStorage.get()); // Hello
