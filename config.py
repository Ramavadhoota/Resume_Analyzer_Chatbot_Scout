
"""
Configuration file for TalentScout Hiring Assistant
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Local LLM Configuration (Ollama)
OPENAI_API_KEY = "local"  # Not needed for local LLMs
OPENAI_MODEL = "llama2"  # or "mistral", "codellama", "llama2:7b", etc.
OPENAI_MAX_TOKENS = 500
OPENAI_TEMPERATURE = 0.7
OPENAI_BASE_URL = "http://localhost:11434/v1"  # Ollama default endpoint

# Streamlit Configuration
STREAMLIT_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", 8501))
STREAMLIT_ADDRESS = os.getenv("STREAMLIT_SERVER_ADDRESS", "localhost")

# Application Configuration
APP_TITLE = "TalentScout Hiring Assistant"
APP_ICON = "🤖"

# Tech Stack Keywords for Detection
TECH_KEYWORDS = [
    # Programming Languages
    'python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'swift', 'kotlin', 'scala',
    
    # Frontend Frameworks
    'react', 'angular', 'vue', 'svelte', 'next.js', 'nuxt.js',
    
    # Backend Frameworks
    'django', 'flask', 'spring', 'node.js', 'express', 'fastapi', 'laravel', 'rails',
    
    # Databases
    'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle', 'sql server',
    
    # Cloud Platforms
    'aws', 'azure', 'gcp', 'heroku', 'digitalocean',
    
    # DevOps & Tools
    'docker', 'kubernetes', 'jenkins', 'git', 'github', 'gitlab', 'jira', 'confluence',
    
    # Methodologies
    'agile', 'scrum', 'kanban', 'waterfall',
    
    # Other Technologies
    'html', 'css', 'sass', 'less', 'typescript', 'webpack', 'babel'
]

# Conversation States
CONVERSATION_STATES = {
    'GREETING': 'greeting',
    'COLLECTING_INFO': 'collecting_info',
    'COLLECTING_TECH_STACK': 'collecting_tech_stack',
    'GENERATING_QUESTIONS': 'generating_questions',
    'TECHNICAL_ASSESSMENT': 'technical_assessment',
    'CONCLUSION': 'conclusion'
}

# Required Candidate Information Fields
REQUIRED_FIELDS = ['name', 'email', 'phone', 'experience', 'position', 'location']

# Conversation Ending Keywords
EXIT_KEYWORDS = ['goodbye', 'exit', 'quit', 'end', 'stop', 'bye', 'finish']

# Fallback Technical Questions
FALLBACK_QUESTIONS = [
    "Can you explain the difference between synchronous and asynchronous programming?",
    "What is your experience with version control systems like Git?",
    "How do you handle debugging and troubleshooting in your preferred programming language?",
    "Can you describe a challenging project you've worked on and how you overcame obstacles?",
    "What's your approach to writing clean, maintainable code?",
    "How do you stay updated with the latest technologies and best practices?",
    "Can you explain the concept of RESTful APIs and when you would use them?",
    "What's your experience with testing methodologies (unit testing, integration testing)?"
]

def validate_config():
    """Validate that all required configuration is set"""
    # For local LLMs, we don't need an API key
    # Just check if Ollama is running
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            return True
        else:
            raise ValueError(
                "Ollama is not running! Please start Ollama first.\n"
                "1. Install Ollama from: https://ollama.ai/\n"
                "2. Run: ollama serve\n"
                "3. Pull a model: ollama pull llama2"
            )
    except Exception as e:
        raise ValueError(
            "Cannot connect to Ollama! Please ensure Ollama is running.\n"
            "1. Install Ollama from: https://ollama.ai/\n"
            "2. Run: ollama serve\n"
            "3. Pull a model: ollama pull llama2\n"
            f"Error: {str(e)}"
        )

def get_config_info():
    """Get configuration information for display"""
    return {
        "openai_model": OPENAI_MODEL,
        "max_tokens": OPENAI_MAX_TOKENS,
        "temperature": OPENAI_TEMPERATURE,
        "streamlit_port": STREAMLIT_PORT,
        "streamlit_address": STREAMLIT_ADDRESS,
        "tech_keywords_count": len(TECH_KEYWORDS),
        "required_fields": REQUIRED_FIELDS,
        "fallback_questions_count": len(FALLBACK_QUESTIONS)
    } 
"""
Configuration file for TalentScout Hiring Assistant
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Local LLM Configuration (Ollama)
OPENAI_API_KEY = "local"  # Not needed for local LLMs
OPENAI_MODEL = "llama2"  # or "mistral", "codellama", "llama2:7b", etc.
OPENAI_MAX_TOKENS = 500
OPENAI_TEMPERATURE = 0.7
OPENAI_BASE_URL = "http://localhost:11434/v1"  # Ollama default endpoint

# Streamlit Configuration
STREAMLIT_PORT = int(os.getenv("STREAMLIT_SERVER_PORT", 8501))
STREAMLIT_ADDRESS = os.getenv("STREAMLIT_SERVER_ADDRESS", "localhost")

# Application Configuration
APP_TITLE = "TalentScout Hiring Assistant"
APP_ICON = "🤖"

# Tech Stack Keywords for Detection
TECH_KEYWORDS = [
    # Programming Languages
    'python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'swift', 'kotlin', 'scala',
    
    # Frontend Frameworks
    'react', 'angular', 'vue', 'svelte', 'next.js', 'nuxt.js',
    
    # Backend Frameworks
    'django', 'flask', 'spring', 'node.js', 'express', 'fastapi', 'laravel', 'rails',
    
    # Databases
    'mysql', 'postgresql', 'mongodb', 'redis', 'sqlite', 'oracle', 'sql server',
    
    # Cloud Platforms
    'aws', 'azure', 'gcp', 'heroku', 'digitalocean',
    
    # DevOps & Tools
    'docker', 'kubernetes', 'jenkins', 'git', 'github', 'gitlab', 'jira', 'confluence',
    
    # Methodologies
    'agile', 'scrum', 'kanban', 'waterfall',
    
    # Other Technologies
    'html', 'css', 'sass', 'less', 'typescript', 'webpack', 'babel'
]

# Conversation States
CONVERSATION_STATES = {
    'GREETING': 'greeting',
    'COLLECTING_INFO': 'collecting_info',
    'COLLECTING_TECH_STACK': 'collecting_tech_stack',
    'GENERATING_QUESTIONS': 'generating_questions',
    'TECHNICAL_ASSESSMENT': 'technical_assessment',
    'CONCLUSION': 'conclusion'
}

# Required Candidate Information Fields
REQUIRED_FIELDS = ['name', 'email', 'phone', 'experience', 'position', 'location']

# Conversation Ending Keywords
EXIT_KEYWORDS = ['goodbye', 'exit', 'quit', 'end', 'stop', 'bye', 'finish']

# Fallback Technical Questions
FALLBACK_QUESTIONS = [
    "Can you explain the difference between synchronous and asynchronous programming?",
    "What is your experience with version control systems like Git?",
    "How do you handle debugging and troubleshooting in your preferred programming language?",
    "Can you describe a challenging project you've worked on and how you overcame obstacles?",
    "What's your approach to writing clean, maintainable code?",
    "How do you stay updated with the latest technologies and best practices?",
    "Can you explain the concept of RESTful APIs and when you would use them?",
    "What's your experience with testing methodologies (unit testing, integration testing)?"
]

def validate_config():
    """Validate that all required configuration is set"""
    # For local LLMs, we don't need an API key
    # Just check if Ollama is running
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            return True
        else:
            raise ValueError(
                "Ollama is not running! Please start Ollama first.\n"
                "1. Install Ollama from: https://ollama.ai/\n"
                "2. Run: ollama serve\n"
                "3. Pull a model: ollama pull llama2"
            )
    except Exception as e:
        raise ValueError(
            "Cannot connect to Ollama! Please ensure Ollama is running.\n"
            "1. Install Ollama from: https://ollama.ai/\n"
            "2. Run: ollama serve\n"
            "3. Pull a model: ollama pull llama2\n"
            f"Error: {str(e)}"
        )

def get_config_info():
    """Get configuration information for display"""
    return {
        "openai_model": OPENAI_MODEL,
        "max_tokens": OPENAI_MAX_TOKENS,
        "temperature": OPENAI_TEMPERATURE,
        "streamlit_port": STREAMLIT_PORT,
        "streamlit_address": STREAMLIT_ADDRESS,
        "tech_keywords_count": len(TECH_KEYWORDS),
        "required_fields": REQUIRED_FIELDS,
        "fallback_questions_count": len(FALLBACK_QUESTIONS)
    } 
