from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def say_hi():
    return "yaaaaaaay!!"

@app.get("/contacts")
def get_all_contacts():
    return "all contacts"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)