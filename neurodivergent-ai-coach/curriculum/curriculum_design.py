"""
NeuroDivergent AI Coach - Curriculum Design

This module defines the comprehensive training curriculum for peer assistants,
counselors, and managers in the Integrated Healthy Empowerment Program.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class TrainingLevel(Enum):
    """Training progression levels"""
    QUALIFIED_MEMBER = 1
    PEER_ASSISTANT = 2
    PEER_COUNSELOR = 3
    PEER_MANAGER = 4


class ModuleType(Enum):
    """Types of training modules"""
    KNOWLEDGE = "knowledge"  # Theoretical understanding
    SKILLS = "skills"  # Practical skills development
    PRACTICE = "practice"  # Hands-on practice scenarios
    ASSESSMENT = "assessment"  # Evaluation and testing
    REFLECTION = "reflection"  # Self-reflection and growth


@dataclass
class LearningObjective:
    """Individual learning objective within a module"""
    id: str
    description: str
    competency: str  # What competency this builds
    assessment_criteria: List[str]  # How to measure mastery


@dataclass
class TrainingModule:
    """Individual training module"""
    id: str
    title: str
    description: str
    module_type: ModuleType
    duration_hours: float
    learning_objectives: List[LearningObjective]
    prerequisites: List[str] = field(default_factory=list)
    content_sections: List[Dict] = field(default_factory=list)
    practice_scenarios: List[Dict] = field(default_factory=list)
    resources: List[str] = field(default_factory=list)


@dataclass
class TrainingLevel:
    """Complete training level with all modules"""
    level: TrainingLevel
    title: str
    description: str
    duration_weeks: tuple  # (min, max)
    compensation_type: str
    hours_per_week: tuple  # (min, max)
    modules: List[TrainingModule]
    qualification_criteria: Dict
    advancement_criteria: Dict


class CurriculumDesign:
    """
    Complete curriculum design for the NeuroDivergent AI Coach system.

    This class defines the entire training progression from qualified member
    to full-time peer manager, including all modules, objectives, and criteria.
    """

    def __init__(self):
        self.curriculum = self._build_curriculum()

    def _build_curriculum(self) -> Dict[int, 'TrainingLevel']:
        """Build the complete curriculum structure"""
        return {
            1: self._build_qualified_member_level(),
            2: self._build_peer_assistant_level(),
            3: self._build_peer_counselor_level(),
            4: self._build_peer_manager_level()
        }

    def _build_qualified_member_level(self) -> 'TrainingLevel':
        """Level 1: Qualified Member - Introduction and Orientation"""

        modules = [
            TrainingModule(
                id="L1M1",
                title="Welcome to Peer Support Training",
                description="Introduction to the peer support role and IHEP mission",
                module_type=ModuleType.KNOWLEDGE,
                duration_hours=2.0,
                learning_objectives=[
                    LearningObjective(
                        id="L1M1-LO1",
                        description="Understand the IHEP mission and values",
                        competency="Program Knowledge",
                        assessment_criteria=[
                            "Can articulate IHEP's mission in own words",
                            "Can identify core values and principles",
                            "Understands holistic health approach"
                        ]
                    ),
                    LearningObjective(
                        id="L1M1-LO2",
                        description="Define peer support and its importance",
                        competency="Role Understanding",
                        assessment_criteria=[
                            "Can explain what peer support means",
                            "Understands difference between peer support and therapy",
                            "Recognizes value of lived experience"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "What is IHEP?",
                        "topics": ["Mission and vision", "Holistic health model", "Community impact"]
                    },
                    {
                        "section": "The Power of Peer Support",
                        "topics": ["Lived experience", "Mutual support", "Hope and recovery"]
                    },
                    {
                        "section": "Your Journey Ahead",
                        "topics": ["Training overview", "Career pathway", "Support available"]
                    }
                ],
                resources=[
                    "IHEP Program Handbook",
                    "Peer Support Research Articles",
                    "Welcome Video Series"
                ]
            ),

            TrainingModule(
                id="L1M2",
                title="Understanding the IHEP Platform",
                description="Comprehensive overview of ihep.app features and tools",
                module_type=ModuleType.KNOWLEDGE,
                duration_hours=3.0,
                learning_objectives=[
                    LearningObjective(
                        id="L1M2-LO1",
                        description="Navigate all platform features confidently",
                        competency="Technical Proficiency",
                        assessment_criteria=[
                            "Can demonstrate all major platform features",
                            "Understands data privacy and security",
                            "Can troubleshoot common user issues"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Platform Overview",
                        "topics": ["Dashboard", "Goal setting", "Progress tracking", "Community features"]
                    },
                    {
                        "section": "Privacy and Security",
                        "topics": ["Data protection", "User confidentiality", "Reporting concerns"]
                    }
                ]
            ),

            TrainingModule(
                id="L1M3",
                title="Ethics and Boundaries in Peer Support",
                description="Foundational ethical principles and professional boundaries",
                module_type=ModuleType.KNOWLEDGE,
                duration_hours=4.0,
                learning_objectives=[
                    LearningObjective(
                        id="L1M3-LO1",
                        description="Apply ethical principles in peer support scenarios",
                        competency="Ethical Practice",
                        assessment_criteria=[
                            "Can identify ethical dilemmas",
                            "Applies ethical decision-making framework",
                            "Maintains appropriate boundaries"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Core Ethical Principles",
                        "topics": ["Beneficence", "Non-maleficence", "Autonomy", "Justice", "Fidelity"]
                    },
                    {
                        "section": "Professional Boundaries",
                        "topics": ["Dual relationships", "Self-disclosure", "Scope of practice"]
                    },
                    {
                        "section": "Confidentiality",
                        "topics": ["Privacy protection", "Mandated reporting", "Information sharing"]
                    }
                ],
                practice_scenarios=[
                    {
                        "scenario": "A member asks for your personal phone number",
                        "learning_focus": "Maintaining boundaries"
                    },
                    {
                        "scenario": "You learn concerning information about a member",
                        "learning_focus": "Confidentiality and duty to report"
                    }
                ]
            ),

            TrainingModule(
                id="L1M4",
                title="Self-Care and Wellness for Peer Supporters",
                description="Building personal resilience and preventing burnout",
                module_type=ModuleType.SKILLS,
                duration_hours=3.0,
                learning_objectives=[
                    LearningObjective(
                        id="L1M4-LO1",
                        description="Develop personal self-care plan",
                        competency="Self-Management",
                        assessment_criteria=[
                            "Creates comprehensive self-care plan",
                            "Recognizes signs of burnout",
                            "Knows when to seek support"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Understanding Compassion Fatigue",
                        "topics": ["Warning signs", "Prevention strategies", "Recovery approaches"]
                    },
                    {
                        "section": "Building Resilience",
                        "topics": ["Stress management", "Mindfulness", "Work-life balance"]
                    }
                ]
            ),

            TrainingModule(
                id="L1M5",
                title="Introduction Assessment",
                description="Evaluation of foundational knowledge and readiness",
                module_type=ModuleType.ASSESSMENT,
                duration_hours=2.0,
                learning_objectives=[
                    LearningObjective(
                        id="L1M5-LO1",
                        description="Demonstrate readiness for peer assistant training",
                        competency="Overall Readiness",
                        assessment_criteria=[
                            "Scores 80% or higher on knowledge assessment",
                            "Demonstrates understanding of ethics",
                            "Shows self-awareness and commitment"
                        ]
                    )
                ],
                prerequisites=["L1M1", "L1M2", "L1M3", "L1M4"]
            )
        ]

        return TrainingLevel(
            level=TrainingLevel.QUALIFIED_MEMBER,
            title="Foundation: Qualified Member",
            description="Orientation and foundational knowledge for peer support",
            duration_weeks=(2, 4),
            compensation_type="None (prerequisite for paid training)",
            hours_per_week=(3, 5),
            modules=modules,
            qualification_criteria={
                "engagement_score": 75,
                "adherence_score": 70,
                "months_active": 3,
                "completion_rate": 80,
                "community_participation": "regular",
                "good_standing": True
            },
            advancement_criteria={
                "complete_all_modules": True,
                "assessment_score": 80,
                "attendance_rate": 90,
                "express_continued_interest": True
            }
        )

    def _build_peer_assistant_level(self) -> 'TrainingLevel':
        """Level 2: Peer Assistant - Core Skills Training"""

        modules = [
            TrainingModule(
                id="L2M1",
                title="Active Listening and Communication Skills",
                description="Master the art of empathetic listening and effective communication",
                module_type=ModuleType.SKILLS,
                duration_hours=6.0,
                learning_objectives=[
                    LearningObjective(
                        id="L2M1-LO1",
                        description="Demonstrate active listening techniques",
                        competency="Communication",
                        assessment_criteria=[
                            "Uses reflective listening",
                            "Asks open-ended questions",
                            "Demonstrates empathy",
                            "Avoids judgment and advice-giving"
                        ]
                    ),
                    LearningObjective(
                        id="L2M1-LO2",
                        description="Adapt communication style to individual needs",
                        competency="Flexibility",
                        assessment_criteria=[
                            "Recognizes communication preferences",
                            "Adjusts approach for different personalities",
                            "Maintains clarity and warmth"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Foundations of Active Listening",
                        "topics": ["Attending", "Reflecting", "Clarifying", "Summarizing"]
                    },
                    {
                        "section": "Nonverbal Communication",
                        "topics": ["Body language", "Tone of voice", "Digital communication cues"]
                    },
                    {
                        "section": "Barriers to Effective Listening",
                        "topics": ["Internal barriers", "External distractions", "Overcoming obstacles"]
                    }
                ],
                practice_scenarios=[
                    {
                        "scenario": "Member expresses frustration with lack of progress",
                        "learning_focus": "Reflective listening and validation"
                    },
                    {
                        "scenario": "Member shares exciting success",
                        "learning_focus": "Celebrating achievements authentically"
                    }
                ]
            ),

            TrainingModule(
                id="L2M2",
                title="Building Rapport and Trust",
                description="Create authentic connections that foster growth",
                module_type=ModuleType.SKILLS,
                duration_hours=5.0,
                learning_objectives=[
                    LearningObjective(
                        id="L2M2-LO1",
                        description="Establish therapeutic rapport with members",
                        competency="Relationship Building",
                        assessment_criteria=[
                            "Creates safe, welcoming environment",
                            "Demonstrates genuineness and warmth",
                            "Builds trust through consistency"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Elements of Rapport",
                        "topics": ["Warmth", "Genuineness", "Unconditional positive regard"]
                    },
                    {
                        "section": "Trust-Building Strategies",
                        "topics": ["Reliability", "Transparency", "Respect for autonomy"]
                    }
                ]
            ),

            TrainingModule(
                id="L2M3",
                title="Goal Setting and Progress Tracking",
                description="Help members set and achieve meaningful goals",
                module_type=ModuleType.SKILLS,
                duration_hours=5.0,
                learning_objectives=[
                    LearningObjective(
                        id="L2M3-LO1",
                        description="Guide members in SMART goal development",
                        competency="Goal Facilitation",
                        assessment_criteria=[
                            "Helps create specific, measurable goals",
                            "Ensures goals are member-driven",
                            "Supports accountability without pressure"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "SMART Goals Framework",
                        "topics": ["Specific", "Measurable", "Achievable", "Relevant", "Time-bound"]
                    },
                    {
                        "section": "Motivational Strategies",
                        "topics": ["Intrinsic vs extrinsic motivation", "Overcoming obstacles", "Celebrating wins"]
                    }
                ]
            ),

            TrainingModule(
                id="L2M4",
                title="Understanding Mental Health and Wellness",
                description="Foundational knowledge of mental health conditions and recovery",
                module_type=ModuleType.KNOWLEDGE,
                duration_hours=8.0,
                learning_objectives=[
                    LearningObjective(
                        id="L2M4-LO1",
                        description="Recognize common mental health challenges",
                        competency="Mental Health Literacy",
                        assessment_criteria=[
                            "Identifies signs of common conditions",
                            "Understands recovery-oriented approach",
                            "Knows when to escalate to professional"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Common Mental Health Conditions",
                        "topics": ["Depression", "Anxiety", "PTSD", "Substance use"]
                    },
                    {
                        "section": "Recovery and Resilience",
                        "topics": ["Recovery model", "Hope and healing", "Strength-based approach"]
                    },
                    {
                        "section": "Scope of Practice",
                        "topics": ["What peer supporters can/cannot do", "When to refer", "Crisis resources"]
                    }
                ]
            ),

            TrainingModule(
                id="L2M5",
                title="Practical Application: Supervised Practice",
                description="Apply skills through supervised member interactions",
                module_type=ModuleType.PRACTICE,
                duration_hours=12.0,
                learning_objectives=[
                    LearningObjective(
                        id="L2M5-LO1",
                        description="Successfully support members under supervision",
                        competency="Applied Practice",
                        assessment_criteria=[
                            "Completes 10+ supervised interactions",
                            "Receives positive feedback from supervisor",
                            "Demonstrates continuous improvement"
                        ]
                    )
                ],
                prerequisites=["L2M1", "L2M2", "L2M3", "L2M4"]
            ),

            TrainingModule(
                id="L2M6",
                title="Peer Assistant Certification Assessment",
                description="Comprehensive evaluation of peer assistant competencies",
                module_type=ModuleType.ASSESSMENT,
                duration_hours=3.0,
                learning_objectives=[
                    LearningObjective(
                        id="L2M6-LO1",
                        description="Demonstrate peer assistant competency",
                        competency="Overall Competency",
                        assessment_criteria=[
                            "Knowledge assessment: 85%+",
                            "Skills demonstration: Proficient",
                            "Supervisor recommendation: Positive"
                        ]
                    )
                ],
                prerequisites=["L2M1", "L2M2", "L2M3", "L2M4", "L2M5"]
            )
        ]

        return TrainingLevel(
            level=TrainingLevel.PEER_ASSISTANT,
            title="Core Skills: Peer Assistant",
            description="Develop essential peer support skills through training and supervised practice",
            duration_weeks=(4, 8),
            compensation_type="Training stipend ($15-20/hour during training)",
            hours_per_week=(5, 10),
            modules=modules,
            qualification_criteria={
                "completed_level_1": True,
                "level_1_assessment_score": 80,
                "continued_engagement": True,
                "supervisor_approval": True
            },
            advancement_criteria={
                "complete_all_modules": True,
                "assessment_score": 85,
                "supervised_practice_hours": 12,
                "supervisor_recommendation": "positive",
                "member_feedback_average": 4.0  # out of 5
            }
        )

    def _build_peer_counselor_level(self) -> 'TrainingLevel':
        """Level 3: Peer Counselor - Advanced Skills and Independence"""

        modules = [
            TrainingModule(
                id="L3M1",
                title="Motivational Interviewing",
                description="Master MI techniques to support behavior change",
                module_type=ModuleType.SKILLS,
                duration_hours=10.0,
                learning_objectives=[
                    LearningObjective(
                        id="L3M1-LO1",
                        description="Apply MI principles and techniques effectively",
                        competency="Advanced Counseling",
                        assessment_criteria=[
                            "Demonstrates MI spirit (partnership, acceptance, compassion, evocation)",
                            "Uses OARS skills proficiently",
                            "Recognizes and responds to change talk"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "MI Foundations",
                        "topics": ["Spirit of MI", "Processes of change", "Righting reflex"]
                    },
                    {
                        "section": "OARS Skills",
                        "topics": ["Open questions", "Affirmations", "Reflections", "Summaries"]
                    },
                    {
                        "section": "Eliciting Change Talk",
                        "topics": ["Recognizing change talk", "Evoking motivation", "Strengthening commitment"]
                    }
                ],
                practice_scenarios=[
                    {
                        "scenario": "Member is ambivalent about medication adherence",
                        "learning_focus": "Exploring ambivalence with MI"
                    },
                    {
                        "scenario": "Member wants to change but feels stuck",
                        "learning_focus": "Eliciting and strengthening change talk"
                    }
                ]
            ),

            TrainingModule(
                id="L3M2",
                title="Crisis Support and De-escalation",
                description="Respond effectively to mental health crises",
                module_type=ModuleType.SKILLS,
                duration_hours=8.0,
                learning_objectives=[
                    LearningObjective(
                        id="L3M2-LO1",
                        description="Manage crisis situations safely and effectively",
                        competency="Crisis Management",
                        assessment_criteria=[
                            "Recognizes crisis warning signs",
                            "Uses de-escalation techniques",
                            "Knows when and how to escalate",
                            "Maintains calm under pressure"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Understanding Crisis",
                        "topics": ["Types of crises", "Crisis development", "Assessing severity"]
                    },
                    {
                        "section": "De-escalation Techniques",
                        "topics": ["Verbal de-escalation", "Creating safety", "Grounding techniques"]
                    },
                    {
                        "section": "Safety Planning",
                        "topics": ["Suicide risk assessment", "Safety plans", "Crisis resources"]
                    },
                    {
                        "section": "Self-Care After Crisis",
                        "topics": ["Debriefing", "Processing vicarious trauma", "Seeking support"]
                    }
                ]
            ),

            TrainingModule(
                id="L3M3",
                title="Trauma-Informed Care",
                description="Understand and respond to trauma with sensitivity",
                module_type=ModuleType.KNOWLEDGE,
                duration_hours=6.0,
                learning_objectives=[
                    LearningObjective(
                        id="L3M3-LO1",
                        description="Provide trauma-informed peer support",
                        competency="Trauma Competency",
                        assessment_criteria=[
                            "Understands impact of trauma",
                            "Avoids re-traumatization",
                            "Creates trauma-sensitive environment"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Understanding Trauma",
                        "topics": ["Types of trauma", "Trauma responses", "Intergenerational trauma"]
                    },
                    {
                        "section": "Trauma-Informed Principles",
                        "topics": ["Safety", "Trustworthiness", "Choice", "Collaboration", "Empowerment"]
                    }
                ]
            ),

            TrainingModule(
                id="L3M4",
                title="Cultural Competence and Diversity",
                description="Provide culturally responsive and inclusive support",
                module_type=ModuleType.SKILLS,
                duration_hours=6.0,
                learning_objectives=[
                    LearningObjective(
                        id="L3M4-LO1",
                        description="Demonstrate cultural humility and competence",
                        competency="Cultural Competence",
                        assessment_criteria=[
                            "Recognizes own biases and privilege",
                            "Respects diverse identities and experiences",
                            "Adapts support to cultural context"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Understanding Diversity",
                        "topics": ["Race and ethnicity", "LGBTQ+ identities", "Disability", "Religion", "Socioeconomic status"]
                    },
                    {
                        "section": "Cultural Humility",
                        "topics": ["Self-reflection", "Lifelong learning", "Power dynamics"]
                    }
                ]
            ),

            TrainingModule(
                id="L3M5",
                title="Group Facilitation Skills",
                description="Lead and facilitate peer support groups",
                module_type=ModuleType.SKILLS,
                duration_hours=8.0,
                learning_objectives=[
                    LearningObjective(
                        id="L3M5-LO1",
                        description="Effectively facilitate peer support groups",
                        competency="Group Leadership",
                        assessment_criteria=[
                            "Creates inclusive group environment",
                            "Manages group dynamics",
                            "Facilitates productive discussions"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Group Development Stages",
                        "topics": ["Forming", "Storming", "Norming", "Performing"]
                    },
                    {
                        "section": "Facilitation Techniques",
                        "topics": ["Setting norms", "Managing conflict", "Encouraging participation"]
                    }
                ]
            ),

            TrainingModule(
                id="L3M6",
                title="Advanced Practice: Independent Support",
                description="Provide peer support with minimal supervision",
                module_type=ModuleType.PRACTICE,
                duration_hours=20.0,
                learning_objectives=[
                    LearningObjective(
                        id="L3M6-LO1",
                        description="Independently support members effectively",
                        competency="Independent Practice",
                        assessment_criteria=[
                            "Manages caseload independently",
                            "Seeks consultation appropriately",
                            "Maintains quality standards"
                        ]
                    )
                ],
                prerequisites=["L3M1", "L3M2", "L3M3", "L3M4", "L3M5"]
            ),

            TrainingModule(
                id="L3M7",
                title="Peer Counselor Certification",
                description="Comprehensive certification assessment",
                module_type=ModuleType.ASSESSMENT,
                duration_hours=4.0,
                learning_objectives=[
                    LearningObjective(
                        id="L3M7-LO1",
                        description="Demonstrate peer counselor competency",
                        competency="Professional Competency",
                        assessment_criteria=[
                            "Knowledge assessment: 90%+",
                            "Skills demonstration: Advanced proficiency",
                            "Independent practice evaluation: Excellent"
                        ]
                    )
                ],
                prerequisites=["L3M1", "L3M2", "L3M3", "L3M4", "L3M5", "L3M6"]
            )
        ]

        return TrainingLevel(
            level=TrainingLevel.PEER_COUNSELOR,
            title="Advanced Practice: Peer Counselor",
            description="Develop advanced counseling skills and independent practice capability",
            duration_weeks=(8, 12),
            compensation_type="Part-time employment ($18-25/hour)",
            hours_per_week=(15, 25),
            modules=modules,
            qualification_criteria={
                "completed_level_2": True,
                "level_2_assessment_score": 85,
                "practice_hours": 12,
                "supervisor_recommendation": "positive",
                "member_satisfaction": 4.0
            },
            advancement_criteria={
                "complete_all_modules": True,
                "assessment_score": 90,
                "independent_practice_hours": 20,
                "supervisor_evaluation": "excellent",
                "member_feedback_average": 4.5,
                "crisis_management_competency": True
            }
        )

    def _build_peer_manager_level(self) -> 'TrainingLevel':
        """Level 4: Peer Manager - Leadership and Program Development"""

        modules = [
            TrainingModule(
                id="L4M1",
                title="Leadership and Team Management",
                description="Lead and mentor peer support teams",
                module_type=ModuleType.SKILLS,
                duration_hours=12.0,
                learning_objectives=[
                    LearningObjective(
                        id="L4M1-LO1",
                        description="Effectively lead peer support teams",
                        competency="Leadership",
                        assessment_criteria=[
                            "Provides effective supervision",
                            "Mentors junior staff",
                            "Manages team dynamics and conflict"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Leadership Styles and Approaches",
                        "topics": ["Servant leadership", "Transformational leadership", "Situational leadership"]
                    },
                    {
                        "section": "Supervision and Mentoring",
                        "topics": ["Providing feedback", "Coaching for growth", "Performance management"]
                    },
                    {
                        "section": "Team Building",
                        "topics": ["Creating cohesion", "Managing conflict", "Fostering collaboration"]
                    }
                ]
            ),

            TrainingModule(
                id="L4M2",
                title="Program Development and Evaluation",
                description="Design, implement, and evaluate peer support programs",
                module_type=ModuleType.SKILLS,
                duration_hours=10.0,
                learning_objectives=[
                    LearningObjective(
                        id="L4M2-LO1",
                        description="Develop effective peer support programs",
                        competency="Program Development",
                        assessment_criteria=[
                            "Conducts needs assessments",
                            "Designs evidence-based programs",
                            "Implements evaluation frameworks"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Needs Assessment",
                        "topics": ["Identifying gaps", "Stakeholder input", "Data analysis"]
                    },
                    {
                        "section": "Program Design",
                        "topics": ["Logic models", "Evidence-based practices", "Resource planning"]
                    },
                    {
                        "section": "Evaluation and Quality Improvement",
                        "topics": ["Outcome measurement", "Data collection", "Continuous improvement"]
                    }
                ]
            ),

            TrainingModule(
                id="L4M3",
                title="Advanced Case Management",
                description="Manage complex cases and coordinate care",
                module_type=ModuleType.SKILLS,
                duration_hours=8.0,
                learning_objectives=[
                    LearningObjective(
                        id="L4M3-LO1",
                        description="Provide sophisticated case management",
                        competency="Case Management",
                        assessment_criteria=[
                            "Manages complex member situations",
                            "Coordinates with external providers",
                            "Advocates for member needs"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Complex Case Assessment",
                        "topics": ["Multidimensional assessment", "Risk factors", "Protective factors"]
                    },
                    {
                        "section": "Care Coordination",
                        "topics": ["Building partnerships", "Service navigation", "Integrated care"]
                    }
                ]
            ),

            TrainingModule(
                id="L4M4",
                title="Advocacy and Systems Change",
                description="Advocate for members and drive systemic improvements",
                module_type=ModuleType.SKILLS,
                duration_hours=6.0,
                learning_objectives=[
                    LearningObjective(
                        id="L4M4-LO1",
                        description="Engage in effective advocacy efforts",
                        competency="Advocacy",
                        assessment_criteria=[
                            "Advocates for individual members",
                            "Identifies systemic barriers",
                            "Promotes policy changes"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Individual Advocacy",
                        "topics": ["Empowering self-advocacy", "Navigating systems", "Challenging barriers"]
                    },
                    {
                        "section": "Systemic Advocacy",
                        "topics": ["Identifying inequities", "Coalition building", "Policy influence"]
                    }
                ]
            ),

            TrainingModule(
                id="L4M5",
                title="Professional Development and Self-Leadership",
                description="Commit to ongoing growth and ethical practice",
                module_type=ModuleType.REFLECTION,
                duration_hours=4.0,
                learning_objectives=[
                    LearningObjective(
                        id="L4M5-LO1",
                        description="Maintain professional excellence",
                        competency="Professional Development",
                        assessment_criteria=[
                            "Engages in continuous learning",
                            "Practices reflective supervision",
                            "Models ethical leadership"
                        ]
                    )
                ],
                content_sections=[
                    {
                        "section": "Lifelong Learning",
                        "topics": ["Professional development planning", "Staying current", "Certifications"]
                    },
                    {
                        "section": "Reflective Practice",
                        "topics": ["Self-awareness", "Identifying blind spots", "Growth mindset"]
                    }
                ]
            ),

            TrainingModule(
                id="L4M6",
                title="Leadership Practicum",
                description="Apply leadership skills in real-world settings",
                module_type=ModuleType.PRACTICE,
                duration_hours=30.0,
                learning_objectives=[
                    LearningObjective(
                        id="L4M6-LO1",
                        description="Demonstrate leadership in practice",
                        competency="Applied Leadership",
                        assessment_criteria=[
                            "Successfully leads team or program",
                            "Achieves measurable outcomes",
                            "Receives positive stakeholder feedback"
                        ]
                    )
                ],
                prerequisites=["L4M1", "L4M2", "L4M3", "L4M4", "L4M5"]
            ),

            TrainingModule(
                id="L4M7",
                title="Peer Manager Certification",
                description="Final certification as peer manager",
                module_type=ModuleType.ASSESSMENT,
                duration_hours=4.0,
                learning_objectives=[
                    LearningObjective(
                        id="L4M7-LO1",
                        description="Demonstrate peer manager mastery",
                        competency="Leadership Mastery",
                        assessment_criteria=[
                            "Knowledge assessment: 95%+",
                            "Leadership demonstration: Exemplary",
                            "Practicum evaluation: Outstanding"
                        ]
                    )
                ],
                prerequisites=["L4M1", "L4M2", "L4M3", "L4M4", "L4M5", "L4M6"]
            )
        ]

        return TrainingLevel(
            level=TrainingLevel.PEER_MANAGER,
            title="Leadership Excellence: Peer Manager",
            description="Master leadership, program development, and advanced practice",
            duration_weeks=(12, 24),  # Ongoing professional development
            compensation_type="Full-time employment with benefits ($45,000-65,000/year)",
            hours_per_week=(40, 40),
            modules=modules,
            qualification_criteria={
                "completed_level_3": True,
                "level_3_assessment_score": 90,
                "independent_practice_hours": 20,
                "demonstrated_leadership_potential": True,
                "supervisor_evaluation": "excellent"
            },
            advancement_criteria={
                "complete_all_modules": True,
                "assessment_score": 95,
                "leadership_practicum_hours": 30,
                "program_outcomes": "positive",
                "team_satisfaction": 4.5,
                "stakeholder_feedback": "outstanding"
            }
        )

    def get_level(self, level_number: int) -> Optional['TrainingLevel']:
        """Get training level by number"""
        return self.curriculum.get(level_number)

    def get_module(self, module_id: str) -> Optional[TrainingModule]:
        """Get specific module by ID"""
        for level in self.curriculum.values():
            for module in level.modules:
                if module.id == module_id:
                    return module
        return None

    def get_all_levels(self) -> List['TrainingLevel']:
        """Get all training levels in order"""
        return [self.curriculum[i] for i in sorted(self.curriculum.keys())]

    def calculate_total_hours(self, level_number: int) -> float:
        """Calculate total training hours for a level"""
        level = self.get_level(level_number)
        if not level:
            return 0.0
        return sum(module.duration_hours for module in level.modules)

    def get_prerequisites(self, module_id: str) -> List[str]:
        """Get all prerequisites for a module"""
        module = self.get_module(module_id)
        if not module:
            return []
        return module.prerequisites

    def validate_progression(self, member_data: Dict) -> Dict:
        """
        Validate if a member meets criteria to advance to next level

        Args:
            member_data: Dictionary containing member's current level, scores, etc.

        Returns:
            Dictionary with validation results and next steps
        """
        current_level = member_data.get('current_level', 1)
        level = self.get_level(current_level)

        if not level:
            return {"valid": False, "reason": "Invalid level"}

        criteria = level.advancement_criteria
        results = {"valid": True, "criteria_met": {}, "criteria_not_met": {}}

        for criterion, required_value in criteria.items():
            actual_value = member_data.get(criterion)

            if actual_value is None:
                results["valid"] = False
                results["criteria_not_met"][criterion] = f"Missing data for {criterion}"
            elif isinstance(required_value, bool):
                if actual_value != required_value:
                    results["valid"] = False
                    results["criteria_not_met"][criterion] = f"Required: {required_value}, Actual: {actual_value}"
                else:
                    results["criteria_met"][criterion] = actual_value
            elif isinstance(required_value, (int, float)):
                if actual_value < required_value:
                    results["valid"] = False
                    results["criteria_not_met"][criterion] = f"Required: {required_value}, Actual: {actual_value}"
                else:
                    results["criteria_met"][criterion] = actual_value
            else:
                if actual_value != required_value:
                    results["valid"] = False
                    results["criteria_not_met"][criterion] = f"Required: {required_value}, Actual: {actual_value}"
                else:
                    results["criteria_met"][criterion] = actual_value

        if results["valid"]:
            results["next_level"] = current_level + 1
            results["message"] = f"Congratulations! You qualify for Level {current_level + 1}"
        else:
            results["message"] = "Additional progress needed before advancing"

        return results


# Example usage
if __name__ == "__main__":
    curriculum = CurriculumDesign()

    # Display overview
    print("NeuroDivergent AI Coach - Training Curriculum\n")
    print("=" * 60)

    for level in curriculum.get_all_levels():
        print(f"\n{level.title}")
        print(f"Duration: {level.duration_weeks[0]}-{level.duration_weeks[1]} weeks")
        print(f"Compensation: {level.compensation_type}")
        print(f"Total Hours: {curriculum.calculate_total_hours(level.level.value)}")
        print(f"\nModules ({len(level.modules)}):")
        for module in level.modules:
            print(f"  - {module.id}: {module.title} ({module.duration_hours}h)")
