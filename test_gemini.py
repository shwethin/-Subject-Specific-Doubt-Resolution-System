# test_gemini.py - Test Google Gemini API connection

import os
from answers import setup_gemini, query_gemini, USE_GEMINI, GEMINI_AVAILABLE

print("="*70)
print("TESTING GOOGLE GEMINI API CONNECTION")
print("="*70)

# Check environment
api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    print("\n❌ GEMINI_API_KEY environment variable not found!")
    print("\nTo set it up:")
    print("\nWindows (PowerShell):")
    print('  $env:GEMINI_API_KEY="your-key-here"')
    print("\nWindows (Command Prompt):")
    print("  set GEMINI_API_KEY=your-key-here")
    print("\nMac/Linux:")
    print('  export GEMINI_API_KEY="your-key-here"')
    print("\nSee API_SETUP.md for more details.")
else:
    print(f"\n✅ API Key found (length: {len(api_key)} characters)")

# Check library
if not GEMINI_AVAILABLE:
    print("\n❌ google-generativeai library not installed!")
    print("\nInstall it with:")
    print("  pip install google-generativeai")
else:
    print("✅ google-generativeai library installed")

# Test setup
if USE_GEMINI and GEMINI_AVAILABLE:
    print("\n🧪 Testing Gemini API connection...")
    
    if setup_gemini():
        print("✅ Successfully connected to Gemini API!")
        
        # Try a simple query
        print("\n📝 Testing with a sample question...")
        answer, source = query_gemini("What is Python?", "Python")
        
        if answer:
            print(f"\n✅ Got response from: {source}")
            print("\nSample Answer:")
            print("-" * 70)
            print(answer[:300] + "..." if len(answer) > 300 else answer)
            print("-" * 70)
        else:
            print("⚠️  Could not get response from Gemini API")
    else:
        print("❌ Failed to setup Gemini API")
else:
    print("\n⚠️  Gemini API not available. System will use cached content.")

print("\n" + "="*70)
print("TEST COMPLETE")
print("="*70)
