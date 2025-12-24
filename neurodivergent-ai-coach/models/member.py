"""
Member data model for tracking trainees in the NeuroDivergent AI Coach system
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional
from enum import Enum
import json


class MemberStatus(Enum):
    """Member status in the training program"""
    ACTIVE_MEMBER = "active_member"
    QUALIFIED = "qualified"
    TRAINING_ASSISTANT = "training_assistant"
    PEER_ASSISTANT = "peer_assistant"
    PEER_COUNSELOR = "peer_counselor"
    PEER_MANAGER = "peer_manager"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"


@dataclass
class EngagementMetrics:
    """Metrics for measuring member engagement with ihep.app"""
    total_logins: int = 0
    days_active_last_30: int = 0
    goals_set: int = 0
    goals_completed: int = 0
    check_ins_completed: int = 0
    community_posts: int = 0
    community_interactions: int = 0
    resources_accessed: int = 0
    average_session_duration_minutes: float = 0.0

    def calculate_engagement_score(self) -> float:
        """
        Calculate engagement score (0-100)

        Weighted formula:
        - Activity frequency: 30%
        - Goal engagement: 25%
        - Community participation: 25%
        - Resource usage: 20%
        """
        # Activity frequency (30%)
        activity_score = min((self.days_active_last_30 / 30) * 100, 100)

        # Goal engagement (25%)
        goal_rate = (self.goals_completed / self.goals_set * 100) if self.goals_set > 0 else 0
        goal_score = min(goal_rate, 100)

        # Community participation (25%)
        community_activity = self.community_posts + (self.community_interactions * 0.5)
        community_score = min((community_activity / 20) * 100, 100)

        # Resource usage (20%)
        resource_score = min((self.resources_accessed / 10) * 100, 100)

        # Weighted total
        engagement_score = (
            activity_score * 0.30 +
            goal_score * 0.25 +
            community_score * 0.25 +
            resource_score * 0.20
        )

        return round(engagement_score, 2)


@dataclass
class AdherenceMetrics:
    """Metrics for measuring member adherence to commitments"""
    commitments_made: int = 0
    commitments_kept: int = 0
    appointments_scheduled: int = 0
    appointments_attended: int = 0
    programs_enrolled: int = 0
    programs_completed: int = 0
    streak_current_days: int = 0
    streak_longest_days: int = 0

    def calculate_adherence_score(self) -> float:
        """
        Calculate adherence score (0-100)

        Weighted formula:
        - Commitment follow-through: 40%
        - Appointment attendance: 30%
        - Program completion: 30%
        """
        # Commitment follow-through (40%)
        commitment_rate = (self.commitments_kept / self.commitments_made * 100) if self.commitments_made > 0 else 0
        commitment_score = min(commitment_rate, 100)

        # Appointment attendance (30%)
        attendance_rate = (self.appointments_attended / self.appointments_scheduled * 100) if self.appointments_scheduled > 0 else 0
        attendance_score = min(attendance_rate, 100)

        # Program completion (30%)
        completion_rate = (self.programs_completed / self.programs_enrolled * 100) if self.programs_enrolled > 0 else 0
        completion_score = min(completion_rate, 100)

        # Weighted total
        adherence_score = (
            commitment_score * 0.40 +
            attendance_score * 0.30 +
            completion_score * 0.30
        )

        return round(adherence_score, 2)


@dataclass
class TrainingProgress:
    """Track progress through training program"""
    current_level: int = 1
    current_module_id: Optional[str] = None
    modules_completed: List[str] = field(default_factory=list)
    modules_in_progress: List[str] = field(default_factory=list)
    assessment_scores: Dict[str, float] = field(default_factory=dict)
    practice_hours: float = 0.0
    supervised_hours: float = 0.0
    independent_hours: float = 0.0
    member_interactions: int = 0
    member_feedback_scores: List[float] = field(default_factory=list)
    supervisor_notes: List[Dict] = field(default_factory=list)

    def get_average_feedback(self) -> float:
        """Calculate average member feedback score"""
        if not self.member_feedback_scores:
            return 0.0
        return round(sum(self.member_feedback_scores) / len(self.member_feedback_scores), 2)

    def get_completion_rate(self, total_modules: int) -> float:
        """Calculate module completion rate"""
        if total_modules == 0:
            return 0.0
        return round((len(self.modules_completed) / total_modules) * 100, 2)


@dataclass
class Member:
    """
    Complete member profile for the NeuroDivergent AI Coach system
    """
    # Identity
    id: str
    name: str
    email: str
    phone: Optional[str] = None
    preferred_pronouns: Optional[str] = None

    # Dates
    date_joined: datetime = field(default_factory=datetime.now)
    date_qualified: Optional[datetime] = None
    date_started_training: Optional[datetime] = None
    last_active: datetime = field(default_factory=datetime.now)

    # Status
    status: MemberStatus = MemberStatus.ACTIVE_MEMBER
    months_active: int = 0
    good_standing: bool = True

    # Metrics
    engagement: EngagementMetrics = field(default_factory=EngagementMetrics)
    adherence: AdherenceMetrics = field(default_factory=AdherenceMetrics)

    # Training
    training_progress: TrainingProgress = field(default_factory=TrainingProgress)
    expressed_interest: bool = False
    interest_date: Optional[datetime] = None
    interest_method: Optional[str] = None  # "outreach" or "solicitation"

    # Compensation
    compensation_rate: Optional[float] = None
    compensation_currency: str = "USD"
    hours_worked: float = 0.0
    total_compensation: float = 0.0

    # Preferences and notes
    learning_preferences: Dict = field(default_factory=dict)
    accessibility_needs: List[str] = field(default_factory=list)
    timezone: str = "UTC"
    availability: Dict = field(default_factory=dict)
    notes: List[Dict] = field(default_factory=list)

    def get_engagement_score(self) -> float:
        """Get current engagement score"""
        return self.engagement.calculate_engagement_score()

    def get_adherence_score(self) -> float:
        """Get current adherence score"""
        return self.adherence.calculate_adherence_score()

    def is_qualified_for_training(self) -> bool:
        """
        Check if member meets minimum qualification criteria

        Criteria:
        - Engagement score >= 75
        - Adherence score >= 70
        - Months active >= 3
        - Good standing = True
        - Expressed interest = True
        """
        return (
            self.get_engagement_score() >= 75 and
            self.get_adherence_score() >= 70 and
            self.months_active >= 3 and
            self.good_standing and
            self.expressed_interest
        )

    def record_interest(self, method: str):
        """Record that member has expressed interest in training"""
        self.expressed_interest = True
        self.interest_date = datetime.now()
        self.interest_method = method

    def start_training(self, level: int = 1, compensation_rate: Optional[float] = None):
        """Begin training at specified level"""
        self.status = MemberStatus.TRAINING_ASSISTANT if level == 2 else self.status
        self.date_started_training = datetime.now()
        self.training_progress.current_level = level
        if compensation_rate:
            self.compensation_rate = compensation_rate

    def complete_module(self, module_id: str, score: Optional[float] = None):
        """Mark a module as completed"""
        if module_id not in self.training_progress.modules_completed:
            self.training_progress.modules_completed.append(module_id)
        if module_id in self.training_progress.modules_in_progress:
            self.training_progress.modules_in_progress.remove(module_id)
        if score is not None:
            self.training_progress.assessment_scores[module_id] = score

    def advance_level(self, new_level: int, new_status: MemberStatus, new_compensation: Optional[float] = None):
        """Advance to next training level"""
        self.training_progress.current_level = new_level
        self.status = new_status
        if new_compensation:
            self.compensation_rate = new_compensation

    def add_note(self, note: str, author: str = "system", note_type: str = "general"):
        """Add a note to member record"""
        self.notes.append({
            "date": datetime.now().isoformat(),
            "author": author,
            "type": note_type,
            "content": note
        })

    def add_supervisor_note(self, note: str, supervisor: str, rating: Optional[int] = None):
        """Add supervisor feedback"""
        self.training_progress.supervisor_notes.append({
            "date": datetime.now().isoformat(),
            "supervisor": supervisor,
            "content": note,
            "rating": rating
        })

    def record_practice_hours(self, hours: float, supervised: bool = True):
        """Record practice hours"""
        self.training_progress.practice_hours += hours
        if supervised:
            self.training_progress.supervised_hours += hours
        else:
            self.training_progress.independent_hours += hours
        self.hours_worked += hours
        if self.compensation_rate:
            self.total_compensation += hours * self.compensation_rate

    def record_member_feedback(self, score: float):
        """Record feedback score from a member (1-5 scale)"""
        if 1 <= score <= 5:
            self.training_progress.member_feedback_scores.append(score)
            self.training_progress.member_interactions += 1

    def to_dict(self) -> Dict:
        """Convert member to dictionary for serialization"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "preferred_pronouns": self.preferred_pronouns,
            "date_joined": self.date_joined.isoformat() if self.date_joined else None,
            "date_qualified": self.date_qualified.isoformat() if self.date_qualified else None,
            "date_started_training": self.date_started_training.isoformat() if self.date_started_training else None,
            "last_active": self.last_active.isoformat() if self.last_active else None,
            "status": self.status.value,
            "months_active": self.months_active,
            "good_standing": self.good_standing,
            "engagement": self.engagement.__dict__,
            "adherence": self.adherence.__dict__,
            "training_progress": {
                "current_level": self.training_progress.current_level,
                "current_module_id": self.training_progress.current_module_id,
                "modules_completed": self.training_progress.modules_completed,
                "modules_in_progress": self.training_progress.modules_in_progress,
                "assessment_scores": self.training_progress.assessment_scores,
                "practice_hours": self.training_progress.practice_hours,
                "supervised_hours": self.training_progress.supervised_hours,
                "independent_hours": self.training_progress.independent_hours,
                "member_interactions": self.training_progress.member_interactions,
                "member_feedback_scores": self.training_progress.member_feedback_scores,
                "supervisor_notes": self.training_progress.supervisor_notes
            },
            "expressed_interest": self.expressed_interest,
            "interest_date": self.interest_date.isoformat() if self.interest_date else None,
            "interest_method": self.interest_method,
            "compensation_rate": self.compensation_rate,
            "compensation_currency": self.compensation_currency,
            "hours_worked": self.hours_worked,
            "total_compensation": self.total_compensation,
            "learning_preferences": self.learning_preferences,
            "accessibility_needs": self.accessibility_needs,
            "timezone": self.timezone,
            "availability": self.availability,
            "notes": self.notes
        }

    def to_json(self) -> str:
        """Convert member to JSON string"""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, data: Dict) -> 'Member':
        """Create Member instance from dictionary"""
        # Handle datetime fields
        if isinstance(data.get('date_joined'), str):
            data['date_joined'] = datetime.fromisoformat(data['date_joined'])
        if isinstance(data.get('date_qualified'), str):
            data['date_qualified'] = datetime.fromisoformat(data['date_qualified'])
        if isinstance(data.get('date_started_training'), str):
            data['date_started_training'] = datetime.fromisoformat(data['date_started_training'])
        if isinstance(data.get('last_active'), str):
            data['last_active'] = datetime.fromisoformat(data['last_active'])
        if isinstance(data.get('interest_date'), str):
            data['interest_date'] = datetime.fromisoformat(data['interest_date'])

        # Handle enum
        if isinstance(data.get('status'), str):
            data['status'] = MemberStatus(data['status'])

        # Handle nested objects
        if 'engagement' in data and isinstance(data['engagement'], dict):
            data['engagement'] = EngagementMetrics(**data['engagement'])
        if 'adherence' in data and isinstance(data['adherence'], dict):
            data['adherence'] = AdherenceMetrics(**data['adherence'])
        if 'training_progress' in data and isinstance(data['training_progress'], dict):
            data['training_progress'] = TrainingProgress(**data['training_progress'])

        return cls(**data)


# Example usage
if __name__ == "__main__":
    # Create a new member
    member = Member(
        id="M001",
        name="Jane Doe",
        email="jane.doe@example.com",
        preferred_pronouns="she/her"
    )

    # Set engagement metrics
    member.engagement.total_logins = 45
    member.engagement.days_active_last_30 = 25
    member.engagement.goals_set = 10
    member.engagement.goals_completed = 8
    member.engagement.check_ins_completed = 20
    member.engagement.community_posts = 15
    member.engagement.community_interactions = 30

    # Set adherence metrics
    member.adherence.commitments_made = 20
    member.adherence.commitments_kept = 18
    member.adherence.appointments_scheduled = 5
    member.adherence.appointments_attended = 5
    member.adherence.programs_enrolled = 3
    member.adherence.programs_completed = 2

    # Set time active
    member.months_active = 4

    # Check qualification
    print(f"Member: {member.name}")
    print(f"Engagement Score: {member.get_engagement_score()}")
    print(f"Adherence Score: {member.get_adherence_score()}")
    print(f"Qualified for Training: {member.is_qualified_for_training()}")

    # Express interest
    member.record_interest("outreach")
    print(f"\nQualified after expressing interest: {member.is_qualified_for_training()}")

    # Save to JSON
    print(f"\nMember JSON:\n{member.to_json()}")
