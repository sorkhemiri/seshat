from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import http.cookies


http.cookies._is_legal_key = lambda _: True

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000, debug=True)
