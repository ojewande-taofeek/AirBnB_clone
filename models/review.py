#!/usr/bin/python3
"""Contains the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The class Review"""
    place_id = ""
    user_id = ""
    text = ""
