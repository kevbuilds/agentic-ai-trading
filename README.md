# 🤖 Autonomous AI Trading Simulation

An equity trading simulation featuring 4 autonomous AI traders powered by the OpenAI Agents SDK and MCP (Model Context Protocol) servers. Watch as Warren, George, Ray, and Cathie manage their portfolios with different investment strategies inspired by legendary investors.

![Trading Simulation](https://img.shields.io/badge/AI-Trading-blue) ![Python](https://img.shields.io/badge/python-3.12+-blue.svg) ![MCP](https://img.shields.io/badge/MCP-Powered-green)

## 🌟 Features

- **4 Autonomous Traders** - Each with unique investment strategies:
  - **Warren** (Patience) - Value investing inspired by Warren Buffett
  - **George** (Bold) - Macro trading inspired by George Soros  
  - **Ray** (Systematic) - Risk parity inspired by Ray Dalio
  - **Cathie** (Crypto) - Innovation focus inspired by Cathie Wood

- **Real-time Market Data** - Integration with Polygon.io API (or simulated data)
- **MCP Server Integration** - Leveraging 44+ tools across multiple MCP servers:
  - Market data and financial information
  - Web search and research capabilities
  - Persistent memory and knowledge graphs
  - Push notifications for trade alerts
  - Account management and transactions

- **Beautiful Web UI** - Built with Gradio to monitor:
  - Portfolio performance over time
  - Real-time trade logs and agent thinking
  - Holdings and transaction history
  - Profit/Loss tracking

- **Multiple AI Models** - Support for:
  - OpenAI GPT-4o-mini (default)
  - DeepSeek V3
  - Google Gemini 2.5 Flash
  - xAI Grok 3 Mini

## 🎯 Project Structure

```
agentic-ai-trading/
├── trading_floor.py        # Scheduler that runs traders periodically
├── traders.py              # Trader agent implementation
├── accounts.py             # Account and transaction management
├── app.py                  # Gradio UI for monitoring
├── reset.py                # Reset traders with initial strategies
├── mcp_params.py           # MCP server configurations
├── templates.py            # Agent instruction templates
├── tracers.py              # Custom tracing for agent activity
├── database.py             # SQLite database operations
├── market.py               # Market data fetching (Polygon.io)
├── util.py                 # UI utilities and styling
├── accounts_server.py      # MCP server for account operations
├── accounts_client.py      # MCP client for accounts
├── market_server.py        # MCP server for market data
├── push_server.py          # MCP server for push notifications
├── accounts.db             # SQLite database (auto-generated)
└── pyproject.toml          # Project dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Node.js (for MCP servers)
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kevbuilds/agentic-ai-trading.git
   cd agentic-ai-trading
   ```

2. **Install uv package manager**
   ```bash
   python3 -m pip install uv
   ```

3. **Create virtual environment**
   ```bash
   python3 -m uv venv
   ```

4. **Install dependencies**
   ```bash
   python3 -m uv pip install --python .venv/bin/python \
     anthropic gradio httpx "mcp[cli]" mcp-server-fetch openai \
     openai-agents plotly polygon-api-client pydantic python-dotenv \
     requests ipykernel jupyter pytest ruff
   ```

5. **Set up environment variables**
   
   Copy `env.example` to `.env` and fill in your API keys:
   ```bash
   cp env.example .env
   ```

   Then edit `.env` with your favorite text editor and add:

   Required API keys:
   - `OPENAI_API_KEY` - Your OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
   - `BRAVE_API_KEY` - For web search ([Get one here](https://brave.com/search/api/))
   - `POLYGON_API_KEY` - For market data ([Get one here](https://polygon.io/))

   Optional API keys:
   - `PUSHOVER_USER` and `PUSHOVER_TOKEN` - For push notifications
   - `DEEPSEEK_API_KEY` - For DeepSeek model
   - `GOOGLE_API_KEY` - For Gemini model
   - `GROK_API_KEY` - For Grok model

6. **Initialize the traders**
   ```bash
   source .venv/bin/activate
   python reset.py
   ```

### Running the Simulation

1. **Start the UI** (in one terminal):
   ```bash
   source .venv/bin/activate
   python app.py
   ```
   This will open a browser window with the trading dashboard at http://127.0.0.1:7860

2. **Start the trading floor** (in another terminal):
   ```bash
   source .venv/bin/activate
   python trading_floor.py
   ```
   This runs the traders immediately, then repeats every 60 minutes (configurable)

## ⚙️ Configuration

You can customize the behavior by setting these environment variables in your `.env` file:

- `RUN_EVERY_N_MINUTES=60` - How often traders make decisions (default: 60)
- `RUN_EVEN_WHEN_MARKET_IS_CLOSED=False` - Run even outside market hours
- `USE_MANY_MODELS=False` - Use multiple AI models (DeepSeek, Gemini, Grok)
- `POLYGON_PLAN=free` - Your Polygon plan: `free`, `paid`, or `realtime`

## 🎮 How It Works

### The Trading Loop

Each trader operates on a cycle:

1. **Research Phase** - Uses MCP tools to:
   - Search financial news via Brave Search
   - Fetch company data and fundamentals
   - Check market conditions
   - Store insights in knowledge graph

2. **Analysis Phase** - The trader:
   - Reviews its portfolio and strategy
   - Analyzes market data
   - Considers risk and diversification
   - Makes investment decisions

3. **Execution Phase** - The trader:
   - Buys or sells shares based on strategy
   - Records rationale for each trade
   - Updates portfolio and sends notifications
   - Logs all activity for monitoring

4. **Rebalancing** - On alternate runs, traders:
   - Review existing positions
   - Consider portfolio rebalancing
   - Can modify their investment strategy

### Agent Architecture

The system uses a hierarchical agent structure:

- **Trader Agents** - Main decision makers with access to:
  - Market data tools
  - Account management tools
  - Push notification tools
  - Researcher agent (as a tool)

- **Researcher Agent** - Specialized for research with:
  - Web search (Brave Search MCP)
  - Web scraping (Fetch MCP)
  - Knowledge graph (Memory MCP)

### MCP Servers

The project leverages these MCP servers:

1. **Custom MCP Servers** (included):
   - `accounts_server.py` - Account operations (buy/sell/balance)
   - `market_server.py` - Market data (backup for free tier)
   - `push_server.py` - Push notifications

2. **External MCP Servers** (auto-installed):
   - `mcp-server-fetch` - Web page fetching
   - `@modelcontextprotocol/server-brave-search` - Web search
   - `mcp-memory-libsql` - Knowledge graph storage
   - `mcp_polygon` - Real-time market data (if paid plan)

## 📊 Monitoring

The Gradio UI provides real-time monitoring of:

- **Portfolio Value Chart** - Track each trader's performance over time
- **Trade Logs** - See agent reasoning and decision-making in real-time
- **Holdings Table** - Current stock positions
- **Transaction History** - All buys and sells with rationale
- **Profit/Loss** - Running P&L for each trader

The UI updates every 2 minutes for portfolio data and every 0.5 seconds for logs.

## 🔒 Important Notes

### API Costs

⚠️ **This simulation uses AI APIs that cost money!** 

- The traders run in a loop and make API calls every hour (or as configured)
- Each run involves multiple LLM calls for research and decision-making
- Monitor your API usage dashboards closely
- Consider using shorter run intervals for testing
- Stop the `trading_floor.py` process when not actively monitoring

### Market Data

- **Free Polygon tier** - End-of-day data only (15+ min delayed)
- **Paid Polygon tier** - Real-time or delayed data based on your plan
- **No Polygon key** - Falls back to random prices (for testing only)

### Production Use

This is a **simulation for educational purposes**. Do not use this for real trading without:
- Proper risk management
- Regulatory compliance
- Extensive testing and validation
- Professional financial advice

## 🛠️ Development

### Running Tests

```bash
source .venv/bin/activate
pytest
```

### Resetting the Simulation

To start fresh with initial balances and strategies:

```bash
source .venv/bin/activate
python reset.py
```

This resets all traders to $10,000 and their original strategies.

### Customizing Traders

Edit `reset.py` to modify trader strategies, or let traders evolve their own strategies over time using the `change_strategy` tool.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Some areas for improvement:

- Additional MCP server integrations
- More sophisticated trading strategies
- Backtesting capabilities
- Risk management tools
- Portfolio optimization algorithms
- Additional trader personas

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with the [OpenAI Agents SDK](https://github.com/openai/openai-python)
- Powered by [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- Market data from [Polygon.io](https://polygon.io/)
- UI built with [Gradio](https://gradio.app/)
- Inspired by legendary investors: Warren Buffett, George Soros, Ray Dalio, and Cathie Wood

## 📧 Contact

Kevin - [@kevbuilds](https://github.com/kevbuilds)

Project Link: [https://github.com/kevbuilds/agentic-ai-trading](https://github.com/kevbuilds/agentic-ai-trading)

---

**Disclaimer**: This is a simulation for educational purposes only. The strategies and trades executed are by AI agents and should not be considered as financial advice. Always consult with qualified financial professionals before making investment decisions.

