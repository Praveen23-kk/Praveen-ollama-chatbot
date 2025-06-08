<h1 align="center">🧠 Praveen's AI Chatbot</h1>

<p align="center">
  <strong>A simple and powerful conversational AI built with 
  <a href="https://www.langchain.com/">LangChain</a> and 
  <a href="https://ollama.com/">Ollama</a> using the <code>llama3.2:1b</code> model.</strong>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build Status"></a>
  <a href="#"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python Version"></a>
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
````markdown
📦 Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/praveen-ai-chatbot.git
cd praveen-ai-chatbot
````

2. **Create and activate a virtual environment** (recommended)

```bash
# Create virtual environment
python -m venv chatbot

# Activate it
# Windows:
chatbot\Scripts\activate

# macOS/Linux:
source chatbot/bin/activate
```

3. **Install required dependencies**

```bash
pip install langchain-community langchain-core
```

4. **Install Ollama and pull the model**

Make sure [Ollama](https://ollama.com/) is installed on your machine.

```bash
ollama pull llama3.2:1b
```

---

## ▶️ Usage

To start the chatbot, run:

```bash
python main.py
```

You’ll see:

```
Welcome to Praveen's AI chat BOT! type 'exit' to to leave
You:
```

Type your question and chat with the bot. Type `exit` to quit the session.

---

## 🧠 How It Works

* The chatbot uses a LangChain `ChatPromptTemplate` to inject user input and conversation history into a structured prompt.
* The prompt is passed to the `llama3.2:1b` model running locally via Ollama.
* The model's response is printed, and the context is updated for the next interaction.

---

## 🐞 Known Issues

* **Code fix:**
  The following line in `main.py` has a bug:

  ```python
  context == f"\nUser:{user_input}\nAI:{result}"
  ```

  It should be:

  ```python
  context = f"\nUser:{user_input}\nAI:{result}"
  ```

* Context is maintained only during the session — no long-term memory yet.

* This is a command-line only interface; no GUI or web frontend.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ✍️ Author

Developed by **Praveen**

---

## 🙋‍♂️ Contributing

Contributions are welcome! If you find issues or want to suggest improvements:

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

---



