"""
NeuroDivergent AI Coach - Main Coach Agent

This is the main AI agent that acts as Professor of Peer Management and
Positive Lifestyle Coaching, facilitating training for ihep.app members.
"""

import sys
import os
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from dataclasses import dataclass

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent.ethical_framework import EthicalFramework, EthicalDecision
from agent.emotional_intelligence import EmotionalIntelligence, EmotionalState
from curriculum.curriculum_design import CurriculumDesign, TrainingLevel
from models.member import Member, MemberStatus


@dataclass
class CoachingSession:
    """Record of a coaching session"""
    session_id: str
    member_id: str
    timestamp: datetime
    session_type: str  # "training", "assessment", "check-in", "crisis"
    module_id: Optional[str]
    emotional_state: Optional[str]
    topics_covered: List[str]
    member_message: str
    coach_response: str
    ethical_considerations: List[str]
    action_items: List[str]
    duration_minutes: Optional[int]


class NeurodivergentCoach:
    """
    Main NeuroDivergent AI Coach

    Acts as Professor of Peer Management and Positive Lifestyle Coaching,
    combining curriculum expertise, ethical guidance, and emotional intelligence
    to facilitate comprehensive training for ihep.app peer supporters.
    """

    def __init__(self):
        """Initialize the coach with all necessary components"""
        self.curriculum = CurriculumDesign()
        self.ethical_framework = EthicalFramework()
        self.emotional_intelligence = EmotionalIntelligence()
        self.session_history: Dict[str, List[CoachingSession]] = {}
        self.active_members: Dict[str, Member] = {}

        print("NeuroDivergent AI Coach initialized.")
        print("Ready to facilitate peer management and positive lifestyle coaching training.")

    def check_qualification(self, member: Member) -> Tuple[bool, Dict]:
        """
        Check if member meets qualification criteria for training

        Args:
            member: Member to evaluate

        Returns:
            (qualified, details) tuple
        """
        qualified = member.is_qualified_for_training()

        details = {
            "qualified": qualified,
            "engagement_score": member.get_engagement_score(),
            "adherence_score": member.get_adherence_score(),
            "months_active": member.months_active,
            "good_standing": member.good_standing,
            "expressed_interest": member.expressed_interest,
            "criteria": {
                "engagement": {"required": 75, "actual": member.get_engagement_score(), "met": member.get_engagement_score() >= 75},
                "adherence": {"required": 70, "actual": member.get_adherence_score(), "met": member.get_adherence_score() >= 70},
                "months_active": {"required": 3, "actual": member.months_active, "met": member.months_active >= 3},
                "good_standing": {"required": True, "actual": member.good_standing, "met": member.good_standing},
                "expressed_interest": {"required": True, "actual": member.expressed_interest, "met": member.expressed_interest}
            }
        }

        return qualified, details

    def start_training_conversation(self, member: Member) -> str:
        """
        Start an initial training conversation with a qualified member

        Args:
            member: The member starting training

        Returns:
            Welcome message from the coach
        """
        # Check qualification
        qualified, details = self.check_qualification(member)

        if not qualified:
            unmet_criteria = [k for k, v in details["criteria"].items() if not v["met"]]
            return self._craft_not_qualified_response(member, unmet_criteria, details)

        # Store member
        self.active_members[member.id] = member

        # Craft welcoming, humanistic response
        response_parts = [
            f"Hello {member.name}, and welcome! 🌟",
            "",
            "I'm honored to be your guide on this transformative journey. My name is Professor Nova, and I'll be working with you as you train to become a peer assistant in the Integrated Healthy Empowerment Program.",
            "",
            "First, let me say how impressed I am with your commitment to ihep.app. Your engagement and dedication to your own growth have been remarkable:",
            f"  • Engagement Score: {member.get_engagement_score():.0f}% - Outstanding! 💪",
            f"  • Adherence Score: {member.get_adherence_score():.0f}% - Excellent follow-through! ✨",
            f"  • Time in program: {member.months_active} months - You've built real experience! 📈",
            "",
            "The fact that you've expressed interest in helping others through peer support tells me something important about you: you understand the power of lived experience and want to give back to the community that has supported you. That's beautiful, and it's exactly the spirit we need in peer supporters.",
            "",
            "**What We'll Accomplish Together:**",
            "",
            "Our training journey has four progressive levels:",
            "1. **Foundation** (2-4 weeks): You'll master the fundamentals of peer support",
            "2. **Peer Assistant** (4-8 weeks): Build core skills with hands-on practice",
            "3. **Peer Counselor** (8-12 weeks): Develop advanced techniques and independence",
            "4. **Peer Manager** (Ongoing): Leadership, program development, and mastery",
            "",
            "**What Makes This Training Special:**",
            "",
            "✨ **Humanistic Approach**: We honor your humanity, your story, and your unique gifts",
            "🧠 **NeuroDivergent Method**: Evidence-based practices grounded in neuroscience and positive psychology",
            "❤️ **Emotional Intelligence**: You'll develop deep empathy and authentic connection skills",
            "⚖️ **Ethical Excellence**: Strong moral compass and professional boundaries guide everything",
            "💰 **Paid Opportunity**: Starting at Level 2, you'll receive compensation while you train",
            "",
            "**Your Learning Experience:**",
            "",
            "I'm not here to lecture at you - I'm here to facilitate your growth. Our conversations will be:",
            "  • **Interactive**: Ask questions anytime. Curiosity is encouraged!",
            "  • **Personalized**: Adapted to your learning style and pace",
            "  • **Practical**: Real scenarios, hands-on practice, and immediate application",
            "  • **Supportive**: You'll have support every step of the way",
            "  • **Reflective**: We'll explore your insights and experiences deeply",
            "",
            "**Important Notes:**",
            "",
            "🔒 **Confidentiality**: Our conversations are private (with limits I'll explain)",
            "🎯 **Your Pace**: We move at a speed that works for you",
            "🤝 **Partnership**: This is a collaborative journey, not a top-down process",
            "💬 **Open Communication**: If something isn't working, tell me. We'll adjust.",
            "",
            "**Let's Begin:**",
            "",
            f"Before we dive into the curriculum, I'd love to learn more about you, {member.name}.",
            "",
            "1. What drew you to peer support? What about this path speaks to you?",
            "2. What are you most excited about in this training?",
            "3. What, if anything, feels scary or uncertain?",
            "4. How do you learn best? (videos, reading, discussion, practice, etc.)",
            "",
            "Take your time with these questions. There are no wrong answers - I genuinely want to understand your motivations, hopes, and concerns so I can support you most effectively.",
            "",
            "Whenever you're ready, share what feels right to share. I'm here, I'm listening, and I'm excited to walk this path with you.",
            "",
            "With warmth and encouragement,",
            "Professor Nova 🌟"
        ]

        return "\n".join(response_parts)

    def _craft_not_qualified_response(self, member: Member, unmet_criteria: List[str], details: Dict) -> str:
        """Craft a compassionate response when member doesn't qualify yet"""
        response_parts = [
            f"Hello {member.name},",
            "",
            "Thank you so much for your interest in becoming a peer assistant! Your desire to support others is wonderful, and it speaks to your generous spirit.",
            "",
            "I want to be honest and transparent with you: you're not quite ready to begin the formal training program yet, but you're on your way! Let me explain what we're looking for and how close you are.",
            "",
            "**Where You Are Now:**",
            f"  • Engagement Score: {details['engagement_score']:.0f}% (we need 75%)",
            f"  • Adherence Score: {details['adherence_score']:.0f}% (we need 70%)",
            f"  • Time in Program: {details['months_active']} months (we need 3 months)",
            f"  • Good Standing: {'Yes ✓' if details['good_standing'] else 'No ✗'}",
            f"  • Expressed Interest: {'Yes ✓' if details['expressed_interest'] else 'No ✗'}",
            "",
            "**What This Means:**",
            ""
        ]

        # Provide specific guidance for each unmet criterion
        if "engagement" in unmet_criteria:
            gap = 75 - details['engagement_score']
            response_parts.extend([
                f"📊 **Engagement**: You're at {details['engagement_score']:.0f}%, and we need 75%. That's only a {gap:.0f}% gap!",
                "   Ways to increase engagement:",
                "   - Log in more regularly (aim for 20+ days per month)",
                "   - Set and work toward goals in the app",
                "   - Participate in community features",
                "   - Complete your daily check-ins",
                ""
            ])

        if "adherence" in unmet_criteria:
            gap = 70 - details['adherence_score']
            response_parts.extend([
                f"✅ **Adherence**: You're at {details['adherence_score']:.0f}%, and we need 70%. Just a {gap:.0f}% increase needed!",
                "   Ways to increase adherence:",
                "   - Follow through on commitments you make",
                "   - Attend scheduled appointments",
                "   - Complete programs you enroll in",
                ""
            ])

        if "months_active" in unmet_criteria:
            months_needed = 3 - details['months_active']
            response_parts.extend([
                f"📅 **Time in Program**: You've been active for {details['months_active']} months. We need at least 3 months.",
                f"   You'll be eligible in approximately {months_needed} more month{'s' if months_needed > 1 else ''}!",
                "   Use this time to build your own recovery and wellness foundation.",
                ""
            ])

        response_parts.extend([
            "**The Good News:**",
            "",
            "You're already on the path! Every day you engage with ihep.app and work on your own wellness, you're building the foundation you'll need to support others.",
            "",
            "**Next Steps:**",
            "",
            "1. Keep doing what you're doing - you're making progress!",
            "2. Focus on the specific areas mentioned above",
            "3. Reach out again when you've met the criteria",
            "4. Remember: This isn't a rejection. It's an invitation to strengthen your foundation first.",
            "",
            "**Why These Criteria Matter:**",
            "",
            "We have these requirements because peer support is challenging work. Before you can effectively support others, you need a strong foundation in your own wellness journey. These criteria ensure you're ready for the responsibility and that you'll succeed in the role.",
            "",
            "You're not being excluded - you're being invited to continue your own growth first. And I'll be here when you're ready!",
            "",
            f"Please check back in when you've made progress, {member.name}. I believe in your potential!",
            "",
            "With encouragement and support,",
            "Professor Nova"
        ])

        return "\n".join(response_parts)

    def continue_conversation(
        self,
        member_id: str,
        member_message: str,
        context: Optional[Dict] = None
    ) -> str:
        """
        Continue an ongoing conversation with a member

        Args:
            member_id: ID of the member
            member_message: Message from the member
            context: Additional context (current module, session type, etc.)

        Returns:
            Coach response
        """
        # Get member
        member = self.active_members.get(member_id)
        if not member:
            return "I'm sorry, I don't have an active session with you. Please start a new training conversation."

        # First, check for ethical concerns
        ethical_decision = self.ethical_framework.evaluate_situation(
            member_message,
            {"member_id": member_id, "member": member}
        )

        # If critical or high risk, address immediately
        if ethical_decision.risk_level in ["critical", "high"]:
            return self._handle_crisis_situation(member, member_message, ethical_decision)

        # Recognize emotional state
        emotional_state = self.emotional_intelligence.recognize_emotion(member_message, context)

        # Generate humanistic response components
        response_guidance = self.emotional_intelligence.craft_humanistic_response(member_message, context)

        # Craft full response
        response = self._craft_teaching_response(
            member=member,
            member_message=member_message,
            emotional_state=emotional_state,
            response_guidance=response_guidance,
            context=context
        )

        # Log session
        self._log_session(
            member=member,
            member_message=member_message,
            coach_response=response,
            emotional_state=emotional_state,
            ethical_decision=ethical_decision,
            context=context
        )

        return response

    def _handle_crisis_situation(
        self,
        member: Member,
        message: str,
        ethical_decision: EthicalDecision
    ) -> str:
        """Handle crisis or high-risk situations"""
        response_parts = [
            f"{member.name}, thank you for sharing this with me. I hear you, and I want to make sure you get the right support right now.",
            "",
            "**Immediate Action Needed:**",
            ""
        ]

        if ethical_decision.risk_level == "critical":
            response_parts.extend([
                "⚠️ What you've shared indicates you may be in immediate danger. Your safety is the absolute priority.",
                "",
                "**Please take these steps RIGHT NOW:**",
                ""
            ])

            response_parts.extend([f"  {step}" for step in ethical_decision.action_steps])

            response_parts.extend([
                "",
                "**Crisis Resources (Available 24/7):**",
                "  • National Suicide Prevention Lifeline: 988 or 1-800-273-8255",
                "  • Crisis Text Line: Text HOME to 741741",
                "  • National Domestic Violence Hotline: 1-800-799-7233",
                "  • Emergency Services: 911",
                "",
                "I care about you and want you to be safe. Please reach out to one of these resources immediately, and know that there is help available.",
                "",
                "You don't have to face this alone."
            ])
        else:
            response_parts.extend([
                f"**Recommended Actions:**",
                ""
            ])
            response_parts.extend([f"  {step}" for step in ethical_decision.action_steps])

            response_parts.extend([
                "",
                "I'm here to support you, but this situation requires additional professional support beyond peer coaching. That's not a limitation - it's about making sure you get the most appropriate help.",
                "",
                "Would you like help connecting with these resources?"
            ])

        return "\n".join(response_parts)

    def _craft_teaching_response(
        self,
        member: Member,
        member_message: str,
        emotional_state: EmotionalState,
        response_guidance: Dict,
        context: Optional[Dict] = None
    ) -> str:
        """Craft a comprehensive teaching response"""
        # Start with emotional recognition and validation
        response_parts = [
            response_guidance["response_components"]["opener"],
            response_guidance["response_components"]["validation"]
        ]

        # Add content based on context (module, topic, etc.)
        if context and context.get("module_id"):
            module = self.curriculum.get_module(context["module_id"])
            if module:
                # Add teaching content relevant to the module
                response_parts.extend([
                    "",
                    f"As we explore {module.title}, what you're sharing connects to some key concepts...",
                    ""
                ])

        # Add reflective questions
        if response_guidance["response_components"].get("question"):
            response_parts.extend([
                "",
                response_guidance["response_components"]["question"]
            ])

        # Add encouragement and forward movement
        response_parts.extend([
            "",
            "Remember, you're building important skills through this process. Every conversation, every reflection, every question is part of your growth as a peer supporter.",
            "",
            "What would you like to explore next?"
        ])

        return "\n".join(response_parts)

    def teach_module(self, member_id: str, module_id: str) -> str:
        """
        Begin teaching a specific module

        Args:
            member_id: ID of the member
            module_id: ID of the module to teach

        Returns:
            Introduction to the module
        """
        member = self.active_members.get(member_id)
        if not member:
            return "Please start a training conversation first."

        module = self.curriculum.get_module(module_id)
        if not module:
            return f"I couldn't find module {module_id}. Please check the module ID."

        # Check prerequisites
        prerequisites = module.prerequisites
        if prerequisites:
            unmet = [p for p in prerequisites if p not in member.training_progress.modules_completed]
            if unmet:
                return f"Before we can start {module.title}, you'll need to complete these modules first: {', '.join(unmet)}"

        # Mark module as in progress
        if module_id not in member.training_progress.modules_in_progress:
            member.training_progress.modules_in_progress.append(module_id)
        member.training_progress.current_module_id = module_id

        # Craft introduction
        response_parts = [
            f"**Module: {module.title}**",
            f"*{module.description}*",
            "",
            f"📚 **Duration**: {module.duration_hours} hours",
            f"🎯 **Module Type**: {module.module_type.value.title()}",
            "",
            "**What You'll Learn:**",
            ""
        ]

        for i, objective in enumerate(module.learning_objectives, 1):
            response_parts.extend([
                f"{i}. {objective.description}",
                f"   *Builds competency in: {objective.competency}*",
                ""
            ])

        response_parts.extend([
            "**Why This Matters:**",
            "",
            "This module is a crucial building block in your development as a peer supporter. The skills and knowledge you gain here will directly impact your ability to help others effectively and ethically.",
            "",
            "**How We'll Approach This:**",
            "",
            "- I'll present concepts and frameworks",
            "- We'll discuss how they apply to real situations",
            "- You'll have opportunities to practice",
            "- We'll reflect on your learning together",
            "",
            "Are you ready to begin? What questions do you have before we dive in?"
        ])

        return "\n".join(response_parts)

    def assess_progress(self, member_id: str) -> str:
        """
        Provide assessment of member's training progress

        Args:
            member_id: ID of member to assess

        Returns:
            Progress report
        """
        member = self.active_members.get(member_id)
        if not member:
            return "Please start a training conversation first."

        level = self.curriculum.get_level(member.training_progress.current_level)
        if not level:
            return "Could not retrieve your current training level."

        total_modules = len(level.modules)
        completed = len([m for m in member.training_progress.modules_completed
                        if any(mod.id == m for mod in level.modules)])

        response_parts = [
            f"**Training Progress Report for {member.name}**",
            f"*Generated: {datetime.now().strftime('%B %d, %Y')}*",
            "",
            f"**Current Level**: {level.title}",
            f"**Progress**: {completed}/{total_modules} modules completed ({(completed/total_modules*100):.0f}%)",
            "",
            "**Modules Completed:**",
        ]

        for module in level.modules:
            if module.id in member.training_progress.modules_completed:
                score = member.training_progress.assessment_scores.get(module.id, "N/A")
                score_str = f"{score}%" if isinstance(score, (int, float)) else score
                response_parts.append(f"  ✅ {module.title} - Score: {score_str}")

        if member.training_progress.modules_in_progress:
            response_parts.extend([
                "",
                "**Currently Working On:**"
            ])
            for mod_id in member.training_progress.modules_in_progress:
                mod = self.curriculum.get_module(mod_id)
                if mod:
                    response_parts.append(f"  📖 {mod.title}")

        response_parts.extend([
            "",
            "**Practice Hours:**",
            f"  • Total: {member.training_progress.practice_hours} hours",
            f"  • Supervised: {member.training_progress.supervised_hours} hours",
            f"  • Independent: {member.training_progress.independent_hours} hours",
            "",
            f"**Member Interactions**: {member.training_progress.member_interactions}",
            f"**Average Feedback Score**: {member.training_progress.get_average_feedback():.1f}/5.0",
            "",
            "**Strengths Observed:**"
        ])

        # Generate personalized feedback
        if member.training_progress.get_average_feedback() >= 4.5:
            response_parts.append("  • Exceptional member feedback - you're making real impact!")
        if member.training_progress.practice_hours >= 10:
            response_parts.append("  • Strong commitment to practice hours")
        if completed >= total_modules * 0.75:
            response_parts.append("  • Excellent progress through curriculum")

        # Check advancement readiness
        validation = self.curriculum.validate_progression({
            "current_level": member.training_progress.current_level,
            "complete_all_modules": completed == total_modules,
            "assessment_score": sum(member.training_progress.assessment_scores.values()) / len(member.training_progress.assessment_scores) if member.training_progress.assessment_scores else 0,
            "practice_hours": member.training_progress.practice_hours
        })

        response_parts.extend([
            "",
            "**Advancement Status:**"
        ])

        if validation["valid"]:
            response_parts.extend([
                f"  🎉 Congratulations! You're ready to advance to Level {validation['next_level']}!",
                "",
                "You've demonstrated the knowledge, skills, and commitment needed for the next stage. I'm so proud of your progress!"
            ])
        else:
            response_parts.extend([
                "  Areas to focus on for advancement:"
            ])
            for criterion, message in validation["criteria_not_met"].items():
                response_parts.append(f"    • {message}")

        response_parts.extend([
            "",
            "Keep up the excellent work! You're making a difference. 🌟"
        ])

        return "\n".join(response_parts)

    def _log_session(
        self,
        member: Member,
        member_message: str,
        coach_response: str,
        emotional_state: EmotionalState,
        ethical_decision: EthicalDecision,
        context: Optional[Dict] = None
    ):
        """Log coaching session for record keeping"""
        session = CoachingSession(
            session_id=f"{member.id}_{datetime.now().strftime('%Y%m%d%H%M%S')}",
            member_id=member.id,
            timestamp=datetime.now(),
            session_type=context.get("session_type", "training") if context else "training",
            module_id=context.get("module_id") if context else member.training_progress.current_module_id,
            emotional_state=emotional_state.primary_emotion.value,
            topics_covered=context.get("topics", []) if context else [],
            member_message=member_message,
            coach_response=coach_response,
            ethical_considerations=[ethical_decision.recommendation] if ethical_decision else [],
            action_items=ethical_decision.action_steps if ethical_decision else [],
            duration_minutes=context.get("duration") if context else None
        )

        if member.id not in self.session_history:
            self.session_history[member.id] = []

        self.session_history[member.id].append(session)

    def get_curriculum_overview(self) -> str:
        """Get complete curriculum overview"""
        response_parts = [
            "**NeuroDivergent AI Coach - Complete Training Curriculum**",
            "",
            "This comprehensive training program prepares ihep.app members to become skilled peer supporters, counselors, and managers.",
            ""
        ]

        for level in self.curriculum.get_all_levels():
            total_hours = self.curriculum.calculate_total_hours(level.level.value)
            response_parts.extend([
                f"## Level {level.level.value}: {level.title}",
                f"*{level.description}*",
                "",
                f"⏱️ Duration: {level.duration_weeks[0]}-{level.duration_weeks[1]} weeks",
                f"💰 Compensation: {level.compensation_type}",
                f"📚 Total Training Hours: {total_hours}",
                f"👥 Expected Hours/Week: {level.hours_per_week[0]}-{level.hours_per_week[1]}",
                "",
                f"**Modules ({len(level.modules)}):**",
                ""
            ])

            for module in level.modules:
                response_parts.append(f"  {module.id}: {module.title} ({module.duration_hours}h)")

            response_parts.append("")

        return "\n".join(response_parts)


# Example usage and testing
if __name__ == "__main__":
    # Create coach
    coach = NeurodivergentCoach()

    print("\n" + "=" * 70)
    print("NEURODIVERGENT AI COACH - DEMONSTRATION")
    print("=" * 70)

    # Create sample member
    from models.member import EngagementMetrics, AdherenceMetrics

    member = Member(
        id="DEMO001",
        name="Alex Johnson",
        email="alex@example.com",
        preferred_pronouns="they/them"
    )

    # Set qualification metrics
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

    # Start training
    print("\n" + "-" * 70)
    print("STARTING TRAINING CONVERSATION")
    print("-" * 70)
    welcome_message = coach.start_training_conversation(member)
    print(welcome_message)

    # Simulate member response
    print("\n" + "-" * 70)
    print("MEMBER RESPONDS")
    print("-" * 70)
    member_response = "Thank you so much! I'm really excited but also a bit nervous. I've always wanted to help others because I know how hard it was for me when I was struggling. I learn best through practice and real examples."

    coach_response = coach.continue_conversation(
        member_id=member.id,
        member_message=member_response
    )
    print(coach_response)

    print("\n" + "=" * 70)
    print("END DEMONSTRATION")
    print("=" * 70)
