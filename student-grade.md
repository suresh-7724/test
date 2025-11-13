Here’s a clear **step-by-step guide** to implement **Set B (Single Responsibility Principle)** using Java.

We’ll start with a **bad design**, then refactor it to follow SRP.

---

## ❌ Step 1: The Problem — Violating SRP

Here’s how a *non-SRP* `Student` class might look:

```java
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class Student {
    private String name;
    private List<Integer> marks;

    public Student(String name, List<Integer> marks) {
        this.name = name;
        this.marks = marks;
    }

    // Calculates average
    public double calculateAverage() {
        double total = 0;
        for (int mark : marks) {
            total += mark;
        }
        return total / marks.size();
    }

    // Saves student data to file
    public void saveToFile() {
        try (FileWriter writer = new FileWriter(name + ".txt")) {
            writer.write("Name: " + name + "\n");
            writer.write("Marks: " + marks + "\n");
            writer.write("Average: " + calculateAverage());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

This class has **three responsibilities**:

1. Managing student data
2. Calculating averages
3. Saving data to a file

That breaks the **Single Responsibility Principle (SRP)**.

---

## ✅ Step 2: Refactor According to SRP

We’ll split responsibilities into three separate classes:

1. **Student** → Holds only student data
2. **GradeCalculator** → Calculates average and grade
3. **StudentRepository** → Handles file saving or database logic

---

### 1. Student.java

Responsible only for storing student information.

```java
import java.util.List;

public class Student {
    private String name;
    private List<Integer> marks;

    public Student(String name, List<Integer> marks) {
        this.name = name;
        this.marks = marks;
    }

    public String getName() {
        return name;
    }

    public List<Integer> getMarks() {
        return marks;
    }
}
```

---

### 2. GradeCalculator.java

Handles all logic related to grades and averages.

```java
import java.util.List;

public class GradeCalculator {

    public double calculateAverage(List<Integer> marks) {
        if (marks == null || marks.isEmpty()) return 0.0;
        double total = 0;
        for (int mark : marks) {
            total += mark;
        }
        return total / marks.size();
    }

    public String findGrade(double average) {
        if (average >= 90) return "A";
        else if (average >= 75) return "B";
        else if (average >= 60) return "C";
        else if (average >= 40) return "D";
        else return "F";
    }
}
```

---

### 3. StudentRepository.java

Handles saving or loading student data (file I/O).

```java
import java.io.FileWriter;
import java.io.IOException;

public class StudentRepository {

    public void saveToFile(Student student, double average, String grade) {
        try (FileWriter writer = new FileWriter(student.getName() + ".txt")) {
            writer.write("Name: " + student.getName() + "\n");
            writer.write("Marks: " + student.getMarks() + "\n");
            writer.write("Average: " + average + "\n");
            writer.write("Grade: " + grade + "\n");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

---

## ✅ Step 3: Main Class — Using the Components

```java
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> marks = Arrays.asList(85, 90, 78, 92);
        Student student = new Student("Suresh", marks);

        GradeCalculator calculator = new GradeCalculator();
        double average = calculator.calculateAverage(student.getMarks());
        String grade = calculator.findGrade(average);

        StudentRepository repository = new StudentRepository();
        repository.saveToFile(student, average, grade);

        System.out.println("Student: " + student.getName());
        System.out.println("Average: " + average);
        System.out.println("Grade: " + grade);
        System.out.println("Data saved to file successfully.");
    }
}
```

---

## 🎯 Final Outcome

* **Student** → handles only student data.
* **GradeCalculator** → performs grade and average calculations.
* **StudentRepository** → handles persistence (file/database).

This structure now follows the **Single Responsibility Principle**, making your code modular, testable, and maintainable.

---

Would you like me to show how to **extend this example to use JSON file saving** instead of plain text (for a more practical application)?
