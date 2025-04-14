class Car {
  constructor(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
  }

  showDetails() {
    console.log(`Car: ${this.make} ${this.model}, Year: ${this.year}`);
  }
}

const myCar = new Car("Toyota", "Corolla", 2022);
myCar.showDetails(); // Output: Car: Toyota Corolla, Year: 2022
