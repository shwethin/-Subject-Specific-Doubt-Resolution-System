# 📚 Subject-Specific Doubt Resolution System

A console-based Python application simulating a blended learning platform where students can post subject-specific questions and receive both automatically web-scraped preliminary answers and instructor-verified authoritative responses.

---

## 🎯 Project Overview

In blended learning environments, students often have subject-related doubts outside classroom hours. This system addresses this need by providing:

1. **Automatic Response**: Simulated web scraping from educational websites for instant preliminary answers
2. **Instructor Response**: Verified authoritative answers from course instructors
3. **Organized Database**: Efficient tracking of questions and their verification status

---

## 📁 Project Structure

```
python/
├── main.py          # Main program entry point with menu system
├── doubts.py        # Question/doubt management functions
├── answers.py       # Answer generation and display functions
├── data.py          # Data storage and web scraping simulation database
└── README.md        # Documentation (this file)
```

### File Descriptions:

- **data.py**: Contains global data structures (lists/dictionaries) storing questions and simulated web content
- **doubts.py**: Functions for posting, viewing, searching, and filtering questions
- **answers.py**: Web scraping simulation logic and response display functions
- **main.py**: User interface and program flow control

---

## 🚀 How to Run

```bash
python main.py
```

---

## ✨ Key Features

### Student Portal:
1. **Post Questions** - Submit doubts with name, subject, and question text
2. **View All Questions** - Browse all posted questions with verification status
3. **View Responses** - See both automatic and instructor responses side-by-side
4. **Filter by Subject** - View questions for specific subjects only

### Instructor Portal:
5. **View Pending Questions** - See questions awaiting verification
6. **Add Authoritative Answers** - Provide verified responses to student questions

---

## 🔄 System Workflow

```
Student Posts Question
         ↓
System Simulates Web Scraping
         ↓
Automatic Response Generated
         ↓
Question Stored (Status: Pending)
         ↓
Instructor Reviews Question
         ↓
Instructor Adds Verified Answer
         ↓
Question Marked as Verified
         ↓
Student Views Both Responses
```

---

## 📝 Detailed Usage

### 🎓 For Students:

**Posting a Question:**
1. Select option 1 from main menu
2. Enter your name
3. Choose subject (Python, Mathematics, Physics, Chemistry, Data Structures)
4. Type your question
5. System automatically performs web scraping simulation
6. Receive Question ID for future reference

**Viewing Responses:**
1. Select option 3 from main menu
2. Enter the Question ID
3. View both:
   - Automatic response (from simulated web scraping)
   - Instructor's authoritative response (if available)

### 👨‍🏫 For Instructors:

**Adding Verified Answers:**
1. Select option 6 from main menu
2. Review pending questions list
3. Enter Question ID to answer
4. See the question and current automatic response
5. Provide your authoritative answer
6. Question automatically marked as "VERIFIED"

---

## 🌐 ACTUAL Web Scraping Implementation

The system performs **REAL web scraping** using Python's built-in `urllib` library:

### ✅ How It Works:

1. **Keyword Detection**: Identifies main topic from student's question
2. **Live HTTP Request**: Makes actual request to Wikipedia's REST API
3. **Content Extraction**: Fetches real content from https://en.wikipedia.org
4. **Smart Fallback**: If web fails (no internet), uses cached educational content
5. **Beginner-Friendly**: Uses only built-in Python libraries (no pip install needed!)

### 🔬 Technical Implementation:

```python
# Makes REAL HTTP request to Wikipedia API
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"

# Add proper headers
req = urllib.request.Request(url, headers={
    'User-Agent': 'DoubtResolutionSystem/1.0',
    'Accept': 'application/json'
})

# Fetch live content
with urllib.request.urlopen(req, timeout=5) as response:
    data = response.read().decode('utf-8')
    # Extract content using string operations (no JSON library!)
```

### 🧪 Test It Yourself:

Run the test file to see **PROOF** of live web scraping:
```bash
python test_webscraping.py
```

This will fetch **actual** Wikipedia content for: function, loop, gravity, atom, calculus

**Output shows:**
- ✅ "SUCCESS! Scraped X characters from REAL Wikipedia"
- Actual live content from the internet
- Proves the system performs genuine web scraping

---

## 🔧 Web Scraping Simulation

When internet is unavailable, the system has a fallback:

1. **Keyword Matching**: Searches question text for subject-specific keywords
2. **Database Lookup**: Retrieves pre-defined content matching those keywords
3. **Source Attribution**: Each response shows simulated source website
4. **Network Delay**: Uses `time.sleep()` to simulate realistic web fetching

**Example:**
```
Question: "What is a loop in Python?"
         ↓
System searches for keyword "loop" in "Python" subject
         ↓
Returns: "Web Source: tutorialspoint.com
         → A loop executes a block of code repeatedly..."
```

---

## 💡 Technical Concepts Demonstrated

### ✅ Core Python Concepts:
- **Lists**: Storing multiple questions in `questions_database`
- **Dictionaries**: Structured data for each question with multiple fields
- **Functions**: Modular code organization
- **Global Variables**: Shared data across modules
- **String Methods**: `.lower()`, `.strip()` for input processing
- **Control Flow**: if-elif-else, while loops, for loops
- **Error Handling**: try-except for user input validation
- **Module Imports**: Organizing code across multiple files

### ✅ No Advanced Concepts:
- ❌ No classes/OOP
- ❌ No external libraries
- ❌ No databases
- ❌ No frameworks
- ❌ No file I/O (data stored in memory)

---

## 🎨 Customization Guide

### Adding New Subjects:

Edit `data.py` and add to `web_scraping_database`:

```python
"Biology": {
    "keywords": {
        "cell": "Web Source: biology.com\n→ A cell is the basic unit of life...",
        "dna": "Web Source: genome.gov\n→ DNA carries genetic information...",
    },
    "default": "Web Source: khanacademy.org\n→ Biology is the study of life..."
}
```

### Adding More Keywords:

Simply add more key-value pairs to existing subjects:

```python
"Python": {
    "keywords": {
        # ... existing keywords ...
        "string": "Web Source: python.org\n→ Strings are sequences of characters...",
        "tuple": "Web Source: w3schools.com\n→ Tuples are immutable sequences...",
    }
}
```

### Modifying Menu Options:

Edit `show_main_menu()` in `main.py` to add/remove features.

---

## 📊 Sample Data Flow

```python
# Student posts question
post_question("John", "Python", "What is a dictionary?")
    ↓
# System creates question record:
{
    "id": 1,
    "student_name": "John",
    "subject": "Python",
    "question": "What is a dictionary?",
    "auto_response": "Web Source: realpython.com...",
    "instructor_response": None,
    "is_verified": False
}
    ↓
# Instructor adds answer
add_instructor_response(question, "Dictionaries in Python...")
    ↓
# Question updated:
{
    ...
    "instructor_response": "Dictionaries in Python...",
    "is_verified": True
}
```

---

## 🎓 Perfect for College Presentations

### Why This Project Works:

✅ **Beginner-Friendly**: Uses only basic Python syntax  
✅ **Well-Documented**: Extensive comments and docstrings  
✅ **Modular Design**: Easy to explain file-by-file  
✅ **Live Modifiable**: Add subjects/keywords during demo  
✅ **Real-World Application**: Solves actual educational problem  
✅ **Complete System**: Full workflow from question to answer  

### Presentation Tips:

1. **Start with `data.py`**: "This is our simulated web database - no internet needed!"
2. **Explain `answers.py`**: "This is where web scraping magic happens"
3. **Show `doubts.py`**: "These functions manage all our questions"
4. **Demo `main.py`**: Live demonstration of posting and answering questions
5. **Customize Live**: Add a new subject during presentation to show understanding

---

## 🎯 Sample Demo Flow

```
1. Run program → Show welcome screen
2. Post question: "What is gravity?" (Physics)
3. Show automatic web-scraped answer
4. Switch to instructor mode
5. Add verified answer with detailed explanation
6. View complete responses side-by-side
7. Filter questions by subject
8. Show pending questions list
```

---

## 📚 Learning Outcomes

Students who complete this project will understand:

- Modular programming and code organization
- Data structures (lists and dictionaries)
- Function design and documentation
- User input handling and validation
- Simulating external systems (web scraping)
- Menu-driven console applications
- Global vs local scope
- Import statements and module interaction

---

## 🔍 Code Statistics

- **Lines of Code**: ~400 lines
- **Number of Functions**: 15+
- **Number of Files**: 4 Python files
- **External Dependencies**: None (pure Python)
- **Complexity**: Beginner to Intermediate

---

## 🚀 Future Enhancement Ideas

1. Save data to text files for persistence
2. Add student login system
3. Export questions to CSV
4. Add question categories/tags
5. Implement search functionality
6. Add timestamp to questions
7. Rating system for answers
8. Statistics dashboard

---

**Built with ❤️ using Pure Python - No external libraries required!** 🐍
