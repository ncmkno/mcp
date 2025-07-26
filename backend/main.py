"""MCP Server for managing user notes with authentication."""
import os

from dotenv import load_dotenv
from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.dependencies import get_access_token, AccessToken
from jose import jwt
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.requests import Request as StarletteRequest
from starlette.responses import JSONResponse

from database import NoteRepository

load_dotenv()

auth = BearerAuthProvider(
    jwks_uri=f"{os.getenv('STYTCH_DOMAIN')}/.well-known/jwks.json",
    issuer=os.getenv("STYTCH_DOMAIN"),
    algorithm="RS256",
    audience=os.getenv("STYTCH_PROJECT_ID")
)

mcp = FastMCP(name="Kino MCP Server", auth=auth)

@mcp.tool()
def get_my_notes() -> str:
    """Get all notes for a user"""
    try:
        access_token = get_access_token()
        if access_token is None:
            return "Authentication required. Please authenticate first."
        
        user_id = jwt.get_unverified_claims(access_token.token)["sub"]
        if not user_id:
            return "Invalid token: missing user ID"

        notes = NoteRepository.get_notes_by_user(user_id)
        if not notes:
            return "no notes found"

        result = "Your notes:\n"
        for note in notes:
            result += f"{note.id}: {note.content}\n"

        return result
    except Exception as e:
        return f"Error retrieving notes: {str(e)}"

@mcp.tool()
def add_note(content: str) -> str:
    """Add a note for a user"""
    try:
        access_token = get_access_token()
        if access_token is None:
            return "Authentication required. Please authenticate first."
        
        user_id = jwt.get_unverified_claims(access_token.token)["sub"]
        if not user_id:
            return "Invalid token: missing user ID"

        if not content or not content.strip():
            return "Note content cannot be empty"

        note = NoteRepository.create_note(user_id, content.strip())
        return f"added note: {note.content}"
    except ValueError as e:
        return f"Validation error: {str(e)}"
    except Exception as e:
        return f"Error creating note: {str(e)}"

@mcp.custom_route(path="/.well-known/oauth-protected-resource", methods=["GET", "OPTIONS"])
def oauth_metadata(request: StarletteRequest) -> JSONResponse:
    """Provide OAuth metadata for the protected resource."""
    base_url = str(request.base_url).rstrip("/")

    return JSONResponse(
        {
            "resource": base_url,
            "authorization_servers": [os.getenv("STYTCH_DOMAIN")],
            "scopes_supported": ["read", "write"],
            "bearer_methods_supported": ["header", "body"],
        }
    )

@mcp.custom_route(path="/.well-known/oauth-authorization-server", methods=["GET", "OPTIONS"])
def oauth_authorization_server(request: StarletteRequest) -> JSONResponse:
    """Provide OAuth authorization server metadata."""
    stytch_domain = os.getenv("STYTCH_DOMAIN")
    
    return JSONResponse(
        {
            "issuer": f"{stytch_domain}/",
            "authorization_endpoint": f"{stytch_domain}/authorize",
            "token_endpoint": f"{stytch_domain}/token",
            "response_types_supported": ["code"],
            "grant_types_supported": ["authorization_code", "refresh_token"],
            "token_endpoint_auth_methods_supported": ["client_secret_post"],
            "code_challenge_methods_supported": ["S256"]
        }
    )

@mcp.custom_route(path="/.well-known/oauth-authorization-server/{path:path}", methods=["GET", "OPTIONS"])
def oauth_authorization_server_path(request: StarletteRequest, path: str) -> JSONResponse:
    """Handle OAuth authorization server requests with path parameters."""
    # Redirect to the base authorization server endpoint
    return oauth_authorization_server(request)

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ]
    )
