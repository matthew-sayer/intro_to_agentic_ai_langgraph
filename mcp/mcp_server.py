from fastmcp import FastMCP
from typing import Dict

mcp = FastMCP(
    "my_first_mcp_server",
    instructions="This is an MCP server for learning",  
)

@mcp.tool()
def fizzbuzz(x: int) -> Dict:
    """A basic FizzBuzz example tool to illustrate MCP.
    Args: x (int) - this is the upper limit to calculate FizzBuzz up to.
    Returns: results (Dict) - this dictionary will contain the appended results for FizzBuzz, Fizz and Buzz.
    """
    results = {}
    for i in range(1, x+1):
        if i % 15 == 0:
            results[i] = "FizzBuzz"
        elif i % 3 == 0:
            results[i] = "Fizz"
        elif i % 5 == 0:
            results[i] = "Buzz"

    return results


mcp.run(transport="streamable-http", port=8080)
