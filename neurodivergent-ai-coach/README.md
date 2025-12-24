# NeuroDivergent AI Coach

A comprehensive AI-powered peer management and positive lifestyle coaching system designed for the Integrated Healthy Empowerment Program (ihep.app).

## Overview

The NeuroDivergent AI Coach acts as a Professor of Peer Management and Positive Lifestyle Coaching, guiding ihep.app members through a structured training program to become peer assistants, peer counselors, and eventually full-time peer managers.

## Features

- **Progressive Training Curriculum**: Multi-level training program from assistant to manager
- **Qualification System**: Merit-based advancement based on engagement and adherence
- **Emotional Intelligence**: Humanistic responses with empathy and understanding
- **Ethical Framework**: Built-in moral compass and ethical best practices
- **Compensation Tracking**: Support for compensation during training and employment phases
- **Adaptive Learning**: Personalized training paths based on member progress

## Architecture

```
neurodivergent-ai-coach/
├── agent/                  # Core AI agent implementation
│   ├── coach.py           # Main coaching agent
│   ├── emotional_intelligence.py  # EI and humanistic response system
│   └── ethical_framework.py      # Ethical guidelines and moral compass
├── curriculum/            # Training curriculum and course content
│   ├── curriculum_design.py      # Curriculum structure
│   ├── level_*.py               # Course content by level
│   └── assessments.py           # Qualification assessments
├── models/               # Data models
│   ├── member.py         # Member/trainee model
│   ├── progress.py       # Progress tracking
│   └── qualification.py  # Qualification criteria
├── utils/               # Utility functions
│   ├── conversation.py  # Conversation management
│   └── analytics.py     # Progress analytics
└── examples/           # Usage examples

```

## Training Progression

### Level 1: Qualified Member
- **Prerequisites**: Minimum engagement/adherence metrics
- **Status**: Expressed interest in training
- **Compensation**: None yet

### Level 2: Peer Assistant (Trainee)
- **Training Duration**: 4-8 weeks
- **Focus**: Basic peer support, active listening, ihep.app platform knowledge
- **Compensation**: Stipend during training
- **Hours**: 5-10 hours/week

### Level 3: Part-Time Peer Counselor
- **Training Duration**: 8-12 weeks
- **Focus**: Advanced counseling techniques, crisis management, motivational interviewing
- **Compensation**: Part-time employment
- **Hours**: 15-25 hours/week

### Level 4: Full-Time Peer Manager
- **Training Duration**: Ongoing professional development
- **Focus**: Team leadership, program development, advanced case management
- **Compensation**: Full-time employment with benefits
- **Hours**: 40 hours/week

## Qualification Criteria

Members qualify for training by meeting these minimum requirements:

1. **Engagement Score**: ≥ 75% (calculated from app usage, check-ins, goal completion)
2. **Adherence Score**: ≥ 70% (following through on commitments and programs)
3. **Time in Program**: Minimum 3 months as active member
4. **Completion Rate**: ≥ 80% of assigned modules/tasks
5. **Community Participation**: Regular participation in community features
6. **Good Standing**: No violations of community guidelines

## Ethical Framework

The AI Coach operates under strict ethical principles:

- **Beneficence**: Act in the best interest of members
- **Non-maleficence**: Do no harm
- **Autonomy**: Respect member self-determination
- **Justice**: Fair and equitable treatment
- **Confidentiality**: Protect member privacy
- **Cultural Competence**: Respect diversity and individual differences
- **Professional Boundaries**: Maintain appropriate relationships

## Getting Started

```python
from agent.coach import NeurodivergentCoach
from models.member import Member

# Initialize the coach
coach = NeurodivergentCoach()

# Create or load a member profile
member = Member(
    id="member_123",
    name="John Doe",
    engagement_score=82,
    adherence_score=75,
    months_active=4
)

# Check qualification
if coach.check_qualification(member):
    # Start training conversation
    response = coach.start_training_conversation(member)
    print(response)
```

## Integration with ihep.app

This system is designed to integrate with the ihep.app platform through:

1. **API Integration**: REST API endpoints for qualification checks and progress tracking
2. **Webhook Support**: Real-time updates on member engagement and adherence
3. **Dashboard Integration**: Training progress visualization
4. **Notification System**: Training reminders and milestone celebrations

## Requirements

- Python 3.8+
- Google Generative AI SDK (Gemini)
- NumPy for analytics
- JSON for data persistence

## License

Copyright 2024 Google, Inc.

Licensed under the Apache License, Version 2.0
