# Quick Start Guide 🚀

Get up and running with the Documentation Explainer Agent Team in 5 minutes!

## Step 1: Install Dependencies ⚙️

```bash
pip install -r requirements.txt --break-system-packages
```

Or manually:
```bash
pip install anthropic --break-system-packages
```

## Step 2: Set Your API Key 🔑

Get your API key from [Anthropic Console](https://console.anthropic.com/)

**Linux/Mac:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

**Windows Command Prompt:**
```cmd
set ANTHROPIC_API_KEY=your-api-key-here
```

**Windows PowerShell:**
```powershell
$env:ANTHROPIC_API_KEY='your-api-key-here'
```

## Step 3: Run the Interactive CLI 💬

```bash
python interactive_cli.py
```

You'll see:
```
======================================================================
          📚 DOCUMENTATION EXPLAINER AGENT TEAM 📚
======================================================================

This system uses two AI agents to help you understand documentation:
  • Agent 1 (Orchestrator): Processes your queries and synthesizes responses
  • Agent 2 (Web Navigator): Searches and extracts information from docs

======================================================================

🔄 Initializing agent team...
✅ Agent team ready!

Type 'help' for available commands, or ask a question about any documentation.

💬 You: 
```

## Step 4: Ask Questions! 🤔

Try these example queries:

### Example 1: Simple Query
```
💬 You: How do I authenticate with the Anthropic API?
```

### Example 2: Technical Details
```
💬 You: Explain the parameters for Claude's messages API
```

### Example 3: Code Examples
```
💬 You: Show me how to use streaming responses in Python
```

### Example 4: Follow-up Questions
```
💬 You: What is Claude's context window?
💬 You: How does it compare to other models?
💬 You: Show me examples of managing long contexts
```

## Available Commands 📋

Once in the CLI, you can use:

- `help` - Show available commands
- `history` - View conversation history
- `summary` - Show session statistics
- `clear` - Clear the screen
- `new` - Start a new conversation
- `exit` - Quit the program

## Programmatic Usage 💻

Want to use it in your own Python scripts?

```python
from doc_explainer_agents import DocumentationExplainerTeam

# Initialize
team = DocumentationExplainerTeam()

# Ask a question
response = team.process_query("How do I use the Claude API?")
print(response)

# Follow-up question
followup = team.handle_followup("Can you show me an example?")
print(followup)
```

## Try Advanced Examples 🎓

Run the advanced examples script:

```bash
python advanced_examples.py
```

This provides an interactive menu with 10 different example scenarios:
1. Basic Query
2. Multi-turn Conversation
3. Technical Documentation
4. Comparison Query
5. Troubleshooting
6. Complex Tables
7. Code Examples
8. Best Practices
9. Specific Feature
10. Contextual Follow-ups

## Troubleshooting 🔧

### "ANTHROPIC_API_KEY not set"
Make sure you've exported/set the environment variable in your current terminal session.

### "Module not found: anthropic"
Run: `pip install anthropic --break-system-packages`

### Slow responses
This is normal - the agents are searching documentation and processing information. Typical response time is 5-10 seconds.

### Can't find information
Try:
- Being more specific with your query
- Rephrasing your question
- Asking follow-up questions to narrow the search

## What Questions Work Best? 💡

The agent team works great with:

✅ **"How do I..." questions**
- "How do I authenticate with the API?"
- "How do I handle errors?"
- "How do I implement streaming?"

✅ **"What is..." questions**
- "What is the context window size?"
- "What are the available models?"
- "What parameters are available?"

✅ **"Show me..." requests**
- "Show me a Python example"
- "Show me how to implement retry logic"
- "Show me the differences between models"

✅ **"Explain..." requests**
- "Explain how tool use works"
- "Explain the rate limits"
- "Explain best practices for prompting"

## Next Steps 📚

1. ✅ Read the full [README.md](README.md) for comprehensive documentation
2. ✅ Explore [advanced_examples.py](advanced_examples.py) for usage patterns
3. ✅ Check [doc_explainer_agents.py](doc_explainer_agents.py) for implementation details
4. ✅ Customize the agents for your specific needs

## Tips for Best Results 🌟

1. **Be specific**: Instead of "Tell me about Claude", try "What are Claude's rate limits?"
2. **Use follow-ups**: Build on previous answers with "Can you show an example?" or "What about error handling?"
3. **Ask for formats**: Request "in a table" or "with code examples" for specific formatting
4. **Clarify context**: Mention the programming language or framework you're using

## Support 💬

- **API Issues**: [Anthropic Documentation](https://docs.anthropic.com)
- **Code Issues**: Check the inline comments in the source files
- **Questions**: Review the [README.md](README.md) for detailed information

---

**Ready to start?** Run `python interactive_cli.py` and ask your first question! 🎉
