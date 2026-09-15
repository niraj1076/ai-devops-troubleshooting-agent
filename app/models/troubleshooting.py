from dataclasses import dataclass, field
from typing import List


@dataclass
class Issue:
    raw_input: str
    platform: str
    service: str
    component: str
    problem_type: str
    symptoms: List[str] = field(default_factory=list)
    possible_causes: List[str] = field(default_factory=list)


@dataclass
class InvestigationStep:
    step_number: int
    objective: str
    command: str
    reason: str


@dataclass
class InvestigationPlan:
    issue: Issue
    steps: List[InvestigationStep] = field(default_factory=list)
