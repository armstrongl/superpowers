# Brainstorming skill — reference sources

Authoritative sources used to ground this skill. Run
`scripts/fetch_resources.py` to pull fresh copies of these documents into
this directory.

## Sources

### Nielsen norman group: design thinking 101

- **URL:** <https://www.nngroup.com/articles/design-thinking/>
- **File:** `nngroup-design-thinking-101.md`
- **Why:** Foundational overview of the design thinking process from the leading
  UX research firm. Covers Empathize, Define, Ideate, Prototype, Test — the
  stages that structure collaborative design sessions.

### Nielsen norman group: ideation for everyday design challenges

- **URL:** <https://www.nngroup.com/articles/ux-ideation/>
- **File:** `nngroup-ideation.md`
- **Why:** Covers brainstorming as formalized ideation (Osborn's rules), when to
  ideate in the design cycle, and how to ground ideas in user needs rather than
  assumptions. Directly informs the clarifying-questions and
  propose-approaches steps of this skill.

### IDEO design thinking: brainstorming

- **URL:** <https://designthinking.ideo.com/resources/brainstorming>
- **File:** `ideo-brainstorming.md`
- **Why:** IDEO's canonical brainstorming rules (defer judgment, one
  conversation at a time) and the broader Design Thinking framework
  (inspiration, synthesis, ideation/experimentation, implementation). Shapes
  the session facilitation principles throughout this skill.

## Fetching

```bash
python scripts/fetch_resources.py
```

The script fetches each URL, strips HTML, and saves plain text to this
directory. It skips unchanged files and reports failures. Re-run whenever
reference content feels outdated or before a major skill revision.
