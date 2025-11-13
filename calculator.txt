Here’s a **step-by-step guide** to create your **MVC-based web calculator** (Addition, Subtraction, Multiplication, Division) using **Java Servlets + JSP**:

---

## 🧩 Project Overview

We’ll create:

1. **Model** → `CalculatorModel.java`
2. **View** → `calculator.jsp`
3. **Controller** → `CalculatorController.java`

You’ll deploy this on **Apache Tomcat** using a **Dynamic Web Project** in Eclipse or similar IDE.

---

## Step 1: Create the Project Structure

In Eclipse:

1. Go to **File → New → Dynamic Web Project**
2. Name it `CalculatorMVC`
3. Click **Finish**
4. Folder structure should look like:

   ```
   CalculatorMVC/
   ├── src/
   │   └── com.example.calculator/
   │       ├── CalculatorModel.java
   │       └── CalculatorController.java
   ├── WebContent/
   │   ├── calculator.jsp
   │   └── WEB-INF/
   │       └── web.xml
   ```

---

## Step 2: Create the Model (`CalculatorModel.java`)

This class holds the operands and performs calculations.

```java
package com.example.calculator;

public class CalculatorModel {
    private double num1;
    private double num2;
    private double result;

    public void setNum1(double num1) {
        this.num1 = num1;
    }

    public void setNum2(double num2) {
        this.num2 = num2;
    }

    public double getResult() {
        return result;
    }

    public void add() {
        result = num1 + num2;
    }

    public void subtract() {
        result = num1 - num2;
    }

    public void multiply() {
        result = num1 * num2;
    }

    public void divide() {
        if (num2 != 0)
            result = num1 / num2;
        else
            result = Double.NaN; // handle divide by zero
    }
}
```

---

## Step 3: Create the View (`calculator.jsp`)

This page takes input from the user and displays the result.

```jsp
<!DOCTYPE html>
<html>
<head>
    <title>Simple MVC Calculator</title>
</head>
<body>
    <h2>Basic Calculator</h2>
    <form action="CalculatorController" method="post">
        <input type="number" name="num1" step="any" required>
        <input type="number" name="num2" step="any" required><br><br>
        
        <input type="submit" name="operation" value="Add">
        <input type="submit" name="operation" value="Subtract">
        <input type="submit" name="operation" value="Multiply">
        <input type="submit" name="operation" value="Divide">
    </form>

    <h3>
        <% 
            String result = (String) request.getAttribute("result");
            if (result != null) { 
        %>
            Result: <%= result %>
        <% 
            } 
        %>
    </h3>
</body>
</html>
```

---

## Step 4: Create the Controller (`CalculatorController.java`)

This servlet receives input, interacts with the model, and forwards data back to the JSP.

```java
package com.example.calculator;

import java.io.IOException;
import javax.servlet.*;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;

@WebServlet("/CalculatorController")
public class CalculatorController extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        double num1 = Double.parseDouble(request.getParameter("num1"));
        double num2 = Double.parseDouble(request.getParameter("num2"));
        String operation = request.getParameter("operation");

        CalculatorModel model = new CalculatorModel();
        model.setNum1(num1);
        model.setNum2(num2);

        switch (operation) {
            case "Add":
                model.add();
                break;
            case "Subtract":
                model.subtract();
                break;
            case "Multiply":
                model.multiply();
                break;
            case "Divide":
                model.divide();
                break;
        }

        String result = String.valueOf(model.getResult());
        request.setAttribute("result", result);
        RequestDispatcher dispatcher = request.getRequestDispatcher("calculator.jsp");
        dispatcher.forward(request, response);
    }
}
```

---

## Step 5: Configure `web.xml` (if not using annotation)

If you didn’t use `@WebServlet`, add this:

```xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" version="3.1">
    <servlet>
        <servlet-name>CalculatorController</servlet-name>
        <servlet-class>com.example.calculator.CalculatorController</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>CalculatorController</servlet-name>
        <url-pattern>/CalculatorController</url-pattern>
    </servlet-mapping>
</web-app>
```

---

## Step 6: Run the Application

1. Right-click on project → **Run As → Run on Server**
2. Choose **Apache Tomcat**
3. Open browser and visit:
   **[http://localhost:8080/CalculatorMVC/calculator.jsp](http://localhost:8080/CalculatorMVC/calculator.jsp)**

---

## Step 7: Test

* Enter numbers and choose an operation.
* The result appears below the form.
* No logic exists in the JSP (view) — all handled by controller + model.

---

Would you like me to extend this with a **Bootstrap-styled calculator interface** for a better look?
