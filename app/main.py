from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Welcome to the api"}


# @app.get("/sqlalchemy")
# def test_post(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"status": posts}


# @app.get("/posts/latest", response_model=schemas.PostResponse)
# def get_latest_post():
#     post = my_posts[-1]
#     return post
