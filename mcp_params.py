import os
from pathlib import Path
from dotenv import load_dotenv
from market import is_paid_polygon, is_realtime_polygon

load_dotenv(override=True)

# Get absolute paths
PROJECT_DIR = Path(__file__).parent.absolute()
PYTHON_BIN = str(PROJECT_DIR / ".venv" / "bin" / "python")

brave_env = {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
polygon_api_key = os.getenv("POLYGON_API_KEY")

# The MCP server for the Trader to read Market Data

if is_paid_polygon or is_realtime_polygon:
    market_mcp = {
        "command": "python3",
        "args": ["-m", "uvx", "--from", "git+https://github.com/polygon-io/mcp_polygon@v0.1.0", "mcp_polygon"],
        "env": {"POLYGON_API_KEY": polygon_api_key},
    }
else:
    market_mcp = {"command": PYTHON_BIN, "args": [str(PROJECT_DIR / "market_server.py")]}


# The full set of MCP servers for the trader: Accounts, Push Notification and the Market

trader_mcp_server_params = [
    {"command": PYTHON_BIN, "args": [str(PROJECT_DIR / "accounts_server.py")]},
    {"command": PYTHON_BIN, "args": [str(PROJECT_DIR / "push_server.py")]},
    market_mcp,
]

# The full set of MCP servers for the researcher: Fetch, Brave Search and Memory


def researcher_mcp_server_params(name: str):
    return [
        {"command": PYTHON_BIN, "args": ["-m", "mcp_server_fetch"]},
        {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": brave_env,
        },
        {
            "command": "npx",
            "args": ["-y", "mcp-memory-libsql"],
            "env": {"LIBSQL_URL": f"file:{PROJECT_DIR}/memory/{name}.db"},
        },
    ]
