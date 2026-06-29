<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=🔁+LoopTalk;Real-time+Video+%2B+Chat;Powered+by+AI+Second+Brain" alt="LoopTalk" />

<br/>

### Connect instantly. Remember everything.

[![React](https://img.shields.io/badge/React_18-61dafb?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![WebRTC](https://img.shields.io/badge/WebRTC-333?style=for-the-badge&logo=webrtc&logoColor=white)](https://webrtc.org)
[![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io)
[![Claude](https://img.shields.io/badge/Claude_API-6B47ED?style=for-the-badge&logo=anthropic&logoColor=white)](https://anthropic.com)

<br/>

[**Features**](#-features) &nbsp;·&nbsp; [**Tech Stack**](#-tech-stack) &nbsp;·&nbsp; [**Getting Started**](#-getting-started) &nbsp;·&nbsp; [**Second Brain**](#-ai-second-brain) &nbsp;·&nbsp; [**API Docs**](#-api-reference) &nbsp;·&nbsp; [**Roadmap**](#-roadmap)

</div>

---

## 🧠 What is LoopTalk?

**LoopTalk** is a full-stack real-time communication platform built as a summer project. It combines **1:1 video calling**, **instant messaging**, and an AI-powered **Second Brain** that learns from every conversation you have.

> 💡 Ask it *"What did we decide about the project deadline last month?"* — and it finds the answer from your actual past conversations, with sources.

Most chat apps let you search messages. LoopTalk lets you *understand* them.

---

## 🗺️ System Architecture

![LoopTalk Full Workflow](docs/workflow.png)

> **Three phases in one diagram:** Core real-time platform → AI summarization → Semantic Second Brain with RAG pipeline

---

## ✨ Features

### 🟦 Phase 1 — Core Platform

| Feature | Details |
|--------|---------|
| 🔐 **Authentication** | JWT access + refresh tokens, bcrypt password hashing, secure sessions |
| 💬 **Real-time chat** | Instant messaging via Socket.IO (python-socketio + FastAPI) with typing indicators and presence |
| 📹 **1:1 Video calls** | Browser-native WebRTC — no plugins, no downloads, pure P2P |
| 🎛️ **Call controls** | Mute, camera toggle, end call, incoming call toasts |
| 📜 **Message history** | Persistent chat logs in PostgreSQL, paginated and searchable |
| 🟢 **Presence system** | Online/offline/away status across all connected rooms |

### 🟡 Phase 2 — AI Summarization

| Feature | Details |
|--------|---------|
| 📝 **Auto summaries** | AI-generated key points and action items after each session |
| ⚡ **Async processing** | Celery background workers — the UI never blocks waiting for AI |
| 🗂️ **Summary history** | All summaries stored in DB and browsable per room/session |

### 🟣 Phase 3 — AI Second Brain ✦

| Feature | Details |
|--------|---------|
| 🧬 **Semantic memory** | Every message embedded (1536-dim vectors) and stored via `pgvector` |
| 🔍 **Natural language search** | Ask questions in plain English across your entire conversation history |
| 🤖 **RAG pipeline** | Top-8 similar past messages retrieved and passed to Claude as context |
| 🃏 **Source cards** | Every AI answer links to the exact conversations it used |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | React 18 + Vite | Fast SPA, HMR in development |
| **State** | Redux Toolkit | Auth state, call state, chat updates |
| **Real-time** | python-socketio + FastAPI | Chat events, signaling, presence |
| **Video** | WebRTC (browser-native) | P2P audio/video streams |
| **Backend** | Python + FastAPI | REST API + socket server |
| **Database** | PostgreSQL 15 | Users, messages, calls, summaries |
| **Vector search** | pgvector | Semantic similarity inside Postgres |
| **Jobs** | Celery + Redis | Async embeddings and summarization |
| **Embeddings** | OpenAI `text-embedding-3-small` | 1536-dim semantic vectors |
| **AI** | Anthropic Claude API | Grounded RAG answers |
| **NAT** | STUN / TURN | WebRTC call connectivity |

---

## 📁 Project Structure

```
looptalk/
│
├── 📂 docs/
│   └── workflow.png                  ← system architecture diagram
│
├── 📂 frontend/
│   └── src/
│       ├── 📂 components/
│       │   ├── Navbar.jsx
│       │   ├── ChatBox.jsx
│       │   ├── VideoPlayer.jsx
│       │   ├── CallControls.jsx
│       │   └── BrainSearch.jsx       ← 🧠 Second Brain UI
│       ├── 📂 pages/
│       │   ├── Home.jsx
│       │   ├── Login.jsx
│       │   ├── Register.jsx
│       │   ├── Chat.jsx
│       │   └── Room.jsx
│       ├── 📂 hooks/
│       │   ├── useAuth.js
│       │   ├── useSocket.js
│       │   └── useWebRTC.js
│       ├── 📂 store/
│       │   └── slices/               ← authSlice, callSlice, chatSlice
│       ├── 📂 services/
│       │   ├── api.js
│       │   └── socket.js
│       ├── App.jsx
│       └── main.jsx
│
├── 📂 backend/
│   └── app/
│       ├── 📂 models/
│       │   ├── user.py
│       │   ├── message.py            ← includes vector(1536) column
│       │   ├── call.py
│       │   └── summary.py
│       ├── 📂 routes/
│       │   ├── auth.py
│       │   ├── users.py
│       │   ├── chats.py
│       │   ├── summaries.py
│       │   └── brain.py             ← 🧠 /api/brain/ask
│       ├── 📂 sockets/
│       │   ├── chat_events.py
│       │   ├── call_events.py
│       │   └── presence_events.py
│       ├── 📂 services/
│       │   ├── auth_service.py
│       │   ├── chat_service.py
│       │   ├── summary_service.py
│       │   ├── embedding_service.py  ← 🧠 OpenAI embeddings
│       │   └── brain_service.py      ← 🧠 pgvector cosine search
│       ├── tasks.py                  ← Celery async jobs
│       ├── dependencies.py           ← FastAPI dependency injection
│       └── config.py
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+ with `pgvector` extension
- Redis

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Copy and fill in your environment variables
cp .env.example .env

# Run database migrations
alembic upgrade head

# Start the FastAPI server (with uvicorn)
uvicorn app.main:app --reload --port 8000

# In a separate terminal — start the Celery worker
celery -A app.tasks worker --loglevel=info
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173) in your browser.

### Environment Variables

```env
# backend/.env
DATABASE_URL=postgresql://user:password@localhost:5432/looptalk
REDIS_URL=redis://localhost:6379/0
SECRET_KEY=your-secret-key
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

---

## 🧠 AI Second Brain

> The most unique feature of LoopTalk — your conversation history becomes a searchable, queryable knowledge base.

### Architecture

```
Every chat message
       │
       ▼
┌─────────────────────────────┐
│   Embedding service         │  OpenAI text-embedding-3-small
│   1536-dimensional vector   │  Runs via Celery (async)
└────────────┬────────────────┘
             │  stored in PostgreSQL
             ▼
┌─────────────────────────────┐
│   messages.embedding        │  pgvector column
│   ivfflat index             │  Fast cosine similarity
└─────────────────────────────┘

                    User asks a question
                           │
                           ▼
              ┌────────────────────────┐
              │  Embed the question    │  Same model → same space
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  <=> cosine search     │  pgvector · top 8 results
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  Claude reads context  │  RAG · Anthropic API
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  Sourced answer        │  Answer + source cards
              └────────────────────────┘
```

### Database migration

```sql
-- Run once after alembic upgrade head
ALTER TABLE messages ADD COLUMN embedding vector(1536);

CREATE INDEX ON messages
  USING ivfflat (embedding vector_cosine_ops)
  WITH (lists = 100);
```

### Real example

```
❓ You ask:
   "What did we decide about the LoopTalk color scheme?"

🧠 Second Brain answers:
   "Based on your conversation on June 14th in the #design room,
    you and Priya decided on a dark blue and white primary palette
    with subtle gradients only in the hero section. You ruled out
    purple because it clashed with the logo.

    Sources
    ┌ June 14 · #design
    │ "Dark blue feels more premium. Let's go with that..."
    └ June 14 · #design
      "Agreed. White text on dark blue. Gradients only hero..."
```

---

## 📡 API Reference

### Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/auth/signup` | Register a new user |
| `POST` | `/api/auth/login` | Login → returns access + refresh tokens |
| `POST` | `/api/auth/refresh` | Refresh access token |
| `POST` | `/api/auth/logout` | Revoke refresh token |

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/users/me` | Get current user profile |
| `PUT` | `/api/users/me` | Update profile (name, avatar) |
| `GET` | `/api/users/search?q=` | Search users by name/email |

### Chat

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/chats/rooms` | List all rooms for current user |
| `GET` | `/api/chats/{roomId}/messages` | Get paginated message history |
| `POST` | `/api/chats/rooms` | Create or open a DM room |

### Summaries

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/summaries/{sessionId}` | Get AI summary for a session |
| `POST` | `/api/summaries/generate` | Manually trigger summary generation |

### Second Brain

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `POST` | `/api/brain/ask` | ✅ JWT | Ask a question about conversation history |

**Request body:**
```json
{
  "question": "What did we decide about the API structure?"
}
```

**Response:**
```json
{
  "answer": "Based on your June 18th conversation in #backend, you decided to use RESTful routes for all CRUD and Socket.IO exclusively for real-time events — no mixing.",
  "sources": [
    {
      "date": "2025-06-18",
      "room": "backend",
      "preview": "Keep REST for CRUD. Socket.IO only for live events..."
    },
    {
      "date": "2025-06-18",
      "room": "backend",
      "preview": "Agreed. No mixed approach — clean separation..."
    }
  ]
}
```

> 💡 FastAPI auto-generates interactive docs at `/docs` (Swagger UI) and `/redoc` — no extra setup needed.

---

### Socket.IO Events

| Event | Direction | Payload | Description |
|-------|-----------|---------|-------------|
| `send_message` | C → S | `{ roomId, content }` | Send a chat message |
| `message` | S → C | `{ id, sender, content, ts }` | Receive a message |
| `typing` | C → S | `{ roomId }` | User typing indicator |
| `call_offer` | C → S | `{ targetUserId, sdp }` | Initiate WebRTC call |
| `call_answer` | C → S | `{ callerId, sdp }` | Accept a call |
| `ice_candidate` | Both | `{ candidate }` | Exchange ICE candidates |
| `call_end` | Both | `{ roomId }` | End a call |
| `user_online` | S → C | `{ userId }` | Presence update |
| `user_offline` | S → C | `{ userId }` | Presence update |

---

## 📦 Dependencies

<details>
<summary><strong>backend/requirements.txt</strong></summary>

```txt
fastapi>=0.110.0
uvicorn[standard]>=0.29.0
python-socketio>=5.11.0
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
sqlalchemy>=2.0.0
alembic>=1.13.0
asyncpg>=0.29.0
pgvector>=0.2.0
celery>=5.3.0
redis>=5.0.0
openai>=1.0.0
anthropic>=0.20.0
python-dotenv>=1.0.0
pydantic-settings>=2.0.0
```

</details>

<details>
<summary><strong>frontend/package.json (key deps)</strong></summary>

```json
{
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-router-dom": "^6.0.0",
    "@reduxjs/toolkit": "^2.0.0",
    "react-redux": "^9.0.0",
    "socket.io-client": "^4.0.0",
    "axios": "^1.6.0"
  }
}
```

</details>

---

## 🗓️ Roadmap

```
✅ Phase 1 — Real-time chat, 1:1 video calls, auth, presence
✅ Phase 2 — AI conversation summarization (async Celery)
✅ Phase 3 — AI Second Brain (pgvector + RAG + Claude)
⬜ Live call translation  (Whisper STT → LLM → TTS)
⬜ Emotion AI overlay     (MediaPipe face + voice tone analysis)
⬜ Collaborative canvas   (shared whiteboard synced via Socket.IO)
⬜ Developer API + bots   (webhooks, custom bot integrations)
⬜ Group video calls      (SFU media server for 3+ participants)
⬜ Mobile app             (React Native)
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repo on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/looptalk.git

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes and commit
git commit -m "feat: add your feature"

# 5. Push and open a Pull Request
git push origin feature/your-feature-name
```

**Guidelines:**
- Keep FastAPI routers in `/routes/`, socket logic in `/sockets/`, business logic in `/services/`
- Add tests for new API endpoints in `/tests/`
- For large changes, open an issue first to discuss

---

## 📄 License

[MIT](LICENSE) © 2025

---

<div align="center">

Made with ❤️ during summer 2025

**React · FastAPI · PostgreSQL · WebRTC · pgvector · Claude API**

⭐ Star this repo if you found it useful!

</div>