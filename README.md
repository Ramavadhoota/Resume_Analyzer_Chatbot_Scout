<<<<<<< HEAD
#  **TalentScout Hiring Assistant**

## **Project Overview**

**TalentScout Hiring Assistant** is an intelligent AI-powered chatbot designed to streamline the initial screening process for technology positions at recruitment agencies. Built with Streamlit and OpenAI's GPT-3.5-turbo, this application provides a seamless, conversational interface for collecting candidate information and conducting technical assessments.

### **Key Features**

- *Intelligent Conversation Flow*: Context-aware conversations that adapt to user responses
- *Automated Information Gathering*: Collects essential candidate details (name, email, experience, etc.)
- *Dynamic Technical Assessment*: Generates relevant technical questions based on declared tech stack
- *Modern UI/UX*: Clean, intuitive interface built with Streamlit
- *Secure Data Handling*: Local data storage with privacy compliance
- *Session Export*: Ability to export conversation data for review

### **Capabilities**

1. *Greeting & Introduction*: Warm welcome with clear purpose explanation
2. *Information Collection*: Systematic gathering of candidate details
3. *Tech Stack Assessment*: Identification and validation of technical skills
4. *Technical Question Generation*: AI-powered question creation based on tech stack
5. *Conversation Management*: Context maintenance and graceful conclusion
6. *Data Export*: Session data export for recruitment team review

## **Installation Instructions**

### **Prerequisites**

- Python 3.7 or higher
- OpenAI API key
- Git (for version control)

### **Step-by-Step Setup**

1. *Clone the Repository*
   ```bash
   git clone <repository-url>
   cd CHATbot
   ```

2. *Create Virtual Environment*
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. *Install Dependencies*
   ```bash
   pip install -r requirements.txt
   ```

4. *Set Up Environment Variables*
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. *Run the Application*
   ```bash
   streamlit run app.py
   ```

6. *Access the Application*
   
   Open your browser and navigate to: `http://localhost:8501`

## **Usage Guide**

### **For Candidates**

1. *Start the Conversation*
   - The chatbot will greet you and explain its purpose
   - Simply type your responses in the chat input

2. *Provide Your Information*
   - *Name*: "My name is [Your Full Name]"
   - *Email*: Include your email address in any message
   - *Phone*: Provide your contact number
   - *Experience*: "I have X years of experience"
   - *Position*: Mention your desired role
   - *Location*: Share your current location

3. *Declare Your Tech Stack*
   - List your programming languages, frameworks, and tools
   - Examples: "I work with Python, Django, React, and PostgreSQL"

4. *Answer Technical Questions*
   - Respond to the AI-generated questions based on your tech stack
   - Be honest and detailed in your responses

5. *Complete the Assessment*
   - The chatbot will conclude the session
   - You'll receive confirmation of completion

### **For Recruiters**

1. *Monitor Sessions*
   - Use the "Current Session Information" expander to view real-time data
   - Track conversation state and collected information

2. *Export Data*
   - Click "Export Session Data" to download conversation details
   - Data is exported in JSON format with timestamp

3. *Review Candidates*
   - Analyze exported data for candidate evaluation
   - Use technical responses to assess skill levels

## **Technical Details**

### **Architecture**

```
TalentScout Hiring Assistant
├── Frontend (Streamlit)
│   ├── Chat Interface
│   ├── Sidebar Information
│   └── Data Export
├── Backend (Python)
│   ├── HiringAssistant Class
│   ├── OpenAI Integration
│   └── State Management
└── Data Layer
    ├── Session Storage
    └── Export Functionality
```

### **Libraries & Technologies**

- *Streamlit (1.28.1)*: Web application framework
- *OpenAI (1.3.7)*: GPT-3.5-turbo integration
- *Python-dotenv (1.0.0)*: Environment variable management
- *Pandas (2.1.3)*: Data manipulation and export
- *NumPy (1.24.3)*: Numerical operations

### **AI Model Configuration**

- *Model*: GPT-3.5-turbo
- *Max Tokens*: 500 per response
- *Temperature*: 0.7 (balanced creativity and consistency)
- *Context Management*: Conversation state tracking

### **Prompt Engineering**

The application uses carefully crafted prompts to ensure:

1. *Information Gathering*: Structured prompts to extract candidate details
2. *Tech Stack Analysis*: Pattern matching for technology identification
3. *Question Generation*: Context-aware technical question creation
4. *Conversation Flow*: Natural progression through assessment stages

#### **Key Prompt Design Principles**

- *Context Awareness*: Each prompt includes current conversation state
- *Role Consistency*: Maintains hiring assistant persona throughout
- *Error Handling*: Graceful fallbacks for unexpected inputs
- *Privacy Compliance*: No sensitive data storage in prompts

### **Data Handling & Privacy**

- *Local Storage*: All data stored in session memory only
- *No Persistence*: Data is not saved to disk by default
- *Export Control*: Users can choose to export their session data
- *GDPR Compliance*: Minimal data collection, user-controlled export

## **Challenges & Solutions**

### *Challenge 1: Context Management*
*Problem*: Maintaining conversation context across multiple interactions
*Solution*: Implemented state machine with conversation states and context tracking

### *Challenge 2: Information Extraction*
*Problem*: Accurately extracting structured data from natural language
*Solution*: Combined regex patterns with AI-powered extraction for robust data capture

### *Challenge 3: Technical Question Generation*
*Problem*: Creating relevant questions for diverse tech stacks
*Solution*: Dynamic prompt generation based on identified technologies with fallback questions

### *Challenge 4: User Experience*
*Problem*: Creating intuitive interface for non-technical users
*Solution*: Streamlit's chat interface with clear visual feedback and progress indicators

### *Challenge 5: Error Handling*
*Problem*: Managing API failures and unexpected inputs
*Solution*: Comprehensive try-catch blocks with user-friendly error messages

## **Optional Enhancements (Bonus Features)**

### **Implemented Enhancements**

1. *Advanced UI/UX*
   - Custom CSS styling for professional appearance
   - Responsive design with sidebar information
   - Real-time session information display

2. *Data Export Functionality*
   - JSON export with timestamp
   - Session data visualization
   - Downloadable conversation logs

3. *Session Monitoring*
   - Real-time conversation state tracking
   - Candidate information display
   - Tech stack validation

### **Future Enhancements**

1. *Sentiment Analysis*: Analyze candidate emotions during conversation
2. *Multilingual Support*: Support for multiple languages
3. *Cloud Deployment*: AWS/GCP deployment with live demo
4. *Database Integration*: Persistent storage for candidate data
5. *Advanced Analytics*: Conversation analytics and insights

## **Performance Optimization**

- *Efficient API Calls*: Minimal token usage with focused prompts
- *Session Management*: Optimized state handling for smooth interactions
- *Memory Management*: Clean session data handling
- *Response Time*: Quick response generation with appropriate timeouts

## **Security Considerations**

- *API Key Protection*: Environment variable usage for sensitive data
- *Data Privacy*: No persistent storage of sensitive information
- *Input Validation*: Sanitization of user inputs
- *Session Isolation*: Separate session data for each user

## **Troubleshooting**

### **Common Issues**

1. *OpenAI API Key Error*
   - Ensure `.env` file exists with correct API key
   - Verify API key has sufficient credits

2. *Dependencies Installation*
   - Use virtual environment to avoid conflicts
   - Update pip: `pip install --upgrade pip`

3. *Streamlit Port Issues*
   - Change port: `streamlit run app.py --server.port 8502`
   - Check firewall settings

4. *Memory Issues*
   - Clear browser cache
   - Restart Streamlit application

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## **License**

This project is created for educational and demonstration purposes as part of an AI/ML Intern assignment.

## **Contact**

For questions or support regarding this project, please refer to the assignment guidelines or contact the development team.

---
=======
#  **TalentScout Hiring Assistant**

## **Project Overview**

**TalentScout Hiring Assistant** is an intelligent AI-powered chatbot designed to streamline the initial screening process for technology positions at recruitment agencies. Built with Streamlit and OpenAI's GPT-3.5-turbo, this application provides a seamless, conversational interface for collecting candidate information and conducting technical assessments.

### **Key Features**

- *Intelligent Conversation Flow*: Context-aware conversations that adapt to user responses
- *Automated Information Gathering*: Collects essential candidate details (name, email, experience, etc.)
- *Dynamic Technical Assessment*: Generates relevant technical questions based on declared tech stack
- *Modern UI/UX*: Clean, intuitive interface built with Streamlit
- *Secure Data Handling*: Local data storage with privacy compliance
- *Session Export*: Ability to export conversation data for review

### **Capabilities**

1. *Greeting & Introduction*: Warm welcome with clear purpose explanation
2. *Information Collection*: Systematic gathering of candidate details
3. *Tech Stack Assessment*: Identification and validation of technical skills
4. *Technical Question Generation*: AI-powered question creation based on tech stack
5. *Conversation Management*: Context maintenance and graceful conclusion
6. *Data Export*: Session data export for recruitment team review

## **Installation Instructions**

### **Prerequisites**

- Python 3.7 or higher
- OpenAI API key
- Git (for version control)

### **Step-by-Step Setup**

1. *Clone the Repository*
   ```bash
   git clone <repository-url>
   cd CHATbot
   ```

2. *Create Virtual Environment*
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. *Install Dependencies*
   ```bash
   pip install -r requirements.txt
   ```

4. *Set Up Environment Variables*
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. *Run the Application*
   ```bash
   streamlit run app.py
   ```

6. *Access the Application*
   
   Open your browser and navigate to: `http://localhost:8501`

## **Usage Guide**

### **For Candidates**

1. *Start the Conversation*
   - The chatbot will greet you and explain its purpose
   - Simply type your responses in the chat input

2. *Provide Your Information*
   - *Name*: "My name is [Your Full Name]"
   - *Email*: Include your email address in any message
   - *Phone*: Provide your contact number
   - *Experience*: "I have X years of experience"
   - *Position*: Mention your desired role
   - *Location*: Share your current location

3. *Declare Your Tech Stack*
   - List your programming languages, frameworks, and tools
   - Examples: "I work with Python, Django, React, and PostgreSQL"

4. *Answer Technical Questions*
   - Respond to the AI-generated questions based on your tech stack
   - Be honest and detailed in your responses

5. *Complete the Assessment*
   - The chatbot will conclude the session
   - You'll receive confirmation of completion

### **For Recruiters**

1. *Monitor Sessions*
   - Use the "Current Session Information" expander to view real-time data
   - Track conversation state and collected information

2. *Export Data*
   - Click "Export Session Data" to download conversation details
   - Data is exported in JSON format with timestamp

3. *Review Candidates*
   - Analyze exported data for candidate evaluation
   - Use technical responses to assess skill levels

## **Technical Details**

### **Architecture**

```
TalentScout Hiring Assistant
├── Frontend (Streamlit)
│   ├── Chat Interface
│   ├── Sidebar Information
│   └── Data Export
├── Backend (Python)
│   ├── HiringAssistant Class
│   ├── OpenAI Integration
│   └── State Management
└── Data Layer
    ├── Session Storage
    └── Export Functionality
```

### **Libraries & Technologies**

- *Streamlit (1.28.1)*: Web application framework
- *OpenAI (1.3.7)*: GPT-3.5-turbo integration
- *Python-dotenv (1.0.0)*: Environment variable management
- *Pandas (2.1.3)*: Data manipulation and export
- *NumPy (1.24.3)*: Numerical operations

### **AI Model Configuration**

- *Model*: GPT-3.5-turbo
- *Max Tokens*: 500 per response
- *Temperature*: 0.7 (balanced creativity and consistency)
- *Context Management*: Conversation state tracking

### **Prompt Engineering**

The application uses carefully crafted prompts to ensure:

1. *Information Gathering*: Structured prompts to extract candidate details
2. *Tech Stack Analysis*: Pattern matching for technology identification
3. *Question Generation*: Context-aware technical question creation
4. *Conversation Flow*: Natural progression through assessment stages

#### **Key Prompt Design Principles**

- *Context Awareness*: Each prompt includes current conversation state
- *Role Consistency*: Maintains hiring assistant persona throughout
- *Error Handling*: Graceful fallbacks for unexpected inputs
- *Privacy Compliance*: No sensitive data storage in prompts

### **Data Handling & Privacy**

- *Local Storage*: All data stored in session memory only
- *No Persistence*: Data is not saved to disk by default
- *Export Control*: Users can choose to export their session data
- *GDPR Compliance*: Minimal data collection, user-controlled export

## **Challenges & Solutions**

### *Challenge 1: Context Management*
*Problem*: Maintaining conversation context across multiple interactions
*Solution*: Implemented state machine with conversation states and context tracking

### *Challenge 2: Information Extraction*
*Problem*: Accurately extracting structured data from natural language
*Solution*: Combined regex patterns with AI-powered extraction for robust data capture

### *Challenge 3: Technical Question Generation*
*Problem*: Creating relevant questions for diverse tech stacks
*Solution*: Dynamic prompt generation based on identified technologies with fallback questions

### *Challenge 4: User Experience*
*Problem*: Creating intuitive interface for non-technical users
*Solution*: Streamlit's chat interface with clear visual feedback and progress indicators

### *Challenge 5: Error Handling*
*Problem*: Managing API failures and unexpected inputs
*Solution*: Comprehensive try-catch blocks with user-friendly error messages

## **Optional Enhancements (Bonus Features)**

### **Implemented Enhancements**

1. *Advanced UI/UX*
   - Custom CSS styling for professional appearance
   - Responsive design with sidebar information
   - Real-time session information display

2. *Data Export Functionality*
   - JSON export with timestamp
   - Session data visualization
   - Downloadable conversation logs

3. *Session Monitoring*
   - Real-time conversation state tracking
   - Candidate information display
   - Tech stack validation

### **Future Enhancements**

1. *Sentiment Analysis*: Analyze candidate emotions during conversation
2. *Multilingual Support*: Support for multiple languages
3. *Cloud Deployment*: AWS/GCP deployment with live demo
4. *Database Integration*: Persistent storage for candidate data
5. *Advanced Analytics*: Conversation analytics and insights

## **Performance Optimization**

- *Efficient API Calls*: Minimal token usage with focused prompts
- *Session Management*: Optimized state handling for smooth interactions
- *Memory Management*: Clean session data handling
- *Response Time*: Quick response generation with appropriate timeouts

## **Security Considerations**

- *API Key Protection*: Environment variable usage for sensitive data
- *Data Privacy*: No persistent storage of sensitive information
- *Input Validation*: Sanitization of user inputs
- *Session Isolation*: Separate session data for each user

## **Troubleshooting**

### **Common Issues**

1. *OpenAI API Key Error*
   - Ensure `.env` file exists with correct API key
   - Verify API key has sufficient credits

2. *Dependencies Installation*
   - Use virtual environment to avoid conflicts
   - Update pip: `pip install --upgrade pip`

3. *Streamlit Port Issues*
   - Change port: `streamlit run app.py --server.port 8502`
   - Check firewall settings

4. *Memory Issues*
   - Clear browser cache
   - Restart Streamlit application

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## **License**

This project is created for educational and demonstration purposes as part of an AI/ML Intern assignment.

## **Contact**

For questions or support regarding this project, please refer to the assignment guidelines or contact the development team.

---
>>>>>>> a431973a36876c8ecd0f0f8a507c1f34b563384c
