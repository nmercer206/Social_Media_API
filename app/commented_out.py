#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#                               MAIN
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# my_posts = [
#     {
#         "title" : "title of post 1",
#         "content" : "content of post 1", 
#         "id" : 1
#     },
#     {
#         "title" : "favorite foods",
#         "content" : "I like pizza", 
#         "id" : 2
#     }
# ]

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id): # this function uses enumerate to loop through my_posts. i = index, p = value, if id == p, return i
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i





# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(posts)
#     return {"data" : posts}

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# USING SQL QUERIES
    # def get_posts():
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # return {"data" : posts}

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# USING SQL QUERIES
    # def create_posts(post: Post): #creates a Post object
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit() #commits changes to database
    # return {"data" : new_post}

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# @app.get("/posts/length") #gets the amount of posts there are
# def get_length():
#     length = len(my_posts)
#     return length

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# @app.get("/posts/latest") #gets the latest post. Since all of the posts are in a "data" ARRAY, we have to do -1
# def get_latest_post():
#     post = my_posts[len(my_posts) - 1]
#     return {"detail" : post}

#----------------------------------------------------------------------------------------------------------------------------------------------------------

 #USING SQL QUERIES
    # def get_post(id: str):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    # post = cursor.fetchone()
    # if not post: #this only runs if the request contains an ID that doesn't exist
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                         detail=f"post with id: {id} not found")
    # return {"post_detail" : post}

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# def delete_post(id: int): 
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    # if deleted_post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                         detail=f"post with id: {id} does not exist")
    #
    # return Response(status_code=status.HTTP_204_NO_CONTENT) #when you're passing through a 204 status code, or trying to delete something,
    #                                                         #you don't want to return anything back               

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# def update_post(id: int, post: Post):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
    # (post.title, post.content, post.published, str(id)))

    # updated_post = cursor.fetchone()
    # conn.commit()

    # if updated_post == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                         detail=f"post with id: {id} does not exist")

    # return {"data" : updated_post}

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------