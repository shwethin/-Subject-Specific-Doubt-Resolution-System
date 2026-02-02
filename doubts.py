# doubts.py - Question/Doubt management module

from data import questions_database, question_id_counter
from answers import simulate_web_scraping


def post_question(student_name, subject, question_text):
    """
    Allows a student to post a new question/doubt
    Automatically triggers web scraping simulation to fetch preliminary answer
    
    Parameters:
        student_name: Name of the student posting the question
        subject: Subject area of the question
        question_text: The actual question
    
    Returns:
        The created question dictionary
    """
    global question_id_counter
    
    # Generate unique ID for this question
    question_id_counter += 1
    
    # Simulate web scraping to get automatic response
    auto_response = simulate_web_scraping(subject, question_text)
    
    # Create question record
    new_question = {
        "id": question_id_counter,
        "student_name": student_name,
        "subject": subject,
        "question": question_text,
        "auto_response": auto_response,
        "instructor_response": None,
        "is_verified": False
    }
    
    # Add to database
    questions_database.append(new_question)
    
    print(f"\n✅ Question posted successfully!")
    print(f"📌 Question ID: {question_id_counter}")
    print(f"🌐 Automatic response has been generated from web sources.")
    
    return new_question


def view_all_questions():
    """
    Displays a list of all posted questions with their status
    """
    if len(questions_database) == 0:
        print("\n⚠️  No questions have been posted yet.")
        return
    
    print("\n" + "="*70)
    print("ALL POSTED QUESTIONS")
    print("="*70)
    
    for question in questions_database:
        print(f"\n📌 ID: {question['id']}")
        print(f"📚 Subject: {question['subject']}")
        print(f"👤 Student: {question['student_name']}")
        print(f"❓ Question: {question['question'][:80]}..." if len(question['question']) > 80 else f"❓ Question: {question['question']}")
        
        # Display verification status
        if question['is_verified']:
            print("✅ Status: VERIFIED (Instructor has answered)")
        else:
            print("⏳ Status: PENDING (Awaiting instructor response)")
        
        print("-" * 70)
    
    print()


def find_question_by_id(question_id):
    """
    Searches for a question by its unique ID
    
    Parameters:
        question_id: The ID to search for
    
    Returns:
        The question dictionary if found, None otherwise
    """
    for question in questions_database:
        if question["id"] == question_id:
            return question
    
    return None


def get_questions_by_subject(subject):
    """
    Retrieves all questions for a specific subject
    
    Parameters:
        subject: The subject to filter by
    
    Returns:
        List of questions for that subject
    """
    subject_questions = []
    for question in questions_database:
        if question["subject"].lower() == subject.lower():
            subject_questions.append(question)
    
    return subject_questions


def get_pending_questions():
    """
    Retrieves all questions that haven't been verified by instructor yet
    
    Returns:
        List of unverified questions
    """
    pending = []
    for question in questions_database:
        if not question["is_verified"]:
            pending.append(question)
    
    return pending
