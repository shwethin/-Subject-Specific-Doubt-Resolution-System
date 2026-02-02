# answers.py - Answer generation and management module

from data import web_scraping_database
import time
import urllib.request
import urllib.parse
import re
import os

# Gemini API Configuration (SAFE - uses environment variable)
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', None)
USE_GEMINI = GEMINI_API_KEY is not None  # Only use if key is provided

# Try to import Gemini (optional, falls back if not installed)
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


def setup_gemini():
    """
    Safely configures Gemini API if available
    Uses environment variable for security
    """
    global USE_GEMINI
    
    if USE_GEMINI and GEMINI_AVAILABLE:
        try:
            genai.configure(api_key=GEMINI_API_KEY)
            return True
        except Exception as e:
            print(f"⚠️  Gemini setup failed: {str(e)[:50]}")
            USE_GEMINI = False
            return False
    
    return False


def query_gemini(question, subject):
    """
    Queries Google Gemini API for intelligent answers
    Falls back to cached content if API fails
    
    Parameters:
        question: The student's question
        subject: The subject area
    
    Returns:
        Tuple of (answer_text, source_type)
    """
    if not USE_GEMINI or not GEMINI_AVAILABLE:
        return None, "fallback"
    
    try:
        print("→ Querying Gemini AI...")
        
        # Create prompt for Gemini
        prompt = f"""
        The student has asked a question about {subject}.
        
        Question: {question}
        
        Please provide a clear, educational answer suitable for a student learning {subject}.
        Keep it concise (2-3 sentences) but informative.
        """
        
        # Call Gemini API
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        
        if response and response.text:
            print("→ ✅ Successfully got response from Gemini AI!")
            return response.text, "gemini"
        else:
            return None, "fallback"
    
    except Exception as e:
        # Fallback if API fails
        error_msg = str(e)
        if "API_KEY" in error_msg or "403" in error_msg:
            print(f"→ API Key error - using cached content")
        else:
            print(f"→ Gemini unavailable - using cached content")
        return None, "fallback"


def fetch_from_web(query):
    """
    Actually fetches content from the web using Wikipedia API
    This is REAL web scraping using urllib (built-in Python library)
    
    Parameters:
        query: Search query to look up
    
    Returns:
        Extracted text content or None if failed
    """
    try:
        # Encode the query for URL
        encoded_query = urllib.parse.quote(query)
        
        # Wikipedia API endpoint - returns JSON with article extract
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_query}"
        
        print(f"→ Fetching from Wikipedia API...")
        
        # Create request with proper headers (Wikipedia requires User-Agent)
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'DoubtResolutionSystem/1.0 (Educational Project)',
                'Accept': 'application/json'
            }
        )
        
        # Make the HTTP request
        with urllib.request.urlopen(req, timeout=5) as response:
            # Read and decode the response
            data = response.read().decode('utf-8')
            
            # Simple extraction of the extract field from JSON
            # Using basic string operations (beginner-friendly, no JSON library needed)
            if '"extract":"' in data:
                start = data.find('"extract":"') + len('"extract":"')
                end = data.find('"', start)
                extract = data[start:end]
                
                # Unescape the text
                extract = extract.replace('\\n', ' ')
                extract = extract.replace('\\"', '"')
                extract = extract.replace('\\/', '/')
                
                return extract if extract else None
        
        return None
    
    except Exception as e:
        # If web scraping fails, return None (will use fallback)
        print(f"→ Web unavailable (using cached content)")
        return None


def simulate_web_scraping(subject, question):
    """
    Performs intelligent answer generation using Google Gemini API
    Falls back to Wikipedia web scraping or cached content if API unavailable
    
    Parameters:
        subject: The subject area of the question
        question: The student's question text
    
    Returns:
        A string containing the automatically generated answer
    """
    print("\n[🤖 INITIATING SMART ANSWER GENERATION...]")
    print("→ Processing your question...")
    time.sleep(0.3)
    
    question_lower = question.lower()
    
    # Step 1: Try Gemini AI first (if configured)
    if USE_GEMINI and GEMINI_AVAILABLE:
        print("→ Querying Google Gemini AI...")
        gemini_answer, source = query_gemini(question, subject)
        
        if gemini_answer and source == "gemini":
            print("→ Processing and formatting response...\n")
            time.sleep(0.3)
            
            formatted_response = f"🤖 AI-GENERATED ANSWER (Google Gemini)\n"
            formatted_response += f"Subject: {subject}\n"
            formatted_response += "-" * 60 + "\n"
            formatted_response += gemini_answer
            
            return formatted_response
    
    # Step 2: Try Wikipedia web scraping
    print("→ Attempting Wikipedia web scraping...")
    
    search_keyword = None
    
    if subject in web_scraping_database:
        subject_data = web_scraping_database[subject]
        keywords = subject_data["keywords"]
        
        # Find matching keyword
        for keyword in keywords:
            if keyword in question_lower:
                search_keyword = keyword
                break
    
    if search_keyword:
        print(f"→ Searching Wikipedia for: '{search_keyword}'...")
        time.sleep(0.3)
        
        web_content = fetch_from_web(search_keyword)
        
        if web_content:
            print("→ ✅ Successfully scraped content from Wikipedia!")
            print("→ Processing and extracting relevant information...\n")
            time.sleep(0.3)
            
            formatted_response = f"🌐 WEB-SCRAPED ANSWER (Wikipedia)\n"
            formatted_response += f"Topic: {search_keyword.title()}\n"
            formatted_response += "-" * 60 + "\n"
            formatted_response += web_content[:500]
            if len(web_content) > 500:
                formatted_response += "..."
            
            return formatted_response
    
    # Step 3: Fallback to cached educational content
    print("→ Using cached educational content...")
    time.sleep(0.3)
    
    if subject in web_scraping_database:
        subject_data = web_scraping_database[subject]
        print(f"→ Searching {subject} resources...")
        
        # Search for matching keywords in the question
        keywords = subject_data["keywords"]
        for keyword, answer in keywords.items():
            if keyword in question_lower:
                print(f"→ Match found! Extracting content from cache...")
                print("→ Content retrieval completed!\n")
                return answer
        
        # No keyword match - return default for subject
        print("→ General content extracted.\n")
        return subject_data["default"]
    
    else:
        # Subject not in database - return generic default
        print("→ Searching general educational resources...\n")
        return web_scraping_database["default"]["default"]


def add_instructor_response(question_dict, instructor_answer):
    """
    Allows instructor to add an authoritative/verified answer to a question
    
    Parameters:
        question_dict: The question dictionary to update
        instructor_answer: The instructor's authoritative answer text
    
    Returns:
        True if successful
    """
    question_dict["instructor_response"] = instructor_answer
    question_dict["is_verified"] = True
    return True


def display_all_responses(question_dict):
    """
    Displays both the automatic web-scraped response and 
    the instructor's authoritative response for a question
    
    Parameters:
        question_dict: The question dictionary containing all data
    """
    print("\n" + "="*70)
    print("QUESTION DETAILS & RESPONSES")
    print("="*70)
    
    # Display question information
    print(f"\n📝 Question ID: {question_dict['id']}")
    print(f"📚 Subject: {question_dict['subject']}")
    print(f"❓ Question: {question_dict['question']}")
    print(f"👤 Posted by: {question_dict['student_name']}")
    
    print("\n" + "-"*70)
    
    # Display automatically scraped response
    print("\n🌐 AUTOMATIC RESPONSE (Web Scraped):")
    print("-"*70)
    if question_dict["auto_response"]:
        print(question_dict["auto_response"])
    else:
        print("No automatic response available.")
    
    print("\n" + "-"*70)
    
    # Display instructor's authoritative response
    print("\n✅ INSTRUCTOR'S AUTHORITATIVE RESPONSE:")
    print("-"*70)
    if question_dict["instructor_response"]:
        print(question_dict["instructor_response"])
        print("\n[STATUS: VERIFIED BY INSTRUCTOR]")
    else:
        print("⏳ Awaiting instructor's response...")
        print("\n[STATUS: NOT YET VERIFIED]")
    
    print("\n" + "="*70 + "\n")
