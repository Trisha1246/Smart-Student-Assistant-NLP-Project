# Part 2: Subjects 11-20 (Cloud Computing, Computer Architecture, Theory of Computation,
# Compiler Design, Object Oriented Design, Natural Language Processing, Digital Electronics,
# Microprocessors, Internet of Things, Big Data Analytics)

PART2_DATA = {
    "Cloud Computing": {
        "Cloud Service & Deployment Models": [
            {
                "question": "Which cloud computing service model provides raw virtualized hardware, storage, and networking on demand?",
                "options": ["SaaS (Software as a Service)", "PaaS (Platform as a Service)", "IaaS (Infrastructure as a Service)", "FaaS (Function as a Service)"],
                "answer": 2,
                "explanation": "IaaS (e.g. AWS EC2, Azure VMs, Google Compute Engine) provisions raw compute infrastructure.",
                "difficulty": "beginner"
            },
            {
                "question": "What service model allows developers to deploy code without managing servers, operating systems, or runtimes?",
                "options": ["IaaS", "PaaS (Platform as a Service)", "Bare Metal", "Colocation"],
                "answer": 1,
                "explanation": "PaaS (e.g. Heroku, AWS Elastic Beanstalk, Google App Engine) abstracts OS and runtime management.",
                "difficulty": "beginner"
            },
            {
                "question": "Google Workspace and Microsoft 365 are primary examples of which cloud computing model?",
                "options": ["IaaS", "PaaS", "SaaS (Software as a Service)", "CaaS (Containers as a Service)"],
                "answer": 2,
                "explanation": "SaaS delivers fully functional end-user applications managed by the cloud vendor over web interfaces.",
                "difficulty": "beginner"
            },
            {
                "question": "What type of cloud deployment combines on-premises private infrastructure with one or more public cloud providers?",
                "options": ["Community Cloud", "Hybrid Cloud", "Distributed Cloud", "Multi-tenant Cloud"],
                "answer": 1,
                "explanation": "Hybrid Cloud bridges on-premises private datacenter resources with public cloud capacity.",
                "difficulty": "beginner"
            },
            {
                "question": "What cloud architectural property refers to the automated scaling of resources dynamically according to current load?",
                "options": ["High Availability", "Elasticity", "Fault Tolerance", "Durability"],
                "answer": 1,
                "explanation": "Elasticity is the ability of cloud systems to provision and de-provision computing capacity adaptively.",
                "difficulty": "intermediate"
            },
            {
                "question": "In the Cloud Shared Responsibility Model for IaaS, what is the customer responsible for securing?",
                "options": [
                    "Physical datacenter security and hardware cooling",
                    "Hypervisor firmware updates",
                    "Guest operating systems, installed applications, network configurations, and data",
                    "Underlying physical host hardware"
                ],
                "answer": 2,
                "explanation": "Under IaaS, the cloud provider secures hardware and hypervisors; the customer owns OS patching, apps, and data.",
                "difficulty": "intermediate"
            }
        ],
        "Virtualization & Containerization": [
            {
                "question": "What is the key technical difference between a Virtual Machine (VM) and a Docker Container?",
                "options": [
                    "Containers include a full guest operating system; VMs do not",
                    "Containers share the host OS kernel and isolate user space; VMs run a full guest OS on a hypervisor",
                    "VMs are always faster to start than containers",
                    "Containers require Type-1 bare metal hypervisors"
                ],
                "answer": 1,
                "explanation": "Containers share the host kernel via Linux namespaces and cgroups, making them lightweight compared to full guest OS VMs.",
                "difficulty": "beginner"
            },
            {
                "question": "What is a Type-1 (Bare-Metal) Hypervisor?",
                "options": [
                    "A hypervisor that runs as a software application on top of an existing OS (like VirtualBox)",
                    "A hypervisor that runs directly on physical server hardware without an underlying host OS",
                    "A software package used exclusively for container orchestration",
                    "A browser extension for testing virtual machines"
                ],
                "answer": 1,
                "explanation": "Type-1 hypervisors (e.g. VMware ESXi, KVM, Xen) execute directly on host bare-metal hardware for maximum performance.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which Linux kernel feature provides resource metering (CPU, memory, disk I/O) for containers?",
                "options": ["Namespaces", "Control Groups (cgroups)", "SELinux", "Chroot"],
                "answer": 1,
                "explanation": "cgroups partition and enforce resource quotas for containerized processes.",
                "difficulty": "advanced"
            },
            {
                "question": "What open-source system is the industry standard for automating container deployment, scaling, and operations?",
                "options": ["Ansible", "Kubernetes (K8s)", "Vagrant", "OpenStack"],
                "answer": 1,
                "explanation": "Kubernetes provides automated container orchestration, self-healing, rolling deployments, and load balancing.",
                "difficulty": "beginner"
            },
            {
                "question": "What is a Kubernetes Pod?",
                "options": [
                    "A physical server in a cloud region",
                    "The smallest deployable computing unit in Kubernetes, encapsulating one or more containers sharing network/storage",
                    "A virtual network interface card",
                    "A storage volume backup"
                ],
                "answer": 1,
                "explanation": "A Pod encapsulates one or more co-located containers with shared IP and volume mounts in Kubernetes.",
                "difficulty": "intermediate"
            }
        ],
        "Cloud Storage, Security & Serverless": [
            {
                "question": "Which cloud storage type stores data as distinct objects with unique identifiers and customizable metadata?",
                "options": ["Block Storage", "Object Storage (e.g. AWS S3)", "File Storage (NFS)", "Tape Archive"],
                "answer": 1,
                "explanation": "Object storage stores unstructured files as objects accessed via HTTP REST APIs with infinite scalability.",
                "difficulty": "beginner"
            },
            {
                "question": "What is Serverless Computing (FaaS - Function as a Service)?",
                "options": [
                    "Computing that does not use physical servers anywhere",
                    "An execution model where the cloud provider manages infrastructure and bills strictly for invocation run time",
                    "A private cloud hosted on dedicated workstations",
                    "Virtual desktop infrastructure"
                ],
                "answer": 1,
                "explanation": "In serverless (e.g. AWS Lambda, Google Cloud Functions), developers run code on demand without provisioning servers.",
                "difficulty": "beginner"
            },
            {
                "question": "What cloud service distributes incoming application traffic across multiple backend compute instances?",
                "options": ["NAT Gateway", "Load Balancer", "VPC Peering", "Route 53"],
                "answer": 1,
                "explanation": "Load balancers distribute network traffic across healthy backend targets to ensure fault tolerance and high availability.",
                "difficulty": "beginner"
            },
            {
                "question": "What is an isolated virtual network dedicated to a specific cloud tenant called?",
                "options": ["VPN Hub", "VPC (Virtual Private Cloud)", "LAN Mesh", "DMZ Pod"],
                "answer": 1,
                "explanation": "A VPC enables users to launch cloud resources into an isolated, logically partitioned virtual network.",
                "difficulty": "intermediate"
            },
            {
                "question": "What does 'Cold Start' refer to in serverless computing?",
                "options": [
                    "Booting a physical server from complete power-off",
                    "The latency incurred when spinning up a new container instance to serve an initial invocation",
                    "Refrigerating server racks in data centers",
                    "Compiling code before deploying"
                ],
                "answer": 1,
                "explanation": "A cold start occurs when an idle serverless function needs container initialization before running code.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Computer Architecture": {
        "Instruction Set Architecture & CPU": [
            {
                "question": "What architectural distinction separates RISC (Reduced Instruction Set) from CISC (Complex Instruction Set)?",
                "options": [
                    "RISC has variable instruction lengths; CISC has fixed lengths",
                    "RISC uses simpler single-cycle instructions with load/store architecture; CISC has complex multi-cycle instructions",
                    "RISC does not use registers",
                    "CISC only executes floating point instructions"
                ],
                "answer": 1,
                "explanation": "RISC emphasizes simple, uniform instructions executed in single cycles, accessing memory only through load/store.",
                "difficulty": "intermediate"
            },
            {
                "question": "In the von Neumann computer architecture, what shared pathway can become a processing throughput bottleneck?",
                "options": ["ALU accumulator", "Von Neumann Bottleneck (shared bus between CPU and Memory)", "Register file", "Instruction decoder"],
                "answer": 1,
                "explanation": "The Von Neumann bottleneck occurs because data and instructions share the same bus, constraining memory bandwidth.",
                "difficulty": "beginner"
            },
            {
                "question": "Which special CPU register holds the memory address of the next instruction to be fetched and executed?",
                "options": ["Instruction Register (IR)", "Program Counter (PC)", "Memory Data Register (MDR)", "Accumulator (ACC)"],
                "answer": 1,
                "explanation": "The Program Counter points to the address of the next sequential instruction in main memory.",
                "difficulty": "beginner"
            },
            {
                "question": "Which CPU component performs arithmetic (addition, subtraction) and logical (AND, OR, NOT) operations?",
                "options": ["Control Unit (CU)", "Arithmetic Logic Unit (ALU)", "Memory Management Unit (MMU)", "Bus Interface Unit (BIU)"],
                "answer": 1,
                "explanation": "The ALU handles all binary arithmetic calculations and Boolean logic decisions in the processor.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the difference between Big-Endian and Little-Endian byte ordering?",
                "options": [
                    "Big-Endian stores Most Significant Byte (MSB) at lowest memory address; Little-Endian stores LSB at lowest address",
                    "Big-Endian is for 64-bit systems; Little-Endian is for 32-bit systems",
                    "Big-Endian stores only signed numbers; Little-Endian stores unsigned",
                    "They refer to CPU fan rotational directions"
                ],
                "answer": 0,
                "explanation": "Big-Endian places the most significant byte first (at lowest memory address), whereas Little-Endian stores least significant byte first.",
                "difficulty": "intermediate"
            },
            {
                "question": "In modern 64-bit x86-64 processors, how many general-purpose registers (RAX, RBX, etc.) are available?",
                "options": ["8", "16", "32", "64"],
                "answer": 1,
                "explanation": "x86-64 architecture doubles the standard 8 general-purpose registers of x86 to 16 registers (RAX through R15).",
                "difficulty": "intermediate"
            }
        ],
        "Memory Hierarchy & Caches": [
            {
                "question": "Which memory level in the computer hierarchy exhibits the fastest access time and lowest latency?",
                "options": ["L3 Cache", "CPU Registers", "Main RAM", "Solid State Drive"],
                "answer": 1,
                "explanation": "CPU registers are built directly into the processor core and can be accessed within a single clock cycle (< 1 ns).",
                "difficulty": "beginner"
            },
            {
                "question": "Which cache mapping technique allows any main memory block to be placed into any arbitrary cache line?",
                "options": ["Direct Mapping", "Fully Associative Mapping", "Set Associative Mapping", "Segmented Mapping"],
                "answer": 1,
                "explanation": "Fully associative caches place memory blocks anywhere, eliminating conflict misses at the expense of comparator hardware.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the principle of Locality of Reference in memory systems?",
                "options": [
                    "Programs access code and data localized in time (Temporal) and nearby memory space (Spatial)",
                    "Data is stored near the motherboard power supply",
                    "Instruction registers point only to local addresses",
                    "RAM is refreshed locally by the memory controller"
                ],
                "answer": 0,
                "explanation": "Temporal locality means recently accessed items will be accessed again soon; Spatial locality means nearby items will be accessed.",
                "difficulty": "intermediate"
            },
            {
                "question": "In cache write policies, what is the Write-Through policy?",
                "options": [
                    "Writes are made only to cache and written to main memory only when the cache line is evicted",
                    "Every write updates both cache memory and main memory simultaneously",
                    "Writes bypass the cache completely and go directly to disk",
                    "Writes require an interrupt service routine"
                ],
                "answer": 1,
                "explanation": "Write-Through immediately writes data to both cache and main memory to guarantee memory consistency.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is a 'Cache Miss'?",
                "options": [
                    "When the CPU encounters a parity error in register files",
                    "When the requested memory address is not found in cache memory and must be fetched from slower RAM",
                    "When the cache is overheated",
                    "When the system memory runs out of page frames"
                ],
                "answer": 1,
                "explanation": "A cache miss occurs when referenced data is absent in cache, requiring higher-latency main memory retrieval.",
                "difficulty": "beginner"
            }
        ],
        "Pipelining & Instruction Level Parallelism": [
            {
                "question": "What hazard occurs when an instruction in the pipeline depends on the result of a prior instruction still being executed?",
                "options": ["Structural Hazard", "Data Hazard (Read-After-Write)", "Control Hazard", "Branch Hazard"],
                "answer": 1,
                "explanation": "Data hazards occur when instruction execution overlaps and creates data dependencies between pipeline stages.",
                "difficulty": "intermediate"
            },
            {
                "question": "In a classic 5-stage RISC processor pipeline, what are the five canonical stages in execution order?",
                "options": [
                    "IF (Instruction Fetch), ID (Instruction Decode), EX (Execute), MEM (Memory Access), WB (Write Back)",
                    "ID, IF, EX, WB, MEM",
                    "EX, IF, ID, MEM, WB",
                    "FETCH, READ, WRITE, EXECUTE, HALT"
                ],
                "answer": 0,
                "explanation": "The 5 canonical stages are Instruction Fetch (IF), Decode (ID), Execute (EX), Memory (MEM), and Write-Back (WB).",
                "difficulty": "intermediate"
            },
            {
                "question": "What technique mitigates data hazards by routing intermediate ALU results directly to waiting pipeline stages?",
                "options": ["Pipeline Stalling (Bubble)", "Operand Forwarding / Bypassing", "Branch Prediction", "Loop Unrolling"],
                "answer": 1,
                "explanation": "Operand forwarding forwards computation results directly from ALU outputs to subsequent instruction inputs without waiting for WB.",
                "difficulty": "advanced"
            },
            {
                "question": "What type of hazard is caused by conditional branch instructions altering program flow?",
                "options": ["Structural Hazard", "Data Hazard", "Control Hazard (Branch Hazard)", "Bus Hazard"],
                "answer": 2,
                "explanation": "Control hazards arise from branches where the target address is undetermined until decode/execute stages finish.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is a Superscalar Processor?",
                "options": [
                    "A processor that can execute instructions without a clock",
                    "A CPU capable of fetching, decoding, and dispatching multiple instructions per clock cycle to redundant execution units",
                    "A processor with more than 1 TB of cache",
                    "A computer made entirely of graphics cards"
                ],
                "answer": 1,
                "explanation": "Superscalar architectures employ multiple execution units (ALUs, FPUs) to achieve IPC (Instructions Per Cycle) > 1.",
                "difficulty": "advanced"
            }
        ]
    },

    "Theory of Computation": {
        "Regular Languages & Finite Automata": [
            {
                "question": "Which automaton recognizes the class of Regular Languages?",
                "options": ["Deterministic and Non-deterministic Finite Automata (DFA / NFA)", "Pushdown Automata (PDA)", "Turing Machine", "Linear Bounded Automata"],
                "answer": 0,
                "explanation": "Regular languages (Chomsky Type-3) are precisely recognized by DFAs, NFAs, and regular expressions.",
                "difficulty": "beginner"
            },
            {
                "question": "What does the Pumping Lemma for Regular Languages prove?",
                "options": [
                    "That a language is regular",
                    "That a specific language is NOT regular by demonstrating contradiction with pumping length",
                    "That an automaton is deterministic",
                    "That a Turing Machine halts"
                ],
                "answer": 1,
                "explanation": "The Pumping Lemma is a necessary condition for regularity used in proofs by contradiction to establish non-regularity.",
                "difficulty": "intermediate"
            },
            {
                "question": "Is an NFA (Non-deterministic Finite Automaton) more expressive in language recognition power than a DFA?",
                "options": [
                    "Yes, NFAs recognize context-free languages",
                    "No, every NFA can be converted into an equivalent DFA via powerset construction (same recognition power)",
                    "Yes, NFAs have unbounded stack memory",
                    "No, DFAs recognize more languages than NFAs"
                ],
                "answer": 1,
                "explanation": "The Powerset Construction algorithm proves DFAs and NFAs recognize the exact same class of regular languages.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which of the following operations is NOT closed under regular languages?",
                "options": ["Union", "Intersection", "Star (Kleene Closure)", "All of these operations ARE closed under regular languages"],
                "answer": 3,
                "explanation": "Regular languages are closed under Union, Intersection, Complement, Concatenation, and Kleene Star.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the minimum number of states in a DFA accepting the language of all strings over {0, 1} ending with '01'?",
                "options": ["2", "3", "4", "5"],
                "answer": 1,
                "explanation": "3 states are required: start/empty state, saw '0' state, and accepting saw '01' state.",
                "difficulty": "intermediate"
            },
            {
                "question": "According to Kleene's Theorem, what is the relationship between finite automata and regular expressions?",
                "options": [
                    "They define completely disjoint classes of languages",
                    "Any language definable by a finite automaton can be expressed by a regular expression, and vice versa",
                    "Regular expressions can describe Context-Sensitive grammars",
                    "Finite automata can parse HTML"
                ],
                "answer": 1,
                "explanation": "Kleene's Theorem establishes equivalence between languages recognized by finite automata and denoted by regular expressions.",
                "difficulty": "beginner"
            }
        ],
        "Context-Free Grammars & Pushdown Automata": [
            {
                "question": "A Pushdown Automaton (PDA) is mathematically equivalent to a Finite Automaton augmented with what memory structure?",
                "options": ["FIFO Queue", "LIFO Stack", "Two-way infinite tape", "Random-Access registers"],
                "answer": 1,
                "explanation": "PDAs recognize Context-Free Languages (Type-2) by pairing a finite state controller with a LIFO Stack.",
                "difficulty": "beginner"
            },
            {
                "question": "Are Deterministic Pushdown Automata (DPDA) as expressive as Non-deterministic Pushdown Automata (NPDA)?",
                "options": [
                    "Yes, both recognize identical languages",
                    "No, NPDAs recognize all CFLs while DPDAs recognize only deterministic CFLs (e.g. valid programming constructs)",
                    "DPDAs recognize more languages than NPDAs",
                    "Neither can recognize palindrome languages"
                ],
                "answer": 1,
                "explanation": "Unlike finite automata, non-determinism strictly increases the computational power of pushdown automata.",
                "difficulty": "advanced"
            },
            {
                "question": "What normal form requires every grammar production to be of the form A -> BC or A -> a?",
                "options": ["Greibach Normal Form (GNF)", "Chomsky Normal Form (CNF)", "Backus-Naur Form (BNF)", "Kleene Normal Form"],
                "answer": 1,
                "explanation": "CNF specifies that all productions yield either two non-terminals or a single terminal.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which algorithm determines whether a string of length n belongs to a CFL in O(n^3) time using CNF grammar?",
                "options": ["Dijkstra's Algorithm", "CYK (Cocke-Younger-Kasami) Algorithm", "Aho-Corasick Algorithm", "Earley Parser"],
                "answer": 1,
                "explanation": "The CYK dynamic programming algorithm solves membership for context-free grammars in Chomsky Normal Form in O(n^3).",
                "difficulty": "advanced"
            },
            {
                "question": "Which classic language is context-free but NOT regular?",
                "options": ["L = {0^n 1^n | n >= 0}", "L = {0^n 1^n 2^n | n >= 0}", "L = {w | w contains even number of 0s}", "L = (0+1)*"],
                "answer": 0,
                "explanation": "L = {0^n 1^n} requires counting 0s using a stack to match with 1s, making it context-free but non-regular.",
                "difficulty": "intermediate"
            }
        ],
        "Turing Machines & Decidability": [
            {
                "question": "What theoretical machine forms the foundation of modern computability and Church-Turing thesis?",
                "options": ["Pushdown Automaton", "Turing Machine (with an infinite read/write tape)", "Finite State Machine", "Linear Bounded Automaton"],
                "answer": 1,
                "explanation": "Alan Turing's universal tape machine defines the boundary of what can be algorithmically computed.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the famous Halting Problem proved undecidable by Alan Turing?",
                "options": [
                    "Determining if a sorting algorithm halts in O(n log n)",
                    "Determining whether an arbitrary computer program and input will eventually halt or run forever",
                    "Determining if a DFA has dead states",
                    "Proving NP-Completeness of SAT"
                ],
                "answer": 1,
                "explanation": "Turing proved by diagonal contradiction that no general algorithm can decide if arbitrary programs halt.",
                "difficulty": "intermediate"
            },
            {
                "question": "In the Chomsky Hierarchy, what type of language corresponds to Turing-recognizable languages?",
                "options": ["Type-0 (Unrestricted / Recursively Enumerable)", "Type-1 (Context-Sensitive)", "Type-2 (Context-Free)", "Type-3 (Regular)"],
                "answer": 0,
                "explanation": "Type-0 grammars generate Recursively Enumerable languages recognized by unrestricted Turing Machines.",
                "difficulty": "intermediate"
            },
            {
                "question": "What complexity class represents decision problems that can be SOLVED by a deterministic Turing machine in polynomial time?",
                "options": ["P", "NP", "NP-Complete", "PSPACE"],
                "answer": 0,
                "explanation": "Class P comprises problems solvable in O(n^k) polynomial time on deterministic Turing machines.",
                "difficulty": "beginner"
            },
            {
                "question": "What does it mean for a problem to be NP-Complete?",
                "options": [
                    "It cannot be solved on any computer",
                    "It is in NP, and every problem in NP can be polynomial-time reduced to it",
                    "It has linear time verification but infinite solution space",
                    "It requires non-polynomial memory"
                ],
                "answer": 1,
                "explanation": "NP-Complete problems are the hardest problems in NP; finding a polynomial solution to one solves all problems in NP.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Compiler Design": {
        "Lexical Analysis & Token Generation": [
            {
                "question": "What is the primary function of the Lexical Analyzer (Scanner) phase in a compiler?",
                "options": [
                    "Generate target machine code",
                    "Read characters from source code and convert them into meaningful syntactic tokens",
                    "Check semantic type compatibility",
                    "Optimize assembly loops"
                ],
                "answer": 1,
                "explanation": "Lexical analysis groups characters into tokens (keywords, identifiers, literals, operators) and strips comments/whitespace.",
                "difficulty": "beginner"
            },
            {
                "question": "Which tool is commonly used to generate lexical analyzers automatically from regular expressions?",
                "options": ["Yacc", "Lex / Flex", "Bison", "LLVM"],
                "answer": 1,
                "explanation": "Lex (and Flex) compiles regular expression rules into fast deterministic finite automaton scanners.",
                "difficulty": "beginner"
            },
            {
                "question": "What is a 'Lexeme' in compiler design?",
                "options": [
                    "A compiler error code",
                    "The concrete sequence of source characters matching the pattern for a token",
                    "An intermediate representation opcode",
                    "A machine instruction"
                ],
                "answer": 1,
                "explanation": "A lexeme is the instance of source characters matching a token pattern (e.g., 'totalScore' for token IDENTIFIER).",
                "difficulty": "intermediate"
            },
            {
                "question": "What central data structure does a compiler use to store identifiers, types, scopes, and memory offsets?",
                "options": ["Stack", "Symbol Table", "Abstract Syntax Tree", "Activation Record"],
                "answer": 1,
                "explanation": "The Symbol Table records variable names, data types, scoping rules, and locations across compilation phases.",
                "difficulty": "beginner"
            },
            {
                "question": "How does a lexical analyzer resolve conflicts when multiple token rules match (e.g., 'if' as keyword vs identifier)?",
                "options": [
                    "Random selection",
                    "Longest match (Maximal Munch) and rule priority order",
                    "Alphabetical order",
                    "Throwing a compilation error immediately"
                ],
                "answer": 1,
                "explanation": "Scanners apply Maximal Munch (longest matched prefix) and break ties using the earlier listed rule in the specification.",
                "difficulty": "intermediate"
            },
            {
                "question": "What buffer technique avoids frequent single-character I/O reads during lexical analysis?",
                "options": ["Two-buffer (Double buffering) with sentinel characters", "Circular queue", "Stack-based cache", "DMA interrupt stream"],
                "answer": 0,
                "explanation": "Double buffering loads chunks of source text into dual memory blocks using EOF sentinels for high throughput.",
                "difficulty": "advanced"
            }
        ],
        "Syntax Analysis & Parsers": [
            {
                "question": "Which data structure is produced by the syntax analysis (parsing) phase to represent hierarchical grammatical structure?",
                "options": ["Symbol Table", "Parse Tree / Abstract Syntax Tree (AST)", "Three-Address Code", "Object File"],
                "answer": 1,
                "explanation": "Parsers verify grammar rules and construct an Abstract Syntax Tree (AST) representing hierarchical relationships.",
                "difficulty": "beginner"
            },
            {
                "question": "What type of parser parses input from Top-to-Bottom by attempting to derive strings from the start symbol?",
                "options": ["Shift-Reduce Parser", "Top-Down Parser (e.g. Recursive Descent)", "LR Parser", "LALR Parser"],
                "answer": 1,
                "explanation": "Top-down parsers construct parse trees from the root (start symbol) down to the terminal leaves.",
                "difficulty": "beginner"
            },
            {
                "question": "What grammatical property causes an infinite recursion loop in Top-Down Recursive Descent parsers?",
                "options": ["Right Recursion", "Left Recursion (e.g. A -> A alpha)", "Ambiguity", "Null productions"],
                "answer": 1,
                "explanation": "Left recursion causes recursive descent functions to immediately call themselves with identical input without consuming tokens.",
                "difficulty": "intermediate"
            },
            {
                "question": "What are the two primary actions performed by a Bottom-Up Shift-Reduce parser?",
                "options": [
                    "Shift input tokens onto the stack, and Reduce handles to non-terminal symbols",
                    "Push and Pop",
                    "Fork and Join",
                    "Branch and Bound"
                ],
                "answer": 0,
                "explanation": "Shift-Reduce parsers shift terminal symbols onto an internal stack until a matching handle is reduced to a non-terminal.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which class of parsers is used by standard tools like Yacc and Bison?",
                "options": ["LL(1) Parsers", "LALR(1) Parsers (Look-Ahead LR)", "Operator Precedence Parsers", "Recursive Descent"],
                "answer": 1,
                "explanation": "Yacc/Bison generate LALR(1) parsing tables, balancing parser power with manageable table state sizes.",
                "difficulty": "intermediate"
            }
        ],
        "Semantic Analysis & Code Optimization": [
            {
                "question": "What compiler phase checks for type compatibility (e.g., adding an array to an integer) and scope validity?",
                "options": ["Lexical Analysis", "Semantic Analysis", "Code Generation", "Linker"],
                "answer": 1,
                "explanation": "Semantic analysis verifies static semantics, enforcing type checking, declarations, and scoping rules.",
                "difficulty": "beginner"
            },
            {
                "question": "What is Three-Address Code (TAC)?",
                "options": [
                    "A linear intermediate representation where each instruction has at most one operator and three memory operands",
                    "Assembly language for 32-bit CPUs",
                    "An IP routing protocol with 3 octets",
                    "A three-register machine code format"
                ],
                "answer": 0,
                "explanation": "TAC linearizes expressions into quadruples or triples of the form x = y op z.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which compiler optimization technique moves loop-invariant computations outside the loop body?",
                "options": ["Dead Code Elimination", "Loop Unrolling", "Code Motion / Loop-Invariant Hoisting", "Constant Folding"],
                "answer": 2,
                "explanation": "Code motion identifies computations yielding identical values across all loop iterations and hoists them out.",
                "difficulty": "intermediate"
            },
            {
                "question": "What optimization evaluates constant expressions (such as 3 * 7) at compile time instead of generating runtime instructions?",
                "options": ["Constant Folding", "Constant Propagation", "Strength Reduction", "Common Subexpression Elimination"],
                "answer": 0,
                "explanation": "Constant folding evaluates operations on literal values during compilation.",
                "difficulty": "beginner"
            },
            {
                "question": "Replacing an expensive operation with a cheaper equivalent operation (e.g., replacing x * 2 with x << 1 or x + x) is called:",
                "options": ["Dead Code Elimination", "Strength Reduction", "Loop Peeling", "Inlining"],
                "answer": 1,
                "explanation": "Strength reduction substitutes computationally cheaper operations (shifts/additions) for expensive ones (multiplication/division).",
                "difficulty": "intermediate"
            }
        ]
    },

    "Object Oriented Design": {
        "OOP Principles & Encapsulation": [
            {
                "question": "Which OOP principle bundles data and the methods that operate on that data into a single unit while restricting direct access?",
                "options": ["Inheritance", "Encapsulation", "Polymorphism", "Abstraction"],
                "answer": 1,
                "explanation": "Encapsulation shields an object's internal representation from unauthorized outside access.",
                "difficulty": "beginner"
            },
            {
                "question": "What is Polymorphism in Object-Oriented Programming?",
                "options": [
                    "The ability of a class to be instantiated only once",
                    "The capability of different classes to respond to the same message/method call in their own specific ways",
                    "Hiding variables behind private getters",
                    "Recompiling code across platforms"
                ],
                "answer": 1,
                "explanation": "Polymorphism allows objects of different subtypes to be treated uniformly through shared parent interfaces.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the primary difference between Composition and Inheritance?",
                "options": [
                    "Composition is an 'is-a' relationship; Inheritance is a 'has-a' relationship",
                    "Inheritance is an 'is-a' relationship; Composition is a 'has-a' relationship modeling component containment",
                    "Composition cannot be used in Java",
                    "Inheritance is evaluated dynamically at runtime while composition is purely static"
                ],
                "answer": 1,
                "explanation": "Inheritance models specialization ('Dog is an Animal'); Composition models containment ('Car has an Engine').",
                "difficulty": "beginner"
            },
            {
                "question": "Why is 'favor composition over inheritance' a widely recommended design guideline?",
                "options": [
                    "Composition provides looser coupling, easier testing, and dynamic runtime behavior changes without rigid hierarchies",
                    "Inheritance is prohibited in modern programming languages",
                    "Composition runs faster on microprocessors",
                    "Inheritance uses too much RAM"
                ],
                "answer": 0,
                "explanation": "Deep inheritance hierarchies cause tight coupling and fragile base class problems; composition avoids these.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is an abstract method?",
                "options": [
                    "A method that can only be called from static functions",
                    "A method declared with a signature but without implementation, requiring concrete subclasses to provide behavior",
                    "A method with private visibility",
                    "A method that accepts any data type"
                ],
                "answer": 1,
                "explanation": "Abstract methods define contracts that must be implemented by concrete subclasses.",
                "difficulty": "beginner"
            },
            {
                "question": "What is Method Overloading?",
                "options": [
                    "Overriding a method in a subclass",
                    "Defining multiple methods in the same class with identical names but different parameter lists",
                    "Invoking a method until the stack overflows",
                    "Calling a method without arguments"
                ],
                "answer": 1,
                "explanation": "Overloading allows multiple functions in the same scope to share a name if their signatures differ.",
                "difficulty": "beginner"
            }
        ],
        "SOLID Principles & UML": [
            {
                "question": "In SOLID, what does the Open/Closed Principle (OCP) state?",
                "options": [
                    "Classes should be open for modification and closed for extension",
                    "Software entities should be open for extension, but closed for modification",
                    "All methods must be declared public",
                    "Databases must be kept open during transactions"
                ],
                "answer": 1,
                "explanation": "OCP ensures systems can be extended with new features without altering existing, tested code.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which SOLID principle states that subclasses should be substitutable for their base classes without breaking program correctness?",
                "options": ["Single Responsibility Principle", "Open/Closed Principle", "Liskov Substitution Principle (LSP)", "Dependency Inversion Principle"],
                "answer": 2,
                "explanation": "LSP requires that subtypes preserve the behavior and expectations guaranteed by the supertype.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which SOLID principle advises that clients should not be forced to depend on interfaces they do not use?",
                "options": ["Single Responsibility Principle", "Interface Segregation Principle (ISP)", "Liskov Substitution Principle", "Open/Closed Principle"],
                "answer": 1,
                "explanation": "ISP advocates small, role-specific interfaces over bloated 'fat' interfaces.",
                "difficulty": "intermediate"
            },
            {
                "question": "What does the Dependency Inversion Principle (DIP) state?",
                "options": [
                    "High-level modules should not depend on low-level modules; both should depend on abstractions",
                    "Low-level modules must inherit from high-level classes",
                    "Dependencies must be declared globally",
                    "Classes should have direct access to database drivers"
                ],
                "answer": 0,
                "explanation": "DIP decouples modules by introducing interfaces and abstractions between layers.",
                "difficulty": "intermediate"
            },
            {
                "question": "In a UML Class Diagram, what does a solid line with a hollow triangular arrowhead denote?",
                "options": ["Composition", "Aggregation", "Generalization / Inheritance", "Dependency"],
                "answer": 2,
                "explanation": "A hollow triangular arrowhead pointing to a parent class signifies Generalization (Inheritance).",
                "difficulty": "intermediate"
            }
        ],
        "Creational & Structural Design Patterns": [
            {
                "question": "Which design pattern ensures a class has only one single instance and provides a global access point to it?",
                "options": ["Factory Method", "Singleton Pattern", "Prototype", "Builder"],
                "answer": 1,
                "explanation": "The Singleton pattern restricts instantiation of a class to one object (e.g., Logger, ThreadPool).",
                "difficulty": "beginner"
            },
            {
                "question": "Which GoF design pattern defines an interface for creating objects, but lets subclasses decide which class to instantiate?",
                "options": ["Factory Method Pattern", "Adapter Pattern", "Composite Pattern", "Facade Pattern"],
                "answer": 0,
                "explanation": "Factory Method decouples object creation logic from client code through inheritance.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which design pattern constructs complex objects step-by-step, allowing different representations with the same construction process?",
                "options": ["Singleton", "Builder Pattern", "Flyweight", "Bridge"],
                "answer": 1,
                "explanation": "The Builder pattern separates construction of a complex object from its representation.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which structural pattern converts the interface of a class into another interface clients expect, enabling incompatible classes to cooperate?",
                "options": ["Adapter Pattern", "Decorator Pattern", "Proxy Pattern", "Observer Pattern"],
                "answer": 0,
                "explanation": "Adapter acts as a wrapper between two incompatible interfaces (like a wall outlet adapter).",
                "difficulty": "beginner"
            },
            {
                "question": "Which pattern dynamically attaches additional responsibilities and behavior to an object without subclassing?",
                "options": ["Decorator Pattern", "State Pattern", "Strategy Pattern", "Visitor Pattern"],
                "answer": 0,
                "explanation": "Decorator wraps an object to dynamically extend functionality at runtime.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Natural Language Processing": {
        "Text Normalization & Tokenization": [
            {
                "question": "Which NLP preprocessing technique reduces words to their meaningful root dictionary form (e.g. 'running' -> 'run', 'better' -> 'good')?",
                "options": ["Stemming", "Lemmatization", "Tokenization", "Parsing"],
                "answer": 1,
                "explanation": "Lemmatization uses vocabulary and morphological analysis to return valid lemma base words.",
                "difficulty": "beginner"
            },
            {
                "question": "How does Stemming differ from Lemmatization?",
                "options": [
                    "Stemming uses grammatical rules to find true base words; Lemmatization strips prefixes",
                    "Stemming chops off word ends using crude heuristics and may produce non-words; Lemmatization uses dictionary vocabularies",
                    "Stemming only works on verbs",
                    "There is no difference between them"
                ],
                "answer": 1,
                "explanation": "Stemming (e.g. Porter Stemmer) trims suffixes blindly, whereas lemmatization ensures output words are linguistically valid.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the process of splitting continuous sentences into individual words, symbols, or subwords called?",
                "options": ["Chunking", "Tokenization", "Tagging", "Parsing"],
                "answer": 1,
                "explanation": "Tokenization breaks input text streams into constituent word, subword, or punctuation tokens.",
                "difficulty": "beginner"
            },
            {
                "question": "What are frequently occurring words like 'the', 'is', 'at', and 'which' that are often filtered out in basic text search pipelines?",
                "options": ["Stop Words", "Keywords", "Nouns", "Stem words"],
                "answer": 0,
                "explanation": "Stop words carry little discriminative semantic information in classical bag-of-words document retrieval.",
                "difficulty": "beginner"
            },
            {
                "question": "Which subword tokenization algorithm is widely used in modern LLMs like GPT and BERT?",
                "options": ["Byte Pair Encoding (BPE) / WordPiece", "Porter Stemming", "Soundex", "Edit Distance"],
                "answer": 0,
                "explanation": "BPE iteratively merges frequent character pairs, compressing common words and decomposing out-of-vocabulary terms.",
                "difficulty": "intermediate"
            },
            {
                "question": "What NLP task involves classifying each word in a sentence into its grammatical category (noun, verb, adjective)?",
                "options": ["Named Entity Recognition (NER)", "Part-of-Speech (POS) Tagging", "Dependency Parsing", "Sentiment Analysis"],
                "answer": 1,
                "explanation": "POS tagging labels tokens with grammatical classifications based on word definition and context.",
                "difficulty": "beginner"
            }
        ],
        "Statistical NLP & Word Embeddings": [
            {
                "question": "What does TF-IDF stand for in information retrieval and statistical NLP?",
                "options": [
                    "Term Frequency - Inverse Document Frequency",
                    "Total Frequency - Index Data File",
                    "Text Factor - Iterative Document Format",
                    "Token Form - Internal Dictionary Function"
                ],
                "answer": 0,
                "explanation": "TF-IDF evaluates how important a word is to a document relative to a collection of documents.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the primary breakthrough of Word2Vec (Skip-gram and CBOW) embeddings over one-hot encoding?",
                "options": [
                    "Word2Vec models text as character trees",
                    "It represents words as dense semantic vectors where semantically similar words are close in vector space",
                    "It replaces neural networks with decision trees",
                    "It only works on English words"
                ],
                "answer": 1,
                "explanation": "Word2Vec captures semantic relationships geometrically (e.g. vector('King') - vector('Man') + vector('Woman') ≈ vector('Queen')).",
                "difficulty": "intermediate"
            },
            {
                "question": "In Word2Vec, what is the objective of the Continuous Bag-of-Words (CBOW) architecture?",
                "options": [
                    "Predict context words given a target word",
                    "Predict the target word given its surrounding context words",
                    "Sort words alphabetically",
                    "Count document word occurrences"
                ],
                "answer": 1,
                "explanation": "CBOW predicts the current word from context window words, whereas Skip-Gram predicts context words from the target word.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is an N-gram in statistical language modeling?",
                "options": [
                    "A continuous sequence of n items (words or characters) from a given text sample",
                    "A metric for neural network size",
                    "A grammatical parsing rule",
                    "A compression ratio"
                ],
                "answer": 0,
                "explanation": "An n-gram models sequences of length n (unigrams, bigrams, trigrams) to estimate word sequence probabilities.",
                "difficulty": "beginner"
            },
            {
                "question": "What NLP task extracts and classifies proper names in text into predefined categories (such as Person, Organization, Location)?",
                "options": ["Named Entity Recognition (NER)", "Coreference Resolution", "Lemmatization", "Topic Modeling"],
                "answer": 0,
                "explanation": "NER locates entities in unstructured text and tags them with categories like Person, Org, or Location.",
                "difficulty": "beginner"
            }
        ],
        "Sequence Models & Transformers": [
            {
                "question": "What core mechanism in the Transformer architecture allows models to process all tokens in parallel and attend to all context positions?",
                "options": ["Convolutional Filter", "Recurrent Feedback", "Self-Attention Mechanism", "Markov Jump"],
                "answer": 2,
                "explanation": "Self-attention computes attention weights between all token pairs simultaneously without sequential recurrent bottlenecking.",
                "difficulty": "intermediate"
            },
            {
                "question": "Why do recurrent neural networks (RNNs) struggle with long-range dependencies in long text passages?",
                "options": [
                    "They cannot process strings",
                    "Vanishing and exploding gradients during backpropagation through time (BPTT)",
                    "They require unsupervised clustering",
                    "They have no activation functions"
                ],
                "answer": 1,
                "explanation": "Repeated matrix multiplications over long sequences cause gradients to vanish or explode in standard RNNs.",
                "difficulty": "intermediate"
            },
            {
                "question": "How do Transformers preserve word order information since self-attention contains no inherent recurrence?",
                "options": ["By processing one word per second", "Using Positional Encodings added to input token embeddings", "By sorting input vectors", "Using FIFO queues"],
                "answer": 1,
                "explanation": "Positional encodings (sinusoidal or learned) inject word sequence order into input embeddings.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is BERT (Bidirectional Encoder Representations from Transformers) primarily pre-trained on?",
                "options": [
                    "Next Token Prediction only",
                    "Masked Language Modeling (MLM) and Next Sentence Prediction (NSP)",
                    "Image classification",
                    "Supervised translation"
                ],
                "answer": 1,
                "explanation": "BERT masks random tokens and trains bidirectional encoders to predict them from left and right context.",
                "difficulty": "advanced"
            },
            {
                "question": "In Transformer self-attention, what three vector projections are computed for each input token?",
                "options": ["Weights, Biases, Outputs", "Query (Q), Key (K), and Value (V)", "Input, Hidden, Output", "Kernel, Filter, Stride"],
                "answer": 1,
                "explanation": "Attention is computed as softmax(Q * K^T / sqrt(d_k)) * V using Query, Key, and Value vectors.",
                "difficulty": "advanced"
            }
        ]
    },

    "Digital Electronics": {
        "Boolean Algebra & Logic Gates": [
            {
                "question": "Which logic gate outputs 0 only when all of its inputs are 1?",
                "options": ["NOR gate", "NAND gate", "XOR gate", "AND gate"],
                "answer": 1,
                "explanation": "NAND is the negation of AND; it outputs 0 only when all inputs are 1.",
                "difficulty": "beginner"
            },
            {
                "question": "Why are NAND and NOR gates called Universal Gates in digital electronics?",
                "options": [
                    "They are used in every computer in the universe",
                    "Any Boolean function or logic circuit can be implemented using exclusively NAND or exclusively NOR gates",
                    "They do not require electrical power",
                    "They operate at light speed"
                ],
                "answer": 1,
                "explanation": "Universal gates can synthesize NOT, AND, OR, and XOR operations without needing other gate types.",
                "difficulty": "beginner"
            },
            {
                "question": "According to De Morgan's Laws, what is the complement of (A + B)?",
                "options": ["A' * B'", "A' + B'", "(A * B)'", "A + B'"],
                "answer": 0,
                "explanation": "De Morgan's first theorem states: (A + B)' = A' * B'.",
                "difficulty": "beginner"
            },
            {
                "question": "Which logic gate produces a 1 output when an ODD number of its inputs are 1?",
                "options": ["XNOR gate", "XOR gate", "AND gate", "OR gate"],
                "answer": 1,
                "explanation": "XOR (Exclusive OR) functions as an odd-parity generator, outputting 1 for odd numbers of true inputs.",
                "difficulty": "beginner"
            },
            {
                "question": "In Boolean algebra, what is the simplified expression for A + A'B?",
                "options": ["A", "B", "A + B", "A * B"],
                "answer": 2,
                "explanation": "By the absorption/distributive law: A + A'B = (A + A')(A + B) = 1 * (A + B) = A + B.",
                "difficulty": "intermediate"
            },
            {
                "question": "How many cells are present in a 4-variable Karnaugh Map (K-Map)?",
                "options": ["4", "8", "16", "32"],
                "answer": 2,
                "explanation": "A K-map with n variables has 2^n cells, so a 4-variable K-map contains 2^4 = 16 cells.",
                "difficulty": "beginner"
            }
        ],
        "Combinational Logic & Arithmetic Circuits": [
            {
                "question": "How many select lines are required for an 8-to-1 Multiplexer (MUX)?",
                "options": ["2", "3", "4", "8"],
                "answer": 1,
                "explanation": "For 2^n inputs, n select lines are needed. Since 2^3 = 8, 3 select lines are required.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the primary difference between a Half Adder and a Full Adder?",
                "options": [
                    "Half adders add 4 bits; Full adders add 8 bits",
                    "A Half Adder adds two 1-bit inputs; a Full Adder adds three 1-bit inputs including an incoming carry",
                    "Half adders use analog circuits",
                    "Full adders cannot generate carries"
                ],
                "answer": 1,
                "explanation": "A half adder sums two bits (A, B); a full adder sums three inputs (A, B, Carry-in).",
                "difficulty": "beginner"
            },
            {
                "question": "What circuit converts an n-bit binary code into at most 2^n unique output lines?",
                "options": ["Multiplexer", "Decoder", "Encoder", "Demultiplexer"],
                "answer": 1,
                "explanation": "A binary decoder activates a specific one of 2^n output lines based on the n-bit input pattern.",
                "difficulty": "beginner"
            },
            {
                "question": "What is a major advantage of a Carry-Lookahead Adder (CLA) over a Ripple-Carry Adder?",
                "options": [
                    "It consumes zero power",
                    "It calculates carry bits in parallel using generate and propagate logic, drastically reducing propagation delay",
                    "It uses fewer gates than a ripple adder",
                    "It only works with negative numbers"
                ],
                "answer": 1,
                "explanation": "CLA eliminates the sequential carry propagation bottleneck across stages by precomputing carries.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which combinational component selects one of many analog or digital input signals and forwards it into a single line?",
                "options": ["Encoder", "Demultiplexer", "Multiplexer (MUX)", "Comparator"],
                "answer": 2,
                "explanation": "A Multiplexer routes one of multiple input data streams to a single shared output line.",
                "difficulty": "beginner"
            }
        ],
        "Sequential Circuits, Flip-Flops & Registers": [
            {
                "question": "What is the fundamental difference between combinational logic and sequential logic circuits?",
                "options": [
                    "Combinational circuits have memory; sequential circuits do not",
                    "Sequential circuits contain memory elements and their output depends on current inputs and past states",
                    "Sequential circuits use only NAND gates",
                    "Combinational circuits require a clock signal"
                ],
                "answer": 1,
                "explanation": "Sequential circuits incorporate feedback/memory elements (flip-flops), making outputs state-dependent.",
                "difficulty": "beginner"
            },
            {
                "question": "What invalid or indeterminate state can occur in an SR Flip-Flop?",
                "options": ["When S=0 and R=0", "When S=1 and R=1", "When S=0 and R=1", "When S=1 and R=0"],
                "answer": 1,
                "explanation": "Setting both Set and Reset to 1 creates race conditions and unpredictable outputs upon release.",
                "difficulty": "intermediate"
            },
            {
                "question": "How does a JK Flip-Flop eliminate the invalid state of the SR Flip-Flop when both inputs are 1?",
                "options": [
                    "By turning off the power",
                    "By toggling the output state (Q_next = Q')",
                    "By forcing output to 0",
                    "By holding the previous state"
                ],
                "answer": 1,
                "explanation": "When J=1 and K=1, the JK flip-flop toggles its output, resolving the indeterminate SR condition.",
                "difficulty": "intermediate"
            },
            {
                "question": "What type of flip-flop simply transfers its D input to output Q on the active clock edge (data latch)?",
                "options": ["T Flip-Flop", "D Flip-Flop", "SR Flip-Flop", "JK Flip-Flop"],
                "answer": 1,
                "explanation": "The D (Data/Delay) flip-flop stores the input bit at the clock trigger, preventing race conditions.",
                "difficulty": "beginner"
            },
            {
                "question": "How many flip-flops are required to construct a MOD-16 counter?",
                "options": ["2", "4", "8", "16"],
                "answer": 1,
                "explanation": "A MOD-N counter requires n flip-flops such that 2^n >= N. For N=16, 2^4 = 16, requiring 4 flip-flops.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Microprocessors": {
        "8085 Architecture & Pin Configuration": [
            {
                "question": "What is the word length (data bus width) and address bus width of the Intel 8085 microprocessor?",
                "options": ["8-bit data, 16-bit address", "16-bit data, 16-bit address", "8-bit data, 8-bit address", "16-bit data, 20-bit address"],
                "answer": 0,
                "explanation": "The 8085 is an 8-bit CPU with an 8-bit data bus and a 16-bit address bus (addressing up to 64 KB memory).",
                "difficulty": "beginner"
            },
            {
                "question": "Which interrupt in the Intel 8085 microprocessor has the highest priority and is non-maskable (NMI)?",
                "options": ["RST 7.5", "RST 6.5", "TRAP", "INTR"],
                "answer": 2,
                "explanation": "TRAP is non-maskable, highest priority, and vectors to memory address 0024H during critical hardware events.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the purpose of the ALE (Address Latch Enable) signal in 8085?",
                "options": [
                    "To enable DMA transfers",
                    "To demultiplex the lower order address and data bus (AD0-AD7)",
                    "To reset the internal accumulator",
                    "To signal parity errors"
                ],
                "answer": 1,
                "explanation": "ALE pulses high during the first clock period (T1) to latch valid address bits off AD0-AD7.",
                "difficulty": "intermediate"
            },
            {
                "question": "How many 8-bit general-purpose registers (excluding accumulator) are available in the 8085?",
                "options": ["4 (A, B, C, D)", "6 (B, C, D, E, H, L)", "8", "16"],
                "answer": 1,
                "explanation": "The 8085 provides 6 general-purpose registers: B, C, D, E, H, and L (pairable as BC, DE, and HL).",
                "difficulty": "beginner"
            },
            {
                "question": "Which register pair in 8085 functions as a default memory pointer (M)?",
                "options": ["B-C pair", "D-E pair", "H-L pair", "Stack Pointer"],
                "answer": 2,
                "explanation": "The HL register pair holds the 16-bit memory address for instructions operating on memory reference 'M'.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the operating supply voltage and standard clock frequency of the Intel 8085?",
                "options": ["+5V DC, 3 MHz", "+12V DC, 10 MHz", "+3.3V DC, 1 GHz", "+1.8V DC, 50 MHz"],
                "answer": 0,
                "explanation": "The classic 8085 operates on a single +5V power supply with a 3.072 MHz internal operating frequency.",
                "difficulty": "beginner"
            }
        ],
        "8086 Architecture & Register Organization": [
            {
                "question": "What is the size of the address bus and addressable memory capacity of the Intel 8086 microprocessor?",
                "options": ["16-bit address bus (64 KB)", "20-bit address bus (1 MB)", "24-bit address bus (16 MB)", "32-bit address bus (4 GB)"],
                "answer": 1,
                "explanation": "The 8086 has a 20-bit address bus allowing it to access 2^20 bytes = 1 MB of physical memory.",
                "difficulty": "beginner"
            },
            {
                "question": "What two independent functional units comprise the internal architecture of the 8086?",
                "options": [
                    "ALU and Memory Controller",
                    "BIU (Bus Interface Unit) and EU (Execution Unit)",
                    "Cache Controller and Register File",
                    "Instruction Decoder and DMA Unit"
                ],
                "answer": 1,
                "explanation": "BIU handles instruction prefetching and bus cycles; EU decodes and executes instructions in parallel.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the size of the prefetch instruction queue in the 8086 Bus Interface Unit?",
                "options": ["2 bytes", "4 bytes", "6 bytes", "16 bytes"],
                "answer": 2,
                "explanation": "The 8086 maintains a 6-byte FIFO instruction queue enabling overlapped instruction fetch and execution.",
                "difficulty": "intermediate"
            },
            {
                "question": "How is a 20-bit physical address calculated in 8086 memory segmentation?",
                "options": [
                    "Physical Address = Segment Register + Offset",
                    "Physical Address = (Segment Register * 16) + Offset",
                    "Physical Address = Segment Register * Offset",
                    "Physical Address = (Offset * 16) + Segment Register"
                ],
                "answer": 1,
                "explanation": "The segment register is shifted left by 4 bits (multiplied by 16 or 10H) and added to the 16-bit offset.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which 8086 segment register holds the base address of the currently executing program instructions?",
                "options": ["Data Segment (DS)", "Code Segment (CS)", "Stack Segment (SS)", "Extra Segment (ES)"],
                "answer": 1,
                "explanation": "CS (Code Segment) points to the active code segment, referenced in conjunction with the IP (Instruction Pointer).",
                "difficulty": "beginner"
            }
        ],
        "Assembly Programming, Addressing & Interrupts": [
            {
                "question": "In 8086 assembly, what addressing mode is illustrated by the instruction: MOV AX, [BX + SI + 10H]?",
                "options": ["Direct Addressing", "Based Indexed with Displacement Addressing", "Register Indirect", "Immediate Addressing"],
                "answer": 1,
                "explanation": "The effective address combines a base register (BX), index register (SI), and constant displacement (10H).",
                "difficulty": "intermediate"
            },
            {
                "question": "Which flag in 8086 is set when an arithmetic or logical operation yields a result of zero?",
                "options": ["Carry Flag (CF)", "Zero Flag (ZF)", "Sign Flag (SF)", "Parity Flag (PF)"],
                "answer": 1,
                "explanation": "ZF is set to 1 whenever the outcome of an ALU operation is exactly zero.",
                "difficulty": "beginner"
            },
            {
                "question": "How many total interrupt types (software and hardware) are supported in the 8086 vector table?",
                "options": ["8", "64", "256", "1024"],
                "answer": 2,
                "explanation": "8086 supports 256 interrupts (Type 0 to Type 255), each occupying 4 bytes in the Interrupt Vector Table (IVT).",
                "difficulty": "intermediate"
            },
            {
                "question": "What 8086 assembly instruction decrements register CX and jumps to a label if CX is not zero?",
                "options": ["JNZ label", "LOOP label", "DEC CX", "JCXZ label"],
                "answer": 1,
                "explanation": "LOOP decrements CX by 1 and branches to the designated target if CX != 0.",
                "difficulty": "beginner"
            },
            {
                "question": "Where is the Interrupt Vector Table (IVT) located in 8086 physical memory?",
                "options": ["At the top of memory (FFFF0H)", "At the lowest 1 KB of memory (00000H to 003FFH)", "In BIOS ROM", "In the stack segment"],
                "answer": 1,
                "explanation": "The IVT occupies the first 1024 bytes (00000H to 003FFH) to hold 256 four-byte segment:offset vector pointers.",
                "difficulty": "advanced"
            }
        ]
    },

    "Internet of Things": {
        "IoT Architecture & Communication Protocols": [
            {
                "question": "Which lightweight publish-subscribe messaging protocol is widely used for resource-constrained IoT sensors?",
                "options": ["HTTP", "MQTT (Message Queuing Telemetry Transport)", "FTP", "SMTP"],
                "answer": 1,
                "explanation": "MQTT is designed for low bandwidth, high latency networks with minimal packet header overhead (2 bytes).",
                "difficulty": "beginner"
            },
            {
                "question": "Which IoT protocol operates over UDP to provide RESTful interaction for constrained devices (equivalent to HTTP)?",
                "options": ["CoAP (Constrained Application Protocol)", "XMPP", "AMQP", "WebSocket"],
                "answer": 0,
                "explanation": "CoAP runs over UDP, offering lightweight GET/POST/PUT/DELETE interactions for constrained embedded nodes.",
                "difficulty": "intermediate"
            },
            {
                "question": "What wireless technology provides long-range, low-power telemetry transmission (up to 10-15 km) for smart cities?",
                "options": ["Bluetooth Classic", "LoRaWAN", "NFC", "Wi-Fi 6"],
                "answer": 1,
                "explanation": "LoRaWAN (Long Range Wide Area Network) uses chirped spread spectrum modulation for low-power long-distance communication.",
                "difficulty": "beginner"
            },
            {
                "question": "What are the four architectural layers of a standard IoT reference model?",
                "options": [
                    "Sensing/Perception, Network/Transport, Data Processing, Application Layer",
                    "Frontend, Backend, Database, Cloud",
                    "Physical, Digital, Mechanical, Electrical",
                    "Input, Output, Memory, CPU"
                ],
                "answer": 0,
                "explanation": "The 4 layers encompass Sensing (Perception), Network transmission, Data/Middleware processing, and User Application.",
                "difficulty": "intermediate"
            },
            {
                "question": "What wireless personal area network standard is based on IEEE 802.15.4 and designed for low-power mesh networking?",
                "options": ["Zigbee", "Ethernet", "Cellular LTE", "WiMAX"],
                "answer": 0,
                "explanation": "Zigbee builds self-healing, low-data-rate mesh topologies for home automation and industrial sensors.",
                "difficulty": "intermediate"
            },
            {
                "question": "In MQTT architecture, what central component receives all published messages and routes them to subscribed clients?",
                "options": ["Gateway", "MQTT Broker", "Edge Router", "Access Point"],
                "answer": 1,
                "explanation": "The MQTT Broker orchestrates topic subscriptions and message distribution across publishers and subscribers.",
                "difficulty": "beginner"
            }
        ],
        "Sensors, Actuators & Microcontrollers": [
            {
                "question": "What popular dual-core microcontroller module features integrated 2.4 GHz Wi-Fi and Bluetooth BLE?",
                "options": ["Arduino Uno (ATmega328P)", "ESP32", "8051", "PIC16F877A"],
                "answer": 1,
                "explanation": "The Espressif ESP32 features dual Tensilica Xtensa cores, Wi-Fi, and BLE, making it an IoT industry favorite.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the difference between a Sensor and an Actuator in IoT systems?",
                "options": [
                    "Sensors convert physical phenomena into electrical signals; Actuators convert electrical signals into physical action",
                    "Sensors move motors; Actuators measure temperature",
                    "Sensors are digital; Actuators are always analog",
                    "There is no distinction"
                ],
                "answer": 0,
                "explanation": "Sensors perceive environmental conditions (temperature, light); Actuators execute physical responses (valves, motors).",
                "difficulty": "beginner"
            },
            {
                "question": "Which serial synchronous communication bus uses two bidirectional lines: SDA (Serial Data) and SCL (Serial Clock)?",
                "options": ["SPI", "I2C (Inter-Integrated Circuit)", "UART", "RS-232"],
                "answer": 1,
                "explanation": "I2C utilizes two lines (SDA and SCL) with device addressing to connect multiple peripheral sensors.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which serial protocol uses separate MOSI, MISO, SCK, and SS lines for high-speed full-duplex communication?",
                "options": ["I2C", "SPI (Serial Peripheral Interface)", "1-Wire", "CAN Bus"],
                "answer": 1,
                "explanation": "SPI uses four wires (Master-Out-Slave-In, Master-In-Slave-Out, Clock, Slave Select) for high-speed data transfer.",
                "difficulty": "intermediate"
            },
            {
                "question": "What electronic circuit converts continuous analog sensor signals (e.g. from a thermistor) into discrete digital values?",
                "options": ["DAC", "ADC (Analog-to-Digital Converter)", "PWM", "Optocoupler"],
                "answer": 1,
                "explanation": "An ADC samples continuous physical voltages and quantizes them into binary values for microcontrollers.",
                "difficulty": "beginner"
            }
        ],
        "Cloud IoT Platforms & Security": [
            {
                "question": "What is Edge Computing in the context of IoT?",
                "options": [
                    "Placing cloud datacenters on mountain tops",
                    "Processing and analyzing data locally near the data source/devices rather than transmitting everything to a centralized cloud",
                    "Running machine learning on quantum computers",
                    "Encrypting network cables with physical shields"
                ],
                "answer": 1,
                "explanation": "Edge computing reduces network bandwidth and latency by filtering, preprocessing, and acting on telemetry locally.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is a 'Digital Twin' in IoT and industrial engineering?",
                "options": [
                    "A duplicate backup hardware sensor",
                    "A dynamic virtual software replica of a physical device, machine, or system updated in real time with sensor telemetry",
                    "Two microcontrollers running identical firmware",
                    "A dual-band Wi-Fi antenna"
                ],
                "answer": 1,
                "explanation": "Digital twins simulate and monitor physical assets in real-time for predictive maintenance and optimization.",
                "difficulty": "intermediate"
            },
            {
                "question": "What major security vulnerability frequently affects low-cost commercial IoT consumer gadgets?",
                "options": [
                    "Lack of firmware updates, hardcoded default credentials, and unencrypted plaintext communication",
                    "Too many quantum encryption keys",
                    "Excessive processor cooling",
                    "Over-reliance on fiber-optic cables"
                ],
                "answer": 0,
                "explanation": "Weak default passwords and unpatched firmware allow IoT devices to be hijacked into massive botnets (like Mirai).",
                "difficulty": "beginner"
            },
            {
                "question": "What mechanism enables IoT devices in the field to receive bug fixes, security patches, and firmware updates remotely?",
                "options": ["Manual soldering", "OTA (Over-The-Air) Firmware Updates", "UART jumper flashing", "EEPROM replacement"],
                "answer": 1,
                "explanation": "OTA updates allow connected devices to download and verify signed firmware binaries over wireless networks.",
                "difficulty": "beginner"
            },
            {
                "question": "Which standard industrial bus protocol is widely used in automotive networks to connect vehicle ECUs without a host computer?",
                "options": ["CAN Bus (Controller Area Network)", "I2C", "Ethernet 100G", "SCSI"],
                "answer": 0,
                "explanation": "CAN bus is a robust differential broadcast vehicle bus standard allowing ECUs to communicate reliably.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Big Data Analytics": {
        "Big Data Characteristics & Hadoop HDFS": [
            {
                "question": "What are the original '3 Vs' that characterize Big Data?",
                "options": ["Volume, Velocity, and Variety", "Vector, Value, and Validity", "Virtualization, Verification, and Volume", "Variable, Visual, and Value"],
                "answer": 0,
                "explanation": "Big Data is classically defined by massive Volume, rapid Velocity of ingestion, and structural Variety of sources.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the default block size in modern Apache Hadoop HDFS (version 3.x)?",
                "options": ["64 KB", "4 MB", "128 MB", "1 GB"],
                "answer": 2,
                "explanation": "HDFS utilizes a large default block size of 128 MB to minimize disk seek overhead during large streaming reads.",
                "difficulty": "intermediate"
            },
            {
                "question": "What central node in Apache Hadoop HDFS manages file system namespace, metadata, and block mapping?",
                "options": ["DataNode", "NameNode", "TaskTracker", "NodeManager"],
                "answer": 1,
                "explanation": "The NameNode maintains directory trees and tracks where data blocks are physically distributed across DataNodes.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the standard replication factor for data blocks in Apache Hadoop HDFS?",
                "options": ["1", "2", "3", "5"],
                "answer": 2,
                "explanation": "HDFS replicates each data block across 3 distinct nodes (often across different racks) for fault tolerance.",
                "difficulty": "beginner"
            },
            {
                "question": "What happens if a DataNode in a Hadoop cluster crashes or fails to send heartbeats?",
                "options": [
                    "The entire Hadoop cluster shuts down",
                    "The NameNode detects the failure and orchestrates re-replication of under-replicated blocks to healthy nodes",
                    "All data stored on that node is permanently lost with no recovery",
                    "Data blocks are converted to local disk files"
                ],
                "answer": 1,
                "explanation": "The NameNode automatically initiates re-replication to maintain the target replication factor across active nodes.",
                "difficulty": "intermediate"
            },
            {
                "question": "What resource management layer was introduced in Hadoop 2.0 to decouple cluster scheduling from MapReduce?",
                "options": ["Mesos", "YARN (Yet Another Resource Negotiator)", "Zookeeper", "Chubby"],
                "answer": 1,
                "explanation": "YARN manages CPU and memory resources across distributed nodes, enabling Spark, Flink, and MapReduce to share clusters.",
                "difficulty": "intermediate"
            }
        ],
        "MapReduce & Apache Spark": [
            {
                "question": "What is the primary distributed in-memory data abstraction provided by Apache Spark?",
                "options": ["DataFrame", "Resilient Distributed Dataset (RDD)", "Hadoop Table", "GraphX"],
                "answer": 1,
                "explanation": "RDDs are immutable, fault-tolerant distributed collections of objects evaluated lazily in RAM.",
                "difficulty": "beginner"
            },
            {
                "question": "Why is Apache Spark significantly faster (up to 100x) than classical Hadoop MapReduce for iterative workloads?",
                "options": [
                    "Spark runs purely on GPU clusters",
                    "Spark processes data in-memory without constantly writing intermediate shuffle results to disk",
                    "Spark doesn't support fault tolerance",
                    "Spark uses compiled assembly code"
                ],
                "answer": 1,
                "explanation": "Spark avoids disk I/O bottlenecks by caching intermediate computation pipelines directly in distributed RAM.",
                "difficulty": "beginner"
            },
            {
                "question": "In MapReduce, what phase sorts and groups data by key between the Map and Reduce steps?",
                "options": ["Filter Phase", "Shuffle and Sort Phase", "Partition Action", "Combiner Stage"],
                "answer": 1,
                "explanation": "The Shuffle and Sort phase transfers mapper outputs across the network, grouping identical keys for reducer processing.",
                "difficulty": "intermediate"
            },
            {
                "question": "In Apache Spark, what is the difference between a Transformation and an Action?",
                "options": [
                    "Transformations are executed immediately; Actions are lazy",
                    "Transformations lazily build an execution graph (DAG); Actions trigger actual computation and return results",
                    "Transformations delete data; Actions write to disk",
                    "There is no difference"
                ],
                "answer": 1,
                "explanation": "Transformations (map, filter) define execution DAGs lazily; Actions (count, collect, save) execute the plan.",
                "difficulty": "intermediate"
            },
            {
                "question": "What Spark module provides high-level DataFrame and Dataset APIs with SQL query capabilities?",
                "options": ["Spark Streaming", "Spark SQL", "MLlib", "GraphX"],
                "answer": 1,
                "explanation": "Spark SQL offers structured data querying with Catalyst optimizer and Tungsten execution engine.",
                "difficulty": "beginner"
            }
        ],
        "NoSQL Databases & Stream Processing": [
            {
                "question": "Which NoSQL database category does Apache Cassandra and HBase belong to?",
                "options": ["Document Stores", "Wide-Column / Column-Family Stores", "Graph Databases", "Key-Value Stores"],
                "answer": 1,
                "explanation": "Cassandra and HBase organize data into sparse, distributed wide-column families inspired by Google Bigtable.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which open-source distributed event streaming platform is designed for high-throughput, fault-tolerant publish-subscribe pipelines?",
                "options": ["Apache Kafka", "Apache Lucene", "MongoDB", "Redis"],
                "answer": 0,
                "explanation": "Apache Kafka uses distributed commit logs to handle millions of real-time streaming events per second.",
                "difficulty": "beginner"
            },
            {
                "question": "What document-oriented NoSQL database stores schema-less records as BSON (binary JSON) documents?",
                "options": ["Neo4j", "MongoDB", "Redis", "Cassandra"],
                "answer": 1,
                "explanation": "MongoDB stores flexible, hierarchical semi-structured documents in BSON format.",
                "difficulty": "beginner"
            },
            {
                "question": "What in-memory key-value data store is widely used as a high-speed distributed cache and session store?",
                "options": ["PostgreSQL", "Redis", "CouchDB", "HDFS"],
                "answer": 1,
                "explanation": "Redis provides sub-millisecond in-memory data storage supporting strings, hashes, sets, and pub/sub.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the Lambda Architecture in Big Data processing?",
                "options": [
                    "An architecture that deploys only AWS Lambda serverless functions",
                    "A data-processing architecture combining a batch layer for comprehensive accuracy and a speed layer for real-time streaming",
                    "A neural network architecture for NLP",
                    "A relational database replication format"
                ],
                "answer": 1,
                "explanation": "Lambda Architecture merges real-time low-latency stream views with accurate, comprehensive historical batch views.",
                "difficulty": "advanced"
            }
        ]
    }
}
