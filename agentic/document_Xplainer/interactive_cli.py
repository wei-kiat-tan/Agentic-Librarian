"""
Interactive CLI for Documentation Explainer Agent Team
======================================================
User-friendly command-line interface for querying documentation
"""

import sys
import os
from doc_explainer_agents import DocumentationExplainerTeam


def print_banner():
    """Print welcome banner"""
    print("\n" + "="*70)
    print(" " * 10 + "📚 DOCUMENTATION EXPLAINER AGENT TEAM 📚")
    print("="*70)
    print("\nThis system uses two AI agents to help you understand documentation:")
    print("  • Agent 1 (Orchestrator): Processes your queries and synthesizes responses")
    print("  • Agent 2 (Web Navigator): Searches and extracts information from docs")
    print("\n" + "="*70 + "\n")


def print_help():
    """Print help information"""
    print("\nAvailable Commands:")
    print("  help, h, ?        - Show this help message")
    print("  clear, cls        - Clear the screen")
    print("  history           - Show conversation history")
    print("  summary           - Show session summary")
    print("  new, restart      - Start a new session")
    print("  exit, quit, q     - Exit the program")
    print("\nTo ask a question, simply type it and press Enter.\n")


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_response(response: str, prefix: str = "📖"):
    """Print formatted response"""
    print(f"\n{prefix} RESPONSE:")
    print("-" * 70)
    print(response)
    print("-" * 70 + "\n")


def main():
    """Main interactive CLI loop"""
    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("\n❌ ERROR: ANTHROPIC_API_KEY environment variable not set!")
        print("\nPlease set your API key:")
        print("  Linux/Mac: export ANTHROPIC_API_KEY='your-api-key'")
        print("  Windows:   set ANTHROPIC_API_KEY=your-api-key\n")
        sys.exit(1)
    
    clear_screen()
    print_banner()
    
    # Initialize agent team
    try:
        print("🔄 Initializing agent team...")
        team = DocumentationExplainerTeam(api_key)
        print("✅ Agent team ready!\n")
    except Exception as e:
        print(f"\n❌ Error initializing agent team: {e}\n")
        sys.exit(1)
    
    print("Type 'help' for available commands, or ask a question about any documentation.\n")
    
    # Main interaction loop
    conversation_count = 0
    
    while True:
        try:
            # Get user input
            user_input = input("💬 You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            command = user_input.lower()
            
            if command in ['exit', 'quit', 'q']:
                print("\n👋 Thank you for using Documentation Explainer Agent Team!")
                print("   Goodbye!\n")
                break
            
            elif command in ['help', 'h', '?']:
                print_help()
                continue
            
            elif command in ['clear', 'cls']:
                clear_screen()
                print_banner()
                continue
            
            elif command == 'history':
                print("\n📜 Conversation History:")
                print("-" * 70)
                for i, msg in enumerate(team.agent1.conversation_history, 1):
                    role = "You" if msg["role"] == "user" else "Agent"
                    print(f"\n{i}. [{role}]:")
                    print(f"   {msg['content'][:200]}..." if len(msg['content']) > 200 else f"   {msg['content']}")
                print("-" * 70 + "\n")
                continue
            
            elif command == 'summary':
                summary = team.get_session_summary()
                print("\n📊 Session Summary:")
                print("-" * 70)
                print(f"  Total Queries: {summary['total_queries']}")
                print(f"  Agent 1 Responses: {summary['agent1_responses']}")
                print(f"  Session Messages: {summary['session_messages']}")
                print("-" * 70 + "\n")
                continue
            
            elif command in ['new', 'restart']:
                confirm = input("\n⚠️  Start a new session? This will clear the conversation history. (y/n): ")
                if confirm.lower() in ['y', 'yes']:
                    team = DocumentationExplainerTeam(api_key)
                    conversation_count = 0
                    clear_screen()
                    print_banner()
                    print("✅ New session started!\n")
                continue
            
            # Process as a query
            conversation_count += 1
            
            if conversation_count == 1:
                # First query
                print("\n🔍 Agent 1 is analyzing your query...")
                print("🌐 Agent 2 is searching documentation...")
                response = team.process_query(user_input)
            else:
                # Follow-up query
                print("\n🔍 Agent 1 is processing your follow-up...")
                response = team.handle_followup(user_input)
            
            print_response(response)
            
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted! Type 'exit' to quit or continue asking questions.\n")
            continue
        
        except Exception as e:
            print(f"\n❌ Error: {e}\n")
            continue


if __name__ == "__main__":
    main()
