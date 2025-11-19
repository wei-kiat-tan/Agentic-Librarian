# Documentation Explainer Agent Team 📚

A sophisticated multi-agent system built with Python and Claude Haiku 4.5 that helps users search, understand, and extract information from documentation websites.

## 🎯 Overview

This system features **two specialized AI agents** working together:

- **Agent 1 (Orchestrator)**: Processes user queries, coordinates searches, and synthesizes responses
- **Agent 2 (Web Navigator)**: Searches documentation sites, interacts with web pages, and extracts information

Both agents use **Claude Haiku 4.5** (`claude-haiku-4-5-20251001`) for efficient text generation and can handle:
- Simple and complex table formatting (including merged cells)
- Code snippets and examples
- Structured documentation navigation
- Multi-turn conversations with context retention

## 🏗️ Architecture

```
User Query
    ↓
┌─────────────────────────────────────────────────┐
│  Agent 1: Orchestrator                          │
│  • Analyzes user intent                         │
│  • Extracts search terms                        │
│  • Creates instructions for Agent 2             │
└─────────────────────────────────────────────────┘
    ↓ (Instructions)
┌─────────────────────────────────────────────────┐
│  Agent 2: Web Navigator                         │
│  • Searches documentation sites                 │
│  • Interacts with search bars and UI elements   │
│  • Extracts relevant information                │
│  • Handles various UI/UX formats                │
└─────────────────────────────────────────────────┘
    ↓ (Extracted Information)
┌─────────────────────────────────────────────────┐
│  Agent 1: Orchestrator                          │
│  • Synthesizes final response                   │
│  • Formats information clearly                  │
│  • Handles follow-up questions                  │
└─────────────────────────────────────────────────┘
    ↓
User Response
```

## 🚀 Features

### Agent 1 Capabilities
- ✅ User query analysis and intent extraction
- ✅ Search strategy formulation
- ✅ Response synthesis and formatting
- ✅ Follow-up query handling with context
- ✅ Table generation (simple and complex)
- ✅ Conversation history management

### Agent 2 Capabilities
- ✅ Web documentation search
- ✅ Search bar interaction
- ✅ Navigation of various UI/UX formats (simple to complex)
- ✅ Information extraction from:
  - Text documentation
  - API references
  - Code examples
  - Tables and structured data
  - Interactive components
- ✅ Content parsing and structuring

## 📋 Prerequisites

- Python 3.8 or higher
- Anthropic API key
- Internet connection (for documentation searches)

## 🔧 Installation

1. **Clone or download the files:**
   ```bash
   # You should have these files:
   # - doc_explainer_agents.py (main agent system)
   # - interactive_cli.py (CLI interface)
   # - README.md (this file)
   ```

2. **Install required packages:**
   ```bash
   pip install anthropic --break-system-packages
   ```

3. **Set up your API key:**
   
   **Linux/Mac:**
   ```bash
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```
   
   **Windows:**
   ```cmd
   set ANTHROPIC_API_KEY=your-api-key-here
   ```
   
   Or add it to your `.bashrc`, `.zshrc`, or system environment variables for persistence.

## 💻 Usage

### Interactive CLI Mode (Recommended)

Start the interactive command-line interface:

```bash
python interactive_cli.py
```

This provides a user-friendly interface with commands:

```
Available Commands:
  help, h, ?        - Show help message
  clear, cls        - Clear the screen
  history           - Show conversation history
  summary           - Show session summary
  new, restart      - Start a new session
  exit, quit, q     - Exit the program
```

**Example Session:**
```
💬 You: How do I authenticate with the Anthropic API?

🔍 Agent 1 is analyzing your query...
🌐 Agent 2 is searching documentation...

📖 RESPONSE:
----------------------------------------------------------------------
To authenticate with the Anthropic API, you need to...
[detailed response]
----------------------------------------------------------------------

💬 You: Can you show me a Python example?

🔍 Agent 1 is processing your follow-up...

📖 RESPONSE:
----------------------------------------------------------------------
Here's a Python example:
[code example]
----------------------------------------------------------------------
```

### Programmatic Usage

You can also use the agent team programmatically in your own Python scripts:

```python
from doc_explainer_agents import DocumentationExplainerTeam

# Initialize the team
team = DocumentationExplainerTeam(api_key="your-api-key")

# Process a query
response = team.process_query("How do I use the Claude API for streaming?")
print(response)

# Handle follow-ups
followup = team.handle_followup("What parameters are available?")
print(followup)

# Get session summary
summary = team.get_session_summary()
print(summary)
```

## 📖 Example Use Cases

### 1. API Documentation Queries
```
Query: "Explain the parameters for Claude's messages API"
→ Agent 2 searches Anthropic documentation
→ Extracts parameter definitions, types, and examples
→ Agent 1 formats into clear explanation with tables
```

### 2. Framework Documentation
```
Query: "How do I set up React hooks?"
→ Agent 2 navigates React documentation
→ Finds hook setup instructions and examples
→ Agent 1 provides step-by-step guide with code
```

### 3. Library Usage
```
Query: "Show me how to use pandas DataFrame groupby"
→ Agent 2 searches pandas documentation
→ Extracts method signatures and examples
→ Agent 1 creates comprehensive guide with examples
```

### 4. Multi-turn Conversations
```
Query 1: "What is FastAPI?"
Response: [Overview of FastAPI]

Query 2: "How do I create a POST endpoint?"
Response: [Uses context from Query 1, provides specific example]

Query 3: "What about async support?"
Response: [Builds on previous context]
```

## 🔍 How It Works

### Query Processing Flow

1. **User Input** → Agent 1 receives query

2. **Analysis Phase** (Agent 1)
   - Extracts key topics and search terms
   - Identifies documentation domain
   - Determines search strategy

3. **Search Phase** (Agent 2)
   - Executes web documentation search
   - Navigates to relevant pages
   - Interacts with search bars/navigation
   - Extracts information from various formats

4. **Synthesis Phase** (Agent 1)
   - Processes extracted information
   - Formats response appropriately
   - Adds tables, code blocks as needed
   - Returns clear, user-friendly answer

5. **Follow-up Handling** (Agent 1)
   - Uses conversation context
   - Determines if new search needed
   - Provides consistent, contextual responses

## 🎨 Output Formatting

The agents can generate:

- **Plain text explanations**
- **Code blocks with syntax**
- **Simple tables:**
  ```
  | Parameter | Type   | Required |
  |-----------|--------|----------|
  | model     | string | Yes      |
  | messages  | array  | Yes      |
  ```

- **Complex tables with merged cells:**
  ```
  | Category    | Details                          |
  |-------------|----------------------------------|
  | Basic       | • Parameter 1                    |
  |             | • Parameter 2                    |
  | Advanced    | • Parameter 3 (nested table)     |
  |             | • Parameter 4                    |
  ```

- **Structured lists and hierarchies**
- **Step-by-step instructions**
- **Examples and demonstrations**

## 🔒 Security & Privacy

- API keys are loaded from environment variables
- No hardcoded credentials in code
- Conversation history stored only in memory (session-based)
- No data persistence between sessions

## ⚙️ Configuration

### Model Configuration
Both agents use Claude Haiku 4.5. To modify:

```python
# In doc_explainer_agents.py
class Agent1Orchestrator:
    def __init__(self, api_key: str):
        self.model = "claude-haiku-4-5-20251001"  # Change here

class Agent2WebNavigator:
    def __init__(self, api_key: str):
        self.model = "claude-haiku-4-5-20251001"  # Change here
```

### Token Limits
Adjust max_tokens in the create() calls:

```python
response = self.client.messages.create(
    model=self.model,
    max_tokens=4000,  # Increase for longer responses
    system=system_prompt,
    messages=messages
)
```

### Retry Logic
Agent 2 has configurable retry attempts:

```python
class Agent2WebNavigator:
    def __init__(self, api_key: str):
        self.max_retries = 3  # Change retry attempts
```

## 🐛 Troubleshooting

### Issue: "ANTHROPIC_API_KEY not set"
**Solution:** Set the environment variable:
```bash
export ANTHROPIC_API_KEY='your-key'
```

### Issue: Import errors
**Solution:** Install the Anthropic package:
```bash
pip install anthropic --break-system-packages
```

### Issue: Agent can't find information
**Solution:** Try:
- Rephrasing your query with more specific terms
- Providing the documentation site URL explicitly
- Using follow-up questions to narrow the search

### Issue: Slow responses
**Solution:** 
- Claude Haiku 4.5 is optimized for speed
- Network latency may affect searches
- Complex queries naturally take longer

## 📊 Performance

- **Agent 1 (Orchestrator):** ~1-3 seconds per operation
- **Agent 2 (Web Navigator):** ~2-5 seconds for search and extraction
- **Full query cycle:** ~5-10 seconds
- **Follow-up queries:** ~1-3 seconds (when no new search needed)

## 🔮 Future Enhancements

Potential improvements:
- [ ] Add web scraping capabilities for direct page access
- [ ] Implement caching for frequently searched topics
- [ ] Add support for multiple documentation sites in one query
- [ ] Include screenshot/visual analysis capabilities
- [ ] Add export functionality (save conversations)
- [ ] Implement parallel searches for complex queries
- [ ] Add custom prompt templates for specific doc types

## 📝 License

This is example code for educational and development purposes.

## 🤝 Contributing

To extend this system:

1. **Add new capabilities to Agent 2:**
   - Modify `search_documentation()` for enhanced search
   - Add methods for specific documentation platforms

2. **Enhance Agent 1's synthesis:**
   - Update system prompts for better formatting
   - Add domain-specific response templates

3. **Add new agent roles:**
   - Create additional agent classes
   - Update coordination in `DocumentationExplainerTeam`

## 📞 Support

For issues related to:
- **Anthropic API:** Check [Anthropic Documentation](https://docs.anthropic.com)
- **Claude Models:** See [Model Overview](https://docs.anthropic.com/en/docs/models-overview)
- **This Code:** Review the inline comments and docstrings

## 🎓 Learning Resources

- [Anthropic API Documentation](https://docs.anthropic.com)
- [Claude Model Guide](https://docs.anthropic.com/en/docs/about-claude/models)
- [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

---

**Built with Claude Haiku 4.5** 🚀

For questions or suggestions, please refer to the inline documentation in the source code.
