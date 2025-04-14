let a: number = 10;
const b: string = "constant";
var c: boolean = true;

// Scope & Mutability:
function scopeExample() {
    if (true) {
        let x = "block scoped";    // Block scoped
        const y = "const scoped";  // Block scoped, immutable
        var z = "function scoped"; // Function scoped
        console.log(x, y, z);
    }
    // console.log(x, y); // ❌ Error: x and y not accessible here
    console.log(c); // ✅ Accessible (var is function scoped)
}
scopeExample();
