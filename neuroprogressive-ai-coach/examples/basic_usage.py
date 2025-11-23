"""
Basic Usage Example for NeuroProgressive AI Coach

This example demonstrates how to:
1. Create members
2. Check qualification
3. Start training conversations
4. Teach modules
5. Track progress
"""

import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.coach import NeuroprogressiveCoach
from models.member import Member, EngagementMetrics, AdherenceMetrics


def create_sample_member(qualified: bool = True) -> Member:
    """Create a sample member for testing"""
    member = Member(
        id=f"MEMBER_{'QUALIFIED' if qualified else 'NOT_QUALIFIED'}",
        name="Jamie Smith",
        email="jamie.smith@example.com",
        preferred_pronouns="she/her"
    )

    if qualified:
        # Set metrics that meet qualification criteria
        member.engagement.total_logins = 50
        member.engagement.days_active_last_30 = 26
        member.engagement.goals_set = 12
        member.engagement.goals_completed = 10
        member.engagement.check_ins_completed = 25
        member.engagement.community_posts = 20
        member.engagement.community_interactions = 45

        member.adherence.commitments_made = 25
        member.adherence.commitments_kept = 22
        member.adherence.appointments_scheduled = 6
        member.adherence.appointments_attended = 6
        member.adherence.programs_enrolled = 4
        member.adherence.programs_completed = 3

        member.months_active = 5
        member.record_interest("outreach")
    else:
        # Set metrics that don't meet qualification
        member.engagement.total_logins = 15
        member.engagement.days_active_last_30 = 10
        member.engagement.goals_set = 3
        member.engagement.goals_completed = 1

        member.adherence.commitments_made = 10
        member.adherence.commitments_kept = 5

        member.months_active = 1
        member.record_interest("outreach")

    return member


def example_1_check_qualification():
    """Example 1: Check if member qualifies for training"""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Checking Member Qualification")
    print("=" * 70)

    coach = NeuroprogressiveCoach()

    # Qualified member
    qualified_member = create_sample_member(qualified=True)
    qualified, details = coach.check_qualification(qualified_member)

    print(f"\nMember: {qualified_member.name}")
    print(f"Qualified: {qualified}")
    print(f"Engagement Score: {details['engagement_score']:.1f}%")
    print(f"Adherence Score: {details['adherence_score']:.1f}%")
    print(f"Months Active: {details['months_active']}")

    # Not qualified member
    print("\n" + "-" * 70)
    not_qualified_member = create_sample_member(qualified=False)
    qualified, details = coach.check_qualification(not_qualified_member)

    print(f"\nMember: {not_qualified_member.name}")
    print(f"Qualified: {qualified}")
    print(f"Engagement Score: {details['engagement_score']:.1f}%")
    print(f"Adherence Score: {details['adherence_score']:.1f}%")
    print(f"Months Active: {details['months_active']}")

    print("\nUnmet Criteria:")
    for criterion, info in details['criteria'].items():
        if not info['met']:
            print(f"  • {criterion}: Required {info['required']}, Actual {info['actual']}")


def example_2_start_training():
    """Example 2: Start training conversation"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Starting Training Conversation")
    print("=" * 70)

    coach = NeuroprogressiveCoach()
    member = create_sample_member(qualified=True)

    welcome_message = coach.start_training_conversation(member)
    print(welcome_message)


def example_3_conversation_flow():
    """Example 3: Full conversation flow"""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Conversation Flow")
    print("=" * 70)

    coach = NeuroprogressiveCoach()
    member = create_sample_member(qualified=True)

    # Start conversation
    print("\n[COACH WELCOMES MEMBER]")
    welcome = coach.start_training_conversation(member)
    print(welcome[:500] + "...\n")  # Print first 500 chars

    # Member responds
    print("\n[MEMBER RESPONDS]")
    member_msg = "Hi Professor Nova! I'm excited to start. I want to help others because I've been through difficult times myself and I know how important support is."
    print(f"Member: {member_msg}")

    # Coach responds
    print("\n[COACH RESPONDS]")
    response = coach.continue_conversation(member.id, member_msg)
    print(response)


def example_4_teach_module():
    """Example 4: Teaching a module"""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Teaching a Module")
    print("=" * 70)

    coach = NeuroprogressiveCoach()
    member = create_sample_member(qualified=True)

    # Start training first
    coach.start_training_conversation(member)

    # Teach first module
    print("\n[STARTING MODULE L1M1]")
    module_intro = coach.teach_module(member.id, "L1M1")
    print(module_intro)


def example_5_track_progress():
    """Example 5: Track training progress"""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Tracking Progress")
    print("=" * 70)

    coach = NeuroprogressiveCoach()
    member = create_sample_member(qualified=True)

    # Start training
    coach.start_training_conversation(member)

    # Simulate completing some modules
    member.complete_module("L1M1", 92)
    member.complete_module("L1M2", 88)
    member.complete_module("L1M3", 95)
    member.record_practice_hours(3.5, supervised=True)
    member.record_member_feedback(4.5)
    member.record_member_feedback(4.8)

    # Get progress report
    print("\n[PROGRESS REPORT]")
    progress_report = coach.assess_progress(member.id)
    print(progress_report)


def example_6_curriculum_overview():
    """Example 6: Get curriculum overview"""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Curriculum Overview")
    print("=" * 70)

    coach = NeuroprogressiveCoach()
    overview = coach.get_curriculum_overview()
    print(overview)


def example_7_emotional_intelligence():
    """Example 7: Emotional intelligence in action"""
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Emotional Intelligence")
    print("=" * 70)

    coach = NeuroprogressiveCoach()
    member = create_sample_member(qualified=True)

    # Start training
    coach.start_training_conversation(member)

    # Test different emotional scenarios
    scenarios = [
        "I'm so excited! I just had a breakthrough in understanding how to listen actively!",
        "I'm feeling really overwhelmed. There's so much to learn and I'm worried I won't be good enough.",
        "I'm frustrated because I keep making the same mistakes in my practice sessions."
    ]

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n[SCENARIO {i}]")
        print(f"Member: {scenario}")
        print(f"\n[COACH RESPONSE]")
        response = coach.continue_conversation(member.id, scenario)
        print(response)
        print("\n" + "-" * 70)


def example_8_ethical_framework():
    """Example 8: Ethical framework in action"""
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Ethical Framework")
    print("=" * 70)

    from agent.ethical_framework import EthicalFramework

    framework = EthicalFramework()

    scenarios = [
        "A member asked me for my personal phone number so we can text outside of sessions",
        "A member just told me they're having thoughts of suicide",
        "A member wants me to keep something confidential that I think their therapist should know about"
    ]

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n[ETHICAL SCENARIO {i}]")
        print(f"Situation: {scenario}")
        print(f"\n[ETHICAL ANALYSIS]")

        decision = framework.evaluate_situation(scenario, {})
        print(f"Risk Level: {decision.risk_level.upper()}")
        print(f"Dilemma Type: {decision.dilemma_type.value if decision.dilemma_type else 'None'}")
        print(f"Escalation Needed: {decision.escalation_needed}")
        print(f"\nRecommendation: {decision.recommendation}")
        print(f"\nAction Steps:")
        for step in decision.action_steps:
            print(f"  {step}")
        print("\n" + "-" * 70)


def run_all_examples():
    """Run all examples"""
    examples = [
        ("Check Qualification", example_1_check_qualification),
        ("Start Training", example_2_start_training),
        ("Conversation Flow", example_3_conversation_flow),
        ("Teach Module", example_4_teach_module),
        ("Track Progress", example_5_track_progress),
        ("Curriculum Overview", example_6_curriculum_overview),
        ("Emotional Intelligence", example_7_emotional_intelligence),
        ("Ethical Framework", example_8_ethical_framework)
    ]

    print("\n" + "=" * 70)
    print("NEUROPROGRESSIVE AI COACH - USAGE EXAMPLES")
    print("=" * 70)

    for i, (name, example_func) in enumerate(examples, 1):
        print(f"\nRunning Example {i}: {name}")
        input("\nPress Enter to continue...")
        example_func()

    print("\n" + "=" * 70)
    print("ALL EXAMPLES COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    # You can run individual examples or all of them
    import sys

    if len(sys.argv) > 1:
        example_num = int(sys.argv[1])
        examples = [
            example_1_check_qualification,
            example_2_start_training,
            example_3_conversation_flow,
            example_4_teach_module,
            example_5_track_progress,
            example_6_curriculum_overview,
            example_7_emotional_intelligence,
            example_8_ethical_framework
        ]

        if 1 <= example_num <= len(examples):
            examples[example_num - 1]()
        else:
            print(f"Invalid example number. Choose 1-{len(examples)}")
    else:
        # Run a quick demo
        print("\nRunning quick demonstration...")
        print("For full examples, run: python basic_usage.py [1-8]")
        print("Or run all examples: python basic_usage.py 0\n")

        example_1_check_qualification()
        example_3_conversation_flow()
