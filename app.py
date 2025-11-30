import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Configure Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)

# Page config
st.set_page_config(
    page_title="AI Knowledge Base Agent",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'knowledge_base' not in st.session_state:
    st.session_state.knowledge_base = ""

def load_documents_from_folder():
    """Load all .txt documents from the documents folder"""
    documents_text = ""
    doc_folder = "documents"
    
    if not os.path.exists(doc_folder):
        return None, "Documents folder not found"
    
    txt_files = [f for f in os.listdir(doc_folder) if f.endswith('.txt')]
    
    if len(txt_files) == 0:
        return None, "No .txt files found in documents folder"
    
    for filename in txt_files:
        filepath = os.path.join(doc_folder, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                documents_text += f"\n\n=== Document: {filename} ===\n{content}"
        except Exception as e:
            st.warning(f"Could not read {filename}: {e}")
    
    return documents_text, f"Loaded {len(txt_files)} documents"

def get_ai_response(question, knowledge_base):
    """Get response from Groq AI"""
    try:
        prompt = f"""You are a helpful AI assistant for a company's knowledge base.
        
Below is the company's knowledge base containing policies and information:

{knowledge_base}

Based ONLY on the information above, please answer the following question.
If the answer is not in the knowledge base, say "I don't have that information in the knowledge base."
Be professional, clear, and cite which document/section your answer comes from.

Question: {question}

Answer:"""
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=1024,
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        return f"Error: {str(e)}\n\nPlease check your GROQ_API_KEY in .env file"

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 AI Knowledge Base Agent</h1>', unsafe_allow_html=True)
    st.markdown("### Ask me anything about company policies and benefits!")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("📚 About This Agent")
        st.write("""
        This AI agent helps you find information from company documents instantly.
        
        **Features:**
        - 🔍 Natural language questions
        - 📄 Answers from company docs
        - 💬 Conversational interface
        - ⚡ Powered by Groq AI (Super Fast!)
        """)
        
        st.markdown("---")
        st.header("🔧 System Status")
        
        # Check API key
        if GROQ_API_KEY:
            st.success("✅ Groq API Key Loaded")
        else:
            st.error("❌ API Key Missing")
            st.info("Add GROQ_API_KEY to your .env file")
            st.stop()
        
        # Check documents
        if os.path.exists('documents'):
            doc_count = len([f for f in os.listdir('documents') if f.endswith('.txt')])
            st.success(f"✅ Found {doc_count} documents")
        else:
            st.error("❌ Documents folder missing")
            st.stop()
        
        st.markdown("---")
        
        # Reload button
        if st.button("🔄 Reload Documents"):
            st.session_state.knowledge_base = ""
            st.rerun()
        
        st.markdown("---")
        st.caption("Built for AI Agent Challenge 2024")
    
    # Load documents if not already loaded
    if not st.session_state.knowledge_base:
        with st.spinner("📚 Loading company documents..."):
            docs, message = load_documents_from_folder()
            if docs:
                st.session_state.knowledge_base = docs
                st.success(f"✅ {message}")
            else:
                st.error(f"❌ {message}")
                st.stop()
    
    # Example questions
    st.info("💡 **Try asking:** 'How many sick leave days do I get?' or 'Tell me about health insurance'")
    
    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(chat["question"])
        with st.chat_message("assistant"):
            st.write(chat["answer"])
    
    # User input
    user_question = st.chat_input("Type your question here...")
    
    if user_question:
        # Display user question
        with st.chat_message("user"):
            st.write(user_question)
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                answer = get_ai_response(user_question, st.session_state.knowledge_base)
                st.write(answer)
                
                # Save to history
                st.session_state.chat_history.append({
                    "question": user_question,
                    "answer": answer
                })
    
    # Clear chat button
    if len(st.session_state.chat_history) > 0:
        if st.button("🗑️ Clear Chat History"):
            st.session_state.chat_history = []
            st.rerun()

if __name__ == "__main__":
    main()