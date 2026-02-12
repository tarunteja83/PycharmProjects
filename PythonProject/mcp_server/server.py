import os
import asyncio
import google.generativeai as genai
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Gemini Agent")

# Configure Gemini API
# Ensure you have GEMINI_API_KEY in your environment variables
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

@mcp.tool()
async def ask_gemini(prompt: str) -> str:
    """
    Ask Gemini a question and get a response.
    
    Args:
        prompt: The question or prompt to send to Gemini.
    """
    try:
        response = await model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini: {str(e)}"

if __name__ == "__main__":
    mcp.run()