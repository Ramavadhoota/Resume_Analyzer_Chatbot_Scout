
"""
Test script for TalentScout Hiring Assistant
This script tests the utility functions and basic functionality without requiring OpenAI API calls.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import (
    extract_email, extract_phone, extract_experience_years, extract_name,
    extract_position, extract_location, extract_tech_stack, validate_candidate_info,
    format_session_data, sanitize_input, get_tech_stack_categories
)
from config import TECH_KEYWORDS, REQUIRED_FIELDS, FALLBACK_QUESTIONS

def test_email_extraction():
    """Test email extraction functionality"""
    print("Testing email extraction...")
    
    test_cases = [
        "My email is john.doe@example.com",
        "Contact me at jane@company.org",
        "Email: test@test.co.uk",
        "No email here",
        "Multiple emails: first@test.com and second@test.org"
    ]
    
    for test_case in test_cases:
        result = extract_email(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_phone_extraction():
    """Test phone number extraction functionality"""
    print("Testing phone extraction...")
    
    test_cases = [
        "My phone is 123-456-7890",
        "Call me at 987.654.3210",
        "Phone: 5551234567",
        "No phone here",
        "Multiple: 111-222-3333 and 444-555-6666"
    ]
    
    for test_case in test_cases:
        result = extract_phone(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_name_extraction():
    """Test name extraction functionality"""
    print("Testing name extraction...")
    
    test_cases = [
        "My name is John Doe",
        "I am Jane Smith",
        "Name: Bob Johnson",
        "Call me Alice",
        "No name mentioned"
    ]
    
    for test_case in test_cases:
        result = extract_name(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_tech_stack_extraction():
    """Test tech stack extraction functionality"""
    print("Testing tech stack extraction...")
    
    test_cases = [
        "I work with Python, Django, and PostgreSQL",
        "My skills include JavaScript, React, and Node.js",
        "I use Java, Spring, and MySQL",
        "No tech mentioned",
        "I know Python, JavaScript, AWS, Docker, and Git"
    ]
    
    for test_case in test_cases:
        result = extract_tech_stack(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_validation():
    """Test candidate information validation"""
    print("Testing validation...")
    
    test_cases = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
            "experience": "5",
            "position": "developer",
            "location": "New York"
        },
        {
            "name": "Jane Smith",
            "email": "invalid-email",
            "phone": "invalid-phone",
            "experience": "invalid",
            "position": "engineer"
            # Missing location
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        result = validate_candidate_info(test_case)
        print(f"Test case {i+1}: {result}")
    
    print()

def test_tech_categorization():
    """Test tech stack categorization"""
    print("Testing tech stack categorization...")
    
    tech_stacks = [
        ["python", "django", "postgresql", "aws"],
        ["javascript", "react", "node.js", "mongodb"],
        ["java", "spring", "mysql", "docker", "kubernetes"]
    ]
    
    for tech_stack in tech_stacks:
        categories = get_tech_stack_categories(tech_stack)
        print(f"Tech stack: {tech_stack}")
        print(f"Categories: {categories}")
        print()

def test_data_formatting():
    """Test session data formatting"""
    print("Testing data formatting...")
    
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
    
    formatted_data = format_session_data(candidate_info, tech_stack, messages, questions)
    print("Formatted data keys:", list(formatted_data.keys()))
    print("Session ID:", formatted_data.get("session_id"))
    print("Total messages:", formatted_data.get("conversation_summary", {}).get("total_messages"))

def test_sanitization():
    """Test input sanitization"""
    print("Testing input sanitization...")
    
    test_cases = [
        "Normal text",
        "Text with <script>alert('xss')</script>",
        "Text with 'quotes' and \"double quotes\"",
        "Very long text " * 100,  # Test length limit
        "Text with < > characters"
    ]
    
    for test_case in test_cases:
        result = sanitize_input(test_case)
        print(f"Original: '{test_case[:50]}...' -> Sanitized: '{result[:50]}...'")

def main():
    """Run all tests"""
    print(" Running TalentScout Hiring Assistant Tests")
    print("=" * 50)
    
    try:
        test_email_extraction()
        test_phone_extraction()
        test_name_extraction()
        test_tech_stack_extraction()
        test_validation()
        test_tech_categorization()
        test_data_formatting()
        test_sanitization()
        
        print(" All tests completed successfully!")
        print("\n Configuration Summary:")
        print(f"- Supported tech keywords: {len(TECH_KEYWORDS)}")
        print(f"- Required fields: {len(REQUIRED_FIELDS)}")
        print(f"- Fallback questions: {len(FALLBACK_QUESTIONS)}")
        
    except Exception as e:
        print(f" Test failed with error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
"""
Test script for TalentScout Hiring Assistant
This script tests the utility functions and basic functionality without requiring OpenAI API calls.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import (
    extract_email, extract_phone, extract_experience_years, extract_name,
    extract_position, extract_location, extract_tech_stack, validate_candidate_info,
    format_session_data, sanitize_input, get_tech_stack_categories
)
from config import TECH_KEYWORDS, REQUIRED_FIELDS, FALLBACK_QUESTIONS

def test_email_extraction():
    """Test email extraction functionality"""
    print("Testing email extraction...")
    
    test_cases = [
        "My email is john.doe@example.com",
        "Contact me at jane@company.org",
        "Email: test@test.co.uk",
        "No email here",
        "Multiple emails: first@test.com and second@test.org"
    ]
    
    for test_case in test_cases:
        result = extract_email(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_phone_extraction():
    """Test phone number extraction functionality"""
    print("Testing phone extraction...")
    
    test_cases = [
        "My phone is 123-456-7890",
        "Call me at 987.654.3210",
        "Phone: 5551234567",
        "No phone here",
        "Multiple: 111-222-3333 and 444-555-6666"
    ]
    
    for test_case in test_cases:
        result = extract_phone(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_name_extraction():
    """Test name extraction functionality"""
    print("Testing name extraction...")
    
    test_cases = [
        "My name is John Doe",
        "I am Jane Smith",
        "Name: Bob Johnson",
        "Call me Alice",
        "No name mentioned"
    ]
    
    for test_case in test_cases:
        result = extract_name(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_tech_stack_extraction():
    """Test tech stack extraction functionality"""
    print("Testing tech stack extraction...")
    
    test_cases = [
        "I work with Python, Django, and PostgreSQL",
        "My skills include JavaScript, React, and Node.js",
        "I use Java, Spring, and MySQL",
        "No tech mentioned",
        "I know Python, JavaScript, AWS, Docker, and Git"
    ]
    
    for test_case in test_cases:
        result = extract_tech_stack(test_case)
        print(f"Input: '{test_case}' -> Result: {result}")
    
    print()

def test_validation():
    """Test candidate information validation"""
    print("Testing validation...")
    
    test_cases = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
            "experience": "5",
            "position": "developer",
            "location": "New York"
        },
        {
            "name": "Jane Smith",
            "email": "invalid-email",
            "phone": "invalid-phone",
            "experience": "invalid",
            "position": "engineer"
            # Missing location
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        result = validate_candidate_info(test_case)
        print(f"Test case {i+1}: {result}")
    
    print()

def test_tech_categorization():
    """Test tech stack categorization"""
    print("Testing tech stack categorization...")
    
    tech_stacks = [
        ["python", "django", "postgresql", "aws"],
        ["javascript", "react", "node.js", "mongodb"],
        ["java", "spring", "mysql", "docker", "kubernetes"]
    ]
    
    for tech_stack in tech_stacks:
        categories = get_tech_stack_categories(tech_stack)
        print(f"Tech stack: {tech_stack}")
        print(f"Categories: {categories}")
        print()

def test_data_formatting():
    """Test session data formatting"""
    print("Testing data formatting...")
    
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
    
    formatted_data = format_session_data(candidate_info, tech_stack, messages, questions)
    print("Formatted data keys:", list(formatted_data.keys()))
    print("Session ID:", formatted_data.get("session_id"))
    print("Total messages:", formatted_data.get("conversation_summary", {}).get("total_messages"))

def test_sanitization():
    """Test input sanitization"""
    print("Testing input sanitization...")
    
    test_cases = [
        "Normal text",
        "Text with <script>alert('xss')</script>",
        "Text with 'quotes' and \"double quotes\"",
        "Very long text " * 100,  # Test length limit
        "Text with < > characters"
    ]
    
    for test_case in test_cases:
        result = sanitize_input(test_case)
        print(f"Original: '{test_case[:50]}...' -> Sanitized: '{result[:50]}...'")

def main():
    """Run all tests"""
    print(" Running TalentScout Hiring Assistant Tests")
    print("=" * 50)
    
    try:
        test_email_extraction()
        test_phone_extraction()
        test_name_extraction()
        test_tech_stack_extraction()
        test_validation()
        test_tech_categorization()
        test_data_formatting()
        test_sanitization()
        
        print(" All tests completed successfully!")
        print("\n Configuration Summary:")
        print(f"- Supported tech keywords: {len(TECH_KEYWORDS)}")
        print(f"- Required fields: {len(REQUIRED_FIELDS)}")
        print(f"- Fallback questions: {len(FALLBACK_QUESTIONS)}")
        
    except Exception as e:
        print(f" Test failed with error: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 