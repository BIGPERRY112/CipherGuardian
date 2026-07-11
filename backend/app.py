from fastapi import FastAPI

app = FastAPI(
    title="CipherGuardian",
    version="0.1.0",
    description="Open-source cybersecurity platform for ethical security assessments."
)

@app.get("/")
def root():
    return {
        "project": "CipherGuardian",
        "status": "Running",
        "version": "0.1.0"
    }
