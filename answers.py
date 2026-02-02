# answers.py - Answer generation and management module

from data import web_scraping_database
import time
import urllib.request
import urllib.parse
import re


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
    Performs REAL web scraping from Wikipedia
    Uses urllib (built-in) to fetch real content from the internet
    Falls back to cached content if web fetch fails
    
    Parameters:
        subject: The subject area of the question
        question: The student's question text
    
    Returns:
        A string containing the automatically scraped answer
    """
    print("\n[🌐 INITIATING WEB SCRAPING...]")
    print("→ Connecting to educational websites...")
    
    question_lower = question.lower()
    
    # Step 1: Try to identify main keyword from question
    search_keyword = None
    
    if subject in web_scraping_database:
        subject_data = web_scraping_database[subject]
        keywords = subject_data["keywords"]
        
        # Find matching keyword
        for keyword in keywords:
            if keyword in question_lower:
                search_keyword = keyword
                break
    
    # Step 2: Attempt REAL web scraping
    if search_keyword:
        print(f"→ Searching Wikipedia for: '{search_keyword}'...")
        time.sleep(0.3)
        
        web_content = fetch_from_web(search_keyword)
        
        if web_content:
            print("→ ✅ Successfully scraped content from Wikipedia!")
            print("→ Processing and extracting relevant information...\n")
            time.sleep(0.3)
            
            # Format the scraped content
            formatted_response = f"Web Source: en.wikipedia.org (LIVE SCRAPED)\n"
            formatted_response += f"Topic: {search_keyword.title()}\n"
            formatted_response += "-" * 60 + "\n"
            formatted_response += web_content[:500]  # Limit to 500 chars
            if len(web_content) > 500:
                formatted_response += "..."
            
            return formatted_response
    
    # Step 3: Fallback to cached/simulated content if web scraping failed
    print("→ Using cached educational content (web fetch unavailable)...")
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
