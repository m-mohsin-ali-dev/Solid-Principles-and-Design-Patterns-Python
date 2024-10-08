# SOLID Principles and Design Patterns

This repository showcases practical implementations of **SOLID principles** and various **Design Patterns** in **Python**. 

## What Are Design Patterns?

Design patterns offer reusable solutions to common programming problems. They were popularized in 1994 by the Gang of Four (GoF) in their book *Design Patterns: Elements of Reusable Object-Oriented Software*.

Originally demonstrated in C++ and Smalltalk, these patterns have since been adapted to languages like C#, Java, Python, and JavaScript. They are widely used in libraries, frameworks, and everyday coding, often without developers even realizing it.

This repository covers all the major **SOLID design principles** and **GoF design patterns**.

## The Appeal of Design Patterns: ##

**Reduced Development Time:** Leverage existing solutions, saving time and effort for common challenges.

**Improved Code Quality:** Promote well-structured, modular, and easier-to-understand code.

**Enhanced Maintainability:** Facilitate code modification and expansion in the future.

**Increased Reusability:** Make code components more adaptable and reusable across projects.

## SOLID Design Principles

| **Principle**                           | **Description**                                                                                                                               |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Single Responsibility Principle (SRP)** | Each class should have one, and only one, reason to change.                                                                                    |
| **Open-Closed Principle (OCP)**          | Software entities should be open for extension, but closed for modification.                                                                  |
| **Liskov Substitution Principle (LSP)**  | Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.                     |
| **Interface Segregation Principle (ISP)**| No client should be forced to depend on methods it does not use.                                                                               |
| **Dependency Inversion Principle (DIP)** | High-level modules should not depend on low-level modules. Both should depend on abstractions.                                                 |


## Design Patterns  

### Creational Design Patterns

| **Pattern**              | **Description**                                                                                                                                               |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Builder**              | Separate the construction of a complex object from its representation, so that the same construction process can create different representations.             |
| **Factory Method**       | Define an interface for creating an object, but let subclasses alter the type of objects that will be created.                                                 |
| **Abstract Factory**     | Provide an interface for creating families of related or dependent objects without specifying their concrete classes.                                           |
| **Prototype**            | Create new objects by copying an existing object, known as the prototype.                                                                                      |
| **Singleton**            | Ensure a class only has one instance and provide a global point of access to it.                                                                               |

### Structural Design Patterns

| **Pattern**             | **Description**                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| **Adapter**             | Allow objects with incompatible interfaces to collaborate.                                                                  |
| **Bridge**              | Decouple an abstraction from its implementation so that the two can vary independently.                                      |
| **Composite**           | Compose objects into tree structures to represent part-whole hierarchies.                                                    |
| **Decorator**           | Attach additional responsibilities to an object dynamically.                                                                |
| **Facade**              | Provide a simplified interface to a complex subsystem.                                                                      |
| **Flyweight**           | Minimize memory usage by sharing as much data as possible with similar objects.                                              |
| **Proxy**               | Provide a surrogate or placeholder for another object to control access to it.                                               |

### Behavioral Design Patterns

| **Pattern**                    | **Description**                                                                                                                                         |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Chain of Responsibility**    | Pass requests along a chain of handlers until one of them handles the request.                                                                        |
| **Command**                    | Encapsulate a request as an object, allowing users to parameterize clients with queues, requests, and operations.                                      |
| **Interpreter**                | Given a language, define a representation for its grammar and an interpreter that uses this representation to interpret sentences in the language.     |
| **Iterator**                   | Provide a way to access elements of a collection sequentially without exposing its underlying representation.                                            |
| **Mediator**                   | Define an object that encapsulates how a set of objects interact.                                                                                      |
| **Memento**                    | Capture and externalize an object's internal state so it can be restored later.                                                                        |
| **Observer**                   | Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.                                 |
| **State**                      | Allow an object to alter its behavior when its internal state changes.                                                                                 |
| **Strategy**                   | Define a family of algorithms, encapsulate each one, and make them interchangeable.                                                                    |
| **Template Method**            | Define the skeleton of an algorithm in a method, deferring some steps to subclasses.                                                                   |
| **Visitor**                    | Represent an operation to be performed on elements of an object structure, allowing new operations to be defined without changing the classes on which they operate. |

---

## How to Use This Repository

Each design pattern and SOLID principle is organized into its own folder, containing:

- A brief explanation of the concept
- Code examples illustrating the pattern or principle
- When and why you should use it

Feel free to explore the examples, run the code, and adapt it to your own projects!

## Contributing

Feel free to contribute by submitting pull requests for enhancements, bug fixes, or implementations of additional design patterns. Let's learn and build together!


---

## License

This repository is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for more details.

---

Happy coding! 🎉

