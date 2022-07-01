from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from db import Post, get_all_posts, get_post_by_id, save_post


class PostCreateSchema(BaseModel):
    body: str
    author: str
    title: str


router = APIRouter()


@router.get("/posts", response_model=list[Post])
def get_all():
    return get_all_posts()


@router.get("/posts/{post_id}", response_model=Post)
def get_by_id(post_id: int):
    post = get_post_by_id(post_id)

    if post is None:
        raise HTTPException(404)

    return post


@router.post("/posts")
def create_new_post(post_create: PostCreateSchema):
    if len(post.title) > 100:
        return "Post title should be max. 100 cahracters long"

    post = Post(**post_create.dict())
    return save_post(post)
