# demo.py - Quick demonstration of the system

from doubts import post_question, view_all_questions
from answers import display_all_responses, add_instructor_response

print("="*70)
print("QUICK DEMONSTRATION - DOUBT RESOLUTION SYSTEM")
print("="*70)

# Student 1 posts a question about gravity
print("\n[1] Student posts question about gravity...")
q1 = post_question("Alice", "Physics", "What is gravity?")

# Student 2 posts question about functions
print("\n[2] Student posts question about functions...")
q2 = post_question("Bob", "Python", "What is a function in programming?")

# Student 3 posts question about atoms
print("\n[3] Student posts question about atoms...")
q3 = post_question("Charlie", "Chemistry", "What is an atom?")

# View all questions
print("\n" + "="*70)
input("Press Enter to view all questions...")
view_all_questions()

# View responses for question 1
print("\n" + "="*70)
input("Press Enter to view Question #1 responses...")
display_all_responses(q1)

# Instructor adds verified answer
print("\n" + "="*70)
input("Press Enter for instructor to add verified answer...")
add_instructor_response(q1, 
    "Gravity is one of the four fundamental forces of nature. "
    "It's described by Newton's Law of Universal Gravitation (F = G*m1*m2/r²) "
    "and more accurately by Einstein's General Relativity as the curvature of spacetime. "
    "On Earth, objects accelerate downward at 9.8 m/s².")

print("\n✅ Instructor has added verified answer!")

# View updated responses
print("\n" + "="*70)
input("Press Enter to see updated responses with verification...")
display_all_responses(q1)

print("\n" + "="*70)
print("✅ DEMONSTRATION COMPLETE!")
print("="*70)
print("\nKey Features Demonstrated:")
print("  ✅ Real web scraping from Wikipedia")
print("  ✅ Automatic preliminary answers")
print("  ✅ Instructor verification")
print("  ✅ Side-by-side response comparison")
print("="*70)
