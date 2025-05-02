# MediHelp AI Bot

MediHelp AI Bot is a **Telegram Bot** that allows users to ask **medical questions** and receive AI-powered answers based on a **retrieval-augmented generation** (RAG) pipeline using **LangChain**, **HuggingFace models**, and **Pinecone**.

---

## Bot Info
- **Bot Name**: `MediHelp AI`
- **Bot Username**: `@MediHelp_AI_Bot` 

---

## Features
-  Answer medical questions based on knowledge base
-  Save user sessions (Q&A history)
-  Start new chat sessions
-  View and download previous chat histories (as `.txt` or `.json`)
-  Powered by **Mistral-7B-Instruct** model from HuggingFace
-  Uses **Pinecone** for vector search

---

## Project Structure
```
├── Bot.py                # Main Telegram bot starter
├── handlers.py           # Telegram command/message handlers
├── llm_chain.py          # LLM and retrieval chain setup
├── session.py            # Session management (save/load/export)
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
├── Procfile              # For deployment (e.g., Heroku)
└── sessions/             # Saved user session files
```

---

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
You already have an `.env` example:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index_name
PINECONE_ENV=your_pinecone_environment_url
HF_TOKEN=your_huggingface_api_token
```

Update it with your credentials.

---

## Running the Bot Locally

```bash
python Bot.py
```

The bot will start polling and will be ready to receive messages!

---

## Commands Available in Bot
| Command         | Description                        |
| --------------- | ---------------------------------- |
| `/start`        | Start interacting with the bot     |
| `/help`         | List all available commands        |
| `/new`          | Start a new session (clear history) |
| `/history`      | View previous questions            |
| `/edit`         | (Coming soon) Edit a past question  |
| `/download txt` | Download chat history as TXT        |
| `/download json`| Download chat history as JSON       |

---

## Notes
- **Editing** previous questions (`/edit`) is not implemented yet (placeholder in code).
- **Pinecone** is used for retrieval: make sure your index is properly populated!
- **Mistral-7B-Instruct** is used through HuggingFace inference endpoint.
- Sessions are saved locally under `sessions/` folder.

