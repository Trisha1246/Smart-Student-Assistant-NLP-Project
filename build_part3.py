# Part 3: Subjects 21-28 (Computer Graphics, Discrete Mathematics, Mobile App Development,
# Information Security, Distributed Systems, Robotics, Web Development, DevOps)

PART3_DATA = {
    "Computer Graphics": {
        "2D Transformations & Matrix Operations": [
            {
                "question": "Which homogeneous coordinate transformation matrix represents 2D translation by (dx, dy)?",
                "options": [
                    "[[1, 0, dx], [0, 1, dy], [0, 0, 1]]",
                    "[[dx, 0, 0], [0, dy, 0], [0, 0, 1]]",
                    "[[cos(t), -sin(t), 0], [sin(t), cos(t), 0], [0, 0, 1]]",
                    "[[1, dy, 0], [dx, 1, 0], [0, 0, 1]]"
                ],
                "answer": 0,
                "explanation": "Homogeneous coordinates enable linear affine transformations including translation by representing 2D points as [x, y, 1]^T.",
                "difficulty": "intermediate"
            },
            {
                "question": "Why are homogeneous coordinates (3x3 for 2D, 4x4 for 3D) used extensively in computer graphics?",
                "options": [
                    "To save video memory",
                    "To represent translations, rotations, and scalings as uniform matrix multiplications that can be composed together",
                    "To replace floating point numbers with integers",
                    "Because GPUs cannot add numbers"
                ],
                "answer": 1,
                "explanation": "Homogeneous coordinates unify translations and linear transforms into composable matrix multiplications.",
                "difficulty": "intermediate"
            },
            {
                "question": "What transformation distorts the shape of an object along an axis proportionally to its coordinate on the other axis?",
                "options": ["Scaling", "Shearing", "Rotation", "Reflection"],
                "answer": 1,
                "explanation": "Shearing shifts coordinate values along one axis proportionally to values on an orthogonal axis (e.g. x' = x + sh_x * y).",
                "difficulty": "beginner"
            },
            {
                "question": "What is the result of rotating a 2D point (x, y) counterclockwise by 90 degrees about the origin?",
                "options": ["(-y, x)", "(y, -x)", "(-x, -y)", "(x, y)"],
                "answer": 0,
                "explanation": "Using rotation matrix for theta=90 deg: x' = x*cos(90) - y*sin(90) = -y, and y' = x*sin(90) + y*cos(90) = x.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the composite matrix of two successive translations T(dx1, dy1) followed by T(dx2, dy2)?",
                "options": ["T(dx1*dx2, dy1*dy2)", "T(dx1 + dx2, dy1 + dy2)", "T(dx1 - dx2, dy1 - dy2)", "Identity matrix"],
                "answer": 1,
                "explanation": "Successive translations are additive: the combined shift is simply (dx1 + dx2, dy1 + dy2).",
                "difficulty": "beginner"
            },
            {
                "question": "In 3D viewing pipelines, what transformation projects 3D scene objects onto a 2D view plane such that parallel lines converge at vanishing points?",
                "options": ["Orthographic Projection", "Perspective Projection", "Isometric Projection", "Oblique Projection"],
                "answer": 1,
                "explanation": "Perspective projection mimics human vision and cameras by dividing coordinates by depth (z), causing distant objects to appear smaller.",
                "difficulty": "intermediate"
            }
        ],
        "Rasterization & Line Drawing Algorithms": [
            {
                "question": "Which integer-based incremental algorithm draws smooth raster lines without requiring floating-point multiplication or division?",
                "options": ["DDA Algorithm", "Bresenham's Line Algorithm", "Midpoint Circle Algorithm", "Painter's Algorithm"],
                "answer": 1,
                "explanation": "Bresenham's algorithm utilizes purely incremental integer additions and sign tests on a decision parameter.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which classic line clipping algorithm assigns a 4-bit region code (outcode) to endpoints to clip line segments against a viewport?",
                "options": ["Cohen-Sutherland Algorithm", "Sutherland-Hodgman", "Liang-Barsky", "Weiler-Atherton"],
                "answer": 0,
                "explanation": "Cohen-Sutherland partitions the 2D plane into 9 regions using 4-bit outcodes (Top, Bottom, Right, Left) to perform fast trivial accepts/rejects.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the primary visual defect in Digital Differential Analyzer (DDA) line drawing?",
                "options": [
                    "Lines cannot have negative slopes",
                    "Accumulation of round-off errors due to floating-point additions causing drift along long line segments",
                    "It only works on 4K monitors",
                    "It causes monitor refresh flicker"
                ],
                "answer": 1,
                "explanation": "DDA relies on floating-point increments that accumulate rounding errors and requires costly round() operations at each step.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which polygon clipping algorithm clips an arbitrary polygon against each rectangular clip window boundary in sequential succession?",
                "options": ["Cohen-Sutherland", "Sutherland-Hodgman Algorithm", "Bresenham", "Flood Fill"],
                "answer": 1,
                "explanation": "Sutherland-Hodgman clips vertices against left, right, bottom, and top clipping boundaries sequentially.",
                "difficulty": "intermediate"
            },
            {
                "question": "What technique reduces the jagged stair-step artifacts (aliasing) visible along high-contrast diagonal edges on raster displays?",
                "options": ["Dithering", "Anti-Aliasing (e.g. Supersampling, MSAA)", "Z-buffering", "Backface culling"],
                "answer": 1,
                "explanation": "Anti-aliasing blends pixel colors along edge boundaries based on subpixel coverage fractions to soften jagged stairs.",
                "difficulty": "beginner"
            }
        ],
        "3D Viewing, Clipping & Shading": [
            {
                "question": "What hardware buffer stores the depth value of every pixel to solve the hidden-surface removal (visibility) problem?",
                "options": ["Frame Buffer", "Z-Buffer (Depth Buffer)", "Stencil Buffer", "Accumulation Buffer"],
                "answer": 1,
                "explanation": "The Z-buffer tracks the closest distance from the camera for each pixel coordinate, overwriting colors only when new z < existing z.",
                "difficulty": "beginner"
            },
            {
                "question": "In computer graphics shading, what is the difference between Gouraud Shading and Phong Shading?",
                "options": [
                    "Gouraud calculates lighting at polygon vertices and interpolates colors; Phong interpolates normal vectors across the face and computes lighting per pixel",
                    "Gouraud is ray tracing; Phong is rasterization",
                    "Phong cannot produce specular highlights",
                    "Gouraud requires GPU ray tracing"
                ],
                "answer": 0,
                "explanation": "Phong shading interpolates surface normals across polygon interiors and calculates lighting per pixel, producing accurate specular highlights.",
                "difficulty": "intermediate"
            },
            {
                "question": "What optimization discards 3D polygon triangles whose normal vectors point away from the camera viewpoint?",
                "options": ["Frustum Clipping", "Back-Face Culling", "Occlusion Culling", "Level of Detail (LOD)"],
                "answer": 1,
                "explanation": "Back-face culling computes the dot product between polygon normals and viewing vectors, skipping non-visible reverse-facing triangles.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the three-component empirical lighting model developed by Bui Tuong Phong composed of?",
                "options": [
                    "Ambient, Diffuse, and Specular reflection",
                    "Red, Green, and Blue photons",
                    "Refraction, Diffraction, and Absorption",
                    "Direct, Indirect, and Shadow rays"
                ],
                "answer": 0,
                "explanation": "The Phong reflection model sums Ambient (base indirect light), Diffuse (Lambertian scatter), and Specular (glossy reflection).",
                "difficulty": "intermediate"
            },
            {
                "question": "What modern rendering technique simulates realistic lighting by tracing the physical paths of light rays as they bounce and interact with surfaces?",
                "options": ["Rasterization", "Ray Tracing / Path Tracing", "Gouraud Shading", "Bresenham Algorithm"],
                "answer": 1,
                "explanation": "Ray tracing simulates optics (reflection, refraction, soft shadows, caustics) by calculating ray intersections backwards from camera to lights.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Discrete Mathematics": {
        "Set Theory, Relations & Functions": [
            {
                "question": "If a finite set S has n elements, how many distinct subsets does its power set P(S) contain?",
                "options": ["n^2", "2^n", "2n", "n!"],
                "answer": 1,
                "explanation": "Each element can independently be either included or excluded, yielding 2^n total possible subsets.",
                "difficulty": "beginner"
            },
            {
                "question": "A binary relation R on set A is an Equivalence Relation if and only if it satisfies which three properties?",
                "options": [
                    "Reflexive, Symmetric, and Transitive",
                    "Reflexive, Antisymmetric, and Transitive",
                    "Irreflexive, Symmetric, and Asymmetric",
                    "Injective, Surjective, and Bijective"
                ],
                "answer": 0,
                "explanation": "An equivalence relation partitions a set into disjoint equivalence classes by being reflexive, symmetric, and transitive.",
                "difficulty": "beginner"
            },
            {
                "question": "What type of function is both Injective (one-to-one) and Surjective (onto)?",
                "options": ["Bijective function (one-to-one correspondence)", "Homomorphism", "Partial function", "Identity projection"],
                "answer": 0,
                "explanation": "A bijection maps distinct inputs to distinct outputs such that every element in the codomain is mapped, permitting inverse functions.",
                "difficulty": "beginner"
            },
            {
                "question": "What principle states that if n items are put into m containers and n > m, then at least one container must contain more than one item?",
                "options": ["Well-Ordering Principle", "Pigeonhole Principle (Dirichlet's Drawer Principle)", "Inclusion-Exclusion Principle", "Mathematical Induction"],
                "answer": 1,
                "explanation": "The Pigeonhole Principle proves that distributing n items across fewer than n bins guarantees collisions.",
                "difficulty": "beginner"
            },
            {
                "question": "A relation that is Reflexive, Antisymmetric, and Transitive is called what?",
                "options": ["Equivalence Relation", "Partial Order Relation (Poset)", "Strict Total Order", "Circular Relation"],
                "answer": 1,
                "explanation": "A partially ordered set (Poset) is defined by a relation that is reflexive, antisymmetric, and transitive (like '<=' on numbers).",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the cardinality of the Cartesian product A x B if |A| = 4 and |B| = 7?",
                "options": ["11", "28", "2^11", "2^28"],
                "answer": 1,
                "explanation": "The Cartesian product contains all ordered pairs (a, b), with cardinality equal to |A| * |B| = 4 * 7 = 28.",
                "difficulty": "beginner"
            }
        ],
        "Propositional Logic & Proof Methods": [
            {
                "question": "What is a compound proposition called that is ALWAYS true regardless of the truth values of its constituent variables?",
                "options": ["Contradiction", "Tautology", "Contingency", "Predicate"],
                "answer": 1,
                "explanation": "A tautology is a propositional formula that evaluates to True under all possible truth value assignments (e.g. P or ~P).",
                "difficulty": "beginner"
            },
            {
                "question": "What is the contrapositive of the conditional statement 'If P, then Q' (P -> Q)?",
                "options": ["If Q, then P", "If not P, then not Q", "If not Q, then not P (~Q -> ~P)", "P and not Q"],
                "answer": 2,
                "explanation": "The contrapositive (~Q -> ~P) is logically equivalent to the original conditional statement (P -> Q).",
                "difficulty": "beginner"
            },
            {
                "question": "Which inference rule states that if both 'P' and 'P -> Q' are true, then 'Q' must be true?",
                "options": ["Modus Tollens", "Modus Ponens", "Hypothetical Syllogism", "Disjunctive Syllogism"],
                "answer": 1,
                "explanation": "Modus Ponens (the law of detachment) deduces the conclusion Q from the premise P and conditional P -> Q.",
                "difficulty": "beginner"
            },
            {
                "question": "What proof method proves a statement P(n) for all integers n >= 1 by verifying P(1) and showing P(k) -> P(k+1)?",
                "options": ["Proof by Contradiction", "Mathematical Induction", "Proof by Exhaustion", "Constructive Proof"],
                "answer": 1,
                "explanation": "Mathematical induction establishes truth across inductive steps anchored by a base case.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the negation of the quantified statement: 'For all x, P(x)' (forall x, P(x))?",
                "options": ["For all x, not P(x)", "There exists x such that not P(x) (exists x, ~P(x))", "There exists x such that P(x)", "No x satisfies P(x)"],
                "answer": 1,
                "explanation": "Negating a universal quantifier changes it into an existential quantifier: ~(forall x, P(x)) <=> exists x, ~P(x).",
                "difficulty": "intermediate"
            }
        ],
        "Graph Theory, Trees & Recurrence Relations": [
            {
                "question": "In graph theory, what is a closed walk that visits every vertex of a graph exactly once called?",
                "options": ["Eulerian Circuit", "Hamiltonian Cycle", "Bipartite Path", "Spanning Tree"],
                "answer": 1,
                "explanation": "A Hamiltonian cycle visits every vertex exactly once, whereas an Eulerian path traverses every edge once.",
                "difficulty": "intermediate"
            },
            {
                "question": "What theorem states that a connected undirected graph has an Eulerian circuit if and only if:",
                "options": [
                    "Every vertex has an even degree",
                    "It has no cycles",
                    "It is a planar graph",
                    "It has chromatic number 2"
                ],
                "answer": 0,
                "explanation": "Euler proved a connected graph contains an Euler tour if and only if every single vertex has an even degree.",
                "difficulty": "intermediate"
            },
            {
                "question": "How many edges does a tree with n vertices have?",
                "options": ["n", "n - 1", "n + 1", "2n"],
                "answer": 1,
                "explanation": "A tree is an acyclic connected graph; any tree with n vertices contains exactly n - 1 edges.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the maximum number of colors needed to color any planar graph such that no two adjacent vertices share the same color?",
                "options": ["3", "4 (Four Color Theorem)", "5", "6"],
                "answer": 1,
                "explanation": "The Four Color Theorem states that four colors suffice to color any planar map without adjacent conflicts.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the solution to the Fibonacci recurrence relation T(n) = T(n-1) + T(n-2) with F(0)=0, F(1)=1 as n approaches infinity?",
                "options": ["Polynomial O(n^2)", "Exponential O(phi^n) where phi ≈ 1.618 (Golden Ratio)", "Logarithmic O(log n)", "Linear O(n)"],
                "answer": 1,
                "explanation": "Binet's formula shows Fibonacci numbers grow exponentially proportional to the golden ratio phi^n / sqrt(5).",
                "difficulty": "intermediate"
            }
        ]
    },

    "Mobile App Development": {
        "Android Architecture & Components": [
            {
                "question": "In the Android Activity lifecycle, which callback method is invoked when an activity enters the interactive foreground?",
                "options": ["onCreate()", "onStart()", "onResume()", "onRestart()"],
                "answer": 2,
                "explanation": "onResume() is called when the Activity is in the foreground and actively accepting user input.",
                "difficulty": "beginner"
            },
            {
                "question": "Which Android app component is used to perform long-running background operations without providing a user interface?",
                "options": ["Activity", "Service", "Broadcast Receiver", "Content Provider"],
                "answer": 1,
                "explanation": "A Service runs in the background to handle tasks like network downloads or audio playback without UI.",
                "difficulty": "beginner"
            },
            {
                "question": "What XML file serves as the root configuration declaring app permissions, activities, services, and hardware features in Android?",
                "options": ["build.gradle", "AndroidManifest.xml", "strings.xml", "settings.json"],
                "answer": 1,
                "explanation": "AndroidManifest.xml presents essential metadata to the Android runtime system and Google Play.",
                "difficulty": "beginner"
            },
            {
                "question": "What asynchronous messaging object is used in Android to request an action from another app component or launch activities?",
                "options": ["Bundle", "Intent", "Parcelable", "ThreadHandler"],
                "answer": 1,
                "explanation": "Intents (Explicit or Implicit) bind separate components at runtime for inter-process communication.",
                "difficulty": "beginner"
            },
            {
                "question": "What component allows an app to share structured data with other applications securely (e.g. Contacts database)?",
                "options": ["Service", "Content Provider", "Shared Preferences", "WorkManager"],
                "answer": 1,
                "explanation": "Content Providers encapsulate relational data access via standard URIs (content://).",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the current official primary programming language recommended by Google for modern Android development?",
                "options": ["Java", "Kotlin", "Dart", "C++"],
                "answer": 1,
                "explanation": "Google designated Kotlin as the preferred, official language for Android development in 2019.",
                "difficulty": "beginner"
            }
        ],
        "UI Layouts, Views & Event Handling": [
            {
                "question": "Which modern declarative UI toolkit is recommended by Google for building native Android user interfaces without XML?",
                "options": ["Jetpack Compose", "Flutter", "SwiftUI", "React Native"],
                "answer": 0,
                "explanation": "Jetpack Compose is Android's modern declarative toolkit using Kotlin composable functions.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which Android view component efficiently displays large datasets by recycling views as items scroll off screen?",
                "options": ["ScrollView", "RecyclerView", "ListView", "LinearLayout"],
                "answer": 1,
                "explanation": "RecyclerView uses the ViewHolder pattern to pool and recycle view memory for smooth scrolling performance.",
                "difficulty": "beginner"
            },
            {
                "question": "Which legacy XML layout allows child views to be positioned flexibly relative to sibling views and parent edges?",
                "options": ["LinearLayout", "FrameLayout", "ConstraintLayout", "GridLayout"],
                "answer": 2,
                "explanation": "ConstraintLayout flattens view hierarchies by anchoring views using relative constraints.",
                "difficulty": "intermediate"
            },
            {
                "question": "In Android, how do you handle configuration changes (like screen rotation) without losing UI state?",
                "options": [
                    "By disabling screen rotation completely",
                    "By storing data in Android Architecture Component ViewModel and using SavedStateHandle",
                    "By restarting the phone",
                    "By saving data in static global variables"
                ],
                "answer": 1,
                "explanation": "ViewModels survive configuration destruction and recreation cycles, retaining presentation state.",
                "difficulty": "intermediate"
            },
            {
                "question": "What Android unit of measure scales automatically based on physical screen pixel density to ensure consistent visual sizing?",
                "options": ["px (pixels)", "dp / dip (density-independent pixels)", "in (inches)", "pt (points)"],
                "answer": 1,
                "explanation": "1 dp corresponds to one physical pixel on a 160 dpi baseline screen, scaling uniformly across displays.",
                "difficulty": "beginner"
            }
        ],
        "Data Persistence & Cross-Platform Frameworks": [
            {
                "question": "In Flutter development, what foundational structural element defines the UI hierarchy?",
                "options": ["Activity", "Component", "Widget (Stateless or Stateful)", "ViewController"],
                "answer": 2,
                "explanation": "In Flutter, everything is a Widget, representing declarative immutable descriptions of the user interface.",
                "difficulty": "beginner"
            },
            {
                "question": "What programming language powers Google's cross-platform UI framework Flutter?",
                "options": ["TypeScript", "Dart", "Swift", "Kotlin"],
                "answer": 1,
                "explanation": "Flutter applications are written in Dart, which compiles to ARM and x86 native machine code.",
                "difficulty": "beginner"
            },
            {
                "question": "Which SQLite abstraction library is part of Android Jetpack for robust, compile-time verified database access?",
                "options": ["Room Persistence Library", "Realm", "CoreData", "Hibernate"],
                "answer": 0,
                "explanation": "Room provides an ORM mapping layer over SQLite with compile-time SQL verification and Rx/Flow observables.",
                "difficulty": "intermediate"
            },
            {
                "question": "In React Native, what JavaScript-based component bridge or modern JSI architecture communicates with native iOS/Android APIs?",
                "options": ["JavaScriptBridge / JSI (JavaScript Interface)", "CORBA", "AJAX", "WebKit DOM"],
                "answer": 0,
                "explanation": "React Native executes JavaScript on Hermes/V8 and interacts with native platform controls via JSI/bridge.",
                "difficulty": "intermediate"
            },
            {
                "question": "What Android mechanism is recommended for persisting small primitive key-value pairs (like user settings)?",
                "options": ["SharedPreferences / Jetpack DataStore", "Raw text file on SD card", "Remote SQL Server", "Content Provider"],
                "answer": 0,
                "explanation": "DataStore (and legacy SharedPreferences) persists key-value properties asynchronously in app sandbox storage.",
                "difficulty": "beginner"
            }
        ]
    },

    "Information Security": {
        "CIA Triad & Security Principles": [
            {
                "question": "Which access control model determines user access strictly based on security classification labels and user clearances?",
                "options": ["Discretionary Access Control (DAC)", "Mandatory Access Control (MAC)", "Role-Based Access Control (RBAC)", "Rule-Based Access Control"],
                "answer": 1,
                "explanation": "MAC enforces strict security labels (e.g. Secret, Top Secret) that individual resource owners cannot override.",
                "difficulty": "intermediate"
            },
            {
                "question": "In the CIA Triad, which pillar guarantees that information has not been tampered with or altered by unauthorized parties?",
                "options": ["Confidentiality", "Integrity", "Availability", "Authenticity"],
                "answer": 1,
                "explanation": "Integrity ensures data remains unaltered, accurate, and trustworthy throughout its lifecycle.",
                "difficulty": "beginner"
            },
            {
                "question": "What principle of information security ensures that an individual cannot deny the authenticity of their signature or sending a message?",
                "options": ["Confidentiality", "Non-Repudiation", "Pseudosymmetry", "Obfuscation"],
                "answer": 1,
                "explanation": "Non-repudiation provides cryptographic proof (via digital signatures) tying an action unequivocally to an identity.",
                "difficulty": "beginner"
            },
            {
                "question": "What security strategy employs multiple layers of defense throughout an IT system to slow down and deter attackers?",
                "options": ["Single Point of Failure", "Defense in Depth (Layered Defense)", "Perimeter Only Model", "Air-gapping"],
                "answer": 1,
                "explanation": "Defense in Depth combines firewalls, endpoint protection, encryption, access controls, and auditing.",
                "difficulty": "beginner"
            },
            {
                "question": "What is a 'Zero-Day Vulnerability'?",
                "options": [
                    "A bug that takes zero days to fix",
                    "A software security flaw unknown to the vendor, for which no patch or remediation exists",
                    "A bug with zero severity rating",
                    "A calendar calculation error"
                ],
                "answer": 1,
                "explanation": "A Zero-Day flaw is actively exploitable because the vendor has had 'zero days' to develop and release a patch.",
                "difficulty": "intermediate"
            },
            {
                "question": "What access control model grants permissions to users based on their defined job functions within an enterprise?",
                "options": ["Discretionary Access Control (DAC)", "Role-Based Access Control (RBAC)", "Mandatory Access Control (MAC)", "Biometric Access Control"],
                "answer": 1,
                "explanation": "RBAC assigns permissions to administrative or organizational roles rather than individual accounts.",
                "difficulty": "beginner"
            }
        ],
        "PKI, Digital Signatures & Hash Functions": [
            {
                "question": "What standard electronic document uses an authorized digital signature to bind a public key with a verified entity identity?",
                "options": ["Access Token", "X.509 Digital Certificate", "SSH Keyring", "Kerberos Ticket"],
                "answer": 1,
                "explanation": "An X.509 Digital Certificate is issued by a trusted Certificate Authority (CA) to cryptographically attest key ownership.",
                "difficulty": "intermediate"
            },
            {
                "question": "In asymmetric public-key cryptography, how is a digital signature generated on a document?",
                "options": [
                    "By encrypting the document hash using the sender's private key",
                    "By encrypting the document using the receiver's public key",
                    "By running a CRC32 check on the network cable",
                    "By adding a watermark image"
                ],
                "answer": 0,
                "explanation": "The signer hashes the document and encrypts that hash with their private key; anyone with the public key can verify it.",
                "difficulty": "intermediate"
            },
            {
                "question": "What mathematical structure in cryptography organizes transactions into a binary hash tree with a single root hash?",
                "options": ["B+ Tree", "Merkle Tree (Hash Tree)", "Red-Black Tree", "Huffman Tree"],
                "answer": 1,
                "explanation": "Merkle Trees allow efficient and secure verification of large data sets (used in Git, Bitcoin, and Certificate Transparency).",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the role of a Certificate Revocation List (CRL) or OCSP in Public Key Infrastructure?",
                "options": [
                    "To generate new prime numbers",
                    "To check whether a digital certificate has been invalidated or compromised prior to its scheduled expiration",
                    "To compress SSL handshake packets",
                    "To encrypt private keys"
                ],
                "answer": 1,
                "explanation": "OCSP and CRLs verify in real-time whether a CA has revoked a certificate due to compromise.",
                "difficulty": "intermediate"
            },
            {
                "question": "What protocol allows a client and server to mutually authenticate and establish a shared symmetric session key over an insecure channel?",
                "options": ["Diffie-Hellman Key Exchange", "FTP", "DNS", "Telnet"],
                "answer": 0,
                "explanation": "Diffie-Hellman allows two parties to agree on a shared secret over an unencrypted channel without sending the key itself.",
                "difficulty": "intermediate"
            }
        ],
        "Access Control Models & Security Auditing": [
            {
                "question": "Which authentication factor category does a fingerprint or retina scan belong to?",
                "options": ["Something you know", "Something you have", "Something you are (Inherence)", "Somewhere you are"],
                "answer": 2,
                "explanation": "Biometric factors (fingerprint, iris, facial geometry) fall under 'Something you are'.",
                "difficulty": "beginner"
            },
            {
                "question": "What security framework specifies that organizations should never implicitly trust any device or user inside or outside the network perimeter?",
                "options": ["Perimeter Defense", "Zero Trust Architecture (ZTA)", "DMZ Model", "NAT Isolation"],
                "answer": 1,
                "explanation": "Zero Trust operates on the principle of 'never trust, always verify', requiring continuous authentication.",
                "difficulty": "intermediate"
            },
            {
                "question": "What type of attack involves manipulating human psychology to trick employees into divulging confidential passwords?",
                "options": ["Social Engineering (Phishing / Pretexting)", "Buffer Overflow", "SQL Injection", "Port Scanning"],
                "answer": 0,
                "explanation": "Social engineering targets human vulnerabilities rather than software bugs to gain unauthorized access.",
                "difficulty": "beginner"
            },
            {
                "question": "What SIEM (Security Information and Event Management) system capability analyzes logs from firewalls, servers, and routers?",
                "options": [
                    "Centralized log aggregation, real-time correlation, and automated threat alert detection",
                    "Automated hard drive reformatting",
                    "Wi-Fi signal amplification",
                    "Compiling C++ code"
                ],
                "answer": 0,
                "explanation": "SIEM platforms aggregate security event logs across an enterprise to detect anomalies and ongoing intrusions.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is Penetration Testing (Ethical Hacking)?",
                "options": [
                    "Cracking passwords to steal intellectual property",
                    "An authorized simulated cyberattack against a computer system to identify exploitable security vulnerabilities",
                    "Installing pirated software",
                    "Testing internet download speed"
                ],
                "answer": 1,
                "explanation": "Penetration testing legally tests system defenses using the same techniques and tools as malicious adversaries.",
                "difficulty": "beginner"
            }
        ]
    },

    "Distributed Systems": {
        "Distributed System Fundamentals & RPC": [
            {
                "question": "According to the CAP Theorem, which guarantee must be compromised during a network partition in a distributed system?",
                "options": ["Consistency or Availability", "Scalability", "Fault tolerance", "Security"],
                "answer": 0,
                "explanation": "When network partitions (P) occur, a distributed system must choose between Consistency (C) and Availability (A).",
                "difficulty": "intermediate"
            },
            {
                "question": "What mechanism enables a program to execute a subroutine on a remote computer without explicitly coding network details?",
                "options": ["RPC (Remote Procedure Call)", "Shared Memory", "Pipes", "Direct DMA"],
                "answer": 0,
                "explanation": "RPC abstracts network transport and serialization, making remote function calls look like local invocations.",
                "difficulty": "beginner"
            },
            {
                "question": "What high-performance open-source RPC framework created by Google uses Protocol Buffers (Protobuf) over HTTP/2?",
                "options": ["gRPC", "SOAP", "CORBA", "Java RMI"],
                "answer": 0,
                "explanation": "gRPC uses binary Protocol Buffers serialization and HTTP/2 multiplexing for fast cross-language RPCs.",
                "difficulty": "beginner"
            },
            {
                "question": "What property describes a distributed operation that produces the exact same result whether executed once or multiple times?",
                "options": ["Atomicity", "Idempotency", "Concurrency", "Serialization"],
                "answer": 1,
                "explanation": "Idempotent operations (like HTTP PUT or GET) can be safely retried upon network timeouts without duplicate side effects.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the primary fallacy among the famous 'Eight Fallacies of Distributed Computing'?",
                "options": [
                    "The network is reliable and latency is zero",
                    "Computers run on electricity",
                    "Code has bugs",
                    "Security is important"
                ],
                "answer": 0,
                "explanation": "The most common false assumption is assuming networks are reliable, latency is zero, and bandwidth is infinite.",
                "difficulty": "intermediate"
            },
            {
                "question": "What distributed data partitioning technique maps both keys and servers to a circular hash ring to minimize remapping during node failures?",
                "options": ["Consistent Hashing", "Modulo Hashing", "Round Robin", "Linear Probing"],
                "answer": 0,
                "explanation": "Consistent hashing ensures adding or removing a node only requires reassigning K/N keys on average.",
                "difficulty": "advanced"
            }
        ],
        "Synchronization & Distributed Clocks": [
            {
                "question": "What logical clock algorithm assigns monotonically increasing scalar timestamps to establish a 'happened-before' relationship?",
                "options": ["Lamport Logical Clocks", "NTP Clock", "Atomic Clock", "Tick Counter"],
                "answer": 0,
                "explanation": "Leslie Lamport's algorithm defines partial ordering of events in distributed systems without physical clock sync.",
                "difficulty": "intermediate"
            },
            {
                "question": "Why are physical wall-clock timestamps (like system time) insufficient for ordering events across different distributed servers?",
                "options": [
                    "CPUs cannot measure time",
                    "Clock Drift and Clock Skew cause hardware quartz oscillators to diverge unpredictably",
                    "Networks block timestamp headers",
                    "Time zones are not supported"
                ],
                "answer": 1,
                "explanation": "Physical clocks drift apart by milliseconds, making it impossible to determine true event order without synchronization bounds.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which extension of Lamport clocks uses an array of integers per process to capture causal dependency relationships accurately?",
                "options": ["Vector Clocks", "Matrix Clocks", "Interval Timers", "Epoch Counters"],
                "answer": 0,
                "explanation": "Vector clocks maintain a full vector of timestamps across all nodes, enabling exact detection of concurrent events.",
                "difficulty": "advanced"
            },
            {
                "question": "What protocol is used worldwide to synchronize computer clocks over packet-switched, variable-latency networks?",
                "options": ["NTP (Network Time Protocol)", "SNMP", "BGP", "ICMP"],
                "answer": 0,
                "explanation": "NTP synchronizes client clocks with stratum time servers using round-trip latency filtering.",
                "difficulty": "beginner"
            },
            {
                "question": "What distributed physical clock technology developed by Google uses GPS and atomic clocks to provide bounded uncertainty (e.g. +/- 7ms)?",
                "options": ["TrueTime (used in Google Spanner)", "Chandy-Lamport Clock", "Quartz Time", "SyncEngine"],
                "answer": 0,
                "explanation": "Google Spanner's TrueTime API provides bounded clock error intervals enabling external consistency at global scale.",
                "difficulty": "advanced"
            }
        ],
        "Consensus Algorithms & Fault Tolerance": [
            {
                "question": "Which consensus protocol is widely known for being designed as an understandable alternative to Paxos, using leader election and log replication?",
                "options": ["Raft", "Two-Phase Commit (2PC)", "Gossip Protocol", "Chandy-Lamport"],
                "answer": 0,
                "explanation": "Raft decomposes consensus into clear, distinct subproblems: leader election, log replication, and safety.",
                "difficulty": "intermediate"
            },
            {
                "question": "In the Raft consensus algorithm, what must a candidate receive to successfully win a leader election?",
                "options": [
                    "Votes from a majority (quorum) of cluster nodes",
                    "Votes from all nodes unanimously",
                    "A cryptographic signature from the master node",
                    "Zero error timeouts"
                ],
                "answer": 0,
                "explanation": "A Raft candidate must secure affirmative votes from a strict majority quorum (> N/2) to assume leadership.",
                "difficulty": "intermediate"
            },
            {
                "question": "What atomic commitment protocol coordinates distributed database participants across Prepare and Commit phases?",
                "options": ["Two-Phase Commit (2PC)", "Three-Phase Consensus", "Bully Algorithm", "Ring Algorithm"],
                "answer": 0,
                "explanation": "2PC asks all resource nodes if they can commit (Prepare), and if all vote YES, commits the transaction globally.",
                "difficulty": "intermediate"
            },
            {
                "question": "What consensus problem involves reaching agreement in the presence of malicious or faulty nodes that may send conflicting messages?",
                "options": ["Byzantine Generals Problem", "Dining Philosophers Problem", "Sleeping Barber Problem", "Readers-Writers Problem"],
                "answer": 0,
                "explanation": "Byzantine fault tolerance handles arbitrary or malicious component behaviors, requiring at least 3f + 1 total nodes to tolerate f faulty nodes.",
                "difficulty": "advanced"
            },
            {
                "question": "What decentralized communication protocol disseminates information across clusters like the spread of an epidemic?",
                "options": ["Gossip Protocol / Epidemic Protocol", "Broadcast Tree", "Master-Worker Protocol", "Sliding Window"],
                "answer": 0,
                "explanation": "Gossip protocols randomly exchange membership and state information with peers, achieving eventual consistency efficiently.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Robotics": {
        "Kinematics & Coordinate Frames": [
            {
                "question": "Which mathematical convention utilizes four geometric parameters (theta, d, a, alpha) to model the kinematics of spatial robotic joints?",
                "options": ["Denavit-Hartenberg (DH) Convention", "Euler Angle System", "Rodrigues Formula", "Quaternion Parameterization"],
                "answer": 0,
                "explanation": "The DH convention attaches local coordinate frames to links and transforms between them via 4 standard parameters.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the difference between Forward Kinematics and Inverse Kinematics?",
                "options": [
                    "Forward computes end-effector position from joint angles; Inverse computes required joint angles to reach a desired position",
                    "Forward is for wheels; Inverse is for arms",
                    "Forward is hardware; Inverse is software",
                    "There is no difference"
                ],
                "answer": 0,
                "explanation": "Forward kinematics calculates cartesian pose from known joint states; Inverse kinematics solves the reverse (often non-linear with multiple solutions).",
                "difficulty": "beginner"
            },
            {
                "question": "How many degrees of freedom (DOF) are required for a robotic arm to position its end-effector arbitrarily in 3D position and orientation?",
                "options": ["3 DOF", "4 DOF", "6 DOF (3 translational + 3 rotational)", "12 DOF"],
                "answer": 2,
                "explanation": "Spatial rigid body pose requires 6 DOFs: 3 for translation (x, y, z) and 3 for orientation (roll, pitch, yaw).",
                "difficulty": "beginner"
            },
            {
                "question": "What mathematical matrix relates the joint velocities of a robot manipulator to the linear and angular velocities of its end-effector?",
                "options": ["Jacobian Matrix", "Inertia Matrix", "Hessian Matrix", "Covariance Matrix"],
                "answer": 0,
                "explanation": "The geometric Jacobian maps joint velocity vector q_dot into operational space end-effector velocities v and omega.",
                "difficulty": "advanced"
            },
            {
                "question": "What is a kinematic singularity in a robot manipulator?",
                "options": [
                    "When the robot runs out of battery",
                    "A configuration where the Jacobian loses rank and the robot loses one or more degrees of freedom",
                    "When two gears collide physically",
                    "When an infinite loop occurs in the firmware"
                ],
                "answer": 1,
                "explanation": "At singularities, the Jacobian determinant vanishes, making movement impossible in certain directions and causing unbounded joint velocities.",
                "difficulty": "advanced"
            },
            {
                "question": "Which coordinate representation avoids 'Gimbal Lock' when calculating 3D robotic wrist rotations?",
                "options": ["Euler Angles", "Quaternions (4-element hypercomplex numbers)", "Direction Cosines", "Roll-Pitch-Yaw"],
                "answer": 1,
                "explanation": "Quaternions represent 3D orientations smoothly on a 4D unit sphere without mathematical gimbal lock singularities.",
                "difficulty": "intermediate"
            }
        ],
        "Sensors, Computer Vision & Perception": [
            {
                "question": "Which optical sensor uses rotating laser beams to generate high-precision 3D point cloud maps of surrounding environments?",
                "options": ["Ultrasonic Sensor", "LiDAR (Light Detection and Ranging)", "Sonar", "Infrared Photodiode"],
                "answer": 1,
                "explanation": "LiDAR measures time-of-flight of pulsed laser reflections to generate dense metric 3D point clouds.",
                "difficulty": "beginner"
            },
            {
                "question": "Which sensor combines 3-axis accelerometers and 3-axis gyroscopes to track orientation and linear acceleration?",
                "options": ["IMU (Inertial Measurement Unit)", "Barometer", "Thermocouple", "Magnetometer only"],
                "answer": 0,
                "explanation": "An IMU fuses angular rates from gyroscopes and accelerations from accelerometers to estimate dynamic pose.",
                "difficulty": "beginner"
            },
            {
                "question": "What type of camera uses two horizontally separated image sensors to compute depth through parallax disparity?",
                "options": ["Monocular Camera", "Stereo Vision Camera", "Thermal Camera", "Omnidirectional Camera"],
                "answer": 1,
                "explanation": "Stereo cameras compute pixel disparity across left and right views using epipolar geometry to deduce depth.",
                "difficulty": "beginner"
            },
            {
                "question": "What algorithm is widely used in robotics for optimal state estimation and fusing noisy sensor observations (e.g. IMU + Wheel Odometry)?",
                "options": ["Kalman Filter / Extended Kalman Filter (EKF)", "A* Search", "K-Means", "Dijkstra's Algorithm"],
                "answer": 0,
                "explanation": "Kalman filters recursively predict and correct state estimates using Gaussian noise covariances.",
                "difficulty": "intermediate"
            },
            {
                "question": "What visual fiduciary marker system (like AprilTag or ArUco) is commonly used to track object poses in robotics with a single camera?",
                "options": ["QR Codes with GPS", "Planar Square Fiducial Markers (ArUco / AprilTags)", "Barcodes", "RFID Tags"],
                "answer": 1,
                "explanation": "ArUco and AprilTags provide 3D corner coordinates that allow closed-form PnP pose estimation from monocular images.",
                "difficulty": "intermediate"
            }
        ],
        "Robot Control, Path Planning & SLAM": [
            {
                "question": "What autonomous capability allows a mobile robot to map unknown surroundings while concurrently tracking its own real-time pose?",
                "options": ["PID Control", "SLAM (Simultaneous Localization and Mapping)", "Inverse Kinematics", "Dead Reckoning"],
                "answer": 1,
                "explanation": "SLAM algorithms solve the chicken-and-egg problem of building an environment map while localizing within it.",
                "difficulty": "intermediate"
            },
            {
                "question": "What widely used sampling-based motion planning algorithm grows random space-filling trees to navigate high-dimensional robot spaces?",
                "options": ["RRT (Rapidly-exploring Random Tree)", "Dijkstra's Algorithm", "Breadth-First Search", "Bubble Sort"],
                "answer": 0,
                "explanation": "RRT samples configuration space randomly and extends toward samples, quickly finding collision-free paths.",
                "difficulty": "intermediate"
            },
            {
                "question": "What classic feedback controller calculates an output based on Proportional, Integral, and Derivative error terms?",
                "options": ["Bang-Bang Controller", "PID Controller", "LQR Controller", "State Machine"],
                "answer": 1,
                "explanation": "PID control minimizes tracking error by reacting to current error (P), past accumulated error (I), and rate of change (D).",
                "difficulty": "beginner"
            },
            {
                "question": "What open-source middleware robotics framework provides publish-subscribe nodes, services, and URDF robot modeling tools?",
                "options": ["ROS (Robot Operating System / ROS 2)", "Android NDK", "OpenCV", "TensorFlow"],
                "answer": 0,
                "explanation": "ROS provides modular plumbing, drivers, visualization (RViz), and simulation (Gazebo) for robotics research and industry.",
                "difficulty": "beginner"
            },
            {
                "question": "What is an Occupancy Grid Map in mobile robotics navigation?",
                "options": [
                    "A 2D or 3D grid where each cell stores a probability value indicating whether that space is free, occupied, or unknown",
                    "A seating chart for robotic conferences",
                    "A motor driver configuration",
                    "A battery charging graph"
                ],
                "answer": 0,
                "explanation": "Occupancy grid maps discretize physical space into binary probabilistic cells to represent obstacles for path planning.",
                "difficulty": "intermediate"
            }
        ]
    },

    "Web Development": {
        "HTML5, Semantic Markup & CSS3": [
            {
                "question": "Which HTML5 semantic element is designed to encapsulate self-contained content that could be distributed independently (e.g. blog post)?",
                "options": ["<section>", "<article>", "<aside>", "<div>"],
                "answer": 1,
                "explanation": "<article> represents standalone, distributable syndication content such as blog entries or forum posts.",
                "difficulty": "beginner"
            },
            {
                "question": "In the CSS Box Model, what is the correct order of layers from the inside content out to the adjacent elements?",
                "options": [
                    "Content -> Padding -> Border -> Margin",
                    "Content -> Border -> Padding -> Margin",
                    "Content -> Margin -> Border -> Padding",
                    "Padding -> Content -> Border -> Margin"
                ],
                "answer": 0,
                "explanation": "The CSS box model surrounds Content with Padding (inside spacing), Border, and Margin (external spacing).",
                "difficulty": "beginner"
            },
            {
                "question": "Which CSS layout module is primarily designed for one-dimensional layouts (either in rows or in columns)?",
                "options": ["CSS Grid Layout", "Flexbox (Flexible Box Layout)", "Float positioning", "Table layout"],
                "answer": 1,
                "explanation": "Flexbox distributes space along a single axis (row or column), whereas CSS Grid handles two-dimensional layouts.",
                "difficulty": "beginner"
            },
            {
                "question": "What CSS property setting causes an element's padding and border to be included within its specified width and height?",
                "options": ["box-sizing: content-box", "box-sizing: border-box", "display: inline-block", "overflow: hidden"],
                "answer": 1,
                "explanation": "box-sizing: border-box prevents elements from expanding beyond their declared width when padding or borders are added.",
                "difficulty": "intermediate"
            },
            {
                "question": "What CSS3 rule enables responsive styling tailored to different screen widths and device orientations?",
                "options": ["@supports", "@media queries", "@keyframes", "@import"],
                "answer": 1,
                "explanation": "Media queries apply conditional CSS rule sets based on device characteristics (like max-width or orientation).",
                "difficulty": "beginner"
            },
            {
                "question": "What is the difference between CSS visibility: hidden and display: none?",
                "options": [
                    "visibility: hidden hides the element but preserves its space in the layout; display: none removes it from the layout flow entirely",
                    "display: none hides only text; visibility: hidden hides images",
                    "They are completely identical",
                    "visibility: hidden causes a browser crash"
                ],
                "answer": 0,
                "explanation": "display: none removes the node from document rendering, whereas visibility: hidden leaves an invisible blank space.",
                "difficulty": "intermediate"
            }
        ],
        "JavaScript ES6+ & DOM Manipulation": [
            {
                "question": "What is the key scoping difference between variables declared with 'let' and 'var' in modern JavaScript?",
                "options": [
                    "'var' is block-scoped; 'let' is function-scoped",
                    "'let' is block-scoped; 'var' is function-scoped and hoisted with undefined value",
                    "'let' creates immutable variables",
                    "'var' is only available in NodeJS"
                ],
                "answer": 1,
                "explanation": "let adheres to enclosing block {} scopes, preventing accidental variable leakage associated with hoisted var.",
                "difficulty": "beginner"
            },
            {
                "question": "What does the JavaScript === (strict equality) operator check compared to == (loose equality)?",
                "options": [
                    "It checks value equality after automatic type coercion",
                    "It checks both value equality and type equality without coercion",
                    "It checks memory pointers exclusively",
                    "It is used only for object comparisons"
                ],
                "answer": 1,
                "explanation": "Strict equality (===) evaluates false if operands have different data types (e.g. 5 === '5' is false).",
                "difficulty": "beginner"
            },
            {
                "question": "What does a JavaScript Promise represent?",
                "options": [
                    "A guaranteed synchronous return value",
                    "The eventual completion (or failure) of an asynchronous operation and its resulting value",
                    "A database transaction lock",
                    "A thread pool worker"
                ],
                "answer": 1,
                "explanation": "Promises model asynchronous operations in one of three states: pending, fulfilled, or rejected.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is an event propagation phase where an event triggers on the target element and travels upward through ancestors in the DOM?",
                "options": ["Event Capturing", "Event Bubbling", "Event Hijacking", "Event Dispatch"],
                "answer": 1,
                "explanation": "Event bubbling notifies handlers starting from the deepest target node up through parent DOM hierarchy to the document root.",
                "difficulty": "intermediate"
            },
            {
                "question": "What modern async syntax simplifies working with Promises by making asynchronous code look synchronous?",
                "options": ["try/catch with threads", "async / await", "callbacks with yield", "setTimeout loops"],
                "answer": 1,
                "explanation": "async/await wraps Promise execution in clean, readable sequential syntax without nested callback hell.",
                "difficulty": "beginner"
            }
        ],
        "RESTful APIs, Fetch & Web Security": [
            {
                "question": "Which HTTP method is designated in RESTful API design for idempotent resource replacement?",
                "options": ["POST", "PUT", "PATCH", "DELETE"],
                "answer": 1,
                "explanation": "PUT replaces the complete target resource at the URI idempotently, whereas PATCH applies partial modifications.",
                "difficulty": "intermediate"
            },
            {
                "question": "What HTTP status code represents '200 OK', '404 Not Found', and '500 Internal Server Error' respectively?",
                "options": [
                    "Success, Client Error, Server Error",
                    "Redirection, Client Error, Success",
                    "Informational, Server Error, Client Error",
                    "Success, Redirection, Network Timeout"
                ],
                "answer": 0,
                "explanation": "2xx series denotes success, 4xx series denotes client-side issues, and 5xx series denotes server failures.",
                "difficulty": "beginner"
            },
            {
                "question": "What security mechanism implemented by browsers prevents a script on one origin from accessing resources on another origin?",
                "options": ["Content-Security-Policy", "Same-Origin Policy (SOP)", "CORS headers", "X-Frame-Options"],
                "answer": 1,
                "explanation": "SOP isolates distinct web origins (protocol, domain, and port) to safeguard user cookies and session data.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which HTTP response header allows servers to whitelist specific external domains for Cross-Origin Resource Sharing (CORS)?",
                "options": [
                    "Access-Control-Allow-Origin",
                    "Content-Security-Policy",
                    "Strict-Transport-Security",
                    "X-Content-Type-Options"
                ],
                "answer": 0,
                "explanation": "Access-Control-Allow-Origin indicates which origin domains are permitted to read response data via browser fetch/XHR.",
                "difficulty": "beginner"
            },
            {
                "question": "Which React Hook is utilized to manage reactive state variables inside a functional React component?",
                "options": ["useEffect", "useState", "useContext", "useReducer"],
                "answer": 1,
                "explanation": "useState declares component state and triggers reactive re-renders whenever state changes.",
                "difficulty": "beginner"
            }
        ]
    },

    "DevOps": {
        "Version Control with Git & Branching": [
            {
                "question": "What command stages modified files in the local Git working directory into the staging index?",
                "options": ["git commit", "git add <file>", "git push", "git checkout"],
                "answer": 1,
                "explanation": "git add moves changed files from the working tree to the staging area ready for the next commit.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the difference between git merge and git rebase?",
                "options": [
                    "git merge combines histories with a dedicated merge commit; git rebase reapplies commits on top of another base tip for a linear history",
                    "git rebase deletes files permanently",
                    "git merge cannot resolve conflicts",
                    "There is no difference"
                ],
                "answer": 0,
                "explanation": "git rebase rewrites project history to produce a clean linear graph, whereas merge preserves original commit chronology.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which Git command is used to temporarily shelve (shelter) uncommitted changes without committing them?",
                "options": ["git stash", "git branch", "git reset", "git revert"],
                "answer": 0,
                "explanation": "git stash stores working tree modifications in a stack, reverting the directory to a clean HEAD state.",
                "difficulty": "beginner"
            },
            {
                "question": "What is the purpose of the .gitignore file in a software repository?",
                "options": [
                    "To delete corrupted commits",
                    "To specify untracked files and patterns (like node_modules, .env, build output) that Git should ignore",
                    "To block unauthorized developers from pulling code",
                    "To store user credentials"
                ],
                "answer": 1,
                "explanation": ".gitignore tells Git to omit build artifacts, secrets, and caches from version tracking.",
                "difficulty": "beginner"
            },
            {
                "question": "What does git cherry-pick do?",
                "options": [
                    "Selects and applies the changes introduced by one or more existing commits from another branch onto the current HEAD",
                    "Deletes all branches except master",
                    "Compares two branches graphically",
                    "Cleans untracked directories"
                ],
                "answer": 0,
                "explanation": "git cherry-pick copies specific individual commits from one branch and commits them onto the active branch.",
                "difficulty": "intermediate"
            },
            {
                "question": "What Git branching model defines separate long-lived 'main' and 'develop' branches with supporting feature and release branches?",
                "options": ["Trunk-Based Development", "GitFlow", "GitHub Flow", "Monorepo Flow"],
                "answer": 1,
                "explanation": "GitFlow introduces structured branch lifecycles for scheduled releases with strict merging policies.",
                "difficulty": "intermediate"
            }
        ],
        "Continuous Integration & Deployment (CI/CD)": [
            {
                "question": "What is the primary technical objective of Continuous Integration (CI)?",
                "options": [
                    "Deploying software once every 6 months",
                    "Automatically building, integrating, and testing code frequently into a shared repository to detect integration errors early",
                    "Replacing manual code reviews completely",
                    "Backing up database tables to tape drives"
                ],
                "answer": 1,
                "explanation": "CI runs automated builds and tests on every commit/PR to discover regressions and merge issues quickly.",
                "difficulty": "beginner"
            },
            {
                "question": "What open-source automation server uses Pipelines declared in Groovy Jenkinsfiles to orchestrate CI/CD jobs?",
                "options": ["Jenkins", "GitLab Runner", "CircleCI", "Travis CI"],
                "answer": 0,
                "explanation": "Jenkins is an extensible Java-based CI/CD orchestration server featuring thousands of pipeline plugins.",
                "difficulty": "beginner"
            },
            {
                "question": "What deployment strategy maintains two identical production environments, switching live router traffic instantly to reduce downtime?",
                "options": ["Canary Deployment", "Blue-Green Deployment", "Rolling Update", "Recreate Strategy"],
                "answer": 1,
                "explanation": "Blue-Green deployment runs identical Blue (active) and Green (idle) environments, swapping router routes seamlessly.",
                "difficulty": "intermediate"
            },
            {
                "question": "What deployment strategy releases a new software version to a small subset (e.g. 5%) of real users before general rollout?",
                "options": ["Canary Deployment", "Blue-Green Deployment", "A/B Testing", "Shadow Deployment"],
                "answer": 0,
                "explanation": "Canary deployments roll out changes to a small percentage of production traffic to monitor errors before full deployment.",
                "difficulty": "intermediate"
            },
            {
                "question": "Which declarative file format is commonly used to define CI/CD workflows in GitHub Actions and GitLab CI?",
                "options": ["XML", "YAML (.yml)", "JSON", "INI"],
                "answer": 1,
                "explanation": "YAML is the standard human-readable configuration format for GitHub Actions and modern CI runners.",
                "difficulty": "beginner"
            }
        ],
        "Containers, Docker & Kubernetes": [
            {
                "question": "In a Dockerfile, which instruction specifies the foundational parent image to start building from?",
                "options": ["RUN", "FROM", "COPY", "WORKDIR"],
                "answer": 1,
                "explanation": "The FROM instruction sets the base OS or language runtime image (e.g. FROM python:3.11-slim).",
                "difficulty": "beginner"
            },
            {
                "question": "What open-source tool defines and manages multi-container Docker applications using a single docker-compose.yml file?",
                "options": ["Docker Compose", "Docker Swarm", "Kubernetes", "Vagrant"],
                "answer": 0,
                "explanation": "Docker Compose launches multi-container environments (app, database, redis) with one command: docker compose up.",
                "difficulty": "beginner"
            },
            {
                "question": "Which open-source Infrastructure as Code (IaC) tool uses declarative HCL configuration files to provision multi-cloud infrastructure?",
                "options": ["Ansible", "Terraform (HashiCorp)", "Jenkins", "Kubernetes"],
                "answer": 1,
                "explanation": "Terraform enables architects to declare cloud resources in HCL and provision them idempotently across AWS, Azure, and GCP.",
                "difficulty": "intermediate"
            },
            {
                "question": "In Kubernetes, what controller manages the automated scaling and rolling updates of replicated Pod instances?",
                "options": ["DaemonSet", "Deployment", "StatefulSet", "ConfigMap"],
                "answer": 1,
                "explanation": "Deployments provide declarative updates for Pods and ReplicaSets, handling rolling updates and rollbacks.",
                "difficulty": "intermediate"
            },
            {
                "question": "What is the role of an Ingress Controller in Kubernetes?",
                "options": [
                    "To clean up crashed Docker containers on worker nodes",
                    "To manage external HTTP/HTTPS routing, SSL termination, and virtual hosts to internal cluster Services",
                    "To store persistent disk backups",
                    "To compile source code into binaries"
                ],
                "answer": 1,
                "explanation": "Ingress acts as an intelligent HTTP reverse proxy (e.g. NGINX Ingress) exposing cluster services to external traffic.",
                "difficulty": "advanced"
            }
        ]
    }
}
