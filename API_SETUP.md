# API_SETUP.md - Gemini API Configuration Guide

## Setting Up Google Gemini API

This guide explains how to safely set up and use the Google Gemini API for the Doubt Resolution System.

---

## Step 1: Get Your Gemini API Key

1. Go to: https://aistudio.google.com/apikey
2. Click **"Create API Key"**
3. A new key will be generated - **copy it immediately**
4. Store it safely (never share it publicly!)

---

## Step 2: Install Required Package

Run this command once to install the Google Gemini library:

```bash
pip install google-generativeai
```

Or if using virtual environment:
```bash
.venv/Scripts/pip install google-generativeai
```

---

## Step 3: Set Your API Key

### Option A: Using Environment Variable (RECOMMENDED - SAFE)

**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your-api-key-here"
python main.py
```

**On Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
python main.py
```

**On Mac/Linux:**
```bash
export GEMINI_API_KEY="your-api-key-here"
python main.py
```

### Option B: Using .env File (Also Safe)

1. Create a `.env` file in your project folder:
```
GEMINI_API_KEY=your-api-key-here
```

2. The system will automatically read it

### Option C: Using Direct Configuration (Less Safe)

Edit `answers.py` and set:
```python
GEMINI_API_KEY = "your-api-key-here"
```

⚠️ **Never commit this to GitHub!** Use Option A or B instead.

---

## Step 4: Run the Program

```bash
python main.py
```

The system will now:
- ✅ Use Gemini API for real-time answers
- ✅ Fall back to cached content if API fails
- ✅ Keep your API key secure

---

## Security Best Practices

✅ **DO:**
- Use environment variables
- Use .env file (add to .gitignore)
- Rotate keys regularly
- Never share your API key

❌ **DON'T:**
- Hardcode keys in source files
- Upload keys to GitHub
- Share keys with others
- Use same key for multiple projects

---

## Testing Your Setup

Run this to verify Gemini API is working:

```bash
python test_gemini.py
```

This will test the API connection without starting the full application.

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'google'"
```bash
pip install google-generativeai
```

### "API key not found" or "Invalid API key"
- Check your environment variable is set correctly
- Verify the key from: https://aistudio.google.com/apikey
- Make sure there are no extra spaces in the key

### "Rate limit exceeded"
- Gemini API has free tier limits
- Wait a few minutes before retrying
- System automatically falls back to cached content

### "Connection timeout"
- Check your internet connection
- System automatically uses cached content as fallback

---

## API Costs

**Gemini API (Free Tier):**
- ✅ Free to use
- Limited requests per day
- Great for development and learning
- Perfect for this project

Visit https://ai.google.dev/pricing for details.

---

## Reverting to Wikipedia

If you want to go back to Wikipedia web scraping:

1. Edit `answers.py`
2. Change the `USE_GEMINI` flag to `False`
3. Save and run `python main.py`

---

**Your project is now AI-powered with Gemini! 🚀**
