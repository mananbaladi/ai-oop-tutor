"""
mermaid_generator.py
Generates Mermaid.js diagram code for OOP concepts.
Streamlit can render these using st.markdown with mermaid support,
or they can be shown as raw code blocks.
"""


def inheritance_diagram(parent: str, children: list) -> str:
    """Generate a Mermaid class inheritance diagram."""
    lines = ["```mermaid", "classDiagram"]
    for child in children:
        lines.append(f"    {parent} <|-- {child}")
    lines.append("```")
    return "\n".join(lines)


def class_diagram(class_name: str, attributes: list, methods: list) -> str:
    """Generate a Mermaid class diagram for a single class."""
    lines = ["```mermaid", "classDiagram", f"    class {class_name} {{"]
    for attr in attributes:
        lines.append(f"        +{attr}")
    for method in methods:
        lines.append(f"        +{method}()")
    lines.append("    }")
    lines.append("```")
    return "\n".join(lines)


def composition_diagram(owner: str, component: str) -> str:
    """Generate a Mermaid composition diagram."""
    return f"""```mermaid
classDiagram
    {owner} *-- {component} : has-a
    class {owner} {{
        +use_{component.lower()}()
    }}
    class {component} {{
        +operate()
    }}
```"""


def full_oop_example() -> str:
    """Generate a complete OOP example diagram."""
    return """```mermaid
classDiagram
    Animal <|-- Dog
    Animal <|-- Cat
    Animal <|-- Bird
    class Animal {
        +String name
        +int age
        +speak()
        +eat()
    }
    class Dog {
        +String breed
        +fetch()
        +speak() bark
    }
    class Cat {
        +String color
        +purr()
        +speak() meow
    }
    class Bird {
        +float wingspan
        +fly()
        +speak() chirp
    }
```"""
