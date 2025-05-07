# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "fastmcp",
# ]
# ///
from fastmcp import FastMCP
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Run the Math Server 🧮")
parser.add_argument("--transport", type=str, default="stdio", choices=["stdio", "sse"], help="Transport type (default: stdio)")
parser.add_argument("--port", type=int, default=8069, help="Port number for SSE transport (default: 8069)")
args = parser.parse_args()

mcp = FastMCP("Math Server 🧮")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

if __name__ == "__main__":
    # Run with specified transport and port
    if args.transport == "sse":
        mcp.run(transport="sse", port=args.port)
    else:
        mcp.run(transport="stdio")