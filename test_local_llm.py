
"""
Test script for local LLM configuration
"""

import sys
import requests

def test_ollama_connection():
    """Test if Ollama is running"""
    print(" Testing Ollama connection...")
    
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print(" Ollama is running!")
            models = response.json().get('models', [])
            if models:
                print(f"   Available models: {[m['name'] for m in models]}")
            else:
                print("   No models found. Run: ollama pull llama2")
            return True
        else:
            print(f" Ollama responded with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print(" Cannot connect to Ollama!")
        print("   Please install and start Ollama:")
        print("   1. Install from: https://ollama.ai/")
        print("   2. Run: ollama serve")
        print("   3. Pull a model: ollama pull llama2")
        return False
    except Exception as e:
        print(f" Error connecting to Ollama: {e}")
        return False

def test_config_import():
    """Test if the configuration imports correctly"""
    print("\n Testing configuration import...")
    
    try:
        from config import (
            OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL,
            validate_config, get_config_info
        )
        print(" Configuration imported successfully")
        print(f"   - Model: {OPENAI_MODEL}")
        print(f"   - Base URL: {OPENAI_BASE_URL}")
        print(f"   - API Key: {OPENAI_API_KEY}")
        return True
    except ImportError as e:
        print(f" Configuration import failed: {e}")
        return False

def test_app_import():
    """Test if the app imports correctly"""
    print("\n Testing app import...")
    
    try:
        # Test basic imports
        import streamlit as st
        import openai
        from app import HiringAssistant
        
        print(" App imports successfully")
        
        # Test HiringAssistant initialization
        assistant = HiringAssistant()
        print(" HiringAssistant initialized successfully")
        print(f"   - Conversation state: {assistant.conversation_state}")
        print(f"   - Tech stack: {assistant.tech_stack}")
        
        return True
    except ImportError as e:
        print(f" App import failed: {e}")
        return False
    except Exception as e:
        print(f" App initialization failed: {e}")
        return False

def main():
    """Run all tests"""
    print(" Testing Local LLM Configuration")
    print("=" * 50)
    
    tests = [
        test_config_import,
        test_app_import,
        test_ollama_connection
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f" Test failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f" Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print(" All tests passed! The application is ready to run.")
        print("\n To run the application:")
        print("1. Ensure Ollama is running: ollama serve")
        print("2. Pull a model: ollama pull llama2")
        print("3. Run: streamlit run app.py")
    else:
        print(" Some tests failed. Please check the errors above.")
        if passed >= 2:  
            print("\n The application is configured correctly, but Ollama needs to be set up.")
            print("   Follow the instructions in OLLAMA_SETUP.md")
    
    return passed == total

if __name__ == "__main__":
    success = main()
"""
Test script for local LLM configuration
"""

import sys
import requests

def test_ollama_connection():
    """Test if Ollama is running"""
    print(" Testing Ollama connection...")
    
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print(" Ollama is running!")
            models = response.json().get('models', [])
            if models:
                print(f"   Available models: {[m['name'] for m in models]}")
            else:
                print("   No models found. Run: ollama pull llama2")
            return True
        else:
            print(f" Ollama responded with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print(" Cannot connect to Ollama!")
        print("   Please install and start Ollama:")
        print("   1. Install from: https://ollama.ai/")
        print("   2. Run: ollama serve")
        print("   3. Pull a model: ollama pull llama2")
        return False
    except Exception as e:
        print(f" Error connecting to Ollama: {e}")
        return False

def test_config_import():
    """Test if the configuration imports correctly"""
    print("\n Testing configuration import...")
    
    try:
        from config import (
            OPENAI_API_KEY, OPENAI_MODEL, OPENAI_BASE_URL,
            validate_config, get_config_info
        )
        print(" Configuration imported successfully")
        print(f"   - Model: {OPENAI_MODEL}")
        print(f"   - Base URL: {OPENAI_BASE_URL}")
        print(f"   - API Key: {OPENAI_API_KEY}")
        return True
    except ImportError as e:
        print(f" Configuration import failed: {e}")
        return False

def test_app_import():
    """Test if the app imports correctly"""
    print("\n Testing app import...")
    
    try:
        # Test basic imports
        import streamlit as st
        import openai
        from app import HiringAssistant
        
        print(" App imports successfully")
        
        # Test HiringAssistant initialization
        assistant = HiringAssistant()
        print(" HiringAssistant initialized successfully")
        print(f"   - Conversation state: {assistant.conversation_state}")
        print(f"   - Tech stack: {assistant.tech_stack}")
        
        return True
    except ImportError as e:
        print(f" App import failed: {e}")
        return False
    except Exception as e:
        print(f" App initialization failed: {e}")
        return False

def main():
    """Run all tests"""
    print(" Testing Local LLM Configuration")
    print("=" * 50)
    
    tests = [
        test_config_import,
        test_app_import,
        test_ollama_connection
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f" Test failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f" Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print(" All tests passed! The application is ready to run.")
        print("\n To run the application:")
        print("1. Ensure Ollama is running: ollama serve")
        print("2. Pull a model: ollama pull llama2")
        print("3. Run: streamlit run app.py")
    else:
        print(" Some tests failed. Please check the errors above.")
        if passed >= 2:  
            print("\n The application is configured correctly, but Ollama needs to be set up.")
            print("   Follow the instructions in OLLAMA_SETUP.md")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 