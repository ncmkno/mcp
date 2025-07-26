"""Database models and repository for the MCP application.

This module provides SQLAlchemy models and repository classes for managing
notes in the application. It includes the Note model and NoteRepository
for database operations.
"""

from typing import List

from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session, declarative_base

engine = create_engine("sqlite:///database.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Note(Base):
    """SQLAlchemy model representing a note in the database.
    
    Attributes:
        id: Primary key identifier for the note
        user_id: Foreign key to identify the user who owns the note
        content: The text content of the note
    """

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False, index=True)
    content = Column(Text, nullable=False)


Base.metadata.create_all(bind=engine)


def get_db():
    """Get a database session with automatic cleanup.
    
    Yields:
        Session: A SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class NoteRepository:
    """Repository class for Note database operations.
    
    Provides static methods for common database operations on notes,
    including creating, retrieving, and deleting notes.
    """

    @staticmethod
    def get_notes_by_user_id(db: Session, user_id: str) -> List[Note]:
        """Retrieve all notes for a specific user.
        
        Args:
            db: Database session
            user_id: ID of the user whose notes to retrieve
            
        Returns:
            List of Note objects belonging to the user
        """
        return db.query(Note).filter(Note.user_id == user_id).all()

    @staticmethod
    def create_note(user_id: str, content: str) -> Note:
        """Create a new note for a user.
        
        Args:
            user_id: ID of the user creating the note
            content: Text content of the note
            
        Returns:
            The created Note object
        """
        if not user_id or not content:
            raise ValueError("user_id and content are required")
            
        db = SessionLocal()
        try:
            note = Note(user_id=user_id, content=content)
            db.add(note)
            db.commit()
            db.refresh(note)
            return note
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    @staticmethod
    def delete_note(note_id: int) -> bool:
        """Delete a note by its ID.
        
        Args:
            note_id: ID of the note to delete
            
        Returns:
            True if note was deleted, False if not found
        """
        db = SessionLocal()
        try:
            note = db.query(Note).filter(Note.id == note_id).first()
            if note:
                db.delete(note)
                db.commit()
                return True
            return False
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()

    @staticmethod
    def get_notes_by_user(user_id: str) -> List[Note]:
        """Retrieve all notes for a specific user.
        
        Args:
            user_id: ID of the user whose notes to retrieve
            
        Returns:
            List of Note objects belonging to the user
        """
        if not user_id:
            raise ValueError("user_id is required")
            
        db = SessionLocal()
        try:
            return db.query(Note).filter(Note.user_id == user_id).all()
        finally:
            db.close()
