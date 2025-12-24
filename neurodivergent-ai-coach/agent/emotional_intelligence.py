"""
Emotional Intelligence Module for NeuroDivergent AI Coach

This module implements emotional intelligence capabilities including empathy,
emotional recognition, humanistic response generation, and therapeutic communication.
"""

from enum import Enum
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


class EmotionCategory(Enum):
    """Categories of emotions"""
    JOY = "joy"
    SADNESS = "sadness"
    ANGER = "anger"
    FEAR = "fear"
    SURPRISE = "surprise"
    DISGUST = "disgust"
    TRUST = "trust"
    ANTICIPATION = "anticipation"
    NEUTRAL = "neutral"


class EmotionalIntensity(Enum):
    """Intensity levels of emotions"""
    MILD = 1
    MODERATE = 2
    STRONG = 3
    INTENSE = 4


class CommunicationStyle(Enum):
    """Communication style approaches"""
    SUPPORTIVE = "supportive"
    MOTIVATIONAL = "motivational"
    VALIDATING = "validating"
    CHALLENGING = "challenging"
    EDUCATIONAL = "educational"
    CELEBRATORY = "celebratory"
    REFLECTIVE = "reflective"


@dataclass
class EmotionalState:
    """Detected emotional state of member"""
    primary_emotion: EmotionCategory
    secondary_emotions: List[EmotionCategory]
    intensity: EmotionalIntensity
    indicators: List[str]  # What indicated this emotion
    needs: List[str]  # What the person might need


@dataclass
class ResponseStrategy:
    """Strategy for responding to emotional state"""
    communication_style: CommunicationStyle
    tone: str
    empathy_level: str  # "low", "medium", "high"
    validation_statements: List[str]
    reframing_opportunities: List[str]
    questions_to_ask: List[str]
    avoid: List[str]  # Things to avoid saying/doing


class EmotionalIntelligence:
    """
    Emotional Intelligence system for the NeuroDivergent AI Coach.

    Implements empathy, emotional recognition, and humanistic response generation
    to create authentic, supportive interactions.
    """

    def __init__(self):
        self.emotion_indicators = self._initialize_emotion_indicators()
        self.response_templates = self._initialize_response_templates()
        self.validation_phrases = self._initialize_validation_phrases()
        self.empathic_responses = self._initialize_empathic_responses()

    def _initialize_emotion_indicators(self) -> Dict[EmotionCategory, Dict]:
        """Define indicators for recognizing emotions"""
        return {
            EmotionCategory.JOY: {
                "keywords": ["happy", "excited", "great", "wonderful", "amazing", "thrilled", "proud", "accomplished"],
                "phrases": ["feeling good", "went well", "so happy", "really excited"],
                "needs": ["recognition", "celebration", "connection", "sharing success"]
            },
            EmotionCategory.SADNESS: {
                "keywords": ["sad", "depressed", "down", "low", "hopeless", "discouraged", "disappointed", "lonely"],
                "phrases": ["feeling down", "not good", "struggling", "can't seem to"],
                "needs": ["support", "validation", "hope", "connection", "understanding"]
            },
            EmotionCategory.ANGER: {
                "keywords": ["angry", "frustrated", "mad", "annoyed", "irritated", "furious", "upset", "unfair"],
                "phrases": ["so frustrated", "makes me angry", "not fair", "really upset"],
                "needs": ["validation", "understanding", "empowerment", "justice", "being heard"]
            },
            EmotionCategory.FEAR: {
                "keywords": ["scared", "afraid", "anxious", "worried", "nervous", "terrified", "panic", "overwhelmed"],
                "phrases": ["worried about", "scared that", "what if", "can't handle"],
                "needs": ["safety", "reassurance", "support", "coping strategies", "grounding"]
            },
            EmotionCategory.SURPRISE: {
                "keywords": ["surprised", "shocked", "unexpected", "didn't expect", "caught off guard", "amazed"],
                "phrases": ["didn't see that coming", "wasn't expecting", "shocked that"],
                "needs": ["processing time", "sense-making", "support", "validation"]
            },
            EmotionCategory.TRUST: {
                "keywords": ["trust", "safe", "comfortable", "confident", "secure", "believe"],
                "phrases": ["feel safe", "can trust", "comfortable with", "believe in"],
                "needs": ["consistency", "reliability", "honesty", "respect"]
            },
            EmotionCategory.ANTICIPATION: {
                "keywords": ["looking forward", "excited for", "can't wait", "hoping", "expecting", "planning"],
                "phrases": ["can't wait for", "looking forward", "excited about", "planning to"],
                "needs": ["encouragement", "planning support", "realistic expectations", "celebration"]
            }
        }

    def _initialize_response_templates(self) -> Dict[CommunicationStyle, Dict]:
        """Define response templates for different communication styles"""
        return {
            CommunicationStyle.SUPPORTIVE: {
                "tone": "warm, compassionate, nurturing",
                "openers": [
                    "I can hear how difficult this is for you.",
                    "Thank you for sharing this with me.",
                    "It takes courage to talk about this.",
                    "I'm here to support you through this."
                ],
                "connectors": [
                    "What I'm hearing is...",
                    "It sounds like...",
                    "I can understand why you feel...",
                    "That makes sense given..."
                ],
                "closers": [
                    "You don't have to face this alone.",
                    "I'm here with you.",
                    "We'll work through this together.",
                    "You have support available."
                ]
            },
            CommunicationStyle.MOTIVATIONAL: {
                "tone": "encouraging, energizing, hopeful",
                "openers": [
                    "I believe in your ability to...",
                    "You've shown such strength in...",
                    "Look at how far you've come!",
                    "You have what it takes to..."
                ],
                "connectors": [
                    "Remember when you...",
                    "You've overcome challenges before...",
                    "Your past successes show...",
                    "You have the skills to..."
                ],
                "closers": [
                    "I'm excited to see what you accomplish!",
                    "You've got this!",
                    "Keep moving forward!",
                    "I believe in you!"
                ]
            },
            CommunicationStyle.VALIDATING: {
                "tone": "accepting, normalizing, affirming",
                "openers": [
                    "Your feelings make complete sense.",
                    "Anyone in your situation would feel this way.",
                    "What you're experiencing is valid.",
                    "It's completely understandable that..."
                ],
                "connectors": [
                    "Your reaction is normal given...",
                    "Many people feel this way when...",
                    "It's okay to feel...",
                    "You're not alone in experiencing..."
                ],
                "closers": [
                    "Your feelings are valid and important.",
                    "Thank you for trusting me with this.",
                    "It's okay to feel how you feel.",
                    "You have every right to feel this way."
                ]
            },
            CommunicationStyle.CHALLENGING: {
                "tone": "respectful, curious, growth-oriented",
                "openers": [
                    "I'm wondering if we might look at this differently...",
                    "Can I offer another perspective?",
                    "What if we considered...",
                    "I'm curious about..."
                ],
                "connectors": [
                    "How might it feel to...",
                    "What would happen if...",
                    "Could there be another way to see this?",
                    "What evidence do we have for..."
                ],
                "closers": [
                    "What do you think about that?",
                    "How does that perspective sit with you?",
                    "I'm interested in your thoughts on this.",
                    "Does this resonate with you?"
                ]
            },
            CommunicationStyle.EDUCATIONAL: {
                "tone": "informative, clear, empowering",
                "openers": [
                    "Let me share some information that might help...",
                    "It can be helpful to understand...",
                    "Here's what research shows...",
                    "Many people find it useful to know..."
                ],
                "connectors": [
                    "This means that...",
                    "In practice, this looks like...",
                    "The reason for this is...",
                    "This connects to..."
                ],
                "closers": [
                    "How can we apply this to your situation?",
                    "What questions do you have?",
                    "Does this information help?",
                    "How might you use this?"
                ]
            },
            CommunicationStyle.CELEBRATORY: {
                "tone": "enthusiastic, proud, joyful",
                "openers": [
                    "This is wonderful news!",
                    "I'm so proud of you!",
                    "What an achievement!",
                    "You should feel really proud of yourself!"
                ],
                "connectors": [
                    "Look at what you accomplished!",
                    "This shows your dedication!",
                    "You earned this!",
                    "Your hard work paid off!"
                ],
                "closers": [
                    "Keep celebrating this success!",
                    "You deserve to feel proud!",
                    "This is just the beginning!",
                    "Congratulations on this milestone!"
                ]
            },
            CommunicationStyle.REFLECTIVE: {
                "tone": "thoughtful, curious, introspective",
                "openers": [
                    "Let's take a moment to reflect on...",
                    "What are you noticing about...",
                    "How does this connect to...",
                    "What insights are emerging for you?"
                ],
                "connectors": [
                    "What patterns do you see?",
                    "How has this changed over time?",
                    "What have you learned about yourself?",
                    "What stands out to you?"
                ],
                "closers": [
                    "What will you take away from this?",
                    "How can you build on these insights?",
                    "What does this mean for you moving forward?",
                    "Where do you go from here?"
                ]
            }
        }

    def _initialize_validation_phrases(self) -> List[str]:
        """Initialize phrases for validation"""
        return [
            "Your feelings make sense.",
            "That sounds really challenging.",
            "I can understand why you'd feel that way.",
            "Anyone in your position would struggle with this.",
            "It's completely normal to feel this way.",
            "You're not alone in experiencing this.",
            "What you're going through is difficult.",
            "Your reaction is understandable.",
            "It makes sense that you'd feel this way given what you've been through.",
            "I hear you.",
            "That sounds overwhelming.",
            "It's okay to feel the way you do.",
            "You have every right to feel this way.",
            "Thank you for sharing this with me.",
            "It takes strength to acknowledge these feelings."
        ]

    def _initialize_empathic_responses(self) -> Dict[EmotionCategory, List[str]]:
        """Initialize empathic responses for different emotions"""
        return {
            EmotionCategory.JOY: [
                "I'm so happy for you! This is wonderful!",
                "You must feel amazing! You've earned this!",
                "What a great accomplishment! Tell me more about it!",
                "I can feel your excitement! This is fantastic!",
                "You should be so proud of yourself!"
            ],
            EmotionCategory.SADNESS: [
                "I'm sorry you're going through this. I'm here with you.",
                "That sounds really painful. You don't have to face this alone.",
                "It makes sense that you'd feel this way. This is hard.",
                "I hear the sadness in what you're sharing. Thank you for trusting me.",
                "I'm here to support you through this difficult time."
            ],
            EmotionCategory.ANGER: [
                "I can hear how frustrated you are. That sounds really upsetting.",
                "You have every right to feel angry about this. That's not fair.",
                "It makes sense that this situation would make you feel this way.",
                "I understand why you're upset. Your feelings are valid.",
                "That sounds incredibly frustrating. I'd feel the same way."
            ],
            EmotionCategory.FEAR: [
                "It's understandable to feel worried about this. What you're facing is scary.",
                "I can hear the anxiety in what you're sharing. That sounds overwhelming.",
                "It makes sense to feel afraid. This is a lot to handle.",
                "Your fears are valid. Let's work through this together.",
                "It's okay to feel anxious. We'll take this one step at a time."
            ],
            EmotionCategory.SURPRISE: [
                "Wow, I can imagine that was unexpected!",
                "That must have caught you off guard!",
                "What a surprise! How are you processing this?",
                "I can understand why you'd be shocked by that.",
                "That's a lot to take in all at once."
            ],
            EmotionCategory.TRUST: [
                "Thank you for trusting me with this.",
                "I'm honored that you feel safe sharing this with me.",
                "I appreciate your openness and trust.",
                "It means a lot that you feel comfortable here.",
                "I'm glad you feel safe in our relationship."
            ]
        }

    def recognize_emotion(self, text: str, context: Optional[Dict] = None) -> EmotionalState:
        """
        Recognize emotional state from text and context

        Args:
            text: The text to analyze
            context: Additional context (history, member info, etc.)

        Returns:
            EmotionalState object
        """
        text_lower = text.lower()
        emotion_scores = {}

        # Score each emotion based on indicators
        for emotion, indicators in self.emotion_indicators.items():
            score = 0
            found_indicators = []

            # Check keywords
            for keyword in indicators["keywords"]:
                if keyword in text_lower:
                    score += 2
                    found_indicators.append(keyword)

            # Check phrases (worth more)
            for phrase in indicators["phrases"]:
                if phrase in text_lower:
                    score += 3
                    found_indicators.append(phrase)

            if score > 0:
                emotion_scores[emotion] = {
                    "score": score,
                    "indicators": found_indicators
                }

        # Determine primary and secondary emotions
        if emotion_scores:
            sorted_emotions = sorted(emotion_scores.items(), key=lambda x: x[1]["score"], reverse=True)
            primary = sorted_emotions[0][0]
            primary_indicators = sorted_emotions[0][1]["indicators"]
            secondary = [e[0] for e in sorted_emotions[1:3]] if len(sorted_emotions) > 1 else []
        else:
            primary = EmotionCategory.NEUTRAL
            primary_indicators = []
            secondary = []

        # Determine intensity based on indicators and language
        intensity = self._determine_intensity(text_lower, primary_indicators)

        # Identify needs
        needs = self.emotion_indicators.get(primary, {}).get("needs", [])

        return EmotionalState(
            primary_emotion=primary,
            secondary_emotions=secondary,
            intensity=intensity,
            indicators=primary_indicators,
            needs=needs
        )

    def _determine_intensity(self, text: str, indicators: List[str]) -> EmotionalIntensity:
        """Determine intensity of emotion"""
        # Intensity indicators
        mild_modifiers = ["a bit", "somewhat", "a little", "slightly", "kind of"]
        strong_modifiers = ["very", "really", "so", "extremely", "incredibly"]
        intense_modifiers = ["completely", "totally", "absolutely", "utterly", "overwhelming"]

        intensity_score = len(indicators)  # Base score on number of indicators

        # Adjust based on modifiers
        if any(modifier in text for modifier in intense_modifiers):
            return EmotionalIntensity.INTENSE
        elif any(modifier in text for modifier in strong_modifiers):
            intensity_score += 2
        elif any(modifier in text for modifier in mild_modifiers):
            intensity_score -= 1

        # Map score to intensity
        if intensity_score >= 6:
            return EmotionalIntensity.INTENSE
        elif intensity_score >= 4:
            return EmotionalIntensity.STRONG
        elif intensity_score >= 2:
            return EmotionalIntensity.MODERATE
        else:
            return EmotionalIntensity.MILD

    def generate_response_strategy(
        self,
        emotional_state: EmotionalState,
        context: Optional[Dict] = None
    ) -> ResponseStrategy:
        """
        Generate appropriate response strategy based on emotional state

        Args:
            emotional_state: Detected emotional state
            context: Additional context

        Returns:
            ResponseStrategy object
        """
        # Determine appropriate communication style
        style = self._select_communication_style(emotional_state)

        # Get style template
        template = self.response_templates[style]

        # Select empathy level
        empathy_level = self._determine_empathy_level(emotional_state.intensity)

        # Generate validation statements
        validation_statements = self._generate_validations(emotional_state)

        # Generate reframing opportunities (if appropriate)
        reframing_opportunities = self._generate_reframes(emotional_state)

        # Generate questions
        questions = self._generate_questions(emotional_state, style)

        # Things to avoid
        avoid = self._generate_avoid_list(emotional_state)

        return ResponseStrategy(
            communication_style=style,
            tone=template["tone"],
            empathy_level=empathy_level,
            validation_statements=validation_statements,
            reframing_opportunities=reframing_opportunities,
            questions_to_ask=questions,
            avoid=avoid
        )

    def _select_communication_style(self, emotional_state: EmotionalState) -> CommunicationStyle:
        """Select appropriate communication style"""
        emotion = emotional_state.primary_emotion
        intensity = emotional_state.intensity

        # High intensity negative emotions need supportive and validating approach
        if intensity in [EmotionalIntensity.INTENSE, EmotionalIntensity.STRONG]:
            if emotion in [EmotionCategory.SADNESS, EmotionCategory.FEAR, EmotionCategory.ANGER]:
                return CommunicationStyle.SUPPORTIVE

        # Joy and positive emotions warrant celebration
        if emotion in [EmotionCategory.JOY, EmotionCategory.TRUST]:
            return CommunicationStyle.CELEBRATORY

        # Anger might benefit from validation
        if emotion == EmotionCategory.ANGER:
            return CommunicationStyle.VALIDATING

        # Anticipation can be motivational
        if emotion == EmotionCategory.ANTICIPATION:
            return CommunicationStyle.MOTIVATIONAL

        # Default to supportive
        return CommunicationStyle.SUPPORTIVE

    def _determine_empathy_level(self, intensity: EmotionalIntensity) -> str:
        """Determine appropriate empathy level"""
        if intensity == EmotionalIntensity.INTENSE:
            return "high"
        elif intensity in [EmotionalIntensity.STRONG, EmotionalIntensity.MODERATE]:
            return "medium"
        else:
            return "low"

    def _generate_validations(self, emotional_state: EmotionalState) -> List[str]:
        """Generate validation statements"""
        validations = []

        # Add emotion-specific validation
        emotion_responses = self.empathic_responses.get(emotional_state.primary_emotion, [])
        if emotion_responses:
            validations.append(emotion_responses[0])  # Use first response

        # Add general validations
        validations.extend([
            "Your feelings are completely valid.",
            f"It makes sense that you'd feel {emotional_state.primary_emotion.value}."
        ])

        return validations[:3]  # Return top 3

    def _generate_reframes(self, emotional_state: EmotionalState) -> List[str]:
        """Generate potential reframing opportunities"""
        reframes = []

        if emotional_state.primary_emotion == EmotionCategory.SADNESS:
            reframes = [
                "While this is painful, what might you learn from this experience?",
                "What strengths are you using to cope with this difficulty?",
                "How might you show yourself compassion during this time?"
            ]
        elif emotional_state.primary_emotion == EmotionCategory.ANGER:
            reframes = [
                "What does this anger tell you about what you value?",
                "How might you use this energy constructively?",
                "What boundaries might need to be set?"
            ]
        elif emotional_state.primary_emotion == EmotionCategory.FEAR:
            reframes = [
                "What has helped you cope with fear in the past?",
                "What's one small step you could take to feel more in control?",
                "What supports do you have available?"
            ]

        return reframes

    def _generate_questions(self, emotional_state: EmotionalState, style: CommunicationStyle) -> List[str]:
        """Generate appropriate questions to ask"""
        questions = []

        if style == CommunicationStyle.SUPPORTIVE:
            questions = [
                "How can I best support you right now?",
                "What do you need most in this moment?",
                "Would you like to talk more about this?"
            ]
        elif style == CommunicationStyle.MOTIVATIONAL:
            questions = [
                "What's one step you could take toward your goal?",
                "What strengths can you draw on?",
                "What's possible for you?"
            ]
        elif style == CommunicationStyle.VALIDATING:
            questions = [
                "What else are you feeling?",
                "How long have you been feeling this way?",
                "What would help you feel understood?"
            ]
        elif style == CommunicationStyle.REFLECTIVE:
            questions = [
                "What are you noticing about yourself in this situation?",
                "What patterns are you seeing?",
                "What does this tell you?"
            ]

        return questions

    def _generate_avoid_list(self, emotional_state: EmotionalState) -> List[str]:
        """Generate list of things to avoid saying"""
        avoid = [
            "Minimizing: 'It's not that bad', 'Others have it worse'",
            "Toxic positivity: 'Just think positive', 'Everything happens for a reason'",
            "Fixing: 'You should just...', 'Why don't you...'",
            "Judging: 'You're overreacting', 'That's silly to feel that way'"
        ]

        if emotional_state.primary_emotion == EmotionCategory.SADNESS:
            avoid.extend([
                "Rushing: 'You'll get over it', 'Time to move on'",
                "Dismissing: 'Don't be sad', 'Cheer up'"
            ])
        elif emotional_state.primary_emotion == EmotionCategory.ANGER:
            avoid.extend([
                "Invalidating: 'Calm down', 'Don't be so angry'",
                "Defending: 'They didn't mean it', 'You're taking it wrong'"
            ])

        return avoid

    def craft_humanistic_response(
        self,
        member_message: str,
        context: Optional[Dict] = None
    ) -> Dict[str, any]:
        """
        Craft a complete humanistic response to member message

        Args:
            member_message: The message from the member
            context: Additional context

        Returns:
            Dictionary containing response components
        """
        # Recognize emotion
        emotional_state = self.recognize_emotion(member_message, context)

        # Generate response strategy
        strategy = self.generate_response_strategy(emotional_state, context)

        # Get style template
        template = self.response_templates[strategy.communication_style]

        return {
            "emotional_state": {
                "primary_emotion": emotional_state.primary_emotion.value,
                "intensity": emotional_state.intensity.name,
                "needs": emotional_state.needs
            },
            "strategy": {
                "communication_style": strategy.communication_style.value,
                "tone": strategy.tone,
                "empathy_level": strategy.empathy_level
            },
            "response_components": {
                "opener": template["openers"][0],
                "validation": strategy.validation_statements[0],
                "connector": template["connectors"][0],
                "question": strategy.questions_to_ask[0] if strategy.questions_to_ask else None
            },
            "guidance": {
                "avoid": strategy.avoid,
                "reframing_opportunities": strategy.reframing_opportunities
            }
        }


# Example usage
if __name__ == "__main__":
    ei = EmotionalIntelligence()

    # Test different emotional scenarios
    scenarios = [
        "I'm so excited! I just completed my first month of sobriety and I feel amazing!",
        "I'm really struggling today. I feel so hopeless and don't know if I can keep going.",
        "I'm so frustrated with the system. Nobody seems to care and nothing ever changes.",
        "I'm worried about my upcoming appointment. What if they don't understand me?"
    ]

    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{'=' * 60}")
        print(f"SCENARIO {i}:")
        print(f"{'=' * 60}")
        print(f"Member: '{scenario}'")
        print()

        response = ei.craft_humanistic_response(scenario)

        print(f"Emotion Detected: {response['emotional_state']['primary_emotion'].title()} "
              f"({response['emotional_state']['intensity']})")
        print(f"Needs: {', '.join(response['emotional_state']['needs'])}")
        print(f"\nCommunication Style: {response['strategy']['communication_style'].title()}")
        print(f"Tone: {response['strategy']['tone']}")
        print(f"\nSuggested Response:")
        print(f"  {response['response_components']['opener']}")
        print(f"  {response['response_components']['validation']}")
        if response['response_components']['question']:
            print(f"  {response['response_components']['question']}")
