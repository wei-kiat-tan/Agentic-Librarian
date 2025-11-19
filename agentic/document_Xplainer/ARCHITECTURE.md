# Documentation Explainer Agent Team - Architecture Diagram

## System Flow Visualization

```
┌─────────────────────────────────────────────────────────────────────┐
│                                 USER                                 │
│                          (Asks Questions)                            │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 │ Query: "How do I use Claude API?"
                                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    DOCUMENTATION EXPLAINER TEAM                      │
│                     (Main Coordination Layer)                        │
└────────────────────────────────┬────────────────────────────────────┘
                                 │
                                 │ Routes to Agent 1
                                 ▼
         ┌───────────────────────────────────────────────────┐
         │         AGENT 1: ORCHESTRATOR                     │
         │         (Claude Haiku 4.5)                        │
         │                                                   │
         │  Responsibilities:                                │
         │  • Analyze user query intent                      │
         │  • Extract search terms                           │
         │  • Identify documentation topics                  │
         │  • Formulate search strategy                      │
         │  • Create instructions for Agent 2                │
         └─────────────────────┬─────────────────────────────┘
                               │
                               │ Instructions:
                               │ • Search terms: ["Claude", "API", "usage"]
                               │ • Doc site: "docs.anthropic.com"
                               │ • Goal: "Find API usage instructions"
                               ▼
         ┌───────────────────────────────────────────────────┐
         │         AGENT 2: WEB NAVIGATOR                    │
         │         (Claude Haiku 4.5)                        │
         │                                                   │
         │  Responsibilities:                                │
         │  • Search documentation websites                  │
         │  • Navigate web pages                             │
         │  • Interact with search bars                      │
         │  • Extract relevant information                   │
         │  • Handle various UI/UX formats                   │
         │  • Parse tables and structured data               │
         └─────────────────────┬─────────────────────────────┘
                               │
                               │ Extracted Information:
                               │ • API endpoint details
                               │ • Authentication methods
                               │ • Code examples
                               │ • Parameter descriptions
                               ▼
         ┌───────────────────────────────────────────────────┐
         │         AGENT 1: ORCHESTRATOR                     │
         │         (Synthesis Phase)                         │
         │                                                   │
         │  Responsibilities:                                │
         │  • Process extracted information                  │
         │  • Synthesize coherent response                   │
         │  • Format with tables/code blocks                 │
         │  • Add examples and clarifications                │
         │  • Store in conversation history                  │
         └─────────────────────┬─────────────────────────────┘
                               │
                               │ Final Response
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                                 USER                                 │
│                       (Receives Response)                            │
└─────────────────────────────────────────────────────────────────────┘
                               │
                               │ Follow-up: "Can you show an example?"
                               ▼
         ┌───────────────────────────────────────────────────┐
         │         AGENT 1: ORCHESTRATOR                     │
         │         (Context-Aware Processing)                │
         │                                                   │
         │  Uses Conversation History:                       │
         │  • Previous query about Claude API                │
         │  • Previous response with details                 │
         │  • Determines if new search needed                │
         │  • Provides contextual answer or                  │
         │  • Triggers new Agent 2 search                    │
         └─────────────────────┬─────────────────────────────┘
                               │
                               │ Contextual Response
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                                 USER                                 │
│                       (Receives Follow-up)                           │
└─────────────────────────────────────────────────────────────────────┘
```

## Detailed Component Breakdown

### Agent 1: Orchestrator
```
┌─────────────────────────────────────────┐
│  AGENT 1 INTERNAL STRUCTURE             │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Query Analysis Engine         │   │
│  │   • Intent extraction           │   │
│  │   • Search term identification  │   │
│  │   • Documentation site detection│   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Agent 2 Instruction Generator │   │
│  │   • Create search parameters    │   │
│  │   • Define extraction goals     │   │
│  │   • Format instructions         │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Response Synthesizer          │   │
│  │   • Process Agent 2 data        │   │
│  │   • Format output (tables, etc) │   │
│  │   • Add examples and clarity    │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Conversation Manager          │   │
│  │   • Track message history       │   │
│  │   • Handle follow-ups           │   │
│  │   • Maintain context            │   │
│  └─────────────────────────────────┘   │
│                                         │
│  Model: claude-haiku-4-5-20251001       │
│  Max Tokens: 2000-4000                  │
└─────────────────────────────────────────┘
```

### Agent 2: Web Navigator
```
┌─────────────────────────────────────────┐
│  AGENT 2 INTERNAL STRUCTURE             │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Search Engine                 │   │
│  │   • Execute web searches        │   │
│  │   • Navigate to doc sites       │   │
│  │   • Follow documentation links  │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   UI Interaction Simulator      │   │
│  │   • Search bar interaction      │   │
│  │   • Menu navigation             │   │
│  │   • Handle various UX formats   │   │
│  │   • Simple to complex layouts   │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Information Extractor         │   │
│  │   • Parse page content          │   │
│  │   • Extract code examples       │   │
│  │   • Process tables              │   │
│  │   • Structure data              │   │
│  └─────────────────────────────────┘   │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │   Retry & Error Handler         │   │
│  │   • Implement retry logic       │   │
│  │   • Handle search failures      │   │
│  │   • Manage rate limits          │   │
│  └─────────────────────────────────┘   │
│                                         │
│  Model: claude-haiku-4-5-20251001       │
│  Max Tokens: 4000                       │
│  Max Retries: 3                         │
└─────────────────────────────────────────┘
```

## Message Flow Diagram

```
USER INPUT → process_query()
              ↓
         ┌────────────────────┐
         │ Agent 1            │
         │ process_user_query()│
         └─────────┬──────────┘
                   │ Returns: {
                   │   "search_terms": [...],
                   │   "instructions": "...",
                   │   "doc_site": "..."
                   │ }
                   ▼
         ┌────────────────────┐
         │ Agent 2            │
         │ search_documentation()│
         └─────────┬──────────┘
                   │ Returns: {
                   │   "success": true,
                   │   "extracted_info": "..."
                   │ }
                   ▼
         ┌────────────────────┐
         │ Agent 1            │
         │ synthesize_response()│
         └─────────┬──────────┘
                   │
                   ▼
              FINAL RESPONSE → USER
```

## Follow-up Flow

```
USER FOLLOW-UP → handle_followup()
                   ↓
         ┌────────────────────┐
         │ Agent 1            │
         │ Check context      │
         └─────────┬──────────┘
                   │
                   ├─→ Can answer with context?
                   │   ┌────────────────────┐
                   │   │ Agent 1            │
                   │   │ Generate response  │
                   │   │ using history      │
                   │   └─────────┬──────────┘
                   │             │
                   │             ▼
                   │        RESPONSE → USER
                   │
                   └─→ Need new search?
                       ┌────────────────────┐
                       │ Trigger full       │
                       │ process_query()    │
                       │ cycle              │
                       └─────────┬──────────┘
                                 │
                                 ▼
                            RESPONSE → USER
```

## Data Structures

### Message Object
```python
Message {
    role: "user" | "assistant"
    content: str
    sender: AgentRole.ORCHESTRATOR | AgentRole.WEB_NAVIGATOR
    timestamp: float
    metadata: {
        "search_result": {...},
        "query_type": str,
        ...
    }
}
```

### Query Analysis Result
```python
QueryAnalysis {
    "analysis": str,           # Brief analysis
    "search_needed": bool,     # Whether to search
    "search_terms": [str],     # Key terms
    "documentation_site": str, # Target site
    "instructions_for_agent2": str  # Detailed instructions
}
```

### Search Result
```python
SearchResult {
    "success": bool,
    "search_query": str,
    "extracted_information": str,
    "timestamp": float,
    "error": str | None
}
```

## Interaction Patterns

### Pattern 1: Simple Query
```
User: "What is Claude?"
→ Agent 1: Analyze → "Need general info about Claude"
→ Agent 2: Search → Extract info from docs
→ Agent 1: Synthesize → "Claude is an AI assistant..."
→ User: Receives answer
```

### Pattern 2: Technical Query
```
User: "Show me Claude API parameters"
→ Agent 1: Analyze → "Need API reference details"
→ Agent 2: Search → Extract parameter table
→ Agent 1: Synthesize → Format as clear table
→ User: Receives formatted table
```

### Pattern 3: Multi-turn Conversation
```
User: "What is streaming?"
→ Full cycle → Response about streaming
User: "Show example"
→ Agent 1: Use context → Provide example
User: "What about errors?"
→ Agent 1: Context or new search → Error handling info
```

## Performance Characteristics

```
┌────────────────────────┬──────────┬─────────────┐
│ Operation              │ Time     │ API Calls   │
├────────────────────────┼──────────┼─────────────┤
│ Query Analysis         │ 1-3s     │ 1           │
│ Documentation Search   │ 2-5s     │ 1           │
│ Response Synthesis     │ 1-3s     │ 1           │
│ Total (First Query)    │ 5-10s    │ 3           │
│ Follow-up (Context)    │ 1-3s     │ 1           │
│ Follow-up (New Search) │ 5-10s    │ 3           │
└────────────────────────┴──────────┴─────────────┘
```

---

This architecture provides:
- ✅ Clear separation of concerns
- ✅ Efficient agent coordination
- ✅ Context-aware processing
- ✅ Scalable design
- ✅ Robust error handling
- ✅ Fast response times
