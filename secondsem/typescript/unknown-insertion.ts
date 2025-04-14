function handleUnknown(value: unknown) {
    if (typeof value === "string") {
        console.log("String length:", (value as string).length);
    } else if (typeof value === "number") {
        console.log("Squared value:", (value as number) ** 2);
    } else {
        console.log("Unknown type");
    }
}

handleUnknown("Hello");
handleUnknown(5);
handleUnknown(true);
