# NLP-Powered College Information Chatbot  

This project leverages Natural Language Processing (NLP) techniques to build an intelligent chatbot that provides accurate and instant answers to college-related queries. Built using Flask and SpaCy, the chatbot uses intent detection, keyword analysis, and a knowledge base to ensure relevant responses.  

---

## 🌐 **Overview**  
The chatbot is designed to streamline communication for students, applicants, and stakeholders by answering frequently asked questions about college admissions, courses, facilities, events, and more.  
- Powered by SpaCy for language understanding.  
- Flask-based backend for seamless interaction.  
- A predefined knowledge base for accurate responses.  

---

## 🚀 **Key Features**  
- **Intent Detection**: Identifies user intent using NLP-based keyword matching.  
- **Knowledge Base Lookup**: Matches keywords in user queries with a predefined FAQ knowledge base.  
- **Error Handling**: Provides meaningful fallback responses when no exact match is found.  
- **Web Interface**: Frontend served via Flask, ensuring a user-friendly interaction point.  

---

## 🛠️ **Setup and Usage**  

### **Requirements**  
- Python 3.7+  
- Flask  
- SpaCy (`en_core_web_sm` model)  

### **Installation Steps**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/srivardhan8919/NLP-Powered-Chatbot-for-College-Information.git  
   cd nlp-college-chatbot  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   python -m spacy download en_core_web_sm  
   ```  

3. Start the application:  
   ```bash  
   python app.py  
   ```  

4. Access the chatbot in your browser at `http://localhost:5000`.  

---

📁 Project File Structure

nlp-college-chatbot
│
├── app.py
├── requirements.txt
├── static/
├── templates/
│   └── index.html
├── knowledge_base.py

---

## 📊 **How It Works**  
1. **Intent Detection**:  
   - The chatbot detects user intent by analyzing keywords in the input.  
   - Keywords are mapped to intents stored in the `intent_keywords` dictionary.  

2. **Knowledge Base Lookup**:  
   - User input is processed to extract keywords.  
   - These keywords are matched against a predefined FAQ knowledge base to find answers.  

3. **Fallback Responses**:  
   - If no match is found, the chatbot provides a polite, generic response, prompting the user to rephrase their query.  

---

## 🧑‍🤝‍🧑 **Contributing**  
Contributions are welcome!  
- Fork the repository.  
- Create a feature branch.  
- Submit a pull request with detailed changes.  

---

## 📄 **License**  
This project is licensed under the [MIT License](LICENSE).  

---

## 🔗 **Contact**  
For any queries or suggestions:  
GitHub: https://github.com/srivardhan8919
LinkedIn: https://linkedin.com/in/sri-vardhan-nutenki-207b55249
G-mail: srivardhannani8919@gmail.com
