"""
python_examples.py
Ready-to-run C++ (Dev C++) code examples for all major OOP concepts.
Used as reference snippets shown in the sidebar or on demand.
"""

EXAMPLES = {

    "class_and_object": '''// ── Class & Object ──────────────────────────────
#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    string name;
    int rollNo;

    // Constructor
    Student(string n, int r) {
        name = n;
        rollNo = r;
    }

    void displayInfo() {
        cout << "Name: " << name << ", Roll No: " << rollNo << endl;
    }
};

int main() {
    // Creating objects (instances)
    Student s1("Alice", 101);
    Student s2("Bob", 102);

    s1.displayInfo();   // Name: Alice, Roll No: 101
    s2.displayInfo();   // Name: Bob, Roll No: 102

    return 0;
}
''',

    "encapsulation": '''// ── Encapsulation ───────────────────────────────
#include <iostream>
#include <string>
using namespace std;

class BankAccount {
private:
    double balance;   // private — hidden from outside
    string owner;

public:
    BankAccount(string o, double initial) {
        owner = o;
        balance = initial;
    }

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: " << amount << ". Balance: " << balance << endl;
        }
    }

    void withdraw(double amount) {
        if (amount > balance) {
            cout << "Insufficient funds!" << endl;
        } else {
            balance -= amount;
            cout << "Withdrew: " << amount << ". Balance: " << balance << endl;
        }
    }

    double getBalance() {   // controlled public access
        return balance;
    }
};

int main() {
    BankAccount account("Alice", 1000);
    account.deposit(500);       // Deposited: 500. Balance: 1500
    account.withdraw(200);      // Withdrew: 200. Balance: 1300
    cout << account.getBalance() << endl;  // 1300

    // account.balance = 9999;  // ERROR! private member not accessible

    return 0;
}
''',

    "inheritance": '''// ── Inheritance ─────────────────────────────────
#include <iostream>
#include <string>
using namespace std;

// Base class (Parent)
class Animal {
public:
    string name;
    int age;

    Animal(string n, int a) {
        name = n;
        age = a;
    }

    void eat() {
        cout << name << " is eating." << endl;
    }

    virtual void speak() {   // virtual allows overriding
        cout << name << " makes a sound." << endl;
    }
};

// Derived class (Child)
class Dog : public Animal {
public:
    string breed;

    Dog(string n, int a, string b) : Animal(n, a) {
        breed = b;
    }

    void speak() override {   // override parent method
        cout << name << " says: Woof! " << endl;
    }

    void fetch() {
        cout << name << " fetches the ball!" << endl;
    }
};

class Cat : public Animal {
public:
    Cat(string n, int a) : Animal(n, a) {}

    void speak() override {
        cout << name << " says: Meow!" << endl;
    }
};

int main() {
    Dog dog("Rex", 3, "Labrador");
    Cat cat("Whiskers", 2);

    dog.speak();    // Rex says: Woof!
    dog.eat();      // Rex is eating. (inherited)
    dog.fetch();    // Rex fetches the ball!
    cat.speak();    // Whiskers says: Meow!

    return 0;
}
''',

    "polymorphism": '''// ── Polymorphism ────────────────────────────────
#include <iostream>
#include <cmath>
using namespace std;

// Base class
class Shape {
public:
    virtual double area() = 0;   // pure virtual function

    void describe() {
        cout << "Area = " << area() << endl;
    }
};

class Circle : public Shape {
private:
    double radius;
public:
    Circle(double r) { radius = r; }

    double area() override {
        return 3.14159 * radius * radius;
    }
};

class Rectangle : public Shape {
private:
    double width, height;
public:
    Rectangle(double w, double h) {
        width = w;
        height = h;
    }

    double area() override {
        return width * height;
    }
};

class Triangle : public Shape {
private:
    double base, height;
public:
    Triangle(double b, double h) {
        base = b;
        height = h;
    }

    double area() override {
        return 0.5 * base * height;
    }
};

int main() {
    // Polymorphism — same interface, different behavior
    Shape* shapes[3];
    shapes[0] = new Circle(5);
    shapes[1] = new Rectangle(4, 6);
    shapes[2] = new Triangle(3, 8);

    for (int i = 0; i < 3; i++) {
        shapes[i]->describe();
    }

    return 0;
}
''',

    "abstraction": '''// ── Abstraction ─────────────────────────────────
#include <iostream>
#include <string>
using namespace std;

// Abstract base class (has at least one pure virtual function)
class Vehicle {
protected:
    string brand;

public:
    Vehicle(string b) { brand = b; }

    // Pure virtual functions — MUST be implemented by child classes
    virtual void start() = 0;
    virtual void stop() = 0;

    // Concrete method — shared by all vehicles
    void refuel() {
        cout << brand << " is being refueled." << endl;
    }
};

class Car : public Vehicle {
public:
    Car(string b) : Vehicle(b) {}

    void start() override {
        cout << brand << " car: Turn key -> Engine starts!" << endl;
    }

    void stop() override {
        cout << brand << " car: Press brake -> Engine stops." << endl;
    }
};

class Motorcycle : public Vehicle {
public:
    Motorcycle(string b) : Vehicle(b) {}

    void start() override {
        cout << brand << " bike: Kick start -> Vroom!" << endl;
    }

    void stop() override {
        cout << brand << " bike: Pull brake -> Stops." << endl;
    }
};

int main() {
    // Vehicle v("X");  // ERROR! Cannot instantiate abstract class

    Car car("Toyota");
    Motorcycle bike("Honda");

    car.start();
    car.refuel();
    bike.start();
    bike.stop();

    return 0;
}
''',

    "constructor_destructor": '''// ── Constructor & Destructor ─────────────────────
#include <iostream>
#include <string>
using namespace std;

class Student {
private:
    string name;
    int* marks;     // dynamic memory
    int numSubjects;

public:
    // Default constructor
    Student() {
        name = "Unknown";
        numSubjects = 0;
        marks = nullptr;
        cout << "Default constructor called." << endl;
    }

    // Parameterized constructor
    Student(string n, int subjects) {
        name = n;
        numSubjects = subjects;
        marks = new int[numSubjects];  // allocate memory
        cout << "Parameterized constructor called for " << name << endl;
    }

    // Copy constructor
    Student(const Student& other) {
        name = other.name;
        numSubjects = other.numSubjects;
        marks = new int[numSubjects];
        for (int i = 0; i < numSubjects; i++) {
            marks[i] = other.marks[i];
        }
        cout << "Copy constructor called." << endl;
    }

    void setMark(int subject, int mark) {
        marks[subject] = mark;
    }

    void display() {
        cout << "Student: " << name << endl;
    }

    // Destructor — frees memory
    ~Student() {
        delete[] marks;   // release dynamic memory
        cout << "Destructor called for " << name << endl;
    }
};

int main() {
    Student s1("Alice", 3);
    s1.setMark(0, 90);
    s1.setMark(1, 85);
    s1.display();

    Student s2 = s1;   // copy constructor
    s2.display();

    return 0;
}   // destructors called automatically here
''',

    "multiple_inheritance": '''// ── Multiple Inheritance ────────────────────────
#include <iostream>
using namespace std;

class Flyable {
public:
    void fly() {
        cout << "I can fly!" << endl;
    }
};

class Swimmable {
public:
    void swim() {
        cout << "I can swim!" << endl;
    }
};

// Duck inherits from BOTH Flyable and Swimmable
class Duck : public Flyable, public Swimmable {
public:
    string name;

    Duck(string n) { name = n; }

    void quack() {
        cout << name << " says: Quack!" << endl;
    }
};

int main() {
    Duck duck("Donald");

    duck.fly();     // from Flyable
    duck.swim();    // from Swimmable
    duck.quack();   // Duck's own method

    return 0;
}
''',

}


def get_example(topic: str) -> str:
    """Return a C++ code example by topic key."""
    return EXAMPLES.get(topic, "// Example not found for this topic.")


def list_examples() -> list:
    """Return all available example topic keys."""
    return list(EXAMPLES.keys())


def format_topic_name(key: str) -> str:
    """Convert snake_case key to Title Case display name."""
    return key.replace("_", " ").title()
