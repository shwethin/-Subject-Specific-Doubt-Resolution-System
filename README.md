# 📚 Subject-Specific Doubt Resolution System

A console-based Python application simulating a blended learning platform where students can post subject-specific questions and receive intelligent responses powered by **Google Gemini AI**, with fallback to **Wikipedia web scraping** and **instructor verification**.

---

## 🎯 Project Overview

In blended learning environments, students often have subject-related doubts outside classroom hours. This system addresses this need by providing:

1. **AI-Powered Responses**: Google Gemini API for intelligent, context-aware answers
2. **Web Scraping Fallback**: Wikipedia integration when API unavailable
3. **Instructor Verification**: Course instructors add verified authoritative answers
4. **Organized Database**: Efficient tracking of questions and their verification status

---

## 🤖 Google Gemini AI Integration (NEW!)

This system now features **Google Gemini AI** for smart answer generation!

### ✨ Answer Generation Priority:

1. **Google Gemini API** (if configured) → AI-powered intelligent answers
2. **Wikipedia Web Scraping** (fallback) → Real web content
3. **Cached Content** (fallback) → Educational database

### 🔒 Safety Features:

- API key stored in **environment variable** (never in code)
- **Optional** - system works without API key
- **Secure** - uses built-in Python libraries only
- **Free tier** available for testing

**See [API_SETUP.md](API_SETUP.md) for Gemini configuration guide**

---

## � Installation & Setup (For External Users)

### Prerequisites:
- **Python 3.7+** installed
- **Git** (optional, for cloning)
- **Gemini API Key** (optional, for AI features)

### Step 1: Get the Code

**Option A: Clone from GitHub**
```bash
git clone https://github.com/shwethin/-Subject-Specific-Doubt-Resolution-System.git
cd -Subject-Specific-Doubt-Resolution-System
```

**Option B: Download as ZIP**
1. Go to https://github.com/shwethin/-Subject-Specific-Doubt-Resolution-System
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal in the extracted folder

### Step 2: Install Dependencies (Optional)

For Gemini AI support:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install google-generativeai
```

### Step 3: Set Gemini API Key (Optional)

To enable AI-powered answers:

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
```

**Mac/Linux:**
```bash
export GEMINI_API_KEY="your-api-key-here"
```

See [API_SETUP.md](API_SETUP.md) for detailed instructions.

### Step 4: Run the Program

```bash
python main.py
```

The system works with or without Gemini API!

### Step 5: Use the System

1. **Post a Question** (Option 1)
   - Enter your name
   - Choose a subject (Python, Mathematics, Physics, Chemistry, Data Structures)
   - Type your question
   - System automatically generates answers using AI or web scraping

2. **View Questions** (Option 2)
   - See all posted questions and their status

3. **View Responses** (Option 3)
   - See automatic AI/web-scraped answer + instructor's verified answer

4. **Add Instructor Answer** (Option 6)
   - Verify student questions with authoritative answers

### Test Gemini API

To test if Gemini is configured:
```bash
python test_gemini.py
```

### Test Web Scraping

To test Wikipedia scraping:
```bash
python test_webscraping.py
```

---

## �📁 Project Structure

```
python/
├── main.py               # Main program entry point with menu system
├── doubts.py             # Question/doubt management functions
├── answers.py            # Answer generation (Gemini + Wikipedia fallback)
├── data.py               # Data storage and fallback content
├── demo.py               # Demo script
├── test_gemini.py        # Test Gemini API connection
├── test_webscraping.py   # Test Wikipedia web scraping
├── requirements.txt      # Python dependencies
├── API_SETUP.md          # Gemini API configuration guide
└── README.md             # Documentation (this file)
```

### File Descriptions:

- **main.py**: Program entry point with user interface and menu
- **answers.py**: Answer generation (Gemini AI → Wikipedia → Cached content)
- **doubts.py**: Question management and filtering
- **data.py**: Data structures and fallback educational content
- **test_gemini.py**: Tests Gemini API connectivity
- **test_webscraping.py**: Tests Wikipedia web scraping

---

## 🚀 How to Run

```bash
python main.py
```

---

## ❓ Troubleshooting

### Issue: "python: command not found"
**Solution**: Python is not installed or not in PATH
- Install Python from https://www.python.org/downloads/
- On Windows, check "Add Python to PATH" during installation
- Use `python3` instead of `python` if needed

### Issue: "ModuleNotFoundError"
**Solution**: Some required module is missing
- Since this project uses only built-in libraries, this shouldn't happen
- Try reinstalling Python

### Issue: Web scraping not working (shows cached content)
**Solution**: Internet connection issue
- Check your internet connection
- The system automatically falls back to cached content
- This is normal behavior

### Issue: Menu shows but input not responding
**Solution**: Terminal input issue
- Try pressing Enter
- Make sure terminal window is in focus
- Restart the program

### Issue: "Permission denied" on Linux/Mac
**Solution**: Need execute permissions
```bash
chmod +x main.py
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
