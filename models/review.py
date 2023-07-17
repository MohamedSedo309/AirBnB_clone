#!/usr/bin/python3
"""create review module
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """ create  review class
    """
    place_id = ""
    user_id = ""
    text = ""
