from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "running"}


@app.get("/technologies")
def read_technologies():
    return {"technologies": ["Python", "FastAPI", "JavaScript", "React"]}


@app.get("/levels")
def read_levels():
    return {"levels": ["Beginner", "Intermediate", "Advanced"]}
