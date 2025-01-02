## Overview

Design patterns are proven, reusable solutions to common problems in software design. They provide a template for solving recurring design challenges, promoting code reusability, scalability, and maintainability.

Originally demonstrated in C++ and Smalltalk, these patterns have since been adapted to languages like C#, Java, Python, and JavaScript. They are widely used in libraries, frameworks, and everyday coding, often without developers even realizing it.

## Categories of Design Patterns

### Creational Design Patterns
Creational patterns simplify object creation by separating the instantiation process from the client code. This makes systems more flexible, scalable, and easier to maintain.

| **Pattern**              | **Description**                                                                                                                                               |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Builder**              | Separate the construction of a complex object from its representation, so that the same construction process can create different representations.             |
| **Factory Method**       | Define an interface for creating an object, but let subclasses alter the type of objects that will be created.                                                 |
| **Abstract Factory**     | Provide an interface for creating families of related or dependent objects without specifying their concrete classes.                                           |
| **Prototype**            | Create new objects by copying an existing object, known as the prototype.                                                                                      |
| **Singleton**            | Ensure a class only has one instance and provide a global point of access to it.                                                                               |

### Structural Design Patterns
Structural Design Patterns deal with how objects and classes are organized to form larger structures, ensuring that they work together efficiently and flexibly.

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
Behavioral Design Patterns focus on how objects communicate and interact with each other, defining the way responsibilities and behaviors are distributed among them.

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
