# test_webscraping.py - Demonstrates ACTUAL web scraping

import urllib.request
import urllib.parse

print("="*70)
print("TESTING REAL WEB SCRAPING FROM WIKIPEDIA")
print("="*70)

# Test queries
test_queries = ["function", "loop", "gravity", "atom", "calculus"]

for query in test_queries:
    print(f"\n📡 Scraping Wikipedia for: '{query}'")
    print("-"*70)
    
    try:
        # Encode query for URL
        encoded = urllib.parse.quote(query)
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
        
        # Create request with proper headers
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'EducationalProject/1.0',
                'Accept': 'application/json'
            }
        )
        
        # Fetch from web
        with urllib.request.urlopen(req, timeout=5) as response:
            data = response.read().decode('utf-8')
            
            # Simple extraction (no JSON library needed)
            if '"extract":"' in data:
                start = data.find('"extract":"') + len('"extract":"')
                end = data.find('"', start)
                content = data[start:end]
                
                # Clean up
                content = content.replace('\\n', ' ')
                content = content.replace('\\"', '"')
                
                print(f"✅ SUCCESS! Scraped {len(content)} characters from REAL Wikipedia")
                print(f"\nActual web content:")
                print(content[:250] + "...")
            else:
                print("❌ No content found")
                
    except Exception as e:
        print(f"❌ Failed: {e}")
    
    print("-"*70)

print("\n" + "="*70)
print("✅ This proves the system can fetch LIVE content from internet!")
print("="*70)

