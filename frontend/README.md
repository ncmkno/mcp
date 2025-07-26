# Authentication Frontend for MCP

A modern React application built with Vite that provides a seamless authentication experience using Stytch's authentication platform. This application demonstrates integration with OAuth providers (Google) and password-based authentication.

> 📖 **See the [main project README](../README.md) for complete project overview and setup instructions.**

## 🚀 Features

- **Modern React 19** with latest features and performance optimizations
- **Vite** for lightning-fast development and build times
- **Stytch Authentication** integration with multiple authentication methods
- **OAuth Support** for Google authentication
- **Password Authentication** with secure login/signup flows
- **Responsive Design** with modern CSS styling
- **ESLint Configuration** for code quality and consistency
- **Hot Module Replacement (HMR)** for rapid development

## 📋 Prerequisites

- Node.js (version 18 or higher)
- npm or yarn package manager

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Configure Stytch**
   
   Update the Stytch public token in `src/main.jsx`:
   ```javascript
   const stytch = createStytchUIClient('your-stytch-public-token');
   ```

4. **Start development server**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

   The application will be available at `http://localhost:5173`

## 📦 Available Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start development server with HMR |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint for code quality |

## 🏗️ Project Structure

```
frontend/
├── public/                # Static assets
│   └── vite.svg           # Vite logo
├── src/
│   ├── App.jsx            # Main application component
│   ├── App.css            # Application styles
│   ├── main.jsx           # Application entry point
│   └── index.css          # Global styles
├── package.json           # Dependencies and scripts
├── vite.config.js         # Vite configuration
├── eslint.config.js       # ESLint configuration
└── index.html             # HTML template
```

## 🔧 Configuration

### Stytch Authentication

The application is configured with Stytch authentication supporting:

- **OAuth Providers**: Google
- **Password Authentication**: Email/password login and signup
- **Session Management**: Automatic user session handling

## 🎨 Customization

### Styling

The application uses CSS modules and global styles. Main styling files:

- `src/index.css` - Global styles and CSS variables
- `src/App.css` - Component-specific styles

### Authentication Flow

Modify the authentication configuration in `src/App.jsx`:

```javascript
const config = {
  "products": ["oauth", "passwords"],
  "oauthOptions": {
    "providers": [
      { "type": "google" }
    ],
    "loginRedirectURL": "your-login-url",
    "signupRedirectURL": "your-signup-url"
  }
  // ... additional configuration
}
```

### Adding Dependencies

```bash
npm install <package-name>
# or
yarn add <package-name>
```

## 📚 Dependencies

### Core Dependencies

- **React 19** - Modern React with latest features
- **React DOM** - React rendering for web
- **Stytch React** - Authentication UI components
- **Stytch Vanilla JS** - Core authentication functionality

### Development Dependencies

- **Vite** - Fast build tool and dev server
- **ESLint** - Code linting and quality
- **React Hooks ESLint Plugin** - Hooks-specific linting rules
- **React Refresh ESLint Plugin** - Fast refresh support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Vite](https://vitejs.dev/) for the excellent build tool
- [React](https://reactjs.org/) for the amazing UI library
- [Stytch](https://stytch.com/) for authentication infrastructure
- [ESLint](https://eslint.org/) for code quality tools
