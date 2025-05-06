from fastmcp import FastMCP

mcp = FastMCP("Math Server 🧮")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

if __name__ == "__main__":
    # Run with stdio transport
    mcp.run(transport="stdio")