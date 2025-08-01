
"""
Utility functions for TalentScout Hiring Assistant
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any, Optional

# Try to import pandas, but handle gracefully if not available
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    pd = None

from config import TECH_KEYWORDS, REQUIRED_FIELDS, FALLBACK_QUESTIONS

def extract_email(text: str) -> Optional[str]:
    """Extract email address from text"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else None

def extract_phone(text: str) -> Optional[str]:
    """Extract phone number from text"""
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    phones = re.findall(phone_pattern, text)
    return phones[0] if phones else None

def extract_experience_years(text: str) -> Optional[str]:
    """Extract years of experience from text"""
    exp_pattern = r'(\d+)\s*(?:years?|yrs?)\s*experience'
    exp_match = re.search(exp_pattern, text.lower())
    return exp_match.group(1) if exp_match else None

def extract_name(text: str) -> Optional[str]:
    """Extract name from text"""
    name_patterns = [
        r'my name is\s+([A-Za-z\s]+)',
        r'i am\s+([A-Za-z\s]+)',
        r'name[:\s]+([A-Za-z\s]+)',
        r'call me\s+([A-Za-z\s]+)'
    ]
    
    text_lower = text.lower()
    for pattern in name_patterns:
        match = re.search(pattern, text_lower)
        if match:
            name = match.group(1).strip()
            # Clean up the name
            name = re.sub(r'\s+', ' ', name).title()
            return name
    return None

def extract_position(text: str) -> Optional[str]:
    """Extract desired position from text"""
    positions = [
        'developer', 'engineer', 'architect', 'manager', 'lead', 'senior', 'junior',
        'frontend', 'backend', 'fullstack', 'devops', 'data scientist', 'analyst',
        'consultant', 'specialist', 'coordinator'
    ]
    
    text_lower = text.lower()
    for position in positions:
        if position in text_lower:
            return position
    return None

def extract_location(text: str) -> Optional[str]:
    """Extract location from text"""
    location_keywords = ['in', 'at', 'live in', 'based in', 'from', 'located in']
    text_lower = text.lower()
    
    for keyword in location_keywords:
        if keyword in text_lower:
            loc_start = text_lower.find(keyword) + len(keyword)
            # Find the end of the location (period, comma, or end of sentence)
            loc_end = len(text_lower)
            for end_char in ['.', ',', ' and', ' but', ' with']:
                end_pos = text_lower.find(end_char, loc_start)
                if end_pos != -1 and end_pos < loc_end:
                    loc_end = end_pos
            
            location = text[loc_start:loc_end].strip()
            if location and len(location) > 2:
                return location
    return None

def extract_tech_stack(text: str) -> List[str]:
    """Extract tech stack from text"""
    found_tech = []
    text_lower = text.lower()
    
    for tech in TECH_KEYWORDS:
        if tech in text_lower:
            found_tech.append(tech)
    
    return found_tech

def validate_candidate_info(info: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and clean candidate information"""
    validation_results = {
        'is_complete': True,
        'missing_fields': [],
        'warnings': []
    }
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in info or not info[field]:
            validation_results['missing_fields'].append(field)
            validation_results['is_complete'] = False
    
    # Validate email format
    if 'email' in info and info['email']:
        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
        if not re.match(email_pattern, info['email']):
            validation_results['warnings'].append('Invalid email format')
    
    # Validate phone format
    if 'phone' in info and info['phone']:
        phone_pattern = r'^\d{3}[-.]?\d{3}[-.]?\d{4}$'
        if not re.match(phone_pattern, info['phone']):
            validation_results['warnings'].append('Invalid phone format')
    
    # Validate experience years
    if 'experience' in info and info['experience']:
        try:
            exp_years = int(info['experience'])
            if exp_years < 0 or exp_years > 50:
                validation_results['warnings'].append('Experience years seem unrealistic')
        except ValueError:
            validation_results['warnings'].append('Experience should be a number')
    
    return validation_results

def format_session_data(candidate_info: Dict[str, Any], tech_stack: List[str], 
                       messages: List[Dict[str, str]], questions: List[str]) -> Dict[str, Any]:
    """Format session data for export"""
    return {
        "timestamp": datetime.now().isoformat(),
        "session_id": f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "candidate_info": candidate_info,
        "tech_stack": tech_stack,
        "technical_questions": questions,
        "conversation_messages": messages,
        "conversation_summary": {
            "total_messages": len(messages),
            "user_messages": len([m for m in messages if m["role"] == "user"]),
            "assistant_messages": len([m for m in messages if m["role"] == "assistant"]),
            "tech_stack_count": len(tech_stack),
            "questions_count": len(questions)
        }
    }

def export_to_json(data: Dict[str, Any], filename: str = None) -> str:
    """Export data to JSON format"""
    if not filename:
        filename = f"talent_scout_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    json_data = json.dumps(data, indent=2, ensure_ascii=False)
    return json_data

def export_to_csv(data: Dict[str, Any]) -> str:
    """Export data to CSV format"""
    if not PANDAS_AVAILABLE:
        # Fallback to manual CSV generation if pandas is not available
        flat_data = {
            "timestamp": data.get("timestamp", ""),
            "session_id": data.get("session_id", ""),
            "name": data.get("candidate_info", {}).get("name", ""),
            "email": data.get("candidate_info", {}).get("email", ""),
            "phone": data.get("candidate_info", {}).get("phone", ""),
            "experience": data.get("candidate_info", {}).get("experience", ""),
            "position": data.get("candidate_info", {}).get("position", ""),
            "location": data.get("candidate_info", {}).get("location", ""),
            "tech_stack": ", ".join(data.get("tech_stack", [])),
            "total_messages": data.get("conversation_summary", {}).get("total_messages", 0),
            "questions_count": data.get("conversation_summary", {}).get("questions_count", 0)
        }
        
        # Create CSV manually
        headers = list(flat_data.keys())
        values = list(flat_data.values())
        csv_content = ",".join(f'"{str(v)}"' for v in values)
        return ",".join(headers) + "\n" + csv_content
    
    # Use pandas if available
    flat_data = {
        "timestamp": data.get("timestamp", ""),
        "session_id": data.get("session_id", ""),
        "name": data.get("candidate_info", {}).get("name", ""),
        "email": data.get("candidate_info", {}).get("email", ""),
        "phone": data.get("candidate_info", {}).get("phone", ""),
        "experience": data.get("candidate_info", {}).get("experience", ""),
        "position": data.get("candidate_info", {}).get("position", ""),
        "location": data.get("candidate_info", {}).get("location", ""),
        "tech_stack": ", ".join(data.get("tech_stack", [])),
        "total_messages": data.get("conversation_summary", {}).get("total_messages", 0),
        "questions_count": data.get("conversation_summary", {}).get("questions_count", 0)
    }
    
    df = pd.DataFrame([flat_data])
    return df.to_csv(index=False)

def generate_conversation_summary(messages: List[Dict[str, str]]) -> str:
    """Generate a summary of the conversation"""
    if not messages:
        return "No conversation data available."
    
    user_messages = [m["content"] for m in messages if m["role"] == "user"]
    assistant_messages = [m["content"] for m in messages if m["role"] == "assistant"]
    
    summary = f"""
Conversation Summary:
- Total Messages: {len(messages)}
- User Messages: {len(user_messages)}
- Assistant Messages: {len(assistant_messages)}
- Conversation Duration: {len(messages) * 2} minutes (estimated)

Key Topics Discussed:
"""
    
    # Extract key topics from user messages
    topics = []
    for msg in user_messages:
        if any(keyword in msg.lower() for keyword in ['experience', 'years', 'work']):
            topics.append("Work Experience")
        if any(keyword in msg.lower() for keyword in ['python', 'javascript', 'java', 'react', 'django']):
            topics.append("Technical Skills")
        if any(keyword in msg.lower() for keyword in ['project', 'challenge', 'problem']):
            topics.append("Project Experience")
    
    unique_topics = list(set(topics))
    for topic in unique_topics:
        summary += f"- {topic}\n"
    
    return summary

def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent injection attacks"""
    # Remove potentially dangerous characters
    sanitized = re.sub(r'[<>"\']', '', text)
    # Limit length
    if len(sanitized) > 1000:
        sanitized = sanitized[:1000]
    return sanitized.strip()

def calculate_response_time(start_time: datetime, end_time: datetime) -> float:
    """Calculate response time in seconds"""
    return (end_time - start_time).total_seconds()

def get_tech_stack_categories(tech_stack: List[str]) -> Dict[str, List[str]]:
    """Categorize tech stack by type"""
    categories = {
        "Programming Languages": [],
        "Frameworks": [],
        "Databases": [],
        "Cloud Platforms": [],
        "DevOps Tools": [],
        "Other": []
    }
    
    for tech in tech_stack:
        if tech in ['python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby', 'go', 'rust']:
            categories["Programming Languages"].append(tech)
        elif tech in ['react', 'angular', 'vue', 'django', 'flask', 'spring', 'express']:
            categories["Frameworks"].append(tech)
        elif tech in ['mysql', 'postgresql', 'mongodb', 'redis']:
            categories["Databases"].append(tech)
        elif tech in ['aws', 'azure', 'gcp']:
            categories["Cloud Platforms"].append(tech)
        elif tech in ['docker', 'kubernetes', 'jenkins', 'git']:
            categories["DevOps Tools"].append(tech)
        else:
            categories["Other"].append(tech)
    
    # Remove empty categories
"""
Utility functions for TalentScout Hiring Assistant
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any, Optional

# Try to import pandas, but handle gracefully if not available
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    pd = None

from config import TECH_KEYWORDS, REQUIRED_FIELDS, FALLBACK_QUESTIONS

def extract_email(text: str) -> Optional[str]:
    """Extract email address from text"""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails[0] if emails else None

def extract_phone(text: str) -> Optional[str]:
    """Extract phone number from text"""
    phone_pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    phones = re.findall(phone_pattern, text)
    return phones[0] if phones else None

def extract_experience_years(text: str) -> Optional[str]:
    """Extract years of experience from text"""
    exp_pattern = r'(\d+)\s*(?:years?|yrs?)\s*experience'
    exp_match = re.search(exp_pattern, text.lower())
    return exp_match.group(1) if exp_match else None

def extract_name(text: str) -> Optional[str]:
    """Extract name from text"""
    name_patterns = [
        r'my name is\s+([A-Za-z\s]+)',
        r'i am\s+([A-Za-z\s]+)',
        r'name[:\s]+([A-Za-z\s]+)',
        r'call me\s+([A-Za-z\s]+)'
    ]
    
    text_lower = text.lower()
    for pattern in name_patterns:
        match = re.search(pattern, text_lower)
        if match:
            name = match.group(1).strip()
            # Clean up the name
            name = re.sub(r'\s+', ' ', name).title()
            return name
    return None

def extract_position(text: str) -> Optional[str]:
    """Extract desired position from text"""
    positions = [
        'developer', 'engineer', 'architect', 'manager', 'lead', 'senior', 'junior',
        'frontend', 'backend', 'fullstack', 'devops', 'data scientist', 'analyst',
        'consultant', 'specialist', 'coordinator'
    ]
    
    text_lower = text.lower()
    for position in positions:
        if position in text_lower:
            return position
    return None

def extract_location(text: str) -> Optional[str]:
    """Extract location from text"""
    location_keywords = ['in', 'at', 'live in', 'based in', 'from', 'located in']
    text_lower = text.lower()
    
    for keyword in location_keywords:
        if keyword in text_lower:
            loc_start = text_lower.find(keyword) + len(keyword)
            # Find the end of the location (period, comma, or end of sentence)
            loc_end = len(text_lower)
            for end_char in ['.', ',', ' and', ' but', ' with']:
                end_pos = text_lower.find(end_char, loc_start)
                if end_pos != -1 and end_pos < loc_end:
                    loc_end = end_pos
            
            location = text[loc_start:loc_end].strip()
            if location and len(location) > 2:
                return location
    return None

def extract_tech_stack(text: str) -> List[str]:
    """Extract tech stack from text"""
    found_tech = []
    text_lower = text.lower()
    
    for tech in TECH_KEYWORDS:
        if tech in text_lower:
            found_tech.append(tech)
    
    return found_tech

def validate_candidate_info(info: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and clean candidate information"""
    validation_results = {
        'is_complete': True,
        'missing_fields': [],
        'warnings': []
    }
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in info or not info[field]:
            validation_results['missing_fields'].append(field)
            validation_results['is_complete'] = False
    
    # Validate email format
    if 'email' in info and info['email']:
        email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
        if not re.match(email_pattern, info['email']):
            validation_results['warnings'].append('Invalid email format')
    
    # Validate phone format
    if 'phone' in info and info['phone']:
        phone_pattern = r'^\d{3}[-.]?\d{3}[-.]?\d{4}$'
        if not re.match(phone_pattern, info['phone']):
            validation_results['warnings'].append('Invalid phone format')
    
    # Validate experience years
    if 'experience' in info and info['experience']:
        try:
            exp_years = int(info['experience'])
            if exp_years < 0 or exp_years > 50:
                validation_results['warnings'].append('Experience years seem unrealistic')
        except ValueError:
            validation_results['warnings'].append('Experience should be a number')
    
    return validation_results

def format_session_data(candidate_info: Dict[str, Any], tech_stack: List[str], 
                       messages: List[Dict[str, str]], questions: List[str]) -> Dict[str, Any]:
    """Format session data for export"""
    return {
        "timestamp": datetime.now().isoformat(),
        "session_id": f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
        "candidate_info": candidate_info,
        "tech_stack": tech_stack,
        "technical_questions": questions,
        "conversation_messages": messages,
        "conversation_summary": {
            "total_messages": len(messages),
            "user_messages": len([m for m in messages if m["role"] == "user"]),
            "assistant_messages": len([m for m in messages if m["role"] == "assistant"]),
            "tech_stack_count": len(tech_stack),
            "questions_count": len(questions)
        }
    }

def export_to_json(data: Dict[str, Any], filename: str = None) -> str:
    """Export data to JSON format"""
    if not filename:
        filename = f"talent_scout_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    json_data = json.dumps(data, indent=2, ensure_ascii=False)
    return json_data

def export_to_csv(data: Dict[str, Any]) -> str:
    """Export data to CSV format"""
    if not PANDAS_AVAILABLE:
        # Fallback to manual CSV generation if pandas is not available
        flat_data = {
            "timestamp": data.get("timestamp", ""),
            "session_id": data.get("session_id", ""),
            "name": data.get("candidate_info", {}).get("name", ""),
            "email": data.get("candidate_info", {}).get("email", ""),
            "phone": data.get("candidate_info", {}).get("phone", ""),
            "experience": data.get("candidate_info", {}).get("experience", ""),
            "position": data.get("candidate_info", {}).get("position", ""),
            "location": data.get("candidate_info", {}).get("location", ""),
            "tech_stack": ", ".join(data.get("tech_stack", [])),
            "total_messages": data.get("conversation_summary", {}).get("total_messages", 0),
            "questions_count": data.get("conversation_summary", {}).get("questions_count", 0)
        }
        
        # Create CSV manually
        headers = list(flat_data.keys())
        values = list(flat_data.values())
        csv_content = ",".join(f'"{str(v)}"' for v in values)
        return ",".join(headers) + "\n" + csv_content
    
    # Use pandas if available
    flat_data = {
        "timestamp": data.get("timestamp", ""),
        "session_id": data.get("session_id", ""),
        "name": data.get("candidate_info", {}).get("name", ""),
        "email": data.get("candidate_info", {}).get("email", ""),
        "phone": data.get("candidate_info", {}).get("phone", ""),
        "experience": data.get("candidate_info", {}).get("experience", ""),
        "position": data.get("candidate_info", {}).get("position", ""),
        "location": data.get("candidate_info", {}).get("location", ""),
        "tech_stack": ", ".join(data.get("tech_stack", [])),
        "total_messages": data.get("conversation_summary", {}).get("total_messages", 0),
        "questions_count": data.get("conversation_summary", {}).get("questions_count", 0)
    }
    
    df = pd.DataFrame([flat_data])
    return df.to_csv(index=False)

def generate_conversation_summary(messages: List[Dict[str, str]]) -> str:
    """Generate a summary of the conversation"""
    if not messages:
        return "No conversation data available."
    
    user_messages = [m["content"] for m in messages if m["role"] == "user"]
    assistant_messages = [m["content"] for m in messages if m["role"] == "assistant"]
    
    summary = f"""
Conversation Summary:
- Total Messages: {len(messages)}
- User Messages: {len(user_messages)}
- Assistant Messages: {len(assistant_messages)}
- Conversation Duration: {len(messages) * 2} minutes (estimated)

Key Topics Discussed:
"""
    
    # Extract key topics from user messages
    topics = []
    for msg in user_messages:
        if any(keyword in msg.lower() for keyword in ['experience', 'years', 'work']):
            topics.append("Work Experience")
        if any(keyword in msg.lower() for keyword in ['python', 'javascript', 'java', 'react', 'django']):
            topics.append("Technical Skills")
        if any(keyword in msg.lower() for keyword in ['project', 'challenge', 'problem']):
            topics.append("Project Experience")
    
    unique_topics = list(set(topics))
    for topic in unique_topics:
        summary += f"- {topic}\n"
    
    return summary

def sanitize_input(text: str) -> str:
    """Sanitize user input to prevent injection attacks"""
    # Remove potentially dangerous characters
    sanitized = re.sub(r'[<>"\']', '', text)
    # Limit length
    if len(sanitized) > 1000:
        sanitized = sanitized[:1000]
    return sanitized.strip()

def calculate_response_time(start_time: datetime, end_time: datetime) -> float:
    """Calculate response time in seconds"""
    return (end_time - start_time).total_seconds()

def get_tech_stack_categories(tech_stack: List[str]) -> Dict[str, List[str]]:
    """Categorize tech stack by type"""
    categories = {
        "Programming Languages": [],
        "Frameworks": [],
        "Databases": [],
        "Cloud Platforms": [],
        "DevOps Tools": [],
        "Other": []
    }
    
    for tech in tech_stack:
        if tech in ['python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby', 'go', 'rust']:
            categories["Programming Languages"].append(tech)
        elif tech in ['react', 'angular', 'vue', 'django', 'flask', 'spring', 'express']:
            categories["Frameworks"].append(tech)
        elif tech in ['mysql', 'postgresql', 'mongodb', 'redis']:
            categories["Databases"].append(tech)
        elif tech in ['aws', 'azure', 'gcp']:
            categories["Cloud Platforms"].append(tech)
        elif tech in ['docker', 'kubernetes', 'jenkins', 'git']:
            categories["DevOps Tools"].append(tech)
        else:
            categories["Other"].append(tech)
    
    # Remove empty categories
    return {k: v for k, v in categories.items() if v} 