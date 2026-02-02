# data.py - Data storage module for the Doubt Resolution System

# Global list to store all questions/doubts
questions_database = []

# Counter to generate unique question IDs
question_id_counter = 0

# Simulated web scraping database - Educational content from various websites
# In real implementation, this would be fetched from actual educational websites
web_scraping_database = {
    "Python": {
        "keywords": {
            "loop": "Web Source: tutorialspoint.com\n→ A loop executes a block of code repeatedly. Python provides 'for' loop (iterates over sequences) and 'while' loop (continues until condition is False). Example: for i in range(5) executes 5 times.",
            "function": "Web Source: w3schools.com\n→ Functions are reusable code blocks defined with 'def' keyword. They can accept parameters and return values. Functions help organize code and avoid repetition.",
            "list": "Web Source: python.org\n→ Lists are ordered, mutable collections defined with square brackets []. They can store multiple items of different types. Common methods: append(), remove(), pop().",
            "dictionary": "Web Source: realpython.com\n→ Dictionaries store key-value pairs using curly braces {}. Keys must be unique and immutable. Access values using dict[key]. Very efficient for lookups.",
            "variable": "Web Source: geeksforgeeks.org\n→ Variables are named references to values in memory. Python uses dynamic typing, so you don't declare types. Example: x = 10 creates an integer variable.",
            "class": "Web Source: python.org\n→ Classes are blueprints for creating objects. Defined with 'class' keyword. They encapsulate data (attributes) and functions (methods) together.",
            "module": "Web Source: docs.python.org\n→ Modules are files containing Python code that can be imported. Use 'import' statement to access their functions and variables.",
        },
        "default": "Web Source: python.org\n→ Python is a high-level, interpreted programming language known for simplicity and readability. Visit python.org for official documentation and tutorials."
    },
    "Mathematics": {
        "keywords": {
            "algebra": "Web Source: khanacademy.org\n→ Algebra uses symbols and letters to represent numbers and quantities in formulas and equations. It involves operations like solving equations, factoring, and working with polynomials.",
            "calculus": "Web Source: mathsisfun.com\n→ Calculus studies continuous change through derivatives (rate of change) and integrals (accumulation). Key concepts: limits, differentiation, and integration.",
            "geometry": "Web Source: mathworld.wolfram.com\n→ Geometry deals with properties and relations of points, lines, surfaces, and solids. Includes concepts like angles, triangles, circles, and area calculations.",
            "trigonometry": "Web Source: khanacademy.org\n→ Trigonometry studies relationships between angles and sides of triangles. Main functions: sin, cos, tan. Used in physics, engineering, and navigation.",
            "matrix": "Web Source: mathsisfun.com\n→ A matrix is a rectangular array of numbers arranged in rows and columns. Used for solving systems of equations and transformations.",
        },
        "default": "Web Source: khanacademy.org\n→ Mathematics is the study of numbers, quantities, structures, and patterns. Practice regularly to improve problem-solving skills."
    },
    "Physics": {
        "keywords": {
            "motion": "Web Source: physicsclassroom.com\n→ Motion is the change in position of an object over time. Described by displacement, velocity (speed with direction), and acceleration (change in velocity).",
            "force": "Web Source: hyperphysics.com\n→ Force is a push or pull that can change an object's motion. Newton's Second Law: F = ma (Force = mass × acceleration). Measured in Newtons.",
            "energy": "Web Source: khanacademy.org\n→ Energy is the capacity to do work. Types include kinetic (motion), potential (position), thermal, and chemical. Law of conservation: energy cannot be created or destroyed.",
            "gravity": "Web Source: nasa.gov\n→ Gravity is the attractive force between objects with mass. On Earth, g = 9.8 m/s². Newton's law: F = G(m1×m2)/r².",
            "velocity": "Web Source: physicsclassroom.com\n→ Velocity is the rate of change of position with respect to time, including direction. It's a vector quantity. Average velocity = displacement/time.",
        },
        "default": "Web Source: physicsclassroom.com\n→ Physics is the study of matter, energy, and their interactions. Understanding fundamental laws helps explain natural phenomena."
    },
    "Chemistry": {
        "keywords": {
            "atom": "Web Source: chemguide.co.uk\n→ An atom is the smallest unit of an element that retains its chemical properties. Contains protons, neutrons (nucleus), and electrons (orbitals).",
            "molecule": "Web Source: chemistry.com\n→ A molecule is formed when two or more atoms bond together chemically. Can be same element (O₂) or different elements (H₂O).",
            "reaction": "Web Source: khanacademy.org\n→ A chemical reaction transforms reactants into products. Involves breaking and forming chemical bonds. Must balance equations to conserve mass.",
            "bond": "Web Source: chemguide.co.uk\n→ Chemical bonds hold atoms together in molecules. Types: ionic (electron transfer), covalent (electron sharing), and metallic bonds.",
            "acid": "Web Source: chemteam.info\n→ An acid is a substance that donates H⁺ ions in solution. Has pH < 7. Examples: HCl, H₂SO₄. Opposite of bases.",
        },
        "default": "Web Source: chemguide.co.uk\n→ Chemistry studies matter's composition, properties, and transformations. Understanding chemical principles is essential for many scientific fields."
    },
    "Data Structures": {
        "keywords": {
            "array": "Web Source: geeksforgeeks.org\n→ An array is a collection of elements stored at contiguous memory locations. Fixed size, same data type. Time complexity: O(1) for access, O(n) for search.",
            "linked list": "Web Source: tutorialspoint.com\n→ A linked list is a linear data structure where elements are stored in nodes. Each node contains data and reference to next node. Dynamic size.",
            "stack": "Web Source: programiz.com\n→ Stack follows LIFO (Last In First Out) principle. Main operations: push (add), pop (remove). Used in recursion, undo features, expression evaluation.",
            "queue": "Web Source: geeksforgeeks.org\n→ Queue follows FIFO (First In First Out) principle. Operations: enqueue (add at rear), dequeue (remove from front). Used in scheduling, BFS.",
            "tree": "Web Source: tutorialspoint.com\n→ A tree is a hierarchical data structure with a root node and child nodes. Binary tree has max 2 children per node. Used in databases, file systems.",
        },
        "default": "Web Source: geeksforgeeks.org\n→ Data structures organize and store data efficiently. Choosing the right structure improves algorithm performance."
    },
    "default": {
        "keywords": {},
        "default": "Web Source: wikipedia.org\n→ Educational content found. Please wait for instructor's verified answer for accurate subject-specific information."
    }
}
