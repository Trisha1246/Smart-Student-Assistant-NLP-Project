import json
import os
import sys

# Builder script to assemble comprehensive 450+ question engineering quiz bank
# for Smart Student Assistant

ENGINEERING_SUBJECTS = [
    "Python", "Java", "DBMS", "Data Structures", "Computer Networks", "Operating Systems",
    "Artificial Intelligence", "Machine Learning", "Software Engineering", "Cyber Security",
    "Cloud Computing", "Computer Architecture", "Theory of Computation", "Compiler Design",
    "Object Oriented Design", "Natural Language Processing", "Digital Electronics",
    "Microprocessors", "Internet of Things", "Big Data Analytics", "Computer Graphics",
    "Discrete Mathematics", "Mobile App Development", "Information Security",
    "Distributed Systems", "Robotics", "Web Development", "DevOps"
]

print(f"Total engineering subjects: {len(ENGINEERING_SUBJECTS)}")
