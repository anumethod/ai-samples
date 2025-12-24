"""
NeuroDivergent AI Coach

A comprehensive AI-powered peer management and positive lifestyle coaching system
for the Integrated Healthy Empowerment Program (ihep.app).
"""

__version__ = "1.0.0"
__author__ = "IHEP Development Team"
__license__ = "Apache 2.0"

from agent.coach import NeurodivergentCoach
from models.member import Member, MemberStatus
from curriculum.curriculum_design import CurriculumDesign

__all__ = [
    "NeurodivergentCoach",
    "Member",
    "MemberStatus",
    "CurriculumDesign"
]
