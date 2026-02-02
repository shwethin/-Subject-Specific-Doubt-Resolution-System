# main.py - Main program entry point for Doubt Resolution System

from doubts import (post_question, view_all_questions, find_question_by_id, 
                    get_questions_by_subject, get_pending_questions)
from answers import add_instructor_response, display_all_responses


def show_main_menu():
    """
    Displays the main menu of the Doubt Resolution System
    """
    print("\n" + "="*70)
    print("    📚 SUBJECT-SPECIFIC DOUBT RESOLUTION SYSTEM 📚")
    print("="*70)
    print("\n🎓 STUDENT PORTAL:")
    print("  1. Post a New Question/Doubt")
    print("  2. View All Questions")
    print("  3. View Responses for a Specific Question")
    print("  4. View Questions by Subject")
    
    print("\n👨‍🏫 INSTRUCTOR PORTAL:")
    print("  5. View Pending Questions (Not Yet Verified)")
    print("  6. Add Authoritative Answer to a Question")
    
    print("\n🚪 GENERAL:")
    print("  7. Exit System")
    print("="*70)


def student_post_question_flow():
    """
    Handles the complete flow for a student posting a question
    Includes web scraping simulation for automatic response
    """
    print("\n" + "-"*70)
    print("POST A NEW QUESTION")
    print("-"*70)
    
    # Get student name
    student_name = input("Enter your name: ").strip()
    if not student_name:
        print("❌ Name cannot be empty!")
        return
    
    # Get subject
    print("\nAvailable subjects: Python, Mathematics, Physics, Chemistry, Data Structures")
    subject = input("Enter subject: ").strip()
    if not subject:
        print("❌ Subject cannot be empty!")
        return
    
    # Get question
    question_text = input("Enter your question: ").strip()
    if not question_text:
        print("❌ Question cannot be empty!")
        return
    
    # Post question (automatically triggers web scraping)
    post_question(student_name, subject, question_text)


def student_view_all_questions_flow():
    """
    Displays all questions posted in the system
    """
    print("\n" + "-"*70)
    print("VIEW ALL QUESTIONS")
    print("-"*70)
    view_all_questions()


def student_view_responses_flow():
    """
    Allows student to view both automatic and instructor responses
    for a specific question
    """
    print("\n" + "-"*70)
    print("VIEW QUESTION RESPONSES")
    print("-"*70)
    
    view_all_questions()
    
    if len(get_all_questions()) == 0:
        return
    
    try:
        question_id = int(input("\nEnter Question ID to view responses: "))
        question = find_question_by_id(question_id)
        
        if question:
            display_all_responses(question)
        else:
            print(f"\n❌ No question found with ID: {question_id}")
    
    except ValueError:
        print("\n❌ Please enter a valid number!")


def student_view_by_subject_flow():
    """
    Allows viewing questions filtered by subject
    """
    print("\n" + "-"*70)
    print("VIEW QUESTIONS BY SUBJECT")
    print("-"*70)
    
    subject = input("Enter subject to filter: ").strip()
    
    if not subject:
        print("❌ Subject cannot be empty!")
        return
    
    subject_questions = get_questions_by_subject(subject)
    
    if len(subject_questions) == 0:
        print(f"\n⚠️  No questions found for subject: {subject}")
        return
    
    print(f"\n📚 Questions for {subject}:")
    print("="*70)
    
    for q in subject_questions:
        print(f"\n📌 ID: {q['id']}")
        print(f"👤 Student: {q['student_name']}")
        print(f"❓ Question: {q['question']}")
        print(f"✅ Verified: {'Yes' if q['is_verified'] else 'No'}")
        print("-" * 70)


def instructor_view_pending_flow():
    """
    Shows all questions that are pending instructor verification
    """
    print("\n" + "-"*70)
    print("PENDING QUESTIONS (AWAITING VERIFICATION)")
    print("-"*70)
    
    pending = get_pending_questions()
    
    if len(pending) == 0:
        print("\n✅ All questions have been verified!")
        return
    
    print(f"\n⏳ {len(pending)} question(s) pending verification:\n")
    
    for q in pending:
        print(f"📌 ID: {q['id']}")
        print(f"📚 Subject: {q['subject']}")
        print(f"👤 Student: {q['student_name']}")
        print(f"❓ Question: {q['question']}")
        print("-" * 70)


def instructor_add_answer_flow():
    """
    Allows instructor to add authoritative/verified answer to a question
    """
    print("\n" + "-"*70)
    print("ADD AUTHORITATIVE ANSWER")
    print("-"*70)
    
    # Show pending questions
    pending = get_pending_questions()
    
    if len(pending) > 0:
        print(f"\n⏳ {len(pending)} question(s) need verification:")
        for q in pending:
            print(f"  → ID {q['id']}: {q['question'][:50]}...")
    
    print("\nAll questions:")
    view_all_questions()
    
    try:
        question_id = int(input("\nEnter Question ID to answer: "))
        question = find_question_by_id(question_id)
        
        if question is None:
            print(f"\n❌ No question found with ID: {question_id}")
            return
        
        # Display question details
        print(f"\n📚 Subject: {question['subject']}")
        print(f"❓ Question: {question['question']}")
        print(f"\n🌐 Current automatic response:")
        print(question['auto_response'])
        
        # Get instructor's answer
        print("\n" + "-"*70)
        print("Enter your authoritative answer:")
        instructor_answer = input("→ ").strip()
        
        if not instructor_answer:
            print("\n❌ Answer cannot be empty!")
            return
        
        # Add instructor response
        add_instructor_response(question, instructor_answer)
        print("\n✅ Authoritative answer added successfully!")
        print("✅ Question marked as VERIFIED")
    
    except ValueError:
        print("\n❌ Please enter a valid number!")


def get_all_questions():
    """
    Helper function to get all questions from database
    """
    from data import questions_database
    return questions_database


def main():
    """
    Main function - Entry point of the program
    Runs the menu loop
    """
    print("\n" + "="*70)
    print("  WELCOME TO SUBJECT-SPECIFIC DOUBT RESOLUTION SYSTEM")
    print("  Blended Learning Platform for Online Doubt Resolution")
    print("="*70)
    print("\n📌 Features:")
    print("  → Post subject-specific questions")
    print("  → Get automatic responses via web scraping simulation")
    print("  → Receive verified answers from course instructors")
    print("="*70)
    
    while True:
        show_main_menu()
        
        choice = input("\n👉 Enter your choice (1-7): ").strip()
        
        if choice == "1":
            student_post_question_flow()
        
        elif choice == "2":
            student_view_all_questions_flow()
        
        elif choice == "3":
            student_view_responses_flow()
        
        elif choice == "4":
            student_view_by_subject_flow()
        
        elif choice == "5":
            instructor_view_pending_flow()
        
        elif choice == "6":
            instructor_add_answer_flow()
        
        elif choice == "7":
            print("\n" + "="*70)
            print("Thank you for using the Doubt Resolution System!")
            print("Goodbye! 👋")
            print("="*70 + "\n")
            break
        
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 7.")


# Program entry point
if __name__ == "__main__":
    main()
