from dataclasses import dataclass


@dataclass
class SessionConfig:
    mode: str
    topic: str | None
    difficulty: str
    problem_id: str | None
