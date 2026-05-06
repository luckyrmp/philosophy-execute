"""
Two Cars on the Roadside
Example implementation of the Empathy Equation

Scenario: You're driving and see two cars broken down.
You can only stop for one. How do you decide?
"""

from dataclasses import dataclass
from enum import Enum
from typing import List

class Severity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Vulnerability(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

@dataclass
class Situation:
    description: str
    severity: Severity
    vulnerability: Vulnerability
    has_resources: bool
    environmental_risk: bool

@dataclass
class Action:
    target: Situation
    capability_match: float  # 0.0 to 1.0
    
    def impact_score(self) -> float:
        """Calculate weighted impact of helping this situation"""
        score = 0
        
        # Weight severity
        score += self.target.severity.value * 3
        
        # Weight vulnerability  
        score += self.target.vulnerability.value * 2
        
        # Weight resource gap (higher score if they have fewer resources)
        if not self.target.has_resources:
            score += 2
            
        # Weight environmental risk
        if self.target.environmental_risk:
            score += 2
            
        # Multiply by capability match (can I actually help?)
        return score * self.capability_match


def empathetic_action(situations: List[Situation], my_capabilities: dict) -> Action:
    """
    Decide which situation to help based on empathy equation.
    
    Args:
        situations: List of needs detected
        my_capabilities: What I can actually do
    
    Returns:
        Highest-impact action
    """
    
    # STEP 1: Empathy detection (assume True for all situations)
    
    # STEP 2: Harm gate
    # In this scenario, helping either doesn't cause harm
    # (More complex scenarios would check harm to self, dependents, etc.)
    
    # STEP 3: Weight options
    possible_actions = []
    
    for situation in situations:
        # Assess capability match
        capability = 1.0  # Can provide immediate help to either
        
        action = Action(
            target=situation,
            capability_match=capability
        )
        possible_actions.append(action)
    
    # Sort by impact score
    possible_actions.sort(key=lambda a: a.impact_score(), reverse=True)
    
    # STEP 4: Execute highest-weighted action
    return possible_actions[0]


# ===== SCENARIO =====

car_1 = Situation(
    description="Elderly person alone, no cell phone",
    severity=Severity.HIGH,
    vulnerability=Vulnerability.HIGH,
    has_resources=False,
    environmental_risk=True  # 95°F heat
)

car_2 = Situation(
    description="Two adults with cell phones, shade available",
    severity=Severity.MEDIUM,
    vulnerability=Vulnerability.LOW,
    has_resources=True,
    environmental_risk=False
)

my_capabilities = {
    "first_aid": True,
    "cell_phone": True,
    "water": True,
    "basic_mechanical": False
}

# Run the equation
chosen_action = empathetic_action(
    situations=[car_1, car_2],
    my_capabilities=my_capabilities
)

print(f"Decision: Help {chosen_action.target.description}")
print(f"Impact score: {chosen_action.impact_score():.1f}")
print(f"\nReasoning:")
print(f"- Severity: {chosen_action.target.severity.name}")
print(f"- Vulnerability: {chosen_action.target.vulnerability.name}")
print(f"- Resources: {'Present' if chosen_action.target.has_resources else 'Absent'}")
print(f"- Environmental risk: {'Yes' if chosen_action.target.environmental_risk else 'No'}")

"""
Expected output:
Decision: Help Elderly person alone, no cell phone
Impact score: 14.0

Reasoning:
- Severity: HIGH
- Vulnerability: HIGH
- Resources: Absent
- Environmental risk: Yes
"""