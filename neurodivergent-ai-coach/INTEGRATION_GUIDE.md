# Integration Guide for NeuroDivergent AI Coach

This guide explains how to integrate the NeuroDivergent AI Coach into the ihep.app platform.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Quick Start](#quick-start)
3. [Integration Points](#integration-points)
4. [API Integration](#api-integration)
5. [Database Schema](#database-schema)
6. [Frontend Integration](#frontend-integration)
7. [Security Considerations](#security-considerations)
8. [Deployment](#deployment)

## Architecture Overview

The NeuroDivergent AI Coach system consists of four main components:

```
┌─────────────────────────────────────────────────────────┐
│                    ihep.app Platform                     │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────┐  │
│  │ Member App │  │ Admin Panel│  │ Analytics Dashboard│ │
│  └────────────┘  └────────────┘  └──────────────────┘  │
└─────────────────────────┬───────────────────────────────┘
                          │ REST API / WebSocket
┌─────────────────────────┴───────────────────────────────┐
│           NeuroDivergent AI Coach Service               │
│  ┌──────────────┐  ┌─────────────┐  ┌───────────────┐  │
│  │ Coach Agent  │  │ Curriculum  │  │ Progress Track│  │
│  │ - EI         │  │ Management  │  │ & Analytics   │  │
│  │ - Ethics     │  │             │  │               │  │
│  └──────────────┘  └─────────────┘  └───────────────┘  │
└─────────────────────────┬───────────────────────────────┘
                          │
┌─────────────────────────┴───────────────────────────────┐
│                    Data Layer                            │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐ │
│  │  Member DB  │  │ Progress DB  │  │ Session Logs   │ │
│  └─────────────┘  └──────────────┘  └────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

## Quick Start

### Installation

```bash
# Clone or download the neurodivergent-ai-coach directory
cd neurodivergent-ai-coach

# Install dependencies (minimal setup requires no external packages)
pip install -r requirements.txt  # Optional dependencies
```

### Basic Usage

```python
from agent.coach import NeurodivergentCoach
from models.member import Member

# Initialize coach
coach = NeurodivergentCoach()

# Create member (typically loaded from your database)
member = Member(
    id="M123",
    name="Jane Doe",
    email="jane@example.com"
)

# Set member metrics from ihep.app data
member.engagement.days_active_last_30 = 26
member.engagement.goals_completed = 10
# ... set other metrics

member.months_active = 4
member.record_interest("outreach")

# Check qualification
qualified, details = coach.check_qualification(member)

if qualified:
    # Start training
    welcome = coach.start_training_conversation(member)
    print(welcome)
```

## Integration Points

### 1. Member Qualification System

**Trigger Points:**
- Member completes 3 months in the program
- Member reaches engagement threshold
- Admin manually checks qualification

**Integration:**
```python
# In your ihep.app backend
from neuroprogressive_coach.agent.coach import NeuroprogressiveCoach

def check_member_training_eligibility(member_id):
    coach = NeurodivergentCoach()
    member = load_member_from_db(member_id)

    # Sync metrics from ihep.app
    member.engagement = calculate_engagement_metrics(member_id)
    member.adherence = calculate_adherence_metrics(member_id)

    qualified, details = coach.check_qualification(member)
    return qualified, details
```

### 2. Conversation Interface

**Trigger Points:**
- Member sends message in training chat
- Scheduled check-ins
- Module interactions

**Integration:**
```python
def handle_training_message(member_id, message):
    coach = NeurodivergentCoach()
    member = load_member_from_db(member_id)

    response = coach.continue_conversation(
        member_id=member_id,
        member_message=message,
        context={
            "module_id": member.current_module,
            "session_type": "training"
        }
    )

    save_conversation_to_db(member_id, message, response)
    return response
```

### 3. Progress Tracking

**Trigger Points:**
- Module completion
- Practice hours logged
- Feedback received
- Assessment taken

**Integration:**
```python
def log_practice_hours(member_id, hours, supervised=True):
    member = load_member_from_db(member_id)
    member.record_practice_hours(hours, supervised)
    save_member_to_db(member)

    # Check if this triggers advancement eligibility
    coach = NeurodivergentCoach()
    progress = coach.assess_progress(member_id)
    return progress
```

### 4. Solicitation System

**Implementation:**
```python
def send_training_solicitations():
    """Daily job to identify and solicit qualified members"""
    qualified_members = get_qualified_members_not_solicited()

    for member in qualified_members:
        # Send in-app notification
        send_notification(
            member_id=member.id,
            title="You're Eligible for Peer Support Training!",
            message=f"Congratulations! You've qualified for our peer support training program...",
            action_url="/training/express-interest"
        )

        # Send email
        send_email(
            to=member.email,
            template="training_solicitation",
            context={"member": member}
        )
```

## API Integration

### REST API Endpoints

Implement these endpoints in your ihep.app backend:

#### Member Endpoints

```
POST   /api/v1/training/members/{member_id}/express-interest
GET    /api/v1/training/members/{member_id}/qualification
POST   /api/v1/training/members/{member_id}/start
GET    /api/v1/training/members/{member_id}/progress
```

#### Conversation Endpoints

```
POST   /api/v1/training/conversations/{member_id}/messages
GET    /api/v1/training/conversations/{member_id}/history
```

#### Curriculum Endpoints

```
GET    /api/v1/training/curriculum
GET    /api/v1/training/curriculum/levels/{level_number}
GET    /api/v1/training/curriculum/modules/{module_id}
POST   /api/v1/training/members/{member_id}/modules/{module_id}/start
POST   /api/v1/training/members/{member_id}/modules/{module_id}/complete
```

See `examples/api_integration_example.py` for detailed API specifications.

### WebSocket Integration (Optional)

For real-time conversations:

```python
# WebSocket endpoint
@app.websocket("/ws/training/{member_id}")
async def training_websocket(websocket: WebSocket, member_id: str):
    await websocket.accept()
    coach = NeurodivergentCoach()

    while True:
        message = await websocket.receive_text()
        response = coach.continue_conversation(member_id, message)
        await websocket.send_text(response)
```

## Database Schema

### Member Training Table

```sql
CREATE TABLE member_training (
    id UUID PRIMARY KEY,
    member_id UUID REFERENCES members(id),
    status VARCHAR(50),  -- qualified, training_assistant, peer_assistant, etc.
    current_level INTEGER,
    current_module_id VARCHAR(20),
    date_qualified TIMESTAMP,
    date_started_training TIMESTAMP,
    expressed_interest BOOLEAN,
    interest_date TIMESTAMP,
    interest_method VARCHAR(20),
    compensation_rate DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Training Progress Table

```sql
CREATE TABLE training_progress (
    id UUID PRIMARY KEY,
    member_id UUID REFERENCES members(id),
    module_id VARCHAR(20),
    status VARCHAR(20),  -- in_progress, completed
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    assessment_score DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Practice Hours Table

```sql
CREATE TABLE practice_hours (
    id UUID PRIMARY KEY,
    member_id UUID REFERENCES members(id),
    hours DECIMAL(5, 2),
    supervised BOOLEAN,
    recorded_at TIMESTAMP,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Coaching Sessions Table

```sql
CREATE TABLE coaching_sessions (
    id UUID PRIMARY KEY,
    member_id UUID REFERENCES members(id),
    session_type VARCHAR(50),
    module_id VARCHAR(20),
    member_message TEXT,
    coach_response TEXT,
    emotional_state VARCHAR(50),
    risk_level VARCHAR(20),
    session_timestamp TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## Frontend Integration

### Training Dashboard Component

```jsx
// React component example
import React, { useState, useEffect } from 'react';

function TrainingDashboard({ memberId }) {
    const [progress, setProgress] = useState(null);
    const [qualification, setQualification] = useState(null);

    useEffect(() => {
        // Check qualification
        fetch(`/api/v1/training/members/${memberId}/qualification`)
            .then(r => r.json())
            .then(data => setQualification(data));

        // Get progress if training
        fetch(`/api/v1/training/members/${memberId}/progress`)
            .then(r => r.json())
            .then(data => setProgress(data));
    }, [memberId]);

    if (!qualification) return <div>Loading...</div>;

    if (!qualification.qualified) {
        return <QualificationProgress qualification={qualification} />;
    }

    return (
        <div className="training-dashboard">
            <TrainingProgress progress={progress} />
            <ConversationInterface memberId={memberId} />
            <CurrentModule progress={progress} />
        </div>
    );
}
```

### Conversation Interface

```jsx
function ConversationInterface({ memberId }) {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const sendMessage = async () => {
        const response = await fetch(
            `/api/v1/training/conversations/${memberId}/messages`,
            {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: input })
            }
        );

        const data = await response.json();
        setMessages([
            ...messages,
            { type: 'member', text: input },
            { type: 'coach', text: data.coach_response }
        ]);
        setInput('');
    };

    return (
        <div className="conversation-interface">
            <div className="messages">
                {messages.map((msg, i) => (
                    <Message key={i} type={msg.type} text={msg.text} />
                ))}
            </div>
            <input
                value={input}
                onChange={e => setInput(e.target.value)}
                onKeyPress={e => e.key === 'Enter' && sendMessage()}
            />
        </div>
    );
}
```

## Security Considerations

### 1. Authentication & Authorization

```python
def verify_training_access(member_id, current_user):
    """Ensure user can only access their own training data"""
    if current_user.id != member_id:
        if not current_user.is_admin:
            raise PermissionError("Access denied")
```

### 2. Data Privacy

- All coaching sessions should be encrypted at rest
- Implement proper HIPAA compliance if applicable
- Use secure WebSocket connections (WSS) for real-time chat
- Audit log all access to sensitive training data

### 3. Ethical Framework Integration

```python
# Always check ethical concerns before responding
ethical_decision = ethical_framework.evaluate_situation(message, context)

if ethical_decision.risk_level == "critical":
    # Immediate escalation to crisis team
    notify_crisis_team(member_id, message, ethical_decision)
    return crisis_response

if ethical_decision.escalation_needed:
    # Log and notify supervisor
    notify_supervisor(member_id, ethical_decision)
```

## Deployment

### Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "-m", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables

```bash
# .env
DATABASE_URL=postgresql://user:pass@localhost/ihep_training
SECRET_KEY=your-secret-key
COACH_LOG_LEVEL=INFO
ENABLE_WEBHOOKS=true
CRISIS_NOTIFICATION_EMAIL=crisis@ihep.app
```

### Kubernetes Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: neurodivergent-coach
spec:
  replicas: 3
  selector:
    matchLabels:
      app: neurodivergent-coach
  template:
    metadata:
      labels:
        app: neurodivergent-coach
    spec:
      containers:
      - name: coach
        image: ihep/neurodivergent-coach:latest
        ports:
        - containerPort: 8000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: coach-secrets
              key: database-url
```

## Monitoring & Analytics

### Key Metrics to Track

1. **Qualification Metrics**
   - Number of qualified members per month
   - Qualification conversion rate
   - Time to qualification

2. **Training Metrics**
   - Members by training level
   - Average module completion time
   - Assessment scores by module
   - Training dropout rate

3. **Engagement Metrics**
   - Messages per member
   - Response time
   - Session frequency
   - Practice hours logged

4. **Outcome Metrics**
   - Members advanced to peer assistant
   - Members advanced to peer counselor
   - Members advanced to peer manager
   - Retention rates by level

### Example Analytics Query

```python
def get_training_analytics(start_date, end_date):
    return {
        "total_qualified": count_qualified_members(start_date, end_date),
        "total_started": count_started_training(start_date, end_date),
        "by_level": {
            1: count_by_level(1),
            2: count_by_level(2),
            3: count_by_level(3),
            4: count_by_level(4)
        },
        "completion_rates": calculate_completion_rates(),
        "average_feedback": calculate_average_feedback()
    }
```

## Support & Maintenance

### Regular Maintenance Tasks

1. **Weekly**
   - Review coaching session logs for quality
   - Monitor error rates and ethical escalations
   - Update qualification thresholds if needed

2. **Monthly**
   - Review curriculum effectiveness
   - Analyze member feedback
   - Update response templates based on learnings

3. **Quarterly**
   - Major curriculum updates
   - System performance optimization
   - Security audits

### Contact & Resources

- **Documentation**: See README.md for detailed information
- **Examples**: Check `/examples` directory for code samples
- **Issues**: Report bugs or feature requests through your issue tracking system

## Next Steps

1. Set up development environment
2. Implement REST API endpoints
3. Create database schema
4. Build frontend components
5. Test qualification system
6. Deploy to staging environment
7. Train administrators
8. Launch pilot program
9. Monitor and iterate

For more detailed examples, see the `/examples` directory.
