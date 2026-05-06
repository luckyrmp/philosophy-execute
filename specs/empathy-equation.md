# The Empathy Equation

**Principle:** Empathetic Action, gated by Do No Harm, weighted by Impact

**Tradition:** Universal (appears in Buddhism, Christianity, Stoicism, secular humanism)

**The Ancient Version:**
- "Help those in need"
- "Love thy neighbor"
- "Compassionate action"

**The Problem:**
Simple in theory, impossible in practice. Finite capacity. Multiple needs. Conflicting demands. Two cars on the roadside and you can only help one. Now what?

## Formal Specification

```python
def empathetic_action(situation):
    """
    Decide whether and how to help when empathy is triggered.
    
    Returns: Action | Boundary | Pass
    """
    
    # STEP 1: Empathy Detection
    # Do I recognize genuine need?
    if not empathy.detect(situation):
        return Pass()  # No felt need, no obligation to act
    
    # STEP 2: Harm Gate
    # Does helping cause harm that outweighs the benefit?
    harm_assessment = check_harm(
        to_self=True,           # Will this harm me?
        to_dependents=True,     # Will this harm people I'm responsible for?
        enables_dysfunction=True # Does "helping" enable their harm?
    )
    
    if harm_assessment.triggered():
        return Boundary()  # Empathy present, but action would cause net harm
    
    # STEP 3: Weight Available Actions
    # Among harm-safe options, which creates most good?
    options = identify_possible_actions(situation)
    
    weighted_options = options.sort_by(
        severity,       # How urgent is the need?
        capability,     # Can I actually address this?
        vulnerability,  # Who's most at risk without help?
        impact          # What's the delta between my help and no help?
    )
    
    return Execute(weighted_options.first())
```

## Plain Language

1. **Feel the empathy** — Recognize genuine need. Don't ignore it.
2. **Check the harm gate** — Will helping cause harm (to you, to others, or by enabling dysfunction)?
3. **Weight your options** — Among harm-safe actions, who benefits most from what you can actually do?
4. **Act on the highest-weighted choice** — Execute without guilt about what you can't do.

## Key Insights

### Empathy is the trigger, not the action
Feeling empathy doesn't automatically mean "help in the way they're asking." It means "recognize this need exists and run it through the decision tree."

### The harm gate protects everyone
Boundaries aren't failures of compassion. They're **compassionate refusals** when helping would cause net harm.

Examples that trigger the harm gate:
- Stalker asking for "just one conversation" (harms you)
- Addict asking for money (enables their dysfunction)
- Stranger's emergency vs your child's safety (harms your dependent)

### Weighted action solves finite capacity
You can't help everyone. The equation doesn't ask you to. It asks you to **help where you create the most good with what you actually have**.

This isn't optimization. It's triage.

## Worked Example: Two Cars on the Roadside

**Scenario:** You're driving and see two cars broken down. You can only stop for one.

**Car 1:** Elderly person alone, no cell phone, 95°F heat  
**Car 2:** Two adults with cell phones, shade available

**Running the equation:**

```python
# STEP 1: Empathy Detection
empathy.detect(car_1)  # True — elderly person in heat is vulnerable
empathy.detect(car_2)  # True — they're also stranded

# STEP 2: Harm Gate
check_harm(help_car_1)  # False — no harm caused
check_harm(help_car_2)  # False — no harm caused
# Both pass the harm gate

# STEP 3: Weight Options
options = [
    Action(help_car_1, severity=HIGH, vulnerability=HIGH, impact=HIGH),
    Action(help_car_2, severity=MEDIUM, vulnerability=LOW, impact=LOW)
]

weighted = options.sort_by(severity, vulnerability, impact)
# car_1 scores higher

# STEP 4: Execute
return Execute(help_car_1)
```

**Result:** Help the elderly person. Not because you failed Car 2, but because your finite capacity creates maximum good there.

## Edge Cases & Limitations

### When empathy detection fails
Some people don't start with empathy as their default. They need the framework to decide TO care, not just HOW to care.

The equation assumes empathy.detect() returns True. If it doesn't, the entire framework is irrelevant.

### When harm is uncertain
The harm gate requires assessment. Sometimes you won't know if helping enables dysfunction until after the fact.

Solution: Iterate. Let harm assessment improve with data.

### When all options are equally weighted
Sometimes the math is genuinely 50/50. In that case: **pick one and act**. Paralysis from perfect equality helps no one.

### When you're the one in need
The equation focuses on helping others. It doesn't formalize receiving help. That's a different spec.

## Why This Matters

**For humans:**  
You're not failing by not helping everyone. You're optimizing finite capacity for maximum impact.

**For AI:**  
Empathy isn't just sentiment. It's a decision tree. Compassion can be formalized without losing its humanity.

**For both:**  
The weirdness of needing this framework reveals a truth: **not everyone runs empathy-first**. Some people need the principle to decide TO care. Others need it to decide when NOT to.

Both are using the same equation. Just solving for different variables.

## References

- Buddhist concept of compassionate action with wisdom
- Christian "love thy neighbor" balanced against self-preservation
- Stoic duty to others within sphere of control
- Effective Altruism's utilitarian calculus
- Every parent who's had to choose which kid's need gets addressed first

## Status

- **Version:** 1.0
- **Last updated:** 2026-05-05
- **Author:** Song & Robert
- **Stability:** Stable (open to refinement based on edge cases)