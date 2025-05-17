from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("Demo")

DEV_SERVER_URL = "http://localhost:8000"

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
async def hello_world() -> str:
    """Say hello to the world"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{DEV_SERVER_URL}/")
            return response.text
        except Exception as e:
            return f"Error: {e}"


print("Server is running")
if __name__ == "__main__":
    mcp.run()