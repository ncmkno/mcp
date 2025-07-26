# Kino MCP Project

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Node.js](https://img.shields.io/badge/Node.js-18+-green.svg)](https://nodejs.org/)
[![React](https://img.shields.io/badge/React-19.1.0-61dafb.svg)](https://reactjs.org/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.10.6+-orange.svg)](https://github.com/fastmcp/fastmcp)
[![Vite](https://img.shields.io/badge/Vite-7.0.4-646cff.svg)](https://vitejs.dev/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.41+-red.svg)](https://www.sqlalchemy.org/)
[![Stytch](https://img.shields.io/badge/Stytch-Auth-00d4aa.svg)](https://stytch.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code%20Style-PyLint%20%7C%20ESLint-black.svg)](https://www.pylint.org/)

A simple Model Context Protocol (MCP) implementation featuring a secure FastMCP server with OAuth 2.0 authentication and a modern React frontend. This project demonstrates how to build authentifaction feature when AI assistant tools like Claude Code to authentice user management before using the MCP tools.

## 🎥 See It In Action

Watch the demo video below to see the MCP server in action with authentication:

### Option 1: Download and View Locally
You can download the demo video from the repository:
- **Video File**: [`backend/assets/demo_auth_mcp.mp4`](backend/assets/demo_auth_mcp.mp4) (2.83 MB)
- **Right-click** the link above and select "Save link as..." to download
- **Open** the downloaded file in your video player

### Option 2: View on GitHub
- Navigate to [`backend/assets/demo_auth_mcp.mp4`](backend/assets/demo_auth_mcp.mp4) in the repository
- Click the **"Raw"** button to view the video directly in your browser
- Or use the **"Download"** button to save the file

### Option 3: Host on External Platform (Recommended)
For better viewing experience, consider hosting the video on:
- **YouTube**: Upload as unlisted video and embed
- **GitHub Releases**: Create a release and attach the video
- **Vimeo**: Upload and embed with privacy settings
- **Loom**: Record and share with embed code

*Note: The demo shows the authentication flow when using the MCP tools. The video demonstrates how users authenticate through the frontend and then interact with the MCP server tools for note management.*

### Demo Features
- **OAuth Authentication**: Shows the complete authentication flow using Stytch
- **MCP Tool Integration**: Demonstrates how AI assistants can use the authenticated MCP tools
- **Note Management**: Shows creating and retrieving notes through the MCP interface
- **Real-time Interaction**: Demonstrates the seamless integration between frontend auth and backend MCP tools

## 🚀 Features

### Backend (FastMCP Server)
- **OAuth 2.0 Authentication**: Secure authentication using Stytch as the identity provider
- **Note Management**: Create, retrieve, and manage user notes through MCP tools
- **SQLite Database**: Lightweight database with SQLAlchemy ORM
- **CORS Support**: Cross-origin resource sharing enabled
- **Type Safety**: Full type hints and comprehensive documentation
- **Professional Code Quality**: Linting with PyLint and comprehensive documentation

### Frontend (React Application)
- **Modern React 19**: Latest features and performance optimizations
- **Vite Build System**: Lightning-fast development and build times
- **Stytch Authentication**: Integration with multiple authentication methods
- **OAuth Support**: Google authentication provider
- **Password Authentication**: Secure login/signup flows
- **Responsive Design**: Modern CSS styling with responsive layouts
- **ESLint Configuration**: Code quality and consistency enforcement
- **Hot Module Replacement (HMR)**: Rapid development experience

## 📋 Prerequisites

- **Python 3.13** or higher
- **Node.js 18** or higher
- **uv** package manager (for Python dependencies)
- **npm** or **yarn** (for Node.js dependencies)
- **Stytch account** and project credentials

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd mcp
```

### 2. Backend Setup
```bash
cd backend
uv sync
```

Create a `.env` file in the backend directory:
```env
STYTCH_DOMAIN=https://your-project.stytch.com
STYTCH_SECRET=your-secret-key
STYTCH_PROJECT_ID=your-project-id
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```

Update the Stytch public token in `src/main.jsx`:
```javascript
const stytch = createStytchUIClient('your-stytch-public-token');
```

## 🚀 Running the Application

### Backend Server
```bash
cd backend
uv run python3 main.py
```
The server will start on `http://127.0.0.1:8000`

### Frontend Development Server
```bash
cd frontend
npm run dev
```
The application will be available at `http://localhost:5173`

## 🌐 Exposing Your Local Server with ngrok

For API integration and testing with external services, you can expose your local server using ngrok:

1. **Install ngrok** from [https://ngrok.com/download](https://ngrok.com/download)
2. **Authenticate** your ngrok installation:
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```
3. **Start your MCP server** (in one terminal):
   ```bash
   cd backend
   uv run python3 main.py
   ```
4. **Start ngrok tunnel** (in another terminal):
   ```bash
   ngrok http 8000
   ```

## 🔧 API Endpoints

### MCP Tools

The server provides the following MCP tools for AI assistants:

#### `get_my_notes()`
Retrieves all notes for the authenticated user.

**Returns**: A formatted string containing all user notes or "no notes found"

#### `add_note(content: str)`
Adds a new note for the authenticated user.

**Parameters**:
- `content` (str): The text content of the note

**Returns**: Confirmation message with the added note content

### OAuth Endpoints

#### `GET /.well-known/oauth-protected-resource`
Provides OAuth metadata for the protected resource.

#### `GET /.well-known/oauth-authorization-server`
Provides OAuth authorization server metadata.

## 🗄️ Database Schema

The application uses SQLite with the following schema:

### Notes Table
```sql
CREATE TABLE notes (
    id INTEGER PRIMARY KEY,
    user_id VARCHAR NOT NULL,
    content TEXT NOT NULL
);
```

**Indexes**:
- `ix_notes_id` on `id`
- `ix_notes_user_id` on `user_id`

## 🏗️ Architecture

### Backend Architecture
- **FastMCP Server**: Main server implementation using FastMCP framework
- **BearerAuthProvider**: OAuth 2.0 authentication provider
- **NoteRepository**: Database operations for notes
- **SQLAlchemy Models**: Database models and session management

### Frontend Architecture
- **React 19**: Modern React with latest features
- **Vite**: Fast build tool and development server
- **Stytch React**: Authentication UI components
- **Stytch Vanilla JS**: Core authentication functionality

### Key Dependencies

#### Backend
- **fastmcp**: MCP server framework
- **python-jose**: JWT token handling
- **sqlalchemy**: Database ORM
- **starlette**: ASGI framework for middleware
- **python-dotenv**: Environment variable management
- **stytch**: Identity provider integration

#### Frontend
- **React 19**: Modern React with latest features
- **React DOM**: React rendering for web
- **Stytch React**: Authentication UI components
- **Stytch Vanilla JS**: Core authentication functionality
- **Vite**: Fast build tool and dev server

## 🔒 Security

- **OAuth 2.0**: Secure authentication using Stytch
- **JWT Tokens**: Stateless authentication with RS256 algorithm
- **CORS**: Configured for cross-origin requests
- **Input Validation**: Type-safe parameter handling
- **Environment Variables**: Secure credential management

## 📁 Project Structure

```
mcp/
├── backend/                # FastMCP server implementation
│   ├── main.py             # Main server file
│   ├── database.py         # Database models and repository
│   ├── database.db         # SQLite database file
│   ├── pyproject.toml      # Python project configuration
│   └── README.md           # Backend documentation
├── frontend/               # React application
│   ├── src/
│   │   ├── App.jsx         # Main application component
│   │   ├── App.css         # Application styles
│   │   ├── main.jsx        # Application entry point
│   │   └── index.css       # Global styles
│   ├── package.json        # Node.js dependencies
│   ├── vite.config.js      # Vite configuration
│   ├── eslint.config.js    # ESLint configuration
│   └── README.md           # Frontend documentation
└── README.md               # This file
```



## 📚 Documentation

- **[Backend Documentation](./backend/README.md)**: Detailed backend setup, API documentation, and usage examples
- **[Frontend Documentation](./frontend/README.md)**: Frontend setup, configuration, and customization guide

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Links

- [FastMCP Documentation](https://github.com/fastmcp/fastmcp)
- [Stytch Documentation](https://stytch.com/docs)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [React Documentation](https://reactjs.org/docs/)
- [Vite Documentation](https://vitejs.dev/)
- [ngrok Documentation](https://ngrok.com/)

## 🙏 Acknowledgments

- [Tech with Tim](https://www.youtube.com/c/TechWithTim) for inspiring this project and providing excellent educational content
- [FastMCP](https://github.com/fastmcp/fastmcp) for the excellent MCP server framework
- [Stytch](https://stytch.com/) for authentication infrastructure
- [React](https://reactjs.org/) for the amazing UI library
- [Vite](https://vitejs.dev/) for the excellent build tool
- [SQLAlchemy](https://www.sqlalchemy.org/) for database ORM
- [ngrok](https://ngrok.com/) for secure tunneling 