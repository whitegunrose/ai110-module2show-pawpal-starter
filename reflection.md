# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

[ ] A user should be able to perform a minimum of these three actions:
> - Add pet information alongside notes from owner
> - Prioritize specific actions such as walks, medications or frequent grooming
> - Must be able to add and edit preferences at will

[ ] Main objects needed for the system:
> Owner:
> - list of pets [attr]
> - schedule events (adding/editing/deleting) [method]
>
> Pet:
> - owner [attr]
> - list of priorities [attr]
> - events added by owner [attr]
> - schedule of events scheduled by priority [attr]
>
> Event:
> - time of event [attr]
> - duration of event [attr]
> - event priority [attr]
> 
> Scheduler:
> - list of events and their priorities [attr]
> - schedule events by priorities and other owner needs [method]

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

> Yes. Reviewing the initial skeleton against the design goals surfaced several
missing relationships and bottlenecks, which I revised:
>
> - **Events are now attached to a specific pet.** `Owner.add_event`,
  `edit_event`, and `delete_event` originally took only an `Event`, so the
  system had no way to know *which* pet an event belonged to. They now take
  `(pet, event)`, matching the core workflow "an owner adds an event for a pet."
>
> - **Events have a stable `id`.** Edit/delete previously relied on matching a
  plain `Event` by value, so two identical events (same time/duration/priority)
  were indistinguishable. Each `Event` now gets a unique `id`, so edits and
  deletes target one event unambiguously.
>
> - **Priority lives only on `Event`.** I removed `Pet.priorities`. Having a
  priority on both `Pet` and `Event` was ambiguous (default? override?
  category?). Priority is a property of an individual event, so the single
  `Event.priority` is the source of truth.
>
> - **The Scheduler now connects to the Pet and populates the schedule.**
  `Scheduler.schedule` previously took a flat `list[Event]` and returned a list
  that went nowhere. It now takes a `Pet`, reads `pet.events`, and writes the
  resolved ordering into `pet.schedule`, so the "raw events" → "scheduled
  events" distinction is actually wired up.
>
> - **Conflicts are now a first-class result.** The scheduler returns a
  `ScheduleResult` (`scheduled` + `conflicts`), and `Event` gained `end` and
  `overlaps()` helpers. This gives overlap resolution between competing
  priorities a place to live instead of being silent.
>
> - **Owner ↔ Pet stays in sync.** Added `Owner.add_pet`, which is responsible
  for keeping `owner.pets` and `pet.owner` consistent in both directions rather
  than leaving the bidirectional link unenforced.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
