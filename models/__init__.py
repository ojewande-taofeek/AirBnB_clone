#!/usr/bin/python3
"""create a unique FileStorage instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
__all__ = ["BaseModel", "User"]
