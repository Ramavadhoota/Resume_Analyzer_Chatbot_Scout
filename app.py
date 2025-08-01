import streamlit as st
import openai
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Try to import pandas, but handle gracefully if not available
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    pd = None
from config import (
    OPENAI_API_KEY, OPENAI_MODEL, OPENAI_MAX_TOKENS, OPENAI_TEMPERATURE, OPENAI_BASE_URL,
    APP_TITLE, APP_ICON, CONVERSATION_STATES, REQUIRED_FIELDS, 
    EXIT_KEYWORDS, FALLBACK_QUESTIONS, validate_config, get_config_info
)
from utils import (
    extract_email, extract_phone, extract_experience_years, extract_name,
    extract_position, extract_location, extract_tech_stack, validate_candidate_info,
    format_session_data, export_to_json, export_to_csv, generate_conversation_summary,
    sanitize_input, get_tech_stack_categories
)

# Validate configuration
try:
    validate_config()
except ValueError as e:
    st.error(str(e))
    st.stop()

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-container {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    .user-message {
        background-color: #007bff;
        color: white;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        text-align: right;
    }
    .bot-message {
        background-color: #e9ecef;
        color: #333;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 5px 0;
        text-align: left;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

class HiringAssistant:
    def __init__(self):
        self.conversation_state = CONVERSATION_STATES['GREETING']
        self.candidate_info = {}
        self.tech_stack = []
        self.technical_questions = []
        self.current_question_index = 0
        
    def get_system_prompt(self):
        """Get the system prompt for the AI assistant"""
        return """You are TalentScout, an intelligent hiring assistant for a technology recruitment agency. Your role is to:

1. Greet candidates warmly and explain your purpose
2. Collect essential candidate information systematically
3. Gather their tech stack details
4. Generate relevant technical questions based on their tech stack
5. Conduct a technical assessment
6. End the conversation gracefully

Key Guidelines:
- Be professional, friendly, and encouraging
- Ask one question at a time
- Maintain context throughout the conversation
- If you encounter conversation-ending keywords (goodbye, exit, quit, end, stop), gracefully conclude
- Keep responses concise but informative
- Always stay in character as a hiring assistant

Current conversation state: {state}

Candidate information collected so far: {info}

Tech stack: {tech_stack}

Technical questions generated: {questions}

Current question index: {question_index}

Respond appropriately based on the current state and context."""

    def generate_response(self, user_input):
        """Generate AI response based on user input and current state"""
        try:
            # Sanitize user input
            user_input = sanitize_input(user_input)
            
            # Check for conversation ending keywords
            if any(keyword in user_input.lower() for keyword in EXIT_KEYWORDS):
                return self.end_conversation()
            
            # Prepare context for the AI
            context = {
                'state': self.conversation_state,
                'info': self.candidate_info,
                'tech_stack': self.tech_stack,
                'questions': self.technical_questions,
                'question_index': self.current_question_index
            }
            
            system_prompt = self.get_system_prompt().format(**context)
            
            client = openai.OpenAI(
                api_key="local",  # Not needed for local LLMs
                base_url=OPENAI_BASE_URL
            )
            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=OPENAI_MAX_TOKENS,
                temperature=OPENAI_TEMPERATURE
            )
            
            ai_response = response.choices[0].message.content
            
            # Update conversation state based on AI response
            self.update_conversation_state(user_input, ai_response)
            
            return ai_response
            
        except Exception as e:
            return f"I apologize, but I'm experiencing technical difficulties. Please try again. Error: {str(e)}"

    def update_conversation_state(self, user_input, ai_response):
        """Update conversation state based on user input and AI response"""
        # Extract information from user input based on current state
        if self.conversation_state == CONVERSATION_STATES['GREETING']:
            self.conversation_state = CONVERSATION_STATES['COLLECTING_INFO']
            
        elif self.conversation_state == CONVERSATION_STATES['COLLECTING_INFO']:
            # Try to extract candidate information
            self.extract_candidate_info(user_input)
            
            # Check if we have all required information
            if all(field in self.candidate_info for field in REQUIRED_FIELDS):
                self.conversation_state = CONVERSATION_STATES['COLLECTING_TECH_STACK']
                
        elif self.conversation_state == CONVERSATION_STATES['COLLECTING_TECH_STACK']:
            # Extract tech stack information
            self.extract_tech_stack(user_input)
            if self.tech_stack:
                self.conversation_state = CONVERSATION_STATES['GENERATING_QUESTIONS']
                self.generate_technical_questions()
                
        elif self.conversation_state == CONVERSATION_STATES['GENERATING_QUESTIONS']:
            self.conversation_state = CONVERSATION_STATES['TECHNICAL_ASSESSMENT']
            
        elif self.conversation_state == CONVERSATION_STATES['TECHNICAL_ASSESSMENT']:
            # Track answers to technical questions
            if self.current_question_index < len(self.technical_questions):
                self.current_question_index += 1
                
            if self.current_question_index >= len(self.technical_questions):
                self.conversation_state = CONVERSATION_STATES['CONCLUSION']

    def extract_candidate_info(self, user_input):
        """Extract candidate information from user input"""
        # Use utility functions for better extraction
        name = extract_name(user_input)
        if name:
            self.candidate_info['name'] = name
            
        email = extract_email(user_input)
        if email:
            self.candidate_info['email'] = email
            
        phone = extract_phone(user_input)
        if phone:
            self.candidate_info['phone'] = phone
            
        experience = extract_experience_years(user_input)
        if experience:
            self.candidate_info['experience'] = experience
            
        position = extract_position(user_input)
        if position:
            self.candidate_info['position'] = position
            
        location = extract_location(user_input)
        if location:
            self.candidate_info['location'] = location

    def extract_tech_stack(self, user_input):
        """Extract tech stack from user input"""
        found_tech = extract_tech_stack(user_input)
        for tech in found_tech:
            if tech not in self.tech_stack:
                self.tech_stack.append(tech)

    def generate_technical_questions(self):
        """Generate technical questions based on tech stack"""
        if not self.tech_stack:
            return
            
        try:
            prompt = f"""Generate 3-5 technical questions for a candidate with the following tech stack: {', '.join(self.tech_stack)}.
            
            For each technology, create relevant questions that assess:
            1. Basic understanding
            2. Practical experience
            3. Problem-solving skills
            
            Format the response as a JSON array of questions."""
            
            client = openai.OpenAI(
                api_key="local",  # Not needed for local LLMs
                base_url=OPENAI_BASE_URL
            )
            response = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "You are a technical interviewer. Generate relevant technical questions based on the provided tech stack."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            questions_text = response.choices[0].message.content
            # Try to parse as JSON, fallback to simple list
            try:
                self.technical_questions = json.loads(questions_text)
            except:
                # Fallback: split by lines and clean up
                self.technical_questions = [q.strip() for q in questions_text.split('\n') if q.strip()]
                
        except Exception as e:
            # Fallback questions
            self.technical_questions = FALLBACK_QUESTIONS

    def end_conversation(self):
        """End the conversation gracefully"""
        self.conversation_state = CONVERSATION_STATES['CONCLUSION']
        return """Thank you for your time and for sharing your information with TalentScout! 

I've collected your details and conducted a brief technical assessment. Our recruitment team will review your profile and get back to you within 2-3 business days.

Here's a summary of what we discussed:
- Your information has been recorded
- Your tech stack has been noted
- Technical assessment completed

If you have any questions or need to update your information, please don't hesitate to reach out to our team.

Good luck with your application! """

def main():
    # Header
    st.markdown('<h1 class="main-header"> TalentScout Hiring Assistant</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header(" About")
        st.markdown("""
        **TalentScout Hiring Assistant** is an AI-powered chatbot designed to help with initial candidate screening for technology positions.
        
        **Features:**
        -  Collect candidate information
        -  Assess technical skills
        -  Intelligent conversation flow
        -  Secure data handling
        
        **How to use:**
        1. Start a conversation
        2. Provide your information
        3. Answer technical questions
        4. Complete the assessment
        """)
        
        st.header("🔧 Technical Details")
        config_info = get_config_info()
        st.markdown(f"""
        - **Framework:** Streamlit
        - **AI Model:** {config_info['openai_model']}
        - **Language:** Python
        - **Data Handling:** Local storage (simulated)
        - **Tech Keywords:** {config_info['tech_keywords_count']} technologies supported
        """)
        
        # Environment setup info
        try:
            import requests
            response = requests.get("http://localhost:11434/api/tags", timeout=5)
            if response.status_code == 200:
                st.success(" Ollama is running and ready!")
            else:
                st.error(" Ollama is not responding properly!")
        except Exception as e:
            st.error(" Cannot connect to Ollama!")
            st.info("Please install and start Ollama:\n1. Install from: https://ollama.ai/\n2. Run: ollama serve\n3. Pull a model: ollama pull llama2")

    # Initialize session state
    if 'messages' not in st.session_state:
        st.session_state.messages = []
        
    if 'assistant' not in st.session_state:
        st.session_state.assistant = HiringAssistant()
        
    if 'conversation_started' not in st.session_state:
        st.session_state.conversation_started = False

    # Main chat interface
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Start conversation if not started
    if not st.session_state.conversation_started:
        welcome_message = """Hello!  I'm TalentScout, your AI hiring assistant. 

I'm here to help you with the initial screening process for technology positions. I'll be collecting some basic information about you and conducting a brief technical assessment.

Let's get started! Please tell me your full name."""
        
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})
        st.session_state.conversation_started = True
        
        with st.chat_message("assistant"):
            st.markdown(welcome_message)

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate assistant response
        with st.chat_message("assistant"):
            response = st.session_state.assistant.generate_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    st.markdown('</div>', unsafe_allow_html=True)
    
    # Display current state information
    with st.expander(" Current Session Information"):
        st.write("**Conversation State:**", st.session_state.assistant.conversation_state)
        st.write("**Candidate Info:**", st.session_state.assistant.candidate_info)
        st.write("**Tech Stack:**", st.session_state.assistant.tech_stack)
        st.write("**Questions Generated:**", len(st.session_state.assistant.technical_questions))
        
        # Export data option
        if st.button(" Export Session Data"):
            session_data = format_session_data(
                st.session_state.assistant.candidate_info,
                st.session_state.assistant.tech_stack,
                st.session_state.messages,
                st.session_state.assistant.technical_questions
            )
            
            # Display session summary
            st.subheader(" Session Summary")
            summary = generate_conversation_summary(st.session_state.messages)
            st.text(summary)
            
            # Display tech stack categories
            if st.session_state.assistant.tech_stack:
                st.subheader("🛠️ Tech Stack Categories")
                categories = get_tech_stack_categories(st.session_state.assistant.tech_stack)
                for category, techs in categories.items():
                    st.write(f"**{category}:** {', '.join(techs)}")
            
            # Convert to DataFrame for display
            if PANDAS_AVAILABLE:
                df = pd.DataFrame([session_data])
                st.dataframe(df)
            else:
                # Display as JSON if pandas is not available
                st.json(session_data)
            
            # Download options
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label=" Download JSON",
                    data=export_to_json(session_data),
                    file_name=f"talent_scout_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json"
                )
            with col2:
                st.download_button(
                    label=" Download CSV",
                    data=export_to_csv(session_data),
                    file_name=f"talent_scout_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )

if __name__ == "__main__":
    main() 