"""
ascii_diagrams.py
Pre-built ASCII diagrams for common OOP concepts.
These are shown as quick-reference visuals in the sidebar.
"""

DIAGRAMS = {
    "class_structure": """
+---------------------------+
|        ClassName          |   <-- Class Name
+---------------------------+
|  - private_attribute      |   <-- Attributes
|  + public_attribute       |       (data/state)
+---------------------------+
|  + public_method()        |   <-- Methods
|  - __private_method()     |       (behavior)
+---------------------------+
""",

    "inheritance": """
         +------------+
         |   Animal   |   <-- Parent / Base Class
         +------------+
         | name       |
         | age        |
         +------------+
         | speak()    |
         | eat()      |
         +------------+
               |
       ________|________
      |                 |
+----------+       +----------+
|   Dog    |       |   Cat    |   <-- Child / Derived Classes
+----------+       +----------+
| breed    |       | color    |
+----------+       +----------+
| fetch()  |       | purr()   |
+----------+       +----------+
""",

    "encapsulation": """
+================================+
|          BankAccount           |
+================================+
|  PRIVATE (hidden from outside) |
|  - __balance = 5000            |
|  - __pin = 1234                |
+================================+
|  PUBLIC (accessible outside)   |
|  + deposit(amount)             |
|  + withdraw(amount)            |
|  + get_balance()               |
+================================+

  Outside World
       |
       |  can ONLY access via
       |  public methods ↑
       |
  [Cannot touch __balance directly!]
""",

    "polymorphism": """
         +----------+
         |  Shape   |
         +----------+
         | area()   |  <-- Same method name
         +----------+
               |
      _________|_________
     |         |         |
+--------+ +--------+ +--------+
| Circle | |  Rect  | |Triangle|
+--------+ +--------+ +--------+
| area() | | area() | | area() |  <-- Different behavior!
+--------+ +--------+ +--------+
 π * r²    l * w    0.5 * b * h
""",

    "abstraction": """
+============================+
|   <<Abstract>>             |
|       Vehicle              |
+============================+
|  + start()   [abstract]    |  <-- Must be implemented
|  + stop()    [abstract]    |      by child classes
|  + refuel()  [concrete]    |  <-- Already implemented
+============================+
         |
    _____|_____
   |           |
+-----+     +----------+
| Car |     | Motorcycle|
+-----+     +----------+
|start()|   |start()   |  <-- Their own implementations
|stop() |   |stop()    |
+-----+     +----------+
""",

    "multiple_inheritance": """
  +-----------+    +-----------+
  |  Flyable  |    | Swimmable |
  +-----------+    +-----------+
  | fly()     |    | swim()    |
  +-----------+    +-----------+
        |                |
        +-------+--------+
                |
          +-----------+
          |   Duck    |   <-- Inherits from BOTH
          +-----------+
          | fly()     |
          | swim()    |
          | quack()   |
          +-----------+
""",

    "composition": """
  INHERITANCE (IS-A relationship):
  Dog IS-A Animal  ✓

       Animal
          ↑
        Dog

  ─────────────────────────────

  COMPOSITION (HAS-A relationship):
  Car HAS-A Engine  ✓

  +-------+       +---------+
  |  Car  |◆----->|  Engine |
  +-------+       +---------+
  | drive()|      | start() |
  +-------+       +---------+
  ◆ = "contains"
"""
}


def get_diagram(name: str) -> str:
    """Return a pre-built ASCII diagram by name."""
    return DIAGRAMS.get(name, "Diagram not found.")


def list_diagrams() -> list:
    """Return all available diagram names."""
    return list(DIAGRAMS.keys())
