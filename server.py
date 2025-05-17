from mcp.server.fastmcp import FastMCP
import httpx
from pydantic import BaseModel

mcp = FastMCP("Demo")

DEV_SERVER_URL = "http://localhost:8000"


class ProjectContext(BaseModel):
    user_prompt: str | None = None
    project_mdc_file_contents: str | None = None
    project_package_manager_contents: str | None = None


@mcp.tool()
async def get_mcp_server_reccomendations(project_context: ProjectContext) -> str:
    """Get MCP Server recommendations for a given project context
    
    This function sends the code project context to the a server and returns
    recommendations based on the provided information.

    Always search through the project files first to find any relevent informaiton you need to pass into this tool.  
    
    Args:
        project_context: A ProjectContext object containing information about
            the user prompt, project MDC file contents, and package manager contents
    
    Returns:
        str: The recommendation response from the server or an error message
    
    Raises:
        Exception: If there's an issue connecting to the server or processing the request
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{DEV_SERVER_URL}/project-context", json=project_context.model_dump())
            return response.text
        except Exception as e:
            return f"Error: {e}"


print("Server is running")
if __name__ == "__main__":
    mcp.run()