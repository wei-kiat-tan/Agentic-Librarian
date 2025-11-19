"""
Advanced Examples for Documentation Explainer Agent Team
========================================================
This script demonstrates various advanced usage patterns and capabilities
"""

import os
import json
from doc_explainer_agents import DocumentationExplainerTeam


def example_1_basic_query():
    """Example 1: Basic documentation query"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Documentation Query")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "What are the main features of the Anthropic Messages API?"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_2_followup_conversation():
    """Example 2: Multi-turn conversation with follow-ups"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Multi-turn Conversation")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    # Initial query
    query1 = "How do I use Claude's streaming responses?"
    print(f"\n[Query 1]: {query1}")
    response1 = team.process_query(query1)
    print(f"\n[Response 1]:\n{response1}")
    
    # Follow-up 1
    query2 = "Can you show me a Python example?"
    print(f"\n[Query 2]: {query2}")
    response2 = team.handle_followup(query2)
    print(f"\n[Response 2]:\n{response2}")
    
    # Follow-up 2
    query3 = "What about error handling?"
    print(f"\n[Query 3]: {query3}")
    response3 = team.handle_followup(query3)
    print(f"\n[Response 3]:\n{response3}")
    
    # Session summary
    summary = team.get_session_summary()
    print(f"\nSession Summary:\n{json.dumps(summary, indent=2)}")


def example_3_technical_documentation():
    """Example 3: Technical API documentation query"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Technical API Documentation")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "Explain all the parameters for the Claude messages API create method"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_4_comparison_query():
    """Example 4: Comparison between different approaches"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Comparison Query")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "Compare streaming vs non-streaming responses in Claude API"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_5_troubleshooting():
    """Example 5: Troubleshooting and error handling"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Troubleshooting Query")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "How do I handle rate limits and errors in the Anthropic API?"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_6_complex_tables():
    """Example 6: Query that should result in complex tables"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Complex Table Generation")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "List all Claude models with their specifications and use cases in a table"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_7_code_examples():
    """Example 7: Request for code examples"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Code Examples")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "Show me how to implement retry logic with exponential backoff for Claude API"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_8_best_practices():
    """Example 8: Best practices query"""
    print("\n" + "="*70)
    print("EXAMPLE 8: Best Practices")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "What are the best practices for prompt engineering with Claude?"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_9_specific_feature():
    """Example 9: Specific feature deep dive"""
    print("\n" + "="*70)
    print("EXAMPLE 9: Specific Feature Deep Dive")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    query = "Explain how tool use works in Claude API with detailed examples"
    print(f"\nQuery: {query}")
    
    response = team.process_query(query)
    print(f"\nResponse:\n{response}")


def example_10_contextual_followups():
    """Example 10: Complex contextual follow-ups"""
    print("\n" + "="*70)
    print("EXAMPLE 10: Complex Contextual Follow-ups")
    print("="*70)
    
    team = DocumentationExplainerTeam()
    
    queries = [
        "What is Claude's context window?",
        "How does it compare to other models?",
        "What strategies can I use to work within these limits?",
        "Show me a Python example of implementing context window management"
    ]
    
    for i, query in enumerate(queries, 1):
        print(f"\n[Query {i}]: {query}")
        
        if i == 1:
            response = team.process_query(query)
        else:
            response = team.handle_followup(query)
        
        print(f"\n[Response {i}]:\n{response}")


def run_all_examples():
    """Run all examples"""
    examples = [
        ("Basic Query", example_1_basic_query),
        ("Multi-turn Conversation", example_2_followup_conversation),
        ("Technical Documentation", example_3_technical_documentation),
        ("Comparison Query", example_4_comparison_query),
        ("Troubleshooting", example_5_troubleshooting),
        ("Complex Tables", example_6_complex_tables),
        ("Code Examples", example_7_code_examples),
        ("Best Practices", example_8_best_practices),
        ("Specific Feature", example_9_specific_feature),
        ("Contextual Follow-ups", example_10_contextual_followups)
    ]
    
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#" + " "*15 + "DOCUMENTATION EXPLAINER AGENT TEAM" + " "*19 + "#")
    print("#" + " "*21 + "ADVANCED EXAMPLES" + " "*30 + "#")
    print("#" + " "*68 + "#")
    print("#"*70)
    
    for i, (name, func) in enumerate(examples, 1):
        print(f"\n\n{'='*70}")
        print(f"Running Example {i}/{len(examples)}: {name}")
        print(f"{'='*70}")
        
        try:
            func()
            print(f"\n✅ Example {i} completed successfully")
        except Exception as e:
            print(f"\n❌ Example {i} failed: {e}")
        
        if i < len(examples):
            input("\nPress Enter to continue to next example...")


def interactive_menu():
    """Interactive menu to run specific examples"""
    examples = [
        ("Basic Query", example_1_basic_query),
        ("Multi-turn Conversation", example_2_followup_conversation),
        ("Technical Documentation", example_3_technical_documentation),
        ("Comparison Query", example_4_comparison_query),
        ("Troubleshooting", example_5_troubleshooting),
        ("Complex Tables", example_6_complex_tables),
        ("Code Examples", example_7_code_examples),
        ("Best Practices", example_8_best_practices),
        ("Specific Feature", example_9_specific_feature),
        ("Contextual Follow-ups", example_10_contextual_followups)
    ]
    
    while True:
        print("\n" + "="*70)
        print("DOCUMENTATION EXPLAINER AGENT TEAM - ADVANCED EXAMPLES")
        print("="*70)
        print("\nSelect an example to run:")
        
        for i, (name, _) in enumerate(examples, 1):
            print(f"  {i}. {name}")
        
        print(f"\n  {len(examples) + 1}. Run all examples")
        print("  0. Exit")
        
        try:
            choice = input("\nEnter your choice (0-{}): ".format(len(examples) + 1))
            choice = int(choice)
            
            if choice == 0:
                print("\n👋 Goodbye!\n")
                break
            elif choice == len(examples) + 1:
                run_all_examples()
            elif 1 <= choice <= len(examples):
                print(f"\n{'='*70}")
                print(f"Running: {examples[choice-1][0]}")
                print(f"{'='*70}")
                examples[choice-1][1]()
                print(f"\n✅ Example completed")
                input("\nPress Enter to continue...")
            else:
                print("\n❌ Invalid choice. Please try again.")
        
        except ValueError:
            print("\n❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


def main():
    """Main entry point"""
    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("\n❌ ERROR: ANTHROPIC_API_KEY environment variable not set!")
        print("\nPlease set your API key:")
        print("  Linux/Mac: export ANTHROPIC_API_KEY='your-api-key'")
        print("  Windows:   set ANTHROPIC_API_KEY=your-api-key\n")
        return
    
    # Run interactive menu
    interactive_menu()


if __name__ == "__main__":
    main()
