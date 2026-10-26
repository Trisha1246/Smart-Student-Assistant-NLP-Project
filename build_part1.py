# Part 1: Subjects 1-10 (Python, Java, DBMS, Data Structures, Computer Networks,
# Operating Systems, Artificial Intelligence, Machine Learning, Software Engineering, Cyber Security)

PART1_DATA = {
    "Python": {
        "Basics & Syntax": [
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "def", "func", "define"],
                "answer": 1,
                "explanation": "In Python, functions are defined using the 'def' keyword followed by the function name and parentheses.",
                "difficulty": "beginner"
            },
            {
                "question": "Which data type represents immutable sequences of arbitrary objects in Python?",
                "options": ["list", "set", "tuple", "dictionary"],
                "answer": 2,
                "explanation": "A tuple is an ordered, immutable collection of elements in Python.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the output of print(type([])) in Python 3?",
                "options": ["<class 'array'>", "<class 'list'>", "<class 'tuple'>", "<class 'dict'>"],
                "answer": 1,
                "explanation": "Square brackets [] instantiate a list object in Python.",
                "difficulty": "beginner"
            },
            {
                "question": "Which operator is used for floor division in Python?",
                "options": ["/", "//", "%", "**"],
                "answer": 1,
                "explanation": "The '//' operator performs floor division, returning the largest integer less than or equal to the quotient.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the default return value of a Python function that does not contain a return statement?",
                "options": ["0", "False", "None", "void"],
                "answer": 2,
                "explanation": "Python functions implicitly return None if no explicit return statement is executed.",
                "difficulty": "beginner"
            },
            {
                "question": "How are variable scopes resolved in Python (order of lookup)?",
                "options": ["Global, Local, Enclosing, Built-in", "Local, Enclosing, Global, Built-in (LEGB)", "Built-in, Global, Enclosing, Local", "Local, Global, Enclosing, System"],
                "answer": 1,
                "explanation": "Python resolves identifiers using the LEGB rule: Local, Enclosing, Global, and Built-in scopes.",
                "difficulty": "intermediate"
            }
        ],
        "OOP & Data Structures": [
            {
                "question": "What method represents the constructor in a Python class?",
                "options": ["__start__()", "__init__()", "__new__()", "__create__()"],
                "answer": 1,
                "explanation": "The '__init__' method initializes attributes when a new instance of a class is created.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which built-in function or keyword is used to access the parent class method?",
                "options": ["parent()", "this()", "super()", "base()"],
                "answer": 2,
                "explanation": "super() returns a proxy object that delegates method calls to a parent or sibling class.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the time complexity of looking up a key in an average Python dictionary?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"],
                "answer": 0,
                "explanation": "Python dictionaries are implemented as hash tables, providing average O(1) time complexity for lookups.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which special method is invoked by the built-in len() function?",
                "options": ["__size__()", "__count__()", "__len__()", "__length__()"],
                "answer": 2,
                "explanation": "The len() function invokes the __len__() dunder method implemented by the object's class.",
                "difficulty": "intermediate"
            },
            {
                "question": "What happens when you use a mutable object (like a list) as a default parameter in a function?",
                "options": [
                    "A new list is created every time the function is called",
                    "The same list instance is shared across all function calls",
                    "Python raises a SyntaxError at compile time",
                    "The list is automatically converted into an immutable tuple"
                ],
                "answer": 1,
                "explanation": "Default argument values in Python are evaluated once when the function definition is executed, sharing mutable objects across calls.",
                "difficulty": "advanced"
            }
        ],
        "Advanced Python & Internals": [
            {
                "question": "What keyword turns a normal function into a generator iterator?",
                "options": ["return", "yield", "generate", "produce"],
                "answer": 1,
                "explanation": "'yield' pauses function execution and returns a generator iterator value without destroying local state.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the primary role of the Python Global Interpreter Lock (GIL)?",
                "options": [
                    "To speed up multi-core processing",
                    "To prevent concurrent native thread execution for thread-safe CPython memory management",
                    "To compile bytecode directly into native machine code",
                    "To manage garbage collection cycles automatically"
                ],
                "answer": 1,
                "explanation": "GIL is a mutex protecting access to Python objects, preventing multiple native threads from executing bytecodes concurrently.",
                "difficulty": "advanced"
            },
            {
                "question": "Which module provides high-performance container alternatives to Python's general-purpose dict, list, set, and tuple?",
                "options": ["itertools", "collections", "functools", "structures"],
                "answer": 1,
                "explanation": "The 'collections' module includes namedtuple, deque, Counter, OrderedDict, and defaultdict.",
                "difficulty": "intermediate"
            },
            {
                "question": "What does the @property decorator do in a Python class?",
                "options": [
                    "Declares a class-level static attribute",
                    "Defines a method that can be accessed like an attribute getter",
                    "Makes the class immutable",
                    "Automatically serializes the class attributes to JSON"
                ],
                "answer": 1,
                "explanation": "The @property decorator allows a method to be accessed as an attribute, enabling custom getter and setter logic.",
                "difficulty": "advanced"
            },
            {
                "question": "How does Python's memory manager handle circular references between objects?",
                "options": [
                    "Circular references cause permanent memory leaks",
                    "Through a cyclic garbage collector using generational reference tracking",
                    "By immediately converting them to weak references",
                    "By deleting both objects when reference count drops below 2"
                ],
                "answer": 1,
                "explanation": "CPython supplements reference counting with a generational cyclic garbage collector to detect and collect circular reference islands.",
                "difficulty": "advanced"
            }
        ]
    },

    "Java": {
        "Core Java & Syntax": [
            {
                "question": "Which of these is NOT a primitive data type in Java?",
                "options": ["int", "boolean", "String", "char"],
                "answer": 2,
                "explanation": "String is a class (reference type), whereas int, boolean, and char are primitive types.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the size of an int data type in Java?",
                "options": ["16 bits", "32 bits", "64 bits", "Depends on OS architecture"],
                "answer": 1,
                "explanation": "Java int is platform-independent and always 32 bits (4 bytes).",
                "difficulty": "beginner"
            },
            {
                "question": "Which method signature serves as the exact entry point for a standard Java application?",
                "options": [
                    "public void main(String args[])",
                    "public static void main(String[] args)",
                    "static void main(String args)",
                    "public static int main(String[] args)"
                ],
                "answer": 1,
                "explanation": "The JVM looks for 'public static void main(String[] args)' to launch standalone Java programs.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the default value of a boolean instance variable in a Java class?",
                "options": ["true", "false", "null", "0"],
                "answer": 1,
                "explanation": "Uninitialized boolean instance variables default to false in Java.",
                "difficulty": "beginner"
            },
            {
                "question": "Which operator is used to compare whether two object references refer to the same memory location?",
                "options": ["equals()", "==", "===", "compareTo()"],
                "answer": 1,
                "explanation": "The '==' operator checks reference equality (identity), whereas equals() compares contents.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which package is automatically imported into every Java compilation unit?",
                "options": ["java.util", "java.io", "java.lang", "java.net"],
                "answer": 2,
                "explanation": "The java.lang package contains core classes (Object, System, String) and is implicitly imported.",
                "difficulty": "beginner"
            }
        ],
        "OOP & Inheritance": [
            {
                "question": "Which keyword prevents a class from being inherited in Java?",
                "options": ["static", "final", "abstract", "const"],
                "answer": 1,
                "explanation": "A 'final' class cannot be subclassed or extended.",
                "difficulty": "intermediate"
            },
            {
                "question": "Can Java achieve multiple inheritance through classes?",
                "options": [
                    "Yes, using the 'extends' keyword with multiple class names",
                    "No, only via interfaces to avoid ambiguity (the diamond problem)",
                    "Yes, using the 'implements' keyword with classes",
                    "Only with abstract classes"
                ],
                "answer": 1,
                "explanation": "Java disallows multiple class inheritance to avoid the diamond problem; interfaces are used instead.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which method of the Object class is called by the garbage collector before an object is reclaimed?",
                "options": ["destroy()", "finalize()", "dispose()", "clean()"],
                "answer": 1,
                "explanation": "The finalize() method was invoked by GC prior to reclaiming memory (deprecated in newer Java versions).",
                "difficulty": "intermediate"
            },
            {
                "question": "Which concept allows a subclass to provide a specific implementation of a method already declared in its parent class?",
                "options": ["Method Overloading", "Method Overriding", "Method Encapsulation", "Method Hiding"],
                "answer": 1,
                "explanation": "Method Overriding occurs when a subclass defines a method with the same signature and return type as in its superclass.",
                "difficulty": "beginner"
            },
            {
                "question": "Can an abstract class in Java have constructors?",
                "options": [
                    "No, abstract classes cannot have constructors",
                    "Yes, called during subclass instantiation via super()",
                    "Only private constructors",
                    "Only static constructors"
                ],
                "answer": 1,
                "explanation": "Abstract classes can have constructors, which are invoked when concrete subclasses are instantiated.",
                "difficulty": "intermediate"
            }
        ],
        "Collections, JVM & Multithreading": [
            {
                "question": "Where are objects allocated memory in Java runtime?",
                "options": ["Stack Memory", "Heap Memory", "Class Area", "Native Method Stack"],
                "answer": 1,
                "explanation": "All Java objects and arrays are dynamically allocated on the Heap memory.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which Collection interface does NOT allow duplicate elements?",
                "options": ["List", "Queue", "Set", "Vector"],
                "answer": 2,
                "explanation": "The Set interface (implemented by HashSet, TreeSet) models mathematical sets with no duplicates.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the difference between HashMap and Hashtable in Java?",
                "options": [
                    "HashMap is synchronized, Hashtable is not",
                    "Hashtable is synchronized and thread-safe; HashMap is non-synchronized and allows one null key",
                    "HashMap does not use hashing",
                    "Hashtable has O(1) operations while HashMap is O(n)"
                ],
                "answer": 1,
                "explanation": "Hashtable is synchronized and legacy; HashMap is unsynchronized, faster, and permits null keys.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which keyword ensures that changes to a variable are immediately visible to all threads?",
                "options": ["synchronized", "volatile", "transient", "atomic"],
                "answer": 1,
                "explanation": "The 'volatile' keyword forces reads and writes to go directly to main memory rather than thread CPU caches.",
                "difficulty": "advanced"
            },
            {
                "question": "What state does a Java thread enter when it invokes Thread.sleep()?",
                "options": ["RUNNABLE", "TIMED_WAITING", "BLOCKED", "TERMINATED"],
                "answer": 1,
                "explanation": "Invoking Thread.sleep(ms) transitions the thread into the TIMED_WAITING state.",
                "difficulty": "advanced"
            }
        ]
    },

    "DBMS": {
        "SQL & Queries": [
            {
                "question": "Which SQL command is used to retrieve data from a database?",
                "options": ["GET", "FETCH", "SELECT", "RETRIEVE"],
                "answer": 2,
                "explanation": "SELECT is the fundamental DQL (Data Query Language) statement in SQL.",
                "difficulty": "beginner"
            },
            {
                "question": "Which clause is used to filter records in a grouped SQL query?",
                "options": ["WHERE", "HAVING", "GROUP BY", "ORDER BY"],
                "answer": 1,
                "explanation": "HAVING filters groups created by GROUP BY, while WHERE filters individual rows before grouping.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which SQL constraint ensures that all values in a column are distinct and not null?",
                "options": ["UNIQUE", "PRIMARY KEY", "CHECK", "FOREIGN KEY"],
                "answer": 1,
                "explanation": "A PRIMARY KEY uniquely identifies each record and enforces both uniqueness and non-null values.",
                "difficulty": "beginner"
            },
            {
                "question": "Which JOIN returns all records from the left table and matching records from the right table?",
                "options": ["INNER JOIN", "LEFT OUTER JOIN", "RIGHT OUTER JOIN", "FULL OUTER JOIN"],
                "answer": 1,
                "explanation": "LEFT OUTER JOIN returns all rows from the left table, with nulls for non-matching right table rows.",
                "difficulty": "beginner"
            },
            {
                "question": "Which SQL command is classified under Data Definition Language (DDL)?",
                "options": ["INSERT", "UPDATE", "ALTER", "DELETE"],
                "answer": 2,
                "explanation": "ALTER modifies the structure of database schemas, making it a DDL command.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the effect of the SQL TRUNCATE TABLE command compared to DELETE?",
                "options": [
                    "TRUNCATE deletes row by row with rollbacks; DELETE removes the entire schema",
                    "TRUNCATE is a DDL operation that resets high water mark and is faster than DELETE without logging individual row deletions",
                    "TRUNCATE only deletes table constraints",
                    "TRUNCATE requires a WHERE clause"
                ],
                "answer": 1,
                "explanation": "TRUNCATE deallocates data pages directly without row-by-row transaction logs, making it faster than DELETE.",
                "difficulty": "intermediate"
            }
        ],
        "Normalization & Schema Design": [
            {
                "question": "A table is in First Normal Form (1NF) if and only if:",
                "options": [
                    "It has no transitive dependencies",
                    "Every attribute contains only atomic (indivisible) values",
                    "All non-key attributes depend on the entire primary key",
                    "There are no foreign keys"
                ],
                "answer": 1,
                "explanation": "1NF requires that table attributes hold atomic values and no repeating groups exist.",
                "difficulty": "beginner"
            },
            {
                "question": "A table is in Second Normal Form (2NF) if it is in 1NF and contains no:",
                "options": ["Transitive dependency", "Partial dependency", "Multivalued dependency", "Join dependency"],
                "answer": 1,
                "explanation": "2NF requires eliminating partial dependencies where a non-prime attribute depends on part of a composite candidate key.",
                "difficulty": "intermediate"
            },
            {
                "question": "Boyce-Codd Normal Form (BCNF) requires that for every non-trivial functional dependency X -> Y:",
                "options": ["Y must be a prime attribute", "X must be a super key", "X must be atomic", "Y must not be null"],
                "answer": 1,
                "explanation": "BCNF is a stricter 3NF where every determinant X must be a super key.",
                "difficulty": "advanced"
            },
            {
                "question": "What type of dependency is eliminated when progressing from 2NF to 3NF?",
                "options": ["Partial functional dependency", "Transitive dependency", "Join dependency", "Multivalued dependency"],
                "answer": 1,
                "explanation": "3NF removes transitive dependencies where non-prime attributes determine other non-prime attributes.",
                "difficulty": "intermediate"
            },
            {
                "question": "In an Entity-Relationship (ER) model, how is a weak entity set represented?",
                "options": ["Single rectangle", "Double rectangle", "Diamond", "Double ellipse"],
                "answer": 1,
                "explanation": "In standard Chen ER notation, a weak entity set is represented by a double rectangle.",
                "difficulty": "beginner"
            }
        ],
        "Transactions, Indexing & ACID": [
            {
                "question": "What does the 'I' in ACID transaction properties stand for?",
                "options": ["Integrity", "Isolation", "Index", "Immutability"],
                "answer": 1,
                "explanation": "Isolation ensures concurrent transaction execution leaves the database in the same state as serial execution.",
                "difficulty": "beginner"
            },
            {
                "question": "Which data structure is most commonly used for database table indexing on disk?",
                "options": ["Binary Search Tree", "B+ Tree", "Skip List", "Splay Tree"],
                "answer": 1,
                "explanation": "B+ Trees have high fan-out, shallow depth, and linked leaf nodes, making them ideal for disk-based range and point queries.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which isolation level prevents Dirty Reads but still permits Non-Repeatable Reads?",
                "options": ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
                "answer": 1,
                "explanation": "Read Committed ensures only committed data is visible, preventing dirty reads while still allowing non-repeatable reads.",
                "difficulty": "advanced"
            },
            {
                "question": "What protocol is widely used in DBMS to guarantee Conflict Serializability?",
                "options": ["Two-Phase Locking (2PL)", "Two-Phase Commit (2PC)", "Checkpoint Protocol", "Sliding Window Protocol"],
                "answer": 0,
                "explanation": "Strict Two-Phase Locking (Growing phase followed by Shrinking phase) guarantees conflict-serializable schedules.",
                "difficulty": "advanced"
            },
            {
                "question": "What mechanism does DBMS use to ensure Durability and crash recovery?",
                "options": ["Memory cache snapshots", "Write-Ahead Logging (WAL) and checkpoints", "Shadow table duplicates", "Client transaction mirrors"],
                "answer": 1,
                "explanation": "WAL logs modifications to disk before applying them to database pages, ensuring recovery after power failure.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Data Structures": {
        "Linear Data Structures": [
            {
                "question": "Which data structure follows the LIFO (Last In First Out) principle?",
                "options": ["Queue", "Stack", "Array", "Linked List"],
                "answer": 1,
                "explanation": "A Stack operates on LIFO order where the last pushed element is popped first.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the worst-case search time complexity in an unsorted singly linked list of size n?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"],
                "answer": 2,
                "explanation": "In a singly linked list, locating an item requires sequential traversal of up to n nodes (O(n)).",
                "difficulty": "beginner"
            },
            {
                "question": "Which data structure is ideal for implementing a First-In-First-Out (FIFO) queue efficiently?",
                "options": ["Array with linear shifting", "Circular Buffer / Doubly Linked List", "Binary Search Tree", "Stack without pointers"],
                "answer": 1,
                "explanation": "A circular array or linked list provides O(1) enqueue and dequeue operations without shifting elements.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the time complexity to insert a node at the head of a singly linked list?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n log n)"],
                "answer": 0,
                "explanation": "Inserting at the head merely updates the new node's next pointer and head reference, requiring O(1) time.",
                "difficulty": "beginner"
            },
            {
                "question": "Which data structure is utilized by CPU recursion and expression evaluation (postfix)?",
                "options": ["Queue", "Stack", "Priority Queue", "Deque"],
                "answer": 1,
                "explanation": "Call stacks and postfix expression parsing natively rely on the LIFO property of Stacks.",
                "difficulty": "intermediate"
            },
            {
                "question": "How do you detect a cycle in a linked list in O(n) time and O(1) extra space?",
                "options": ["Hash Set of visited nodes", "Floyd's Tortoise and Hare algorithm", "Breadth-First Search", "Binary search"],
                "answer": 1,
                "explanation": "Floyd's algorithm uses two pointers moving at different speeds (1 step and 2 steps) to detect loops in O(1) space.",
                "difficulty": "intermediate"
            }
        ],
        "Trees & Binary Search Trees": [
            {
                "question": "What is the height of a balanced binary search tree with n nodes?",
                "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
                "answer": 1,
                "explanation": "Balanced trees (like AVL and Red-Black trees) maintain logarithmic height O(log n).",
                "difficulty": "intermediate"
            },
            {
                "question": "Which tree traversal of a Binary Search Tree (BST) visits nodes in strictly ascending sorted order?",
                "options": ["Preorder traversal", "Inorder traversal", "Postorder traversal", "Level-order traversal"],
                "answer": 1,
                "explanation": "Inorder traversal visits Left subtree, Root, then Right subtree, producing ascending values for a BST.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the maximum balance factor allowed for any node in an AVL tree?",
                "options": ["0", "1 (i.e. -1, 0, or +1)", "2", "log(n)"],
                "answer": 1,
                "explanation": "An AVL tree maintains height balance such that the difference between left and right subtree heights is at most 1.",
                "difficulty": "intermediate"
            },
            {
                "question": "In a Min-Heap of n elements, where is the minimum value always located?",
                "options": ["At the leaf nodes", "At the root node", "At index n-1", "At index n/2"],
                "answer": 1,
                "explanation": "In a Min-Heap, the root element satisfies heap property and always holds the smallest element (index 0).",
                "difficulty": "beginner"
            },
            {
                "question": "What is the time complexity to insert an element into a binary heap of size n?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
                "answer": 1,
                "explanation": "Insertion appends at the bottom and bubbles up along the tree height, taking O(log n) time.",
                "difficulty": "intermediate"
            }
        ],
        "Graphs, Hashing & Sorting": [
            {
                "question": "Which algorithm finds the single-source shortest path in a weighted graph with non-negative edge weights?",
                "options": ["Prim's algorithm", "Kruskal's algorithm", "Dijkstra's algorithm", "Floyd-Warshall"],
                "answer": 2,
                "explanation": "Dijkstra's algorithm greedily determines single-source shortest paths in non-negative weighted graphs.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the average and worst-case time complexity of QuickSort?",
                "options": [
                    "Average: O(n log n), Worst-case: O(n^2)",
                    "Average: O(n), Worst-case: O(n log n)",
                    "Average: O(n^2), Worst-case: O(n^2)",
                    "Average: O(n log n), Worst-case: O(n log n)"
                ],
                "answer": 0,
                "explanation": "QuickSort averages O(n log n), but degrades to O(n^2) when poor pivots are chosen repeatedly.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which collision resolution technique in hash tables chains elements with identical hash keys into a linked list?",
                "options": ["Linear Probing", "Separate Chaining", "Quadratic Probing", "Double Hashing"],
                "answer": 1,
                "explanation": "Separate Chaining maintains an auxiliary linked list (or tree) at each bucket for colliding keys.",
                "difficulty": "beginner"
            },
            {
                "question": "Which graph algorithm determines a Minimum Spanning Tree by sorting all edges by weight?",
                "options": ["Dijkstra's algorithm", "Bellman-Ford", "Kruskal's algorithm", "Tarjan's algorithm"],
                "answer": 2,
                "explanation": "Kruskal's algorithm sorts edges by weight and adds them using Disjoint Set Union (DSU) to avoid cycles.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the worst-case time complexity of MergeSort?",
                "options": ["O(n)", "O(n log n)", "O(n^2)", "O(2^n)"],
                "answer": 1,
                "explanation": "MergeSort recursively divides in halves and merges in linear time, guaranteeing O(n log n) in all cases.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Computer Networks": {
        "OSI & TCP/IP Reference Models": [
            {
                "question": "Which layer of the OSI model is responsible for end-to-end reliability, flow control, and segmentation?",
                "options": ["Network Layer", "Transport Layer", "Data Link Layer", "Session Layer"],
                "answer": 1,
                "explanation": "The Transport Layer (Layer 4, TCP/UDP) manages end-to-end communication, segmentation, and error checking.",
                "difficulty": "beginner"
            },
            {
                "question": "What protocol translates human-readable domain names (e.g. google.com) into numerical IP addresses?",
                "options": ["DHCP", "DNS", "ARP", "NAT"],
                "answer": 1,
                "explanation": "DNS (Domain Name System) maps hostnames to IP addresses over port 53.",
                "difficulty": "beginner"
            },
            {
                "question": "Which protocol resolves a known IP address to a physical MAC address on a local area network?",
                "options": ["RARP", "ARP", "ICMP", "IGMP"],
                "answer": 1,
                "explanation": "Address Resolution Protocol (ARP) broadcasts to discover MAC addresses associated with IP addresses.",
                "difficulty": "intermediate"
            },
            {
                "question": "How many layers are defined in the standard ISO-OSI reference model?",
                "options": ["4", "5", "7", "8"],
                "answer": 2,
                "explanation": "OSI has 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application.",
                "difficulty": "beginner"
            },
            {
                "question": "At which layer of the OSI model do network switches primarily operate?",
                "options": ["Physical (Layer 1)", "Data Link (Layer 2)", "Network (Layer 3)", "Transport (Layer 4)"],
                "answer": 1,
                "explanation": "Standard Ethernet switches examine Layer 2 MAC addresses to forward frames to correct ports.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the size of an IPv4 address versus an IPv6 address?",
                "options": ["32 bits vs 64 bits", "32 bits vs 128 bits", "64 bits vs 128 bits", "16 bits vs 32 bits"],
                "answer": 1,
                "explanation": "IPv4 uses 32-bit addresses (approx 4.3 billion), while IPv6 uses 128-bit addresses.",
                "difficulty": "beginner"
            }
        ],
        "Network Layer & Routing Protocols": [
            {
                "question": "Which protocol provides reliable, connection-oriented byte stream transmission with congestion control?",
                "options": ["UDP", "TCP", "ICMP", "IGMP"],
                "answer": 1,
                "explanation": "TCP establishes connections via a 3-way handshake and guarantees packet ordering and delivery.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the standard port number for secure HTTPS communication?",
                "options": ["80", "443", "8080", "22"],
                "answer": 1,
                "explanation": "Port 443 is assigned for HTTPS (HTTP encrypted over TLS/SSL).",
                "difficulty": "beginner"
            },
            {
                "question": "Which routing algorithm is used by the Open Shortest Path First (OSPF) protocol?",
                "options": ["Bellman-Ford Distance Vector", "Dijkstra's Link-State Algorithm", "Flooding", "Random Walk"],
                "answer": 1,
                "explanation": "OSPF is a link-state routing protocol that utilizes Dijkstra's algorithm to compute shortest paths.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the purpose of the TTL (Time to Live) field in an IPv4 packet header?",
                "options": [
                    "To measure connection speed",
                    "To prevent packets from looping endlessly in routing loops",
                    "To calculate encryption keys",
                    "To set TCP window size"
                ],
                "answer": 1,
                "explanation": "TTL decrements at each hop; when it reaches zero, the packet is discarded and an ICMP message returned.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which protocol dynamically assigns IP addresses, subnet masks, and default gateways to host devices?",
                "options": ["DNS", "DHCP", "SNMP", "BGP"],
                "answer": 1,
                "explanation": "DHCP (Dynamic Host Configuration Protocol) automates host network configuration.",
                "difficulty": "beginner"
            }
        ],
        "Transport Layer & Application Protocols": [
            {
                "question": "How many packets are exchanged in the standard TCP connection establishment handshake?",
                "options": ["2 (SYN, ACK)", "3 (SYN, SYN-ACK, ACK)", "4 (SYN, SYN, ACK, ACK)", "1 (SYN)"],
                "answer": 1,
                "explanation": "TCP uses a three-way handshake: SYN from client, SYN-ACK from server, and ACK from client.",
                "difficulty": "beginner"
            },
            {
                "question": "Which transport protocol is best suited for real-time video streaming and DNS queries due to low latency?",
                "options": ["TCP", "UDP", "SCTP", "FTP"],
                "answer": 1,
                "explanation": "UDP has minimal header overhead and no handshake or retransmission delays, making it ideal for real-time media.",
                "difficulty": "beginner"
            },
            {
                "question": "What mechanism does TCP use to prevent a sender from overwhelming a receiver's buffer?",
                "options": ["Congestion Window", "Flow Control (Sliding Window)", "Bandwidth Throttling", "Checksums"],
                "answer": 1,
                "explanation": "TCP flow control uses the Receiver Advertised Window (rwnd) to prevent buffer overflows.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which diagnostic utility uses ICMP Echo Request and Echo Reply messages to verify host reachability?",
                "options": ["traceroute", "ping", "netstat", "nslookup"],
                "answer": 1,
                "explanation": "The 'ping' tool sends ICMP Echo Requests and listens for Echo Replies to measure latency and packet loss.",
                "difficulty": "beginner"
            },
            {
                "question": "What type of attack involves an attacker forging the source IP address in packet headers to disguise identity?",
                "options": ["Man-in-the-Middle", "IP Spoofing", "Phishing", "Buffer Overflow"],
                "answer": 1,
                "explanation": "IP Spoofing crafts packets with fake source IP addresses to bypass filters or launch amplification attacks.",
                "difficulty": "advanced"
            }
        ]
    },

    "Operating Systems": {
        "Processes, Threads & CPU Scheduling": [
            {
                "question": "What is a lightweight process that shares the code, data, and resources of its parent?",
                "options": ["Thread", "Daemon", "Fiber", "Zombie process"],
                "answer": 0,
                "explanation": "A thread is a basic unit of CPU execution sharing memory and file handles with peer threads.",
                "difficulty": "beginner"
            },
            {
                "question": "Which CPU scheduling algorithm may suffer from the 'Convoy Effect'?",
                "options": ["Round Robin", "First-Come First-Served (FCFS)", "Shortest Job First", "Priority Scheduling"],
                "answer": 1,
                "explanation": "FCFS causes short jobs to wait behind long CPU-burst jobs, resulting in poor average turnaround time.",
                "difficulty": "intermediate"
            },
            {
                "question": "What state does a process enter when it is waiting for an I/O operation to complete?",
                "options": ["Ready", "Running", "Waiting / Blocked", "Terminated"],
                "answer": 2,
                "explanation": "When requesting I/O, a process transitions from Running to Waiting/Blocked until signaled by an interrupt.",
                "difficulty": "beginner"
            },
            {
                "question": "Which scheduling algorithm gives each process a small fixed unit of CPU time (time quantum) in a circular fashion?",
                "options": ["Shortest Remaining Time First", "Round Robin", "Multilevel Queue", "Priority Preemption"],
                "answer": 1,
                "explanation": "Round Robin assigns a cyclic time slice (quantum) to each ready process to ensure fairness and responsiveness.",
                "difficulty": "beginner"
            },
            {
                "question": "What is a process called that has completed execution but still has an entry in the process table?",
                "options": ["Orphan Process", "Zombie Process", "Daemon Process", "Init Process"],
                "answer": 1,
                "explanation": "A zombie process has exited, but its parent has not yet read its exit status via wait().",
                "difficulty": "intermediate"
            },
            {
                "question": "What happens during a CPU context switch?",
                "options": [
                    "The operating system restarts the kernel",
                    "The state of the currently executing process is saved and the state of the scheduled process is loaded",
                    "Virtual memory is formatted",
                    "The disk cache is flushed to hard drive"
                ],
                "answer": 1,
                "explanation": "Context switching saves program counters, registers, and memory maps of one process and restores another.",
                "difficulty": "intermediate"
            }
        ],
        "Memory Management & Virtual Memory": [
            {
                "question": "What hardware component translates virtual memory addresses into physical RAM addresses?",
                "options": ["ALU", "MMU (Memory Management Unit)", "DMA Controller", "Bus Interface"],
                "answer": 1,
                "explanation": "The MMU performs hardware address translation between virtual memory and physical memory frames.",
                "difficulty": "beginner"
            },
            {
                "question": "What phenomenon occurs when excessive paging causes the CPU to spend more time swapping pages than executing code?",
                "options": ["Deadlock", "Starvation", "Thrashing", "Fragmentation"],
                "answer": 2,
                "explanation": "Thrashing happens when the working set exceeds physical memory, causing continuous page faults.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the purpose of the Translation Lookaside Buffer (TLB)?",
                "options": [
                    "A hardware cache to speed up virtual-to-physical address translation",
                    "A buffer for network packets",
                    "A disk storage partition for swap space",
                    "An interrupt vector table"
                ],
                "answer": 0,
                "explanation": "The TLB is an associative high-speed hardware cache storing recent page table entries.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which page replacement algorithm suffers from Belady's Anomaly (where increasing frames increases page faults)?",
                "options": ["LRU (Least Recently Used)", "FIFO (First In First Out)", "Optimal Page Replacement", "Clock Algorithm"],
                "answer": 1,
                "explanation": "FIFO is not a stack algorithm and can experience Belady's Anomaly for certain reference strings.",
                "difficulty": "advanced"
            },
            {
                "question": "What is external fragmentation in memory management?",
                "options": [
                    "Unused memory inside allocated fixed-size partitions",
                    "Total free memory is sufficient to satisfy a request, but it is non-contiguous",
                    "Virtual addresses pointing to invalid physical pages",
                    "Memory leaked by user space applications"
                ],
                "answer": 1,
                "explanation": "External fragmentation leaves free memory scattered in small blocks unable to accommodate large requests.",
                "difficulty": "intermediate"
            }
        ],
        "Synchronization, Deadlocks & File Systems": [
            {
                "question": "Which algorithm is used by operating systems for deadlock avoidance?",
                "options": ["Dijkstra's Banker's Algorithm", "Kruskal's Algorithm", "Peterson's Algorithm", "Lamport's Bakery Algorithm"],
                "answer": 0,
                "explanation": "Banker's Algorithm tests for safe states before allocating resources to prevent deadlocks.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which of the following is NOT one of Coffman's four necessary conditions for deadlock?",
                "options": ["Mutual Exclusion", "Hold and Wait", "Preemption Allowed", "Circular Wait"],
                "answer": 2,
                "explanation": "The four conditions are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Preemption breaks deadlock.",
                "difficulty": "intermediate"
            },
            {
                "question": "What synchronization primitive uses integer counters with wait() (P) and signal() (V) operations?",
                "options": ["Mutex", "Counting Semaphore", "Spinlock", "Condition Variable"],
                "answer": 1,
                "explanation": "Counting semaphores maintain an integer value accessed only via atomic wait (decrement) and signal (increment).",
                "difficulty": "beginner"
            },
            {
                "question": "In Unix-like file systems, what data structure stores file metadata (size, permissions, disk block pointers)?",
                "options": ["Superblock", "Inode", "File Allocation Table (FAT)", "Directory Entry"],
                "answer": 1,
                "explanation": "An Inode stores all metadata for a file except its name and directory path.",
                "difficulty": "intermediate"
            },
            {
                "question": "What condition occurs when multiple threads access shared data concurrently and the final result depends on execution order?",
                "options": ["Deadlock", "Race Condition", "Starvation", "Priority Inversion"],
                "answer": 1,
                "explanation": "A Race Condition occurs when unsynchronized threads race to read and modify shared state.",
                "difficulty": "beginner"
            }
        ]
    },

    "Artificial Intelligence": {
        "Problem Solving & Search Heuristics": [
            {
                "question": "Which search algorithm uses a heuristic function h(n) combined with exact path cost g(n)?",
                "options": ["Depth-First Search", "Breadth-First Search", "A* Search", "Hill Climbing"],
                "answer": 2,
                "explanation": "A* search evaluates nodes with f(n) = g(n) + h(n), balancing path cost and estimated heuristic to goal.",
                "difficulty": "intermediate"
            },
            {
                "question": "A heuristic function h(n) is admissible if it:",
                "options": [
                    "Never underestimates the true cost to reach the goal",
                    "Never overestimates the true cost to reach the goal",
                    "Is strictly greater than the true cost",
                    "Is equal to zero for all nodes"
                ],
                "answer": 1,
                "explanation": "An admissible heuristic never overestimates the actual minimal cost to reach the nearest goal state.",
                "difficulty": "intermediate"
            },
            {
                "question": "The Turing Test was proposed by Alan Turing to evaluate what capability of a computer?",
                "options": ["Processing speed", "Human-like conversational intelligence", "Memory capacity", "Energy efficiency"],
                "answer": 1,
                "explanation": "Alan Turing proposed the test to see if a computer could converse indistinguishably from a human.",
                "difficulty": "beginner"
            },
            {
                "question": "Which uninformed search algorithm is guaranteed to find the shallowest goal in an unweighted tree?",
                "options": ["Depth-First Search", "Breadth-First Search", "Depth-Limited Search", "Bidirectional DFS"],
                "answer": 1,
                "explanation": "BFS explores level by level, ensuring the first goal encountered has the minimum number of steps.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the primary drawback of greedy best-first search?",
                "options": [
                    "It has exponential memory requirements",
                    "It can get trapped in false starts or loops because it only considers h(n) and ignores g(n)",
                    "It is computationally too slow",
                    "It cannot use heuristics"
                ],
                "answer": 1,
                "explanation": "Greedy search relies solely on h(n), making it susceptible to deceptive local minima and non-optimal paths.",
                "difficulty": "intermediate"
            },
            {
                "question": "What optimization technique systematically prunes branches in a Minimax game tree without altering the final outcome?",
                "options": ["Beam Search", "Alpha-Beta Pruning", "Simulated Annealing", "Genetic Crossover"],
                "answer": 1,
                "explanation": "Alpha-Beta pruning discards game subtrees that cannot influence the final decision of Minimax.",
                "difficulty": "advanced"
            }
        ],
        "Knowledge Representation & Logic": [
            {
                "question": "Which logic system supports quantifiers such as 'For all' (universal) and 'There exists' (existential)?",
                "options": ["Propositional Logic", "First-Order Predicate Logic (FOL)", "Boolean Algebra", "Fuzzy Logic"],
                "answer": 1,
                "explanation": "FOL extends propositional logic by introducing predicates, functions, objects, and quantifiers.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is an ontology in Artificial Intelligence knowledge representation?",
                "options": [
                    "A formal specification of concepts, relationships, and categories within a domain",
                    "A machine learning algorithm for clustering",
                    "A search algorithm for robotics",
                    "A compiler phase for AI languages"
                ],
                "answer": 0,
                "explanation": "An ontology models domain knowledge through structured taxonomies, classes, properties, and axioms.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which inference rule concludes B given 'A' and 'If A then B' (A -> B)?",
                "options": ["Modus Tollens", "Modus Ponens", "Resolution", "Conjunction"],
                "answer": 1,
                "explanation": "Modus Ponens is the foundational rule of deduction: from P and P -> Q, infer Q.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the Closed World Assumption (CWA) in knowledge bases?",
                "options": [
                    "Any statement that is not currently known to be true is assumed false",
                    "Only positive assertions are allowed",
                    "All facts must be provable in polynomial time",
                    "The world is finite and bounded"
                ],
                "answer": 0,
                "explanation": "Under CWA, if a fact cannot be proven true from the existing knowledge base, it is presumed false.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which knowledge representation structure models semantic memory as nodes (concepts) connected by labeled relationship edges?",
                "options": ["Decision Trees", "Semantic Networks", "Production Rules", "Truth Tables"],
                "answer": 1,
                "explanation": "Semantic networks represent concepts as vertices connected by relational links such as 'is-a' and 'part-of'.",
                "difficulty": "beginner"
            }
        ],
        "Game Playing & Expert Systems": [
            {
                "question": "In an Expert System, what component contains the domain-specific IF-THEN rules and facts?",
                "options": ["Inference Engine", "Knowledge Base", "User Interface", "Explanation Facility"],
                "answer": 1,
                "explanation": "The Knowledge Base stores domain expertise in the form of facts and production rules.",
                "difficulty": "beginner"
            },
            {
                "question": "What does forward chaining do in an expert system inference engine?",
                "options": [
                    "Starts with known facts and applies rules to deduce new facts (data-driven)",
                    "Starts with a goal and works backward to find supporting facts (goal-driven)",
                    "Translates English text to SQL queries",
                    "Computes neural network weights using backpropagation"
                ],
                "answer": 0,
                "explanation": "Forward chaining is a data-driven approach that triggers rules when conditions match known facts.",
                "difficulty": "intermediate"
            },
            {
                "question": "What stochastic search algorithm is inspired by the metallurgical process of heating and controlled cooling?",
                "options": ["Hill Climbing", "Simulated Annealing", "Genetic Algorithm", "Particle Swarm"],
                "answer": 1,
                "explanation": "Simulated Annealing escapes local optima by probabilistically accepting worse states at higher temperatures.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is a major limitation of classical rule-based expert systems?",
                "options": [
                    "They cannot perform Boolean logic",
                    "Brittleness and difficulty acquiring/updating large manual rule sets",
                    "They require GPU supercomputers to evaluate single rules",
                    "They cannot output textual responses"
                ],
                "answer": 1,
                "explanation": "Rule-based expert systems suffer from the knowledge acquisition bottleneck and break when encountering unseen edge cases.",
                "difficulty": "advanced"
            },
            {
                "question": "In game playing AI, what heuristic evaluation approach replaced manual evaluation functions in modern chess engines like AlphaZero?",
                "options": ["Deep Neural Networks trained via self-play Reinforcement Learning", "Depth-First Search", "A* search with Manhattan distance", "Rule-based lookup tables"],
                "answer": 0,
                "explanation": "AlphaZero utilizes deep neural networks combined with Monte Carlo Tree Search (MCTS) trained purely by self-play.",
                "difficulty": "advanced"
            }
        ]
    },

    "Machine Learning": {
        "Supervised Learning & Regression": [
            {
                "question": "Which algorithm is suitable for predicting continuous numeric values (such as house prices)?",
                "options": ["Linear Regression", "Logistic Regression", "K-Means Clustering", "Apriori Algorithm"],
                "answer": 0,
                "explanation": "Linear Regression models the relationship between independent features and a continuous target variable.",
                "difficulty": "beginner"
            },
            {
                "question": "What occurs when a machine learning model memorizes training noise and fails to generalize to unseen test data?",
                "options": ["Underfitting", "Overfitting", "High Bias", "Convergence"],
                "answer": 1,
                "explanation": "Overfitting happens when model complexity is too high, fitting training anomalies rather than underlying signals.",
                "difficulty": "beginner"
            },
            {
                "question": "What regularization technique adds the L1 norm of the weights to the loss function, promoting sparsity?",
                "options": ["Ridge Regularization (L2)", "Lasso Regularization (L1)", "ElasticNet", "Dropout"],
                "answer": 1,
                "explanation": "Lasso adds the sum of absolute coefficients, driving unimportant feature weights to exactly zero.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the primary optimization algorithm used to iteratively adjust weights by stepping down the loss gradient?",
                "options": ["K-Nearest Neighbors", "Gradient Descent", "Principal Component Analysis", "Breadth First Search"],
                "answer": 1,
                "explanation": "Gradient Descent updates model parameters proportionally to the negative gradient of the loss surface.",
                "difficulty": "beginner"
            },
            {
                "question": "What does a high bias model typically suffer from?",
                "options": ["Underfitting due to oversimplifying assumptions", "Overfitting to training noise", "Excessive variance", "Zero training error"],
                "answer": 0,
                "explanation": "High bias models make strong assumptions (like linear models on complex non-linear data), leading to underfitting.",
                "difficulty": "intermediate"
            },
            {
                "question": "In polynomial regression, increasing the degree of the polynomial generally causes:",
                "options": [
                    "Decreased variance and increased bias",
                    "Increased variance and potential overfitting",
                    "Zero computational cost",
                    "Automatic feature selection"
                ],
                "answer": 1,
                "explanation": "Higher-order polynomials increase model flexibility (variance), making it susceptible to overfitting the training set.",
                "difficulty": "intermediate"
            }
        ],
        "Classification & Model Evaluation": [
            {
                "question": "Which classification algorithm models the probability of a binary outcome using the sigmoid function?",
                "options": ["Linear Regression", "Logistic Regression", "K-Means", "DBSCAN"],
                "answer": 1,
                "explanation": "Logistic Regression applies the logistic (sigmoid) function to map linear combinations into [0, 1] probabilities.",
                "difficulty": "beginner"
            },
            {
                "question": "What metric represents the harmonic mean of Precision and Recall?",
                "options": ["Accuracy", "ROC-AUC", "F1 Score", "Log Loss"],
                "answer": 2,
                "explanation": "F1 Score = 2 * (Precision * Recall) / (Precision + Recall), balancing false positives and false negatives.",
                "difficulty": "intermediate"
            },
            {
                "question": "In an imbalanced dataset where 99% of samples are class 0, why is raw accuracy a deceptive metric?",
                "options": [
                    "Accuracy is impossible to compute on imbalanced data",
                    "A naive classifier that always predicts 0 will achieve 99% accuracy while failing on class 1 entirely",
                    "Accuracy is only defined for regression problems",
                    "Accuracy requires balanced cross-validation"
                ],
                "answer": 1,
                "explanation": "The accuracy paradox occurs because majority-class dominance hides total failure on minority classes.",
                "difficulty": "intermediate"
            },
            {
                "question": "What validation technique splits data into k equal folds, training on k-1 folds and validating on the remaining fold iteratively?",
                "options": ["Bootstrapping", "k-Fold Cross-Validation", "Holdout validation", "Leave-One-Out Regression"],
                "answer": 1,
                "explanation": "k-Fold Cross-Validation provides a robust estimate of generalization error across all samples.",
                "difficulty": "beginner"
            },
            {
                "question": "In a Confusion Matrix, what does Recall (Sensitivity) measure?",
                "options": [
                    "True Positives / (True Positives + False Positives)",
                    "True Positives / (True Positives + False Negatives)",
                    "True Negatives / (True Negatives + False Positives)",
                    "(True Positives + True Negatives) / Total"
                ],
                "answer": 1,
                "explanation": "Recall measures the fraction of actual positive instances correctly identified by the model.",
                "difficulty": "intermediate"
            }
        ],
        "Unsupervised Learning & Neural Networks": [
            {
                "question": "Which unsupervised clustering algorithm partitions n observations into k clusters centered around centroids?",
                "options": ["KNN", "K-Means", "SVM", "Random Forest"],
                "answer": 1,
                "explanation": "K-Means iteratively assigns points to the nearest centroid and updates centroids to the mean of clusters.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the primary objective of Principal Component Analysis (PCA)?",
                "options": [
                    "Dimensionality reduction while maximizing retained variance",
                    "Supervised multi-class classification",
                    "Deep reinforcement learning",
                    "Text generation"
                ],
                "answer": 0,
                "explanation": "PCA projects high-dimensional data onto orthogonal axes that capture the greatest directions of variance.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which algorithm is used in artificial neural networks to propagate errors backward and compute weight gradients?",
                "options": ["Forward propagation", "Backpropagation using the chain rule of calculus", "Simulated Annealing", "Bellman equation"],
                "answer": 1,
                "explanation": "Backpropagation calculates partial derivatives of the loss with respect to all layer weights using the chain rule.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which activation function is most widely used in hidden layers of modern deep networks to mitigate vanishing gradients?",
                "options": ["Sigmoid", "Tanh", "ReLU (Rectified Linear Unit)", "Softmax"],
                "answer": 2,
                "explanation": "ReLU (f(x) = max(0, x)) has constant gradient 1 for positive inputs, reducing vanishing gradients and speeding convergence.",
                "difficulty": "intermediate"
            },
            {
                "question": "What ensemble method builds multiple independent decision trees on bootstrap samples and aggregates their predictions?",
                "options": ["AdaBoost", "Random Forest (Bagging)", "Gradient Boosting Machine (GBM)", "XGBoost"],
                "answer": 1,
                "explanation": "Random Forest trains diverse decision trees on random data/feature subsets and averages predictions to reduce variance.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Software Engineering": {
        "SDLC & Agile Methodologies": [
            {
                "question": "In Scrum agile methodology, what is the fixed time-box for completing a sprint backlog?",
                "options": ["Milestone", "Sprint (typically 1 to 4 weeks)", "Epoch", "Release cycle"],
                "answer": 1,
                "explanation": "A Sprint is a time-boxed iteration where a cross-functional team completes designated backlog items.",
                "difficulty": "beginner"
            },
            {
                "question": "Which software development life cycle (SDLC) model follows a strictly sequential, phase-by-phase approach?",
                "options": ["Agile Model", "Waterfall Model", "Spiral Model", "RAD Model"],
                "answer": 1,
                "explanation": "The Waterfall model is linear-sequential: Requirements -> Design -> Implementation -> Verification -> Maintenance.",
                "difficulty": "beginner"
            },
            {
                "question": "What does CI/CD stand for in modern DevOps and software engineering?",
                "options": [
                    "Continuous Integration and Continuous Delivery / Deployment",
                    "Code Inspection and Code Delivery",
                    "Centralized Indexing and Continuous Data",
                    "Concurrent Iteration and Concurrent Design"
                ],
                "answer": 0,
                "explanation": "CI/CD automates code merging, building, automated testing, and release delivery.",
                "difficulty": "beginner"
            },
            {
                "question": "Who is responsible for maximizing product value and managing the Product Backlog in Scrum?",
                "options": ["Scrum Master", "Product Owner", "Development Team Lead", "Software Architect"],
                "answer": 1,
                "explanation": "The Product Owner owns the vision, prioritizes the product backlog, and represents stakeholder interests.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the primary focus of the Spiral SDLC model developed by Barry Boehm?",
                "options": ["Rapid prototyping without documentation", "Explicit risk assessment and risk mitigation at every loop", "Purely test-driven implementation", "Zero maintenance overhead"],
                "answer": 1,
                "explanation": "The Spiral model combines iterative development with systematic risk analysis and management.",
                "difficulty": "intermediate"
            },
            {
                "question": "What short daily ceremony in Scrum keeps team members aligned on what was done, what is planned, and blockers?",
                "options": ["Sprint Retrospective", "Daily Standup / Daily Scrum", "Sprint Planning", "Backlog Grooming"],
                "answer": 1,
                "explanation": "The Daily Scrum is a 15-minute time-boxed check-in to inspect progress and synchronize daily tasks.",
                "difficulty": "beginner"
            }
        ],
        "Requirements & Design Patterns": [
            {
                "question": "What type of software requirement specifies quality attributes such as security, scalability, and performance?",
                "options": ["Functional Requirements", "Non-Functional Requirements (NFR)", "User Story Tasks", "Interface Signatures"],
                "answer": 1,
                "explanation": "Non-Functional Requirements describe system properties, quality constraints, and operational criteria.",
                "difficulty": "beginner"
            },
            {
                "question": "Which design principle states that a module should have only one reason to change?",
                "options": ["Open/Closed Principle", "Single Responsibility Principle (SRP)", "Interface Segregation", "Liskov Substitution"],
                "answer": 1,
                "explanation": "SRP (from SOLID) dictates that each class should encapsulate a single distinct responsibility.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which UML diagram visualizes interactions between objects arranged in a time sequence?",
                "options": ["Class Diagram", "Sequence Diagram", "Use Case Diagram", "State Machine Diagram"],
                "answer": 1,
                "explanation": "Sequence diagrams illustrate message exchanges between lifelines chronologically down the page.",
                "difficulty": "intermediate"
            },
            {
                "question": "What architectural pattern separates an application into Presentation, Business Logic, and Data Access layers?",
                "options": ["Monolithic Sprawl", "Three-Tier / Layered Architecture", "Microkernel", "Peer-to-Peer"],
                "answer": 1,
                "explanation": "Three-Tier Architecture enforces clean separation of concerns between UI, domain logic, and persistence.",
                "difficulty": "beginner"
            },
            {
                "question": "What is 'Technical Debt' in software engineering?",
                "options": [
                    "Financial loans taken out to buy developer laptops",
                    "The implied cost of future rework caused by choosing quick/easy hacks over clean architectural design",
                    "Unpaid software licensing fees",
                    "Depreciation of server hardware"
                ],
                "answer": 1,
                "explanation": "Technical debt reflects the compounding engineering interest incurred when shortcuts are taken in codebase design.",
                "difficulty": "intermediate"
            }
        ],
        "Software Testing & Quality Assurance": [
            {
                "question": "Which testing type examines individual units or components in isolation from the rest of the application?",
                "options": ["Integration Testing", "Unit Testing", "System Testing", "Acceptance Testing"],
                "answer": 1,
                "explanation": "Unit testing tests individual functions, methods, or classes using mock dependencies.",
                "difficulty": "beginner"
            },
            {
                "question": "What testing approach involves writing automated test cases BEFORE writing the implementation code?",
                "options": ["Behavior-Driven Architecture", "Test-Driven Development (TDD)", "Regression Testing", "Smoke Testing"],
                "answer": 1,
                "explanation": "TDD follows the Red-Green-Refactor cycle: write failing test, write code to pass, refactor.",
                "difficulty": "beginner"
            },
            {
                "question": "What is Regression Testing?",
                "options": [
                    "Testing newly added modules only",
                    "Re-running tests to ensure recent code changes have not broken existing functionality",
                    "Stress testing the system under maximum network load",
                    "Testing code compatibility on legacy operating systems"
                ],
                "answer": 1,
                "explanation": "Regression testing confirms that updates, fixes, or refactoring haven't reintroduced previously solved bugs.",
                "difficulty": "intermediate"
            },
            {
                "question": "In software testing, what is Black-Box testing?",
                "options": [
                    "Testing internal code structure and logic branches with knowledge of source code",
                    "Testing software functionality against requirements without viewing internal implementation",
                    "Testing server hardware in dark data centers",
                    "Decompiling binary code to look for vulnerabilities"
                ],
                "answer": 1,
                "explanation": "Black-Box testing focuses purely on inputs and outputs according to functional specifications.",
                "difficulty": "beginner"
            },
            {
                "question": "What metric measures the percentage of source code statements executed by an automated test suite?",
                "options": ["Cyclomatic Complexity", "Code Coverage", "Defect Density", "Technical Velocity"],
                "answer": 1,
                "explanation": "Code Coverage evaluates what percentage of branches, statements, and lines are exercised during test runs.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Cyber Security": {
        "Cryptography & Encryption Standards": [
            {
                "question": "Which encryption type uses two mathematically related keys (public and private)?",
                "options": ["Symmetric Encryption", "Asymmetric Encryption (Public Key)", "Hashing", "Obfuscation"],
                "answer": 1,
                "explanation": "Asymmetric encryption (e.g. RSA, ECC) utilizes a public key for encryption and private key for decryption.",
                "difficulty": "beginner"
            },
            {
                "question": "Which symmetric block cipher standard was selected by NIST in 2001 to replace DES?",
                "options": ["Blowfish", "AES (Advanced Encryption Standard)", "RC4", "MD5"],
                "answer": 1,
                "explanation": "AES (Rijndael cipher) supports 128, 192, and 256-bit keys and is the global symmetric encryption standard.",
                "difficulty": "beginner"
            },
            {
                "question": "What is a cryptographic hash function property that makes it computationally infeasible to find two different inputs with the same hash output?",
                "options": ["Pre-image resistance", "Collision resistance", "Symmetry", "Non-repudiation"],
                "answer": 1,
                "explanation": "Collision resistance ensures that finding any two distinct inputs x and y where H(x) = H(y) is computationally impossible.",
                "difficulty": "intermediate"
            },
            {
                "question": "Why is salt appended to user passwords before cryptographic hashing?",
                "options": [
                    "To make the password longer for UI validation",
                    "To defend against rainbow table and precomputed dictionary attacks",
                    "To encrypt the password symmetrically",
                    "To compress the password into 32 bits"
                ],
                "answer": 1,
                "explanation": "Salting adds unique random bytes to each password, ensuring identical passwords generate distinct hashes.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which hashing algorithm is considered cryptographically broken and unsafe for digital signatures?",
                "options": ["SHA-256", "SHA-3", "MD5", "Argon2"],
                "answer": 2,
                "explanation": "MD5 suffers from demonstrated collision vulnerabilities and must never be used for security-critical applications.",
                "difficulty": "beginner"
            },
            {
                "question": "What protocol provides end-to-end cryptographic transport security for HTTPS web browsing?",
                "options": ["IPSec", "TLS (Transport Layer Security)", "SSH", "Kerberos"],
                "answer": 1,
                "explanation": "TLS (successor to SSL) secures HTTP communications with cipher suites and certificate authentication.",
                "difficulty": "beginner"
            }
        ],
        "Network Attacks & Vulnerabilities": [
            {
                "question": "What type of cyber attack floods a server with distributed traffic to make it unavailable to legitimate users?",
                "options": ["SQL Injection", "DDoS (Distributed Denial of Service)", "Cross-Site Scripting (XSS)", "Man-in-the-Middle"],
                "answer": 1,
                "explanation": "DDoS attacks saturate network links and compute resources using coordinated botnets.",
                "difficulty": "beginner"
            },
            {
                "question": "Which vulnerability allows attackers to manipulate backend database queries via unsanitized user inputs?",
                "options": ["Cross-Site Request Forgery (CSRF)", "SQL Injection (SQLi)", "Buffer Overflow", "Clickjacking"],
                "answer": 1,
                "explanation": "SQL Injection occurs when untrusted input is directly concatenated into SQL queries rather than using parameterized queries.",
                "difficulty": "beginner"
            },
            {
                "question": "What vulnerability occurs when an application embeds unescaped user input into web pages, executing malicious scripts in client browsers?",
                "options": ["Cross-Site Scripting (XSS)", "Server-Side Request Forgery", "Directory Traversal", "Zero-Day Exploit"],
                "answer": 0,
                "explanation": "XSS allows attackers to inject malicious JavaScript into viewed pages, hijacking cookies and sessions.",
                "difficulty": "intermediate"
            },
            {
                "question": "What attack tricks an authenticated user's browser into submitting unauthorized commands to a vulnerable web application?",
                "options": ["Cross-Site Request Forgery (CSRF)", "Phishing", "Man-in-the-Middle", "Port Scanning"],
                "answer": 0,
                "explanation": "CSRF exploits ambient credentials (cookies/sessions) by inducing victims to execute unwanted state-changing actions.",
                "difficulty": "intermediate"
            },
            {
                "question": "What type of attack intercepts and potentially alters communication between two parties without their knowledge?",
                "options": ["Man-in-the-Middle (MitM)", "Brute Force Attack", "Ransomware", "DNS Amplification"],
                "answer": 0,
                "explanation": "In a MitM attack, an attacker relays and eavesdrops on messages between endpoints who believe they are talking directly.",
                "difficulty": "intermediate"
            }
        ],
        "Authentication, Authorization & Firewalls": [
            {
                "question": "What security framework represents the three fundamental pillars of information security?",
                "options": ["TCP/IP Model", "CIA Triad (Confidentiality, Integrity, Availability)", "SOLID Model", "OSI Model"],
                "answer": 1,
                "explanation": "The CIA Triad guides information security policies across data confidentiality, integrity, and availability.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the difference between Authentication and Authorization?",
                "options": [
                    "Authentication verifies identity; Authorization verifies what permissions that identity has",
                    "Authentication grants permissions; Authorization checks passwords",
                    "They are interchangeable terms",
                    "Authentication is for networks; Authorization is for databases"
                ],
                "answer": 0,
                "explanation": "Authentication checks 'Who are you?'; Authorization checks 'What are you allowed to do?'.",
                "difficulty": "beginner"
            },
            {
                "question": "What type of firewall inspects traffic based on active connection state and context in addition to IP and port headers?",
                "options": ["Packet Filtering Firewall", "Stateful Inspection Firewall", "Circuit-Level Gateway", "Static Proxy"],
                "answer": 1,
                "explanation": "Stateful firewalls track the state of active TCP streams and only allow packets that belong to established connections.",
                "difficulty": "intermediate"
            },
            {
                "question": "What open standard token format is commonly used to securely transmit authorization claims between a client and server?",
                "options": ["JWT (JSON Web Token)", "XML Schema", "SOAP Envelope", "PEM Certificate"],
                "answer": 0,
                "explanation": "JWT represents claims cryptographically signed (via HMAC or RSA) for stateless authentication in REST APIs.",
                "difficulty": "intermediate"
            },
            {
                "question": "What security principle dictates that users and applications should be granted only the minimum permissions necessary to perform their jobs?",
                "options": ["Principle of Least Privilege (PoLP)", "Defense in Depth", "Fail-Safe Defaults", "Separation of Duties"],
                "answer": 0,
                "explanation": "PoLP limits privileges to minimize the blast radius of compromises or insider threats.",
                "difficulty": "beginner"
            }
        ]
    }
}
