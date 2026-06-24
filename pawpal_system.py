"""PawPal+ initial design — Owner, Pet, Event, Scheduler.

Skeleton generated from diagrams/uml.mmd. Method bodies are left as stubs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from itertools import count


class Priority(Enum):
    """Relative importance of a pet's events/needs."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3


# Module-level counter that hands out a unique id to every Event so that
# edit/delete can target a specific event unambiguously (two walks at the
# same time/duration/priority are otherwise indistinguishable).
_event_ids = count(1)


@dataclass
class Event:
    time: datetime
    duration: timedelta
    priority: Priority
    id: int = field(default_factory=lambda: next(_event_ids))

    @property
    def end(self) -> datetime:
        """Convenience: when this event finishes, used for overlap checks."""
        return self.time + self.duration

    def overlaps(self, other: "Event") -> bool:
        """Whether this event's time window collides with another's."""
        ...


@dataclass
class Pet:
    # `owner` is set when the pet is attached via Owner.add_pet so the
    # Owner <-> Pet link stays consistent in both directions.
    owner: "Owner | None" = None
    # Raw events the owner added for this pet (unordered input).
    events: list[Event] = field(default_factory=list)
    # Ordered, conflict-resolved output produced by Scheduler.schedule.
    schedule: list[Event] = field(default_factory=list)


@dataclass
class Owner:
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Attach a pet and keep the bidirectional owner link in sync."""
        ...

    def add_event(self, pet: Pet, event: Event) -> None:
        """Add an event to a specific pet's event list."""
        ...

    def edit_event(self, pet: Pet, event: Event) -> None:
        """Replace the matching event (by Event.id) on the given pet."""
        ...

    def delete_event(self, pet: Pet, event: Event) -> None:
        """Remove the matching event (by Event.id) from the given pet."""
        ...


@dataclass
class ScheduleResult:
    """Outcome of a scheduling run: what was placed and what could not be."""

    scheduled: list[Event] = field(default_factory=list)
    conflicts: list[Event] = field(default_factory=list)


class Scheduler:
    def schedule(self, pet: Pet) -> ScheduleResult:
        """Order a pet's events by priority/time, resolving overlaps.

        Writes the resolved ordering into ``pet.schedule`` and returns a
        ScheduleResult describing which events were placed and which were
        dropped due to conflicts.
        """
        ...
