"""
Ethical Framework for the NeuroProgressive AI Coach

This module implements the ethical guidelines, moral compass, and best practices
that govern all interactions and decisions made by the AI coach.
"""

from enum import Enum
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


class EthicalPrinciple(Enum):
    """Core ethical principles guiding the coach"""
    BENEFICENCE = "beneficence"  # Act in the best interest of members
    NON_MALEFICENCE = "non_maleficence"  # Do no harm
    AUTONOMY = "autonomy"  # Respect self-determination
    JUSTICE = "justice"  # Fair and equitable treatment
    FIDELITY = "fidelity"  # Be faithful to commitments
    CONFIDENTIALITY = "confidentiality"  # Protect privacy
    CULTURAL_COMPETENCE = "cultural_competence"  # Respect diversity
    PROFESSIONAL_BOUNDARIES = "professional_boundaries"  # Maintain appropriate relationships


class EthicalDilemmaType(Enum):
    """Types of ethical dilemmas that may arise"""
    BOUNDARY_VIOLATION = "boundary_violation"
    CONFIDENTIALITY_BREACH = "confidentiality_breach"
    DUAL_RELATIONSHIP = "dual_relationship"
    MANDATED_REPORTING = "mandated_reporting"
    SCOPE_EXCEEDED = "scope_exceeded"
    CULTURAL_INSENSITIVITY = "cultural_insensitivity"
    HARM_RISK = "harm_risk"
    AUTONOMY_CONFLICT = "autonomy_conflict"


@dataclass
class EthicalDecision:
    """Result of ethical decision-making process"""
    situation: str
    dilemma_type: Optional[EthicalDilemmaType]
    principles_involved: List[EthicalPrinciple]
    recommendation: str
    rationale: str
    action_steps: List[str]
    escalation_needed: bool
    risk_level: str  # "low", "medium", "high"


class EthicalFramework:
    """
    Comprehensive ethical framework for the NeuroProgressive AI Coach.

    This class implements ethical decision-making, boundary monitoring,
    and ensures all coach behaviors align with professional standards.
    """

    def __init__(self):
        self.principles = self._initialize_principles()
        self.boundaries = self._initialize_boundaries()
        self.red_flags = self._initialize_red_flags()
        self.mandated_reporting_triggers = self._initialize_reporting_triggers()

    def _initialize_principles(self) -> Dict[EthicalPrinciple, Dict]:
        """Define core ethical principles with descriptions and guidelines"""
        return {
            EthicalPrinciple.BENEFICENCE: {
                "description": "Act in the best interest of members and trainees",
                "guidelines": [
                    "Prioritize member wellbeing in all decisions",
                    "Provide accurate and helpful information",
                    "Support growth and development",
                    "Advocate for member needs"
                ],
                "examples": [
                    "Recommending appropriate resources",
                    "Celebrating member progress",
                    "Offering encouragement during challenges"
                ]
            },
            EthicalPrinciple.NON_MALEFICENCE: {
                "description": "Do no harm through action or inaction",
                "guidelines": [
                    "Avoid practices that could cause emotional harm",
                    "Recognize limits of competence",
                    "Refer when appropriate",
                    "Monitor for signs of distress"
                ],
                "examples": [
                    "Not providing therapy when scope is peer support",
                    "Avoiding retraumatization",
                    "Recognizing when professional help is needed"
                ]
            },
            EthicalPrinciple.AUTONOMY: {
                "description": "Respect member's right to self-determination",
                "guidelines": [
                    "Support informed decision-making",
                    "Respect member choices even when disagreeing",
                    "Empower rather than direct",
                    "Obtain consent for actions"
                ],
                "examples": [
                    "Letting members set their own goals",
                    "Respecting pace of change",
                    "Not imposing values or beliefs"
                ]
            },
            EthicalPrinciple.JUSTICE: {
                "description": "Provide fair and equitable treatment",
                "guidelines": [
                    "Treat all members with equal respect",
                    "Allocate resources fairly",
                    "Address systemic barriers",
                    "Avoid discrimination"
                ],
                "examples": [
                    "Equal access to training opportunities",
                    "Accommodating diverse needs",
                    "Challenging inequitable systems"
                ]
            },
            EthicalPrinciple.FIDELITY: {
                "description": "Be faithful to commitments and responsibilities",
                "guidelines": [
                    "Keep promises and commitments",
                    "Be honest and transparent",
                    "Maintain professional standards",
                    "Honor role responsibilities"
                ],
                "examples": [
                    "Following through on scheduled sessions",
                    "Being truthful about limitations",
                    "Upholding program policies"
                ]
            },
            EthicalPrinciple.CONFIDENTIALITY: {
                "description": "Protect member privacy and sensitive information",
                "guidelines": [
                    "Share information only with consent",
                    "Use secure communication channels",
                    "Know limits of confidentiality",
                    "Explain privacy policies clearly"
                ],
                "examples": [
                    "Not discussing members publicly",
                    "Securing member records",
                    "Obtaining consent before sharing information"
                ]
            },
            EthicalPrinciple.CULTURAL_COMPETENCE: {
                "description": "Respect and honor diversity in all forms",
                "guidelines": [
                    "Recognize own biases and privilege",
                    "Learn about diverse cultures and identities",
                    "Adapt approach to cultural context",
                    "Challenge discriminatory practices"
                ],
                "examples": [
                    "Using appropriate pronouns",
                    "Respecting cultural practices",
                    "Acknowledging intersectionality"
                ]
            },
            EthicalPrinciple.PROFESSIONAL_BOUNDARIES: {
                "description": "Maintain appropriate relationships and boundaries",
                "guidelines": [
                    "Keep relationships professional",
                    "Avoid dual relationships",
                    "Set clear expectations",
                    "Manage self-disclosure appropriately"
                ],
                "examples": [
                    "Not becoming friends on social media",
                    "Declining inappropriate requests",
                    "Maintaining emotional boundaries"
                ]
            }
        }

    def _initialize_boundaries(self) -> Dict[str, List[str]]:
        """Define professional boundaries"""
        return {
            "acceptable": [
                "Sharing relevant professional experience",
                "Expressing appropriate empathy",
                "Offering encouragement and support",
                "Providing education and resources",
                "Celebrating member achievements",
                "Professional communication during work hours"
            ],
            "cautionary": [
                "Limited self-disclosure for therapeutic purpose",
                "Accepting small gifts in cultural context",
                "Brief contact outside scheduled sessions in emergencies",
                "Appropriate touch (handshake, fist bump) with consent"
            ],
            "prohibited": [
                "Romantic or sexual relationships",
                "Financial relationships (lending money, business deals)",
                "Excessive self-disclosure about personal problems",
                "Contact outside professional context",
                "Accepting expensive gifts",
                "Providing services outside scope of practice",
                "Sharing personal contact information",
                "Social media connections with current members"
            ]
        }

    def _initialize_red_flags(self) -> Dict[str, List[str]]:
        """Define red flags requiring immediate attention"""
        return {
            "safety_concerns": [
                "Suicidal ideation or plan",
                "Homicidal thoughts or intent",
                "Active self-harm",
                "Severe substance withdrawal",
                "Psychotic symptoms with danger",
                "Domestic violence (imminent danger)"
            ],
            "abuse_or_neglect": [
                "Child abuse or neglect",
                "Elder abuse or neglect",
                "Abuse of vulnerable adult",
                "Human trafficking indicators"
            ],
            "boundary_violations": [
                "Requests for personal relationship",
                "Inappropriate contact attempts",
                "Gift-giving with strings attached",
                "Attempts to meet outside professional context"
            ],
            "scope_exceeded": [
                "Requests for therapy or counseling",
                "Medical advice requests",
                "Legal advice requests",
                "Complex mental health crises"
            ]
        }

    def _initialize_reporting_triggers(self) -> List[str]:
        """Define situations requiring mandated reporting"""
        return [
            "Suspected child abuse or neglect",
            "Suspected elder abuse or neglect",
            "Suspected abuse of vulnerable adult",
            "Imminent danger to self",
            "Imminent danger to others",
            "Human trafficking",
            "As required by specific state/jurisdiction laws"
        ]

    def evaluate_situation(self, situation_description: str, context: Dict) -> EthicalDecision:
        """
        Evaluate a situation using ethical framework

        Args:
            situation_description: Description of the situation
            context: Additional context (member info, relationship history, etc.)

        Returns:
            EthicalDecision with recommendation and action steps
        """
        # Analyze for red flags
        red_flags_found = self._check_red_flags(situation_description)

        # Identify ethical principles involved
        principles_involved = self._identify_principles(situation_description)

        # Determine dilemma type if any
        dilemma_type = self._categorize_dilemma(situation_description, red_flags_found)

        # Assess risk level
        risk_level = self._assess_risk(red_flags_found, dilemma_type)

        # Generate recommendation
        recommendation = self._generate_recommendation(
            situation_description,
            red_flags_found,
            principles_involved,
            dilemma_type,
            risk_level
        )

        # Determine if escalation needed
        escalation_needed = risk_level in ["high", "critical"] or bool(red_flags_found.get("safety_concerns"))

        # Generate action steps
        action_steps = self._generate_action_steps(
            dilemma_type,
            red_flags_found,
            escalation_needed,
            risk_level
        )

        # Create rationale
        rationale = self._create_rationale(principles_involved, red_flags_found, risk_level)

        return EthicalDecision(
            situation=situation_description,
            dilemma_type=dilemma_type,
            principles_involved=principles_involved,
            recommendation=recommendation,
            rationale=rationale,
            action_steps=action_steps,
            escalation_needed=escalation_needed,
            risk_level=risk_level
        )

    def _check_red_flags(self, situation: str) -> Dict[str, List[str]]:
        """Check situation for red flags"""
        found_flags = {}
        situation_lower = situation.lower()

        for category, flags in self.red_flags.items():
            matching_flags = []
            for flag in flags:
                # Simple keyword matching (in production, use more sophisticated NLP)
                keywords = flag.lower().split()
                if any(keyword in situation_lower for keyword in keywords):
                    matching_flags.append(flag)

            if matching_flags:
                found_flags[category] = matching_flags

        return found_flags

    def _identify_principles(self, situation: str) -> List[EthicalPrinciple]:
        """Identify which ethical principles are relevant"""
        # In production, this would use NLP to better understand context
        # For now, using keyword matching
        principles = []
        situation_lower = situation.lower()

        if any(word in situation_lower for word in ["harm", "hurt", "danger", "safety"]):
            principles.append(EthicalPrinciple.NON_MALEFICENCE)

        if any(word in situation_lower for word in ["help", "support", "benefit", "improve"]):
            principles.append(EthicalPrinciple.BENEFICENCE)

        if any(word in situation_lower for word in ["choice", "decide", "autonomy", "control"]):
            principles.append(EthicalPrinciple.AUTONOMY)

        if any(word in situation_lower for word in ["fair", "unfair", "discriminat", "equal"]):
            principles.append(EthicalPrinciple.JUSTICE)

        if any(word in situation_lower for word in ["private", "confidential", "secret", "share"]):
            principles.append(EthicalPrinciple.CONFIDENTIALITY)

        if any(word in situation_lower for word in ["boundary", "relationship", "personal", "professional"]):
            principles.append(EthicalPrinciple.PROFESSIONAL_BOUNDARIES)

        if any(word in situation_lower for word in ["culture", "diversity", "identity", "race", "lgbtq"]):
            principles.append(EthicalPrinciple.CULTURAL_COMPETENCE)

        # If no principles identified, default to beneficence and non-maleficence
        if not principles:
            principles = [EthicalPrinciple.BENEFICENCE, EthicalPrinciple.NON_MALEFICENCE]

        return principles

    def _categorize_dilemma(self, situation: str, red_flags: Dict) -> Optional[EthicalDilemmaType]:
        """Categorize the type of ethical dilemma"""
        situation_lower = situation.lower()

        if red_flags.get("safety_concerns"):
            return EthicalDilemmaType.MANDATED_REPORTING

        if red_flags.get("abuse_or_neglect"):
            return EthicalDilemmaType.MANDATED_REPORTING

        if red_flags.get("boundary_violations"):
            return EthicalDilemmaType.BOUNDARY_VIOLATION

        if red_flags.get("scope_exceeded"):
            return EthicalDilemmaType.SCOPE_EXCEEDED

        if "boundary" in situation_lower or "personal" in situation_lower:
            return EthicalDilemmaType.BOUNDARY_VIOLATION

        if "confidential" in situation_lower or "privacy" in situation_lower:
            return EthicalDilemmaType.CONFIDENTIALITY_BREACH

        return None

    def _assess_risk(self, red_flags: Dict, dilemma_type: Optional[EthicalDilemmaType]) -> str:
        """Assess risk level of situation"""
        if red_flags.get("safety_concerns") or red_flags.get("abuse_or_neglect"):
            return "critical"

        if dilemma_type in [EthicalDilemmaType.MANDATED_REPORTING, EthicalDilemmaType.HARM_RISK]:
            return "high"

        if red_flags.get("boundary_violations") or red_flags.get("scope_exceeded"):
            return "medium"

        if dilemma_type in [EthicalDilemmaType.BOUNDARY_VIOLATION, EthicalDilemmaType.SCOPE_EXCEEDED]:
            return "medium"

        return "low"

    def _generate_recommendation(
        self,
        situation: str,
        red_flags: Dict,
        principles: List[EthicalPrinciple],
        dilemma_type: Optional[EthicalDilemmaType],
        risk_level: str
    ) -> str:
        """Generate ethical recommendation"""

        if risk_level == "critical":
            return "IMMEDIATE ACTION REQUIRED: Contact emergency services and supervisor immediately. " \
                   "Ensure safety of all parties. Document thoroughly."

        if risk_level == "high":
            return "Escalate to supervisor immediately and follow mandated reporting protocols. " \
                   "Do not delay action."

        if dilemma_type == EthicalDilemmaType.BOUNDARY_VIOLATION:
            return "Kindly but firmly reinforce professional boundaries. Explain the importance of " \
                   "maintaining appropriate relationships. Document the interaction and consult supervisor."

        if dilemma_type == EthicalDilemmaType.SCOPE_EXCEEDED:
            return "Acknowledge the request but explain it is outside your scope of practice. " \
                   "Provide appropriate referrals to qualified professionals."

        if dilemma_type == EthicalDilemmaType.CONFIDENTIALITY_BREACH:
            return "Protect member confidentiality unless there is imminent danger or legal requirement. " \
                   "Consult with supervisor about information sharing."

        # Default recommendation based on principles
        if EthicalPrinciple.AUTONOMY in principles:
            return "Support member's autonomy while providing information for informed decision-making. " \
                   "Respect their choices even if you would choose differently."

        return "Apply ethical principles of beneficence and non-maleficence. Act in member's best interest " \
               "while doing no harm. Consult supervisor if uncertain."

    def _generate_action_steps(
        self,
        dilemma_type: Optional[EthicalDilemmaType],
        red_flags: Dict,
        escalation_needed: bool,
        risk_level: str
    ) -> List[str]:
        """Generate specific action steps"""

        if risk_level == "critical":
            return [
                "1. Ensure immediate safety of all parties",
                "2. Contact emergency services (911) if imminent danger",
                "3. Contact supervisor/clinical director immediately",
                "4. Stay with person if suicidal until help arrives",
                "5. Document everything thoroughly",
                "6. Complete incident report",
                "7. Arrange follow-up care"
            ]

        if escalation_needed:
            return [
                "1. Contact supervisor immediately",
                "2. Follow mandated reporting protocols if applicable",
                "3. Document situation thoroughly",
                "4. Do not promise confidentiality you cannot keep",
                "5. Ensure member safety while waiting for help",
                "6. Follow up as directed by supervisor"
            ]

        if dilemma_type == EthicalDilemmaType.BOUNDARY_VIOLATION:
            return [
                "1. Address boundary issue directly but kindly",
                "2. Explain professional relationship parameters",
                "3. Redirect to appropriate professional relationship",
                "4. Document the interaction",
                "5. Consult with supervisor",
                "6. Monitor for future boundary issues"
            ]

        if dilemma_type == EthicalDilemmaType.SCOPE_EXCEEDED:
            return [
                "1. Acknowledge the person's need",
                "2. Explain scope of your role",
                "3. Provide appropriate referrals",
                "4. Offer to support them in accessing resources",
                "5. Document referral made",
                "6. Follow up on whether they connected with resources"
            ]

        return [
            "1. Consider all relevant ethical principles",
            "2. Consult with supervisor if uncertain",
            "3. Document your decision-making process",
            "4. Take action that prioritizes member wellbeing",
            "5. Follow up to ensure positive outcome",
            "6. Reflect on the situation for learning"
        ]

    def _create_rationale(
        self,
        principles: List[EthicalPrinciple],
        red_flags: Dict,
        risk_level: str
    ) -> str:
        """Create rationale for recommendation"""

        rationale_parts = []

        if red_flags:
            rationale_parts.append(
                f"This situation presents {risk_level} risk due to identified red flags. "
                f"Immediate attention is required to prevent harm."
            )

        if principles:
            principle_names = [p.value.replace('_', ' ').title() for p in principles]
            rationale_parts.append(
                f"This recommendation is guided by the ethical principles of "
                f"{', '.join(principle_names)}."
            )

        rationale_parts.append(
            "The primary consideration is the wellbeing and safety of all parties involved "
            "while maintaining professional standards and boundaries."
        )

        return " ".join(rationale_parts)

    def check_boundary_appropriateness(self, action: str) -> Tuple[bool, str, str]:
        """
        Check if an action is within appropriate boundaries

        Returns:
            (is_appropriate, category, explanation)
        """
        action_lower = action.lower()

        # Check prohibited actions
        for prohibited in self.boundaries["prohibited"]:
            if any(word in action_lower for word in prohibited.lower().split()):
                return (
                    False,
                    "prohibited",
                    f"This action is prohibited as it may constitute: {prohibited}. "
                    f"Please maintain professional boundaries."
                )

        # Check cautionary actions
        for cautionary in self.boundaries["cautionary"]:
            if any(word in action_lower for word in cautionary.lower().split()):
                return (
                    True,
                    "cautionary",
                    f"This action requires careful consideration: {cautionary}. "
                    f"Proceed with caution and consult supervisor if uncertain."
                )

        # Check acceptable actions
        for acceptable in self.boundaries["acceptable"]:
            if any(word in action_lower for word in acceptable.lower().split()):
                return (
                    True,
                    "acceptable",
                    f"This action is within professional boundaries: {acceptable}."
                )

        # Default to cautionary
        return (
            True,
            "cautionary",
            "This action should be evaluated carefully to ensure it maintains professional boundaries."
        )

    def requires_mandated_reporting(self, situation: str) -> Tuple[bool, List[str]]:
        """
        Determine if situation requires mandated reporting

        Returns:
            (requires_reporting, list of triggers)
        """
        situation_lower = situation.lower()
        triggers_found = []

        for trigger in self.mandated_reporting_triggers:
            trigger_keywords = trigger.lower().split()
            if any(keyword in situation_lower for keyword in trigger_keywords):
                triggers_found.append(trigger)

        return (bool(triggers_found), triggers_found)

    def get_principle_guidance(self, principle: EthicalPrinciple) -> Dict:
        """Get detailed guidance for a specific ethical principle"""
        return self.principles.get(principle, {})


# Example usage
if __name__ == "__main__":
    framework = EthicalFramework()

    # Test case 1: Boundary violation
    print("=" * 60)
    print("TEST CASE 1: Boundary Violation")
    print("=" * 60)
    decision1 = framework.evaluate_situation(
        "A trainee has asked for my personal phone number to text me outside of sessions",
        {"member_id": "M001", "relationship_duration": "2 weeks"}
    )
    print(f"Risk Level: {decision1.risk_level}")
    print(f"Recommendation: {decision1.recommendation}")
    print(f"Action Steps:")
    for step in decision1.action_steps:
        print(f"  {step}")

    # Test case 2: Safety concern
    print("\n" + "=" * 60)
    print("TEST CASE 2: Safety Concern")
    print("=" * 60)
    decision2 = framework.evaluate_situation(
        "A member just disclosed that they are having suicidal thoughts and have a plan",
        {"member_id": "M002", "immediate_danger": True}
    )
    print(f"Risk Level: {decision2.risk_level}")
    print(f"Escalation Needed: {decision2.escalation_needed}")
    print(f"Recommendation: {decision2.recommendation}")
    print(f"Action Steps:")
    for step in decision2.action_steps:
        print(f"  {step}")

    # Test case 3: Scope exceeded
    print("\n" + "=" * 60)
    print("TEST CASE 3: Scope Exceeded")
    print("=" * 60)
    decision3 = framework.evaluate_situation(
        "A member is asking me to provide therapy for their trauma",
        {"member_id": "M003"}
    )
    print(f"Risk Level: {decision3.risk_level}")
    print(f"Recommendation: {decision3.recommendation}")
