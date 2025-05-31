#Advanced Python Answers

**Q1: What is a decorator in Python?**  
**A1:** A decorator is a function that modifies the behavior of another function or method. It is often used to add functionality to existing code in a clean and readable way.

**Q2: How do you create a generator in Python?**  
**A2:** A generator is created using a function that contains one or more `yield` statements. When called, it returns an iterator that produces values one at a time, allowing for efficient memory usage.

**Q3: What is the purpose of a context manager in Python?**  
**A3:** A context manager is used to manage resources, ensuring that they are properly acquired and released. It is commonly used with the `with` statement to handle file operations and other resource management tasks.

**Q4: How can you handle exceptions in Python?**  
**A4:** Exceptions can be handled using `try` and `except` blocks. You can catch specific exceptions or use a general `except` to handle any exception that may occur.

**Q5: What is the difference between `@staticmethod` and `@classmethod`?**  
**A5:** `@staticmethod` defines a method that does not require access to the instance or class, while `@classmethod` defines a method that receives the class as the first argument and can modify class state.

**Q6: What are metaclasses in Python?**  
**A6:** Metaclasses are classes of classes that define how a class behaves. They allow for customization of class creation and can be used to enforce certain patterns or behaviors in class definitions.

**Q7: How do you implement multiple inheritance in Python?**  
**A7:** Multiple inheritance is implemented by defining a class that inherits from multiple parent classes. Python uses the Method Resolution Order (MRO) to determine the order in which base classes are searched for methods.

**Q8: What is the purpose of the `__init__` method in a class?**  
**A8:** The `__init__` method is a special method called when an instance of a class is created. It is used to initialize the object's attributes and set up any necessary state.

**Q9: How can you create a custom exception in Python?**  
**A9:** A custom exception can be created by defining a new class that inherits from the built-in `Exception` class. You can add custom attributes or methods as needed.

**Q10: What is the Global Interpreter Lock (GIL) in Python?**  
**A10:** The Global Interpreter Lock (GIL) is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecode simultaneously. This can limit the performance of CPU-bound multi-threaded programs.
