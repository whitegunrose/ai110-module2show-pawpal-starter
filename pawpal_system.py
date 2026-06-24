"""PawPal+ initial design — Owner, Pet, Event, Scheduler.

Skeleton generated from diagrams/uml.mmd. Method bodies are left as stubs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum


class Priority(Enum):
    """Relative importance of a pet's events/needs."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3


@dataclass
class Event:
    time: datetime
    duration: timedelta
    priority: Priority


@dataclass
class Pet:
    owner: "Owner"
    priorities: list[Priority] = field(default_factory=list)
    events: list[Event] = field(default_factory=list)
    schedule: list[Event] = field(default_factory=list)


@dataclass
class Owner:
    pets: list[Pet] = field(default_factory=list)

    def add_event(self, event: Event) -> None:
        ...

    def edit_event(self, event: Event) -> None:
        ...

    def delete_event(self, event: Event) -> None:
        ...


class Scheduler:
    def __init__(self, events: list[Event] | None = None) -> None:
        self.events: list[Event] = events if events is not None else []

    def schedule(self, events: list[Event]) -> list[Event]:
        ...
