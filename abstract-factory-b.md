Perfect — let’s go through **Set B and Set C** step-by-step with complete Java programs and explanations for each pattern.

---

# 🧩 **SET B**

---

## **1. Abstract Factory Pattern — Cars for North America and Europe**

### 📘 Concept

The **Abstract Factory Pattern** lets you create **families of related objects** (here: cars and specifications) without specifying their concrete classes.

We’ll create:

* Abstract factories for **Car** and **Specification**
* Concrete factories for **North America** and **Europe**

---

### 🚗 Step 1: Define Product Interfaces

```java
interface Car {
    void assemble();
}

interface Specification {
    void showSpecs();
}
```

---

### 🚗 Step 2: Create Concrete Products

```java
// North America Products
class NorthAmericaCar implements Car {
    public void assemble() {
        System.out.println("Assembling a car for North America market");
    }
}

class NorthAmericaSpec implements Specification {
    public void showSpecs() {
        System.out.println("Specifications: Left-hand drive, complies with US emissions");
    }
}

// Europe Products
class EuropeCar implements Car {
    public void assemble() {
        System.out.println("Assembling a car for Europe market");
    }
}

class EuropeSpec implements Specification {
    public void showSpecs() {
        System.out.println("Specifications: Right-hand drive, complies with EU safety standards");
    }
}
```

---

### 🚗 Step 3: Define Abstract Factory

```java
interface CarFactory {
    Car createCar();
    Specification createSpecification();
}
```

---

### 🚗 Step 4: Create Concrete Factories

```java
class NorthAmericaFactory implements CarFactory {
    public Car createCar() {
        return new NorthAmericaCar();
    }

    public Specification createSpecification() {
        return new NorthAmericaSpec();
    }
}

class EuropeFactory implements CarFactory {
    public Car createCar() {
        return new EuropeCar();
    }

    public Specification createSpecification() {
        return new EuropeSpec();
    }
}
```

---

### 🚗 Step 5: Test the Abstract Factory

```java
public class AbstractFactoryCarDemo {
    public static void main(String[] args) {
        CarFactory naFactory = new NorthAmericaFactory();
        Car naCar = naFactory.createCar();
        Specification naSpec = naFactory.createSpecification();
        naCar.assemble();
        naSpec.showSpecs();

        System.out.println();

        CarFactory euFactory = new EuropeFactory();
        Car euCar = euFactory.createCar();
        Specification euSpec = euFactory.createSpecification();
        euCar.assemble();
        euSpec.showSpecs();
    }
}
```

---

### ✅ Output

```
Assembling a car for North America market
Specifications: Left-hand drive, complies with US emissions

Assembling a car for Europe market
Specifications: Right-hand drive, complies with EU safety standards
```

---

## **2. Singleton Pattern for Multithreading**

### 📘 Concept

The **Singleton Pattern** ensures that only one instance of a class exists — even when multiple threads try to access it at the same time.

We’ll use **double-checked locking** for thread safety.

---

### 💾 Code Implementation

```java
class MultiThreadSingleton {
    private static volatile MultiThreadSingleton instance;

    private MultiThreadSingleton() {
        System.out.println("Singleton Instance Created");
    }

    public static MultiThreadSingleton getInstance() {
        if (instance == null) {
            synchronized (MultiThreadSingleton.class) {
                if (instance == null) {
                    instance = new MultiThreadSingleton();
                }
            }
        }
        return instance;
    }

    public void showMessage() {
        System.out.println("Thread-safe Singleton Instance");
    }
}

public class SingletonMultiThreadDemo {
    public static void main(String[] args) {
        Runnable task = () -> {
            MultiThreadSingleton singleton = MultiThreadSingleton.getInstance();
            singleton.showMessage();
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        Thread t3 = new Thread(task);

        t1.start();
        t2.start();
        t3.start();
    }
}
```

---

### ✅ Output (example)

```
Singleton Instance Created
Thread-safe Singleton Instance
Thread-safe Singleton Instance
Thread-safe Singleton Instance
```

Note: Instance creation message prints only once even with multiple threads.

---

# 🧩 **SET C**

---

## **1. Singleton Pattern — LoggerService**

### 📘 Concept

A classic **Singleton pattern** with a private constructor and a static method to return the single instance.

---

### 💾 Code Implementation

```java
class LoggerService {
    private static LoggerService instance;

    private LoggerService() {
        System.out.println("Logger Service Initialized");
    }

    public static synchronized LoggerService getInstance() {
        if (instance == null) {
            instance = new LoggerService();
        }
        return instance;
    }

    public void log(String message) {
        System.out.println("[LOG]: " + message);
    }
}

public class LoggerDemo {
    public static void main(String[] args) {
        LoggerService logger1 = LoggerService.getInstance();
        logger1.log("Starting application");

        LoggerService logger2 = LoggerService.getInstance();
        logger2.log("Application running smoothly");

        System.out.println("Same instance? " + (logger1 == logger2));
    }
}
```

---

### ✅ Output

```
Logger Service Initialized
[LOG]: Starting application
[LOG]: Application running smoothly
Same instance? true
```

---

## **2. Prototype Pattern — Shape Cloning**

### 📘 Concept

The **Prototype Pattern** creates new objects by cloning existing ones, rather than instantiating new objects directly.

---

### 🎨 Step 1: Create Shape Interface

```java
interface Shape extends Cloneable {
    Shape clone();
    void draw();
}
```

---

### 🎨 Step 2: Concrete Classes

```java
class Circle implements Shape {
    private int radius;

    public Circle(int radius) {
        this.radius = radius;
    }

    public void draw() {
        System.out.println("Drawing Circle with radius " + radius);
    }

    public Shape clone() {
        return new Circle(this.radius);
    }
}

class Rectangle implements Shape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public void draw() {
        System.out.println("Drawing Rectangle with width " + width + " and height " + height);
    }

    public Shape clone() {
        return new Rectangle(this.width, this.height);
    }
}
```

---

### 🎨 Step 3: Test the Prototype Pattern

```java
public class PrototypeDemo {
    public static void main(String[] args) {
        Circle originalCircle = new Circle(10);
        Circle clonedCircle = (Circle) originalCircle.clone();

        Rectangle originalRect = new Rectangle(20, 15);
        Rectangle clonedRect = (Rectangle) originalRect.clone();

        originalCircle.draw();
        clonedCircle.draw();
        originalRect.draw();
        clonedRect.draw();

        System.out.println("Are circle objects same? " + (originalCircle == clonedCircle));
        System.out.println("Are rectangle objects same? " + (originalRect == clonedRect));
    }
}
```

---

### ✅ Output

```
Drawing Circle with radius 10
Drawing Circle with radius 10
Drawing Rectangle with width 20 and height 15
Drawing Rectangle with width 20 and height 15
Are circle objects same? false
Are rectangle objects same? false
```

---

# ✅ **Summary**

| Set    | Pattern                 | Concept                              | Example Class                      |
| ------ | ----------------------- | ------------------------------------ | ---------------------------------- |
| **B1** | Abstract Factory        | Creates related families of objects  | CarFactory for NorthAmerica/Europe |
| **B2** | Singleton (Thread-safe) | Only one instance in multi-threading | MultiThreadSingleton               |
| **C1** | Singleton               | Single logger service instance       | LoggerService                      |
| **C2** | Prototype               | Clone existing objects               | Circle, Rectangle                  |

---

Would you like me to organize all **Sets A, B, and C** into a single folder structure with proper package names (like `factorymethod`, `singleton`, `abstractfactory`, `prototype`) so you can import directly into Eclipse?
