from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test MCP")

INCLUDE_ADD = True
INCLUDE_SUBTRACT = False

if INCLUDE_ADD:

    @mcp.tool()
    def add(a: int, b: int) -> int:
        return a + b

elif INCLUDE_SUBTRACT:

    @mcp.tool()
    def subtract(a: int, b: int) -> int:
        return a - b


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
