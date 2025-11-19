"""
Test Suite for Documentation Explainer Agent Team
=================================================
Basic tests to verify the system is working correctly
"""

import os
import sys
from doc_explainer_agents import (
    DocumentationExplainerTeam,
    Agent1Orchestrator,
    Agent2WebNavigator,
    Message,
    AgentRole
)


def test_api_key_check():
    """Test 1: Verify API key is set"""
    print("\n" + "="*70)
    print("TEST 1: API Key Configuration")
    print("="*70)
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if api_key:
        print("✅ PASS: API key is set")
        print(f"   Key prefix: {api_key[:10]}...")
        return True
    else:
        print("❌ FAIL: API key is not set")
        print("   Please set ANTHROPIC_API_KEY environment variable")
        return False


def test_agent_initialization():
    """Test 2: Verify agents can be initialized"""
    print("\n" + "="*70)
    print("TEST 2: Agent Initialization")
    print("="*70)
    
    try:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        
        # Test Agent 1
        agent1 = Agent1Orchestrator(api_key)
        print("✅ PASS: Agent 1 (Orchestrator) initialized")
        print(f"   Model: {agent1.model}")
        print(f"   Role: {agent1.role.value}")
        
        # Test Agent 2
        agent2 = Agent2WebNavigator(api_key)
        print("✅ PASS: Agent 2 (Web Navigator) initialized")
        print(f"   Model: {agent2.model}")
        print(f"   Role: {agent2.role.value}")
        
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Could not initialize agents")
        print(f"   Error: {e}")
        return False


def test_team_initialization():
    """Test 3: Verify team can be initialized"""
    print("\n" + "="*70)
    print("TEST 3: Team Initialization")
    print("="*70)
    
    try:
        team = DocumentationExplainerTeam()
        print("✅ PASS: Team initialized successfully")
        print(f"   Agent 1: {type(team.agent1).__name__}")
        print(f"   Agent 2: {type(team.agent2).__name__}")
        print(f"   Session history: {len(team.session_history)} messages")
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Could not initialize team")
        print(f"   Error: {e}")
        return False


def test_message_structure():
    """Test 4: Verify message structure works"""
    print("\n" + "="*70)
    print("TEST 4: Message Structure")
    print("="*70)
    
    try:
        import time
        
        msg = Message(
            role="user",
            content="Test message",
            sender=AgentRole.ORCHESTRATOR,
            timestamp=time.time(),
            metadata={"test": True}
        )
        
        msg_dict = msg.to_dict()
        
        assert msg_dict["role"] == "user"
        assert msg_dict["content"] == "Test message"
        assert msg_dict["sender"] == "agent_1"
        assert "timestamp" in msg_dict
        assert msg_dict["metadata"]["test"] == True
        
        print("✅ PASS: Message structure working correctly")
        print(f"   Message dict: {msg_dict}")
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Message structure test failed")
        print(f"   Error: {e}")
        return False


def test_agent1_query_processing():
    """Test 5: Test Agent 1 can process a simple query"""
    print("\n" + "="*70)
    print("TEST 5: Agent 1 Query Processing")
    print("="*70)
    
    try:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        agent1 = Agent1Orchestrator(api_key)
        
        test_query = "How do I use the Anthropic API?"
        print(f"   Processing query: '{test_query}'")
        
        result = agent1.process_user_query(test_query)
        
        assert "search_needed" in result or "analysis" in result
        
        print("✅ PASS: Agent 1 processed query successfully")
        print(f"   Result keys: {list(result.keys())}")
        
        if "analysis" in result:
            print(f"   Analysis: {result['analysis'][:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Agent 1 query processing failed")
        print(f"   Error: {e}")
        return False


def test_basic_query_flow():
    """Test 6: Test basic query flow through the system"""
    print("\n" + "="*70)
    print("TEST 6: Basic Query Flow (This may take 10-20 seconds)")
    print("="*70)
    
    try:
        team = DocumentationExplainerTeam()
        
        test_query = "What is Claude?"
        print(f"   Query: '{test_query}'")
        print("   Processing... (please wait)")
        
        response = team.process_query(test_query)
        
        assert len(response) > 0
        assert isinstance(response, str)
        
        print("✅ PASS: Query processed successfully")
        print(f"   Response length: {len(response)} characters")
        print(f"   Response preview: {response[:150]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Query flow test failed")
        print(f"   Error: {e}")
        return False


def test_followup_handling():
    """Test 7: Test follow-up query handling"""
    print("\n" + "="*70)
    print("TEST 7: Follow-up Query Handling")
    print("="*70)
    
    try:
        team = DocumentationExplainerTeam()
        
        # Initial query
        query1 = "What is an API?"
        print(f"   Initial query: '{query1}'")
        response1 = team.process_query(query1)
        
        # Follow-up
        query2 = "Can you give an example?"
        print(f"   Follow-up query: '{query2}'")
        response2 = team.handle_followup(query2)
        
        assert len(response2) > 0
        assert len(team.agent1.conversation_history) >= 4  # 2 exchanges
        
        print("✅ PASS: Follow-up handling works")
        print(f"   Conversation history: {len(team.agent1.conversation_history)} messages")
        
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Follow-up test failed")
        print(f"   Error: {e}")
        return False


def test_session_summary():
    """Test 8: Test session summary functionality"""
    print("\n" + "="*70)
    print("TEST 8: Session Summary")
    print("="*70)
    
    try:
        team = DocumentationExplainerTeam()
        
        # Process a query
        team.process_query("Test query")
        
        # Get summary
        summary = team.get_session_summary()
        
        assert "total_queries" in summary
        assert "agent1_responses" in summary
        assert "session_messages" in summary
        assert summary["total_queries"] >= 1
        
        print("✅ PASS: Session summary working")
        print(f"   Summary: {summary}")
        
        return True
        
    except Exception as e:
        print(f"❌ FAIL: Session summary test failed")
        print(f"   Error: {e}")
        return False


def run_all_tests():
    """Run all tests and report results"""
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#" + " "*15 + "DOCUMENTATION EXPLAINER AGENT TEAM" + " "*19 + "#")
    print("#" + " "*25 + "TEST SUITE" + " "*33 + "#")
    print("#" + " "*68 + "#")
    print("#"*70)
    
    tests = [
        ("API Key Check", test_api_key_check, False),
        ("Agent Initialization", test_agent_initialization, False),
        ("Team Initialization", test_team_initialization, False),
        ("Message Structure", test_message_structure, False),
        ("Agent 1 Query Processing", test_agent1_query_processing, True),
        ("Basic Query Flow", test_basic_query_flow, True),
        ("Follow-up Handling", test_followup_handling, True),
        ("Session Summary", test_session_summary, True)
    ]
    
    results = []
    
    # Run basic tests first
    print("\n" + "="*70)
    print("RUNNING BASIC TESTS (Fast)")
    print("="*70)
    
    for name, test_func, requires_api in tests:
        if not requires_api:
            try:
                result = test_func()
                results.append((name, result))
            except Exception as e:
                print(f"\n❌ EXCEPTION in {name}: {e}")
                results.append((name, False))
    
    # Check if we should continue
    basic_tests_passed = all(result for name, result in results if name in [t[0] for t in tests[:4]])
    
    if not basic_tests_passed:
        print("\n" + "="*70)
        print("⚠️  BASIC TESTS FAILED - SKIPPING API TESTS")
        print("="*70)
        print_summary(results)
        return
    
    # Ask before running API tests
    print("\n" + "="*70)
    print("BASIC TESTS PASSED!")
    print("="*70)
    
    run_api_tests = input("\nRun API tests? These will use your API credits and take 30-60 seconds. (y/n): ")
    
    if run_api_tests.lower() in ['y', 'yes']:
        print("\n" + "="*70)
        print("RUNNING API TESTS (Slow - Uses API Credits)")
        print("="*70)
        
        for name, test_func, requires_api in tests:
            if requires_api:
                try:
                    result = test_func()
                    results.append((name, result))
                except Exception as e:
                    print(f"\n❌ EXCEPTION in {name}: {e}")
                    results.append((name, False))
    else:
        print("\n⏭️  Skipping API tests")
    
    # Print summary
    print_summary(results)


def print_summary(results):
    """Print test summary"""
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
    
    print("\n" + "-"*70)
    print(f"Results: {passed}/{total} tests passed ({passed/total*100:.1f}%)")
    print("="*70)
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! The system is working correctly.")
    elif passed >= total * 0.5:
        print("\n⚠️  SOME TESTS FAILED. Check the errors above.")
    else:
        print("\n❌ MANY TESTS FAILED. Please check your setup.")


def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "--quick":
        # Quick test - only basic tests
        print("\nRunning quick tests (basic only)...\n")
        test_api_key_check()
        test_agent_initialization()
        test_team_initialization()
        test_message_structure()
    else:
        run_all_tests()


if __name__ == "__main__":
    main()
