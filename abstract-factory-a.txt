Here’s a **step-by-step implementation guide for Set A** that covers all three design pattern programs (Factory Method, Singleton, and Abstract Factory) in Java with clear code examples and explanations.

---

## 🧩 **1. Factory Method Pattern — Pizza Store Example**

### 📘 Concept

The **Factory Method Pattern** defines an interface for creating an object but lets subclasses decide which class to instantiate.

Here, we’ll have:

* `PizzaStore` as the **creator**
* `createPizza()` as the **factory method**
* Concrete stores (`NYPizzaStore`, `ChicagoPizzaStore`) create specific pizzas.

---

### 🍕 Step 1: Create Abstract `Pizza` Class

```java
abstract class Pizza {
    String name;

    void prepare() {
        System.out.println("Preparing " + name);
    }

    void bake() {
        System.out.println("Baking " + name);
    }

    void cut() {
        System.out.println("Cutting " + name);
    }

    void box() {
        System.out.println("Boxing " + name);
    }

    public String getName() {
        return name;
    }
}
```

---

### 🍕 Step 2: Create Concrete Pizza Classes

```java
class NYStyleCheesePizza extends Pizza {
    public NYStyleCheesePizza() {
        name = "New York Style Cheese Pizza";
    }
}

class ChicagoStyleCheesePizza extends Pizza {
    public ChicagoStyleCheesePizza() {
        name = "Chicago Style Deep Dish Cheese Pizza";
    }

    @Override
    void cut() {
        System.out.println("Cutting the pizza into square slices");
    }
}
```

---

### 🍕 Step 3: Create Abstract `PizzaStore`

```java
abstract class PizzaStore {

    public Pizza orderPizza(String type) {
        Pizza pizza = createPizza(type); // Factory Method

        pizza.prepare();
        pizza.bake();
        pizza.cut();
        pizza.box();

        return pizza;
    }

    protected abstract Pizza createPizza(String type);
}
```

---

### 🍕 Step 4: Create Concrete Stores

```java
class NYPizzaStore extends PizzaStore {
    protected Pizza createPizza(String type) {
        if (type.equalsIgnoreCase("cheese")) {
            return new NYStyleCheesePizza();
        }
        return null;
    }
}

class ChicagoPizzaStore extends PizzaStore {
    protected Pizza createPizza(String type) {
        if (type.equalsIgnoreCase("cheese")) {
            return new ChicagoStyleCheesePizza();
        }
        return null;
    }
}
```

---

### 🍕 Step 5: Test the Factory Method

```java
public class FactoryMethodDemo {
    public static void main(String[] args) {
        PizzaStore nyStore = new NYPizzaStore();
        PizzaStore chicagoStore = new ChicagoPizzaStore();

        Pizza pizza1 = nyStore.orderPizza("cheese");
        System.out.println("Ordered a " + pizza1.getName() + "\n");

        Pizza pizza2 = chicagoStore.orderPizza("cheese");
        System.out.println("Ordered a " + pizza2.getName());
    }
}
```

---

## 🧭 **Output**

```
Preparing New York Style Cheese Pizza
Baking New York Style Cheese Pizza
Cutting New York Style Cheese Pizza
Boxing New York Style Cheese Pizza
Ordered a New York Style Cheese Pizza

Preparing Chicago Style Deep Dish Cheese Pizza
Baking Chicago Style Deep Dish Cheese Pizza
Cutting the pizza into square slices
Boxing Chicago Style Deep Dish Cheese Pizza
Ordered a Chicago Style Deep Dish Cheese Pizza
```

---

## 🧩 **2. Singleton Pattern — Database Connection Example**

### 📘 Concept

The **Singleton Pattern** ensures that only one instance of a class is created and provides a global point of access to it.

We’ll make the class thread-safe using **synchronized blocks** and **lazy initialization**.

---

### 💾 Step 1: Create `DatabaseConnection` Class

```java
public class DatabaseConnection {
    private static volatile DatabaseConnection instance;

    private DatabaseConnection() {
        System.out.println("Database Connection created.");
    }

    public static DatabaseConnection getConnection() {
        if (instance == null) { // First check
            synchronized (DatabaseConnection.class) {
                if (instance == null) { // Second check for thread safety
                    instance = new DatabaseConnection();
                }
            }
        }
        return instance;
    }

    public void connect() {
        System.out.println("Connected to database...");
    }
}
```

---

### 💾 Step 2: Test the Singleton

```java
public class SingletonDemo {
    public static void main(String[] args) {
        DatabaseConnection c1 = DatabaseConnection.getConnection();
        DatabaseConnection c2 = DatabaseConnection.getConnection();

        c1.connect();
        c2.connect();

        System.out.println("Are both connections same? " + (c1 == c2));
    }
}
```

---

### ✅ Output

```
Database Connection created.
Connected to database...
Connected to database...
Are both connections same? true
```

---

## 📱 **3. Abstract Factory Pattern — Mobile Phone Functionalities**

### 📘 Concept

The **Abstract Factory Pattern** provides an interface for creating families of related objects without specifying their concrete classes.

We’ll define:

* Abstract factories for **Camera** and **VideoRecorder**
* Concrete factories for **Android** and **iPhone**

---

### 📱 Step 1: Define Product Interfaces

```java
interface Camera {
    void takePhoto();
}

interface VideoRecorder {
    void recordVideo();
}
```

---

### 📱 Step 2: Concrete Product Implementations

```java
class AndroidCamera implements Camera {
    public void takePhoto() {
        System.out.println("Android: Taking photo using Android Camera");
    }
}

class IPhoneCamera implements Camera {
    public void takePhoto() {
        System.out.println("iPhone: Taking photo using iPhone Camera");
    }
}

class AndroidVideoRecorder implements VideoRecorder {
    public void recordVideo() {
        System.out.println("Android: Recording video using Android Recorder");
    }
}

class IPhoneVideoRecorder implements VideoRecorder {
    public void recordVideo() {
        System.out.println("iPhone: Recording video using iPhone Recorder");
    }
}
```

---

### 📱 Step 3: Define Abstract Factory

```java
interface MobileFactory {
    Camera createCamera();
    VideoRecorder createVideoRecorder();
}
```

---

### 📱 Step 4: Concrete Factories

```java
class AndroidFactory implements MobileFactory {
    public Camera createCamera() {
        return new AndroidCamera();
    }
    public VideoRecorder createVideoRecorder() {
        return new AndroidVideoRecorder();
    }
}

class IPhoneFactory implements MobileFactory {
    public Camera createCamera() {
        return new IPhoneCamera();
    }
    public VideoRecorder createVideoRecorder() {
        return new IPhoneVideoRecorder();
    }
}
```

---

### 📱 Step 5: Client Code

```java
public class AbstractFactoryDemo {
    public static void main(String[] args) {
        MobileFactory androidFactory = new AndroidFactory();
        Camera androidCam = androidFactory.createCamera();
        VideoRecorder androidVid = androidFactory.createVideoRecorder();

        androidCam.takePhoto();
        androidVid.recordVideo();

        System.out.println();

        MobileFactory iphoneFactory = new IPhoneFactory();
        Camera iphoneCam = iphoneFactory.createCamera();
        VideoRecorder iphoneVid = iphoneFactory.createVideoRecorder();

        iphoneCam.takePhoto();
        iphoneVid.recordVideo();
    }
}
```

---

### ✅ Output

```
Android: Taking photo using Android Camera
Android: Recording video using Android Recorder

iPhone: Taking photo using iPhone Camera
iPhone: Recording video using iPhone Recorder
```

---

## 🎯 Summary

| Pattern              | Purpose                                 | Example                                    |
| -------------------- | --------------------------------------- | ------------------------------------------ |
| **Factory Method**   | Delegates object creation to subclasses | PizzaStore creating different pizza types  |
| **Singleton**        | Ensures a single instance of a class    | DatabaseConnection                         |
| **Abstract Factory** | Creates families of related objects     | MobileFactory for Camera and VideoRecorder |

---

Would you like me to combine all these programs into **a single Java project folder structure (with packages)** so you can run them easily in Eclipse or IntelliJ?
