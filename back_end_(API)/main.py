# call the pieces needed
import uvicorn 
from fastapi import FastAPI 

app = FastAPI()

# Not sure if root is always needed
@app.get("/")
async def home():
    return {"message": "Tracking the Homestead"}

# one POST request (create)


# two GET requests (read)

# one PUT request (update)

# one DELETE request (delete)






# Then this actually runs the server 
if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)