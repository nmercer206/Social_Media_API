from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from.config import settings


print(settings.database_password)

models.Base.metadata.create_all(bind=engine)    # this is the command that told SQLAlchemy to run create statement, so that it creates all tables when starting up
                                                # Now that we have alembic, we no longer need this line of code. You can still keep it, but that would just mean that
                                                # your first alembic migration won't have to do anything, since everything will already be there.

app = FastAPI()

origins = ["https://www.google.com"] # [*] specifies that any domain can access it


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='postgres1', cursor_factory=RealDictCursor) 
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error: ", error)
#         time.sleep(2)
#         #(host (local IP address), database (matches up with the name of the database we created), user(username = postgres), password(postgres password), cursor_factory(gives you the column name, as well as the value.. makes a nice python dict when it returns value))

#$$$$$$$$$$$$$$$$$$$$$$$$ MOVED THIS BLOCK OF CODE  ^^^^^^^^^^^ INTO database.py $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

#----------------------------------------------------------------------------------------------------------------------------------------------------------

