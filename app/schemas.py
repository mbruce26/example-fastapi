from datetime import datetime
from pydantic import BaseModel, EmailStr, conint
from typing import Optional

from app.models import Post


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserOut

    class Config:
        from_attributes = True


class PostVote(BaseModel):
    Post: PostResponse
    votes: int


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
