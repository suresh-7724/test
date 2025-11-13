Here’s a **complete and clear solution** for each program in **Set A, Set B, and Set C**, showing correct implementation of Decorator, Adapter, Bridge, Proxy, and Composite patterns.
All are **Java console-based** examples that can compile and run individually.

---

## **SET A**

### **1. I/O Decorator to convert uppercase to lowercase**

```java
import java.io.*;

class LowerCaseInputStream extends FilterInputStream {
    protected LowerCaseInputStream(InputStream in) {
        super(in);
    }

    public int read() throws IOException {
        int c = super.read();
        return (c == -1 ? c : Character.toLowerCase((char) c));
    }

    public int read(byte[] b, int offset, int len) throws IOException {
        int result = super.read(b, offset, len);
        for (int i = offset; i < offset + result; i++) {
            b[i] = (byte) Character.toLowerCase((char) b[i]);
        }
        return result;
    }
}

public class LowerCaseDecoratorTest {
    public static void main(String[] args) throws IOException {
        String input = "HELLO JAVA DECORATOR PATTERN";
        InputStream in = new ByteArrayInputStream(input.getBytes());
        InputStream lowerCaseIn = new LowerCaseInputStream(in);

        int c;
        while ((c = lowerCaseIn.read()) >= 0) {
            System.out.print((char) c);
        }
        lowerCaseIn.close();
    }
}
```

---

### **2. Adapter Pattern for Enumeration to Iterator**

```java
import java.util.*;

class EnumerationIteratorAdapter<E> implements Iterator<E> {
    private Enumeration<E> enumeration;

    public EnumerationIteratorAdapter(Enumeration<E> enumeration) {
        this.enumeration = enumeration;
    }

    public boolean hasNext() {
        return enumeration.hasMoreElements();
    }

    public E next() {
        return enumeration.nextElement();
    }
}

public class AdapterExample {
    public static void main(String[] args) {
        Vector<String> vector = new Vector<>();
        vector.add("Apple");
        vector.add("Banana");
        vector.add("Cherry");

        Enumeration<String> enumeration = vector.elements();
        Iterator<String> iterator = new EnumerationIteratorAdapter<>(enumeration);

        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }
}
```

---

### **3. Bridge Pattern – Produce and Assemble Vehicles**

```java
interface Workshop {
    void work();
}

class Produce implements Workshop {
    public void work() {
        System.out.print("Produced");
    }
}

class Assemble implements Workshop {
    public void work() {
        System.out.print(" and Assembled");
    }
}

abstract class Vehicle {
    protected Workshop produce;
    protected Workshop assemble;

    protected Vehicle(Workshop produce, Workshop assemble) {
        this.produce = produce;
        this.assemble = assemble;
    }

    abstract void manufacture();
}

class Car extends Vehicle {
    public Car(Workshop produce, Workshop assemble) {
        super(produce, assemble);
    }

    void manufacture() {
        System.out.print("Car ");
        produce.work();
        assemble.work();
        System.out.println();
    }
}

class Bike extends Vehicle {
    public Bike(Workshop produce, Workshop assemble) {
        super(produce, assemble);
    }

    void manufacture() {
        System.out.print("Bike ");
        produce.work();
        assemble.work();
        System.out.println();
    }
}

public class BridgePatternDemo {
    public static void main(String[] args) {
        Vehicle car = new Car(new Produce(), new Assemble());
        Vehicle bike = new Bike(new Produce(), new Assemble());

        car.manufacture();
        bike.manufacture();
    }
}
```

---

## **SET B**

### **1. Adapter Pattern – Heart Model to Beat Model**

```java
interface HeartModel {
    int getHeartRate();
}

class SimpleHeartModel implements HeartModel {
    public int getHeartRate() {
        return 72; // bpm
    }
}

interface BeatModel {
    void beat();
}

class HeartToBeatAdapter implements BeatModel {
    private HeartModel heartModel;

    public HeartToBeatAdapter(HeartModel heartModel) {
        this.heartModel = heartModel;
    }

    public void beat() {
        System.out.println("Heart beating at " + heartModel.getHeartRate() + " bpm");
    }
}

public class HeartAdapterTest {
    public static void main(String[] args) {
        HeartModel heart = new SimpleHeartModel();
        BeatModel beatModel = new HeartToBeatAdapter(heart);
        beatModel.beat();
    }
}
```

---

### **2. Proxy Pattern for Image Loading**

```java
interface Image {
    void display();
}

class RealImage implements Image {
    private String filename;

    public RealImage(String filename) {
        this.filename = filename;
        loadFromDisk();
    }

    private void loadFromDisk() {
        System.out.println("Loading " + filename);
    }

    public void display() {
        System.out.println("Displaying " + filename);
    }
}

class ProxyImage implements Image {
    private RealImage realImage;
    private String filename;

    public ProxyImage(String filename) {
        this.filename = filename;
    }

    public void display() {
        if (realImage == null) {
            realImage = new RealImage(filename);
        }
        realImage.display();
    }
}

public class ProxyPatternDemo {
    public static void main(String[] args) {
        Image image = new ProxyImage("test_image.jpg");
        image.display(); // loaded and displayed
        image.display(); // uses cache
    }
}
```

---

### **3. Decorator Pattern – Pizza Toppings**

```java
interface Pizza {
    String getDescription();
    double getCost();
}

class BasicPizza implements Pizza {
    public String getDescription() {
        return "Plain Pizza";
    }

    public double getCost() {
        return 5.00;
    }
}

abstract class ToppingDecorator implements Pizza {
    protected Pizza pizza;

    public ToppingDecorator(Pizza pizza) {
        this.pizza = pizza;
    }
}

class Cheese extends ToppingDecorator {
    public Cheese(Pizza pizza) {
        super(pizza);
    }

    public String getDescription() {
        return pizza.getDescription() + ", Cheese";
    }

    public double getCost() {
        return pizza.getCost() + 1.5;
    }
}

class Olives extends ToppingDecorator {
    public Olives(Pizza pizza) {
        super(pizza);
    }

    public String getDescription() {
        return pizza.getDescription() + ", Olives";
    }

    public double getCost() {
        return pizza.getCost() + 1.0;
    }
}

class Mushrooms extends ToppingDecorator {
    public Mushrooms(Pizza pizza) {
        super(pizza);
    }

    public String getDescription() {
        return pizza.getDescription() + ", Mushrooms";
    }

    public double getCost() {
        return pizza.getCost() + 1.2;
    }
}

public class PizzaDecoratorDemo {
    public static void main(String[] args) {
        Pizza pizza = new BasicPizza();
        pizza = new Cheese(new Olives(new Mushrooms(pizza)));

        System.out.println(pizza.getDescription() + " Cost: $" + pizza.getCost());
    }
}
```

---

## **SET C**

### **Composite Pattern – Employee Hierarchy**

```java
import java.util.ArrayList;
import java.util.List;

interface Employee {
    void showDetails();
}

class Worker implements Employee {
    private String name;
    private String position;

    public Worker(String name, String position) {
        this.name = name;
        this.position = position;
    }

    public void showDetails() {
        System.out.println(name + " (" + position + ")");
    }
}

class Manager implements Employee {
    private String name;
    private String position;
    private List<Employee> subordinates = new ArrayList<>();

    public Manager(String name, String position) {
        this.name = name;
        this.position = position;
    }

    public void add(Employee e) {
        subordinates.add(e);
    }

    public void remove(Employee e) {
        subordinates.remove(e);
    }

    public void showDetails() {
        System.out.println(name + " (" + position + ")");
        for (Employee e : subordinates) {
            e.showDetails();
        }
    }
}

public class CompositePatternDemo {
    public static void main(String[] args) {
        Worker w1 = new Worker("Alice", "Developer");
        Worker w2 = new Worker("Bob", "Tester");

        Manager m1 = new Manager("Charlie", "Project Manager");
        m1.add(w1);
        m1.add(w2);

        Manager ceo = new Manager("David", "CEO");
        ceo.add(m1);

        ceo.showDetails();
    }
}
```

---

Would you like me to combine all sets (A, B, C) into one file with comments separating each example for easier submission formatting (like a single `.java` file for assignment upload)?
