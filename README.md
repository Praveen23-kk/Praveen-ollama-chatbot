<p align="center">
  <h1>🧠 Praveen's AI Chatbot</h1>
  <p>A simple and powerful conversational AI built with <a href="https://www.langchain.com/">LangChain</a> and <a href="https://ollama.com/">Ollama</a> using the <code>llama3.2:1b</code> model.</p>
</p>

<p align="center">
  <a href="https://github.com/yourusername/praveen-ai-chatbot/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/yourusername/praveen-ai-chatbot/ci.yml" alt="Build Status"/>
  </a>
  <a href="https://github.com/yourusername/praveen-ai-chatbot/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/yourusername/praveen-ai-chatbot" alt="License"/>
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version"/>
  </a>
</p>

---

## 🚀 Features

- 💬 Context-aware chat using LangChain prompt chaining  
- 🤖 Powered by Ollama running local LLaMA 3.2 model  
- 🖥️ Terminal-based simple conversational interface  
- ⚙️ Easily customizable and extendable  

---

## 🛠️ Tech Stack

- Python 3.8+  
- [LangChain](https://www.langchain.com/)  
- [Ollama](https://ollama.com/)  
- LLama 3.2 (1B parameters) model  

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/praveen-ai-chatbot.git
cd praveen-ai-chatbot

Create and activate a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install langchain-community langchain-core
Install and run Ollama

Download Ollama from https://ollama.com/

Pull the model:

bash
Copy
Edit
ollama pull llama3.2:1b
▶️ Usage
Run the chatbot:

bash
Copy
Edit
python chatbot.py
You will see:

rust
Copy
Edit
Welcome to Praveen's AI chat BOT! type 'exit' to to leave
You:
Start typing your questions and interact with the bot. Type exit to quit.

🧠 How It Works
The chatbot uses a LangChain prompt template to pass the conversation history and user questions to the LLaMA model via Ollama, generating context-aware responses.

🐞 Known Issues
The current code has a bug:

python
Copy
Edit
context==f"\nUser:{user_input}\nAI:{result}"
should be

python
Copy
Edit
context = f"\nUser:{user_input}\nAI:{result}"
Context is only maintained during the current session; no persistent memory.

Terminal-only interface; no web UI yet.

📄 License
This project is licensed under the MIT License.

✍️ Author
Developed by Praveen

Feel free to open issues or contribute!

yaml
Copy
Edit

---

### Notes:

- Replace all instances of `yourusername` with your GitHub username.
- If you don’t have a CI workflow, you can remove the Build Status badge line.
- The license badge requires that you add an MIT `LICENSE` file.
- You can add screenshots or demo GIFs below the heading by adding an image markdown line.

---

If you want me to generate a `.md` file or help set up badges or CI workflows, just ask!
