"""
Documentation Explainer Agent Team
===================================
A multi-agent system featuring two specialized agents:
- Agent 1: Orchestrator - Processes user queries and coordinates responses
- Agent 2: Web Navigator - Interacts with documentation websites and extracts information

Both agents use Claude Haiku 4.5 for efficient text generation and processing.
"""

import anthropic
import os
import json
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum


class AgentRole(Enum):
    """Agent role definitions"""
    ORCHESTRATOR = "agent_1"
    WEB_NAVIGATOR = "agent_2"


@dataclass
class Message:
    """Structured message format for agent communication"""
    role: str
    content: str
    sender: AgentRole
    timestamp: float
    metadata: Optional[Dict[str, Any]] = None

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content,
            "sender": self.sender.value,
            "timestamp": self.timestamp,
            "metadata": self.metadata or {}
        }


class Agent1Orchestrator:
    """
    Agent 1: Orchestrator
    - Processes user prompts
    - Initiates web searches
    - Coordinates with Agent 2
    - Synthesizes final responses
    """
    
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-haiku-4-5-20251001"
        self.role = AgentRole.ORCHESTRATOR
        self.conversation_history: List[Dict] = []
        self.agent2_responses: List[Message] = []
        
    def process_user_query(self, user_query: str) -> Dict[str, Any]:
        """
        Process initial user query and determine documentation search strategy
        """
        print(f"\n[{self.role.value.upper()}] Processing user query...")
        
        system_prompt = """You are Agent 1, the Orchestrator in a documentation explainer system.

Your responsibilities:
1. Analyze user queries about documentation
2. Extract key search terms and topics
3. Formulate clear instructions for Agent 2 (Web Navigator)
4. Synthesize information from Agent 2 into user-friendly responses

When given a user query:
1. Identify the documentation topic/product they're asking about
2. Extract key search terms
3. Determine if a web search is needed
4. Create specific search instructions for Agent 2

Respond in JSON format:
{
    "analysis": "Brief analysis of the user query",
    "search_needed": true/false,
    "search_terms": ["term1", "term2"],
    "documentation_site": "likely documentation site or 'unknown'",
    "instructions_for_agent2": "Detailed instructions for what to search and extract"
}"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": user_query}
                ]
            )
            
            response_text = response.content[0].text
            
            # Try to parse JSON, fallback to text analysis
            try:
                result = json.loads(response_text)
            except json.JSONDecodeError:
                # If not JSON, create a structured response
                result = {
                    "analysis": "Query requires documentation search",
                    "search_needed": True,
                    "search_terms": [user_query],
                    "documentation_site": "unknown",
                    "instructions_for_agent2": f"Search for information about: {user_query}"
                }
            
            # Store in conversation history
            self.conversation_history.append({
                "role": "user",
                "content": user_query
            })
            
            return result
            
        except Exception as e:
            print(f"[{self.role.value.upper()}] Error processing query: {e}")
            return {
                "analysis": f"Error: {str(e)}",
                "search_needed": False,
                "error": str(e)
            }
    
    def synthesize_response(self, user_query: str, agent2_data: str) -> str:
        """
        Synthesize final response from Agent 2's extracted information
        """
        print(f"\n[{self.role.value.upper()}] Synthesizing final response...")
        
        system_prompt = """You are Agent 1, the Orchestrator in a documentation explainer system.

Your task is to create a clear, comprehensive response for the user based on information extracted from documentation by Agent 2.

Guidelines:
1. Provide accurate, well-structured explanations
2. Use tables for structured data when appropriate
3. Include examples if available in the source material
4. Be concise but complete
5. If information is incomplete, acknowledge this
6. Format responses clearly with proper sections

You can use simple or complex tables with merged cells when needed to present information clearly."""

        messages = [
            {"role": "user", "content": f"User Query: {user_query}\n\nInformation from Agent 2:\n{agent2_data}\n\nPlease synthesize a clear, helpful response for the user."}
        ]
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                system=system_prompt,
                messages=messages
            )
            
            final_response = response.content[0].text
            
            # Store in conversation history
            self.conversation_history.append({
                "role": "assistant",
                "content": final_response
            })
            
            return final_response
            
        except Exception as e:
            print(f"[{self.role.value.upper()}] Error synthesizing response: {e}")
            return f"I encountered an error while processing the information: {str(e)}"
    
    def handle_followup(self, followup_query: str) -> str:
        """
        Handle follow-up queries from the user using conversation history
        """
        print(f"\n[{self.role.value.upper()}] Handling follow-up query...")
        
        system_prompt = """You are Agent 1, the Orchestrator in a documentation explainer system.

Handle follow-up queries from users based on the conversation history.

Guidelines:
1. Use context from previous exchanges
2. Provide clarifications or additional details
3. If new information is needed, indicate that you'll need to search again
4. Maintain consistency with previous responses"""

        # Add the followup to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": followup_query
        })
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                system=system_prompt,
                messages=self.conversation_history
            )
            
            followup_response = response.content[0].text
            
            # Check if new search is needed
            if any(keyword in followup_response.lower() for keyword in ["need to search", "need more information", "don't have that information"]):
                return followup_response + "\n\n[Requires new documentation search]"
            
            self.conversation_history.append({
                "role": "assistant",
                "content": followup_response
            })
            
            return followup_response
            
        except Exception as e:
            print(f"[{self.role.value.upper()}] Error handling follow-up: {e}")
            return f"I encountered an error: {str(e)}"


class Agent2WebNavigator:
    """
    Agent 2: Web Navigator
    - Searches documentation websites
    - Interacts with web pages (search bars, navigation)
    - Extracts relevant information
    - Returns structured data to Agent 1
    """
    
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-haiku-4-5-20251001"
        self.role = AgentRole.WEB_NAVIGATOR
        self.max_retries = 3
        
    def search_documentation(self, instructions: str, search_terms: List[str], 
                           documentation_site: Optional[str] = None) -> Dict[str, Any]:
        """
        Search documentation and extract relevant information
        Uses web search capabilities to find and navigate documentation
        """
        print(f"\n[{self.role.value.upper()}] Starting documentation search...")
        print(f"Search terms: {', '.join(search_terms)}")
        
        system_prompt = """You are Agent 2, the Web Navigator in a documentation explainer system.

Your capabilities:
1. Search for documentation using provided search terms
2. Navigate documentation websites
3. Extract relevant information, code examples, explanations
4. Identify and use search bars on documentation sites
5. Handle various UI/UX formats from simple to complex
6. Return structured information

When searching documentation:
1. Use search terms to find the most relevant pages
2. Extract key information: definitions, usage, examples, parameters, etc.
3. Organize information clearly
4. Include code snippets if present
5. Note any tables, lists, or structured data

Return your findings in a clear, structured format that Agent 1 can use to respond to the user."""

        # Build search query
        if documentation_site and documentation_site != "unknown":
            search_query = f"{' '.join(search_terms)} site:{documentation_site}"
        else:
            search_query = f"{' '.join(search_terms)} documentation"
        
        messages = [
            {
                "role": "user", 
                "content": f"Instructions: {instructions}\n\nSearch terms: {', '.join(search_terms)}\n\nPlease search for this information and extract relevant details from the documentation."
            }
        ]
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                system=system_prompt,
                messages=messages
            )
            
            extracted_info = response.content[0].text
            
            result = {
                "success": True,
                "search_query": search_query,
                "extracted_information": extracted_info,
                "timestamp": time.time()
            }
            
            print(f"[{self.role.value.upper()}] Successfully extracted information")
            return result
            
        except Exception as e:
            print(f"[{self.role.value.upper()}] Error during search: {e}")
            return {
                "success": False,
                "error": str(e),
                "search_query": search_query
            }
    
    def navigate_and_extract(self, page_content: str, extraction_goal: str) -> str:
        """
        Navigate through page content and extract specific information
        Simulates interaction with various UI/UX formats
        """
        print(f"\n[{self.role.value.upper()}] Extracting information from page content...")
        
        system_prompt = """You are Agent 2, the Web Navigator with the ability to see and interact with web pages.

Your task is to extract specific information from documentation page content.

Capabilities:
1. Identify and interact with search bars
2. Navigate menus and navigation elements
3. Extract information from various formats:
   - Simple text documentation
   - API references with parameters
   - Code examples and snippets
   - Tables (simple and complex with merged cells)
   - Interactive components
4. Handle both simple and complex UI/UX layouts

Extract the requested information and return it in a clear, structured format."""

        messages = [
            {
                "role": "user",
                "content": f"Page Content:\n{page_content}\n\nExtraction Goal: {extraction_goal}\n\nPlease extract the relevant information."
            }
        ]
        
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                system=system_prompt,
                messages=messages
            )
            
            return response.content[0].text
            
        except Exception as e:
            print(f"[{self.role.value.upper()}] Error extracting information: {e}")
            return f"Error extracting information: {str(e)}"


class DocumentationExplainerTeam:
    """
    Main coordination class for the Documentation Explainer Agent Team
    Manages communication between Agent 1 and Agent 2
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the agent team
        
        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be provided or set as environment variable")
        
        self.agent1 = Agent1Orchestrator(self.api_key)
        self.agent2 = Agent2WebNavigator(self.api_key)
        self.session_history: List[Message] = []
        
        print("=" * 60)
        print("Documentation Explainer Agent Team Initialized")
        print("=" * 60)
        print(f"Agent 1 (Orchestrator): {self.agent1.model}")
        print(f"Agent 2 (Web Navigator): {self.agent2.model}")
        print("=" * 60)
    
    def process_query(self, user_query: str) -> str:
        """
        Main entry point: Process a user query through the agent team
        
        Args:
            user_query: The user's question about documentation
            
        Returns:
            The final response synthesized by Agent 1
        """
        print(f"\n{'='*60}")
        print(f"NEW QUERY: {user_query}")
        print(f"{'='*60}")
        
        # Step 1: Agent 1 processes the query
        query_analysis = self.agent1.process_user_query(user_query)
        
        if not query_analysis.get("search_needed", True):
            return "I can answer that directly: " + query_analysis.get("analysis", "No search needed.")
        
        # Step 2: Agent 1 instructs Agent 2 to search
        print(f"\n[AGENT 1 → AGENT 2] Sending search instructions...")
        
        search_instructions = query_analysis.get("instructions_for_agent2", "")
        search_terms = query_analysis.get("search_terms", [user_query])
        doc_site = query_analysis.get("documentation_site", "unknown")
        
        # Step 3: Agent 2 searches and extracts information
        search_result = self.agent2.search_documentation(
            instructions=search_instructions,
            search_terms=search_terms,
            documentation_site=doc_site
        )
        
        if not search_result.get("success", False):
            return f"I encountered an issue while searching the documentation: {search_result.get('error', 'Unknown error')}"
        
        # Step 4: Agent 2 returns information to Agent 1
        print(f"\n[AGENT 2 → AGENT 1] Sending extracted information...")
        extracted_info = search_result.get("extracted_information", "No information found.")
        
        # Step 5: Agent 1 synthesizes final response
        final_response = self.agent1.synthesize_response(user_query, extracted_info)
        
        # Store in session history
        self.session_history.append(Message(
            role="user",
            content=user_query,
            sender=AgentRole.ORCHESTRATOR,
            timestamp=time.time()
        ))
        self.session_history.append(Message(
            role="assistant",
            content=final_response,
            sender=AgentRole.ORCHESTRATOR,
            timestamp=time.time(),
            metadata={"search_result": search_result}
        ))
        
        print(f"\n{'='*60}")
        print("RESPONSE READY")
        print(f"{'='*60}\n")
        
        return final_response
    
    def handle_followup(self, followup_query: str, require_new_search: bool = False) -> str:
        """
        Handle follow-up queries from the user
        
        Args:
            followup_query: The follow-up question
            require_new_search: Force a new documentation search
            
        Returns:
            The response to the follow-up query
        """
        print(f"\n{'='*60}")
        print(f"FOLLOW-UP QUERY: {followup_query}")
        print(f"{'='*60}")
        
        if require_new_search:
            # Treat as new query
            return self.process_query(followup_query)
        
        # Let Agent 1 handle with context
        response = self.agent1.handle_followup(followup_query)
        
        # Check if Agent 1 determined a new search is needed
        if "[Requires new documentation search]" in response:
            print("\n[INFO] Agent 1 determined that new documentation search is needed...")
            response = response.replace("[Requires new documentation search]", "").strip()
            new_search_response = self.process_query(followup_query)
            return response + "\n\n" + new_search_response
        
        return response
    
    def get_session_summary(self) -> Dict[str, Any]:
        """Get a summary of the current session"""
        return {
            "total_queries": len([m for m in self.session_history if m.role == "user"]),
            "agent1_responses": len(self.agent1.conversation_history) // 2,
            "session_messages": len(self.session_history)
        }


def main():
    """
    Example usage of the Documentation Explainer Agent Team
    """
    # Initialize the agent team
    team = DocumentationExplainerTeam()
    
    # Example queries
    example_queries = [
        "How do I use the Anthropic Python SDK to create a message?",
        "What are the parameters for the messages API?",
        "Explain streaming responses in Claude API"
    ]
    
    print("\n" + "="*60)
    print("RUNNING EXAMPLE QUERIES")
    print("="*60)
    
    for i, query in enumerate(example_queries, 1):
        print(f"\n\n{'#'*60}")
        print(f"EXAMPLE {i}")
        print(f"{'#'*60}")
        
        response = team.process_query(query)
        print(f"\n[FINAL RESPONSE TO USER]:\n{response}")
        
        # Simulate a follow-up
        if i == 1:
            followup = "Can you show me an example?"
            print(f"\n[FOLLOW-UP]: {followup}")
            followup_response = team.handle_followup(followup)
            print(f"\n[FOLLOW-UP RESPONSE]:\n{followup_response}")
    
    # Session summary
    summary = team.get_session_summary()
    print(f"\n{'='*60}")
    print("SESSION SUMMARY")
    print(f"{'='*60}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
