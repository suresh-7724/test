var a = 10;
var b = "constant";
var c = true;
// Scope & Mutability:
function scopeExample() {
    if (true) {
        var x = "block scoped"; // Block scoped
        var y = "const scoped"; // Block scoped, immutable
        var z = "function scoped"; // Function scoped
        console.log(x, y, z);
    }
    // console.log(x, y); // ❌ Error: x and y not accessible here
    console.log(c); // ✅ Accessible (var is function scoped)
}
scopeExample();
