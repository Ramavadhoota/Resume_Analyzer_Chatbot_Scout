
"""
Simple test script for TalentScout Hiring Assistant
Tests core functionality without requiring all dependencies
"""

import sys
import os

def test_basic_imports():
    """Test basic imports and functionality"""
    print(" Testing basic imports...")
    
    try:
        # Test config import
        from config import TECH_KEYWORDS, REQUIRED_FIELDS, FALLBACK_QUESTIONS
        print(" Config module imported successfully")
        print(f"   - Tech keywords: {len(TECH_KEYWORDS)}")
        print(f"   - Required fields: {len(REQUIRED_FIELDS)}")
        print(f"   - Fallback questions: {len(FALLBACK_QUESTIONS)}")
        
    except ImportError as e:
        print(f" Config import failed: {e}")
        return False
    
    try:
        # Test utils import (without pandas)
        from utils import extract_email, extract_phone, extract_name
        print(" Utils module imported successfully")
        
        # Test basic functions
        test_email = extract_email("My email is test@example.com")
        test_phone = extract_phone("Call me at 123-456-7890")
        test_name = extract_name("My name is John Doe")
        
        print(f"   - Email extraction: {test_email}")
        print(f"   - Phone extraction: {test_phone}")
        print(f"   - Name extraction: {test_name}")
        
    except ImportError as e:
        print(f" Utils import failed: {e}")
        return False
    
    return True

def test_tech_stack_extraction():
    """Test tech stack extraction"""
    print("\n Testing tech stack extraction...")
    
    try:
        from utils import extract_tech_stack
        
        test_cases = [
            "I work with Python, Django, and PostgreSQL",
            "My skills include JavaScript, React, and Node.js",
            "I use Java, Spring, and MySQL"
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            result = extract_tech_stack(test_case)
            print(f"   Test {i}: '{test_case}' -> {result}")
            
        return True
        
    except Exception as e:
        print(f" Tech stack extraction failed: {e}")
        return False

def test_data_formatting():
    """Test data formatting functions"""
    print("\n Testing data formatting...")
    
    try:
        from utils import format_session_data, export_to_json
        
        # Test data
        candidate_info = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "123-456-7890",
            "experience": "3",
            "position": "developer",
            "location": "Test City"
        }
        
        tech_stack = ["python", "django", "postgresql"]
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        questions = ["What is Python?", "Explain Django"]
        
        # Test formatting
        formatted_data = format_session_data(candidate_info, tech_stack, messages, questions)
        print(f"   - Session ID: {formatted_data.get('session_id')}")
        print(f"   - Total messages: {formatted_data.get('conversation_summary', {}).get('total_messages')}")
        
        # Test JSON export
        json_data = export_to_json(formatted_data)
        print(f"   - JSON export length: {len(json_data)} characters")
        
        return True
        
    except Exception as e:
        print(f" Data formatting failed: {e}")
        return False

def test_configuration():
    """Test configuration settings"""
    print("\n Testing configuration...")
    
    try:
        from config import get_config_info
        
        config_info = get_config_info()
        print(f"   - OpenAI model: {config_info['openai_model']}")
        print(f"   - Max tokens: {config_info['max_tokens']}")
        print(f"   - Temperature: {config_info['temperature']}")
        print(f"   - Tech keywords count: {config_info['tech_keywords_count']}")
        
        return True
        
    except Exception as e:
        print(f" Configuration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print(" Running TalentScout Hiring Assistant Simple Tests")
    print("=" * 60)
    
    tests = [
        test_basic_imports,
        test_tech_stack_extraction,
        test_data_formatting,
        test_configuration
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f" Test failed with exception: {e}")
    
    print("\n" + "=" * 60)
    print(f" Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print(" All tests passed! The application is ready to run.")
        print("\n To run the application:")
        print("1. Install dependencies: pip install streamlit openai python-dotenv")
        print("2. Set your OpenAI API key in a .env file")
        print("3. Run: streamlit run app.py")
    else:
        print(" Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
"""
Simple test script for TalentScout Hiring Assistant
Tests core functionality without requiring all dependencies
"""

import sys
import os

def test_basic_imports():
    """Test basic imports and functionality"""
    print(" Testing basic imports...")
    
    try:
        # Test config import
        from config import TECH_KEYWORDS, REQUIRED_FIELDS, FALLBACK_QUESTIONS
        print(" Config module imported successfully")
        print(f"   - Tech keywords: {len(TECH_KEYWORDS)}")
        print(f"   - Required fields: {len(REQUIRED_FIELDS)}")
        print(f"   - Fallback questions: {len(FALLBACK_QUESTIONS)}")
        
    except ImportError as e:
        print(f" Config import failed: {e}")
        return False
    
    try:
        # Test utils import (without pandas)
        from utils import extract_email, extract_phone, extract_name
        print(" Utils module imported successfully")
        
        # Test basic functions
        test_email = extract_email("My email is test@example.com")
        test_phone = extract_phone("Call me at 123-456-7890")
        test_name = extract_name("My name is John Doe")
        
        print(f"   - Email extraction: {test_email}")
        print(f"   - Phone extraction: {test_phone}")
        print(f"   - Name extraction: {test_name}")
        
    except ImportError as e:
        print(f" Utils import failed: {e}")
        return False
    
    return True

def test_tech_stack_extraction():
    """Test tech stack extraction"""
    print("\n Testing tech stack extraction...")
    
    try:
        from utils import extract_tech_stack
        
        test_cases = [
            "I work with Python, Django, and PostgreSQL",
            "My skills include JavaScript, React, and Node.js",
            "I use Java, Spring, and MySQL"
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            result = extract_tech_stack(test_case)
            print(f"   Test {i}: '{test_case}' -> {result}")
            
        return True
        
    except Exception as e:
        print(f" Tech stack extraction failed: {e}")
        return False

def test_data_formatting():
    """Test data formatting functions"""
    print("\n Testing data formatting...")
    
    try:
        from utils import format_session_data, export_to_json
        
        # Test data
        candidate_info = {
            "name": "Test User",
            "email": "test@example.com",
            "phone": "123-456-7890",
            "experience": "3",
            "position": "developer",
            "location": "Test City"
        }
        
        tech_stack = ["python", "django", "postgresql"]
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        questions = ["What is Python?", "Explain Django"]
        
        # Test formatting
        formatted_data = format_session_data(candidate_info, tech_stack, messages, questions)
        print(f"   - Session ID: {formatted_data.get('session_id')}")
        print(f"   - Total messages: {formatted_data.get('conversation_summary', {}).get('total_messages')}")
        
        # Test JSON export
        json_data = export_to_json(formatted_data)
        print(f"   - JSON export length: {len(json_data)} characters")
        
        return True
        
    except Exception as e:
        print(f" Data formatting failed: {e}")
        return False

def test_configuration():
    """Test configuration settings"""
    print("\n Testing configuration...")
    
    try:
        from config import get_config_info
        
        config_info = get_config_info()
        print(f"   - OpenAI model: {config_info['openai_model']}")
        print(f"   - Max tokens: {config_info['max_tokens']}")
        print(f"   - Temperature: {config_info['temperature']}")
        print(f"   - Tech keywords count: {config_info['tech_keywords_count']}")
        
        return True
        
    except Exception as e:
        print(f" Configuration test failed: {e}")
        return False

def main():
    """Run all tests"""
    print(" Running TalentScout Hiring Assistant Simple Tests")
    print("=" * 60)
    
    tests = [
        test_basic_imports,
        test_tech_stack_extraction,
        test_data_formatting,
        test_configuration
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f" Test failed with exception: {e}")
    
    print("\n" + "=" * 60)
    print(f" Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print(" All tests passed! The application is ready to run.")
        print("\n To run the application:")
        print("1. Install dependencies: pip install streamlit openai python-dotenv")
        print("2. Set your OpenAI API key in a .env file")
        print("3. Run: streamlit run app.py")
    else:
        print(" Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 