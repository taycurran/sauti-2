from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(__name__)
  
@app.get("/")
async def root():
  """
  Sauti Market Monitor API  
  Verifies the API is deployed, and links to the docs.
  """
  return HTMLResponse("""
  <h1>Sauti Market Monitor</h1>
  <p>Go to <a href="/docs">/docs</a> for documentation.</p>
  """)