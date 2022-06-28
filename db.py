from datetime import datetime
from typing import Callable, Optional, Union

from fastapi import APIRouter
from pydantic import BaseModel, Field


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


@static_vars(counter=0)
def next_post_id():
    next_post_id.counter += 1
    return next_post_id.counter


class Post(BaseModel):
    id: int = Field(default_factory=next_post_id)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    body: str
    author: str


in_memory_db: dict[str, list[Post]] = {"posts": []}


def save_post(post: Post):
    """
    Persists the given post in our database

    :return: returns the persisted model
    """
    in_memory_db["posts"].append(post)
    return post


def get_all_posts():
    """
    PReturns all posts in the database
    """
    return in_memory_db["posts"]


def get_post_by_id(post_id: int):
    """
    Finds the given post in our database
    :param post_id: Id of the post to find in the database

    :return: the post with given id model or None if no post with given id was found
    """
    return next((post for post in in_memory_db["posts"] if post.id == post_id), None)
