<p align="center">
  <h1>🧠 Praveen's AI Chatbot</h1>
</p>

<p align="center">
  A simple and powerful conversational AI built with <a href="https://www.langchain.com/">LangChain</a> and <a href="https://ollama.com/">Ollama</a> running <code>llama3.2:1b</code> model.
</p>

---

<p align="center">
  <img src="https://github.com/yourusername/praveen-ai-chatbot/raw/main/demo.gif" alt="Chatbot Demo" width="600"/>
</p>

---

<h2 align="center">🚀 Features</h2>

<ul>
  <li>💬 Context-aware chat with LangChain prompt chaining</li>
  <li>🤖 Powered by Ollama & LLaMA 3.2 local large language model</li>
  <li>🖥️ Simple command-line interface</li>
  <li>⚙️ Easy to customize and extend</li>
</ul>

---

<h2 align="center">🛠️ Tech Stack</h2>

<p align="center">
  Python 3.8+ • LangChain • Ollama • LLaMA 3.2
</p>

---

<h2 align="center">📦 Installation</h2>

```bash
# Clone repo
git clone https://github.com/yourusername/praveen-ai-chatbot.git
cd praveen-ai-chatbot

# Create & activate virtual env (optional but recommended)
python -m venv venv
venv\Scripts\activate     # Windows
# or
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install langchain-community langchain-core

# Setup Ollama model (install Ollama first: https://ollama.com/)
ollama pull llama3.2:1b
