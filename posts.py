from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from db import Post, get_all_posts, get_post_by_id, save_post


class PostCreateSchema(BaseModel):
    body: str
    author: str


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
    post = Post(**post_create.dict())

    if "python" in post.body or "Python" in post.body:
        post.tags.append("python")
    if "vue" in post.body or "Vue" in post.body:
        post.tags.append("vue")
    if "nodejs" in post.body or "NodeJS" in post.body:
        post.tags.append("nodejs")
    if "php" in post.body or "PHP" in post.body:
        post.tags.append("php")

    return save_post(post)


@router.post("/posts/{postId}/edit-tags")
def set_tags_on_post(postId: str, newTags: list[str]):
    post = get_post_by_id(postId)

    post.tags = newTags
    post = save_post(post)
    return post
