# Installing superpowers for OpenCode

## Prerequisites

- [OpenCode.AI](https://opencode.ai) installed
- Git installed

## Installation steps

### 1. clone superpowers

```bash
git clone https://github.com/armstrongl/superpowers.git ~/.config/opencode/superpowers
```

### 2. register the plugin

Create a symlink so OpenCode discovers the plugin:

```bash
mkdir -p ~/.config/opencode/plugins
rm -f ~/.config/opencode/plugins/superpowers.js
ln -s ~/.config/opencode/superpowers/.opencode/plugins/superpowers.js ~/.config/opencode/plugins/superpowers.js
```

### 3. symlink skills

Create a symlink so OpenCode's native skill tool discovers superpowers skills:

```bash
mkdir -p ~/.config/opencode/skills
rm -rf ~/.config/opencode/skills/superpowers
ln -s ~/.config/opencode/superpowers/skills ~/.config/opencode/skills/superpowers
```

### 4. restart OpenCode

Restart OpenCode. The plugin will automatically inject superpowers context.

Verify by asking: "do you have superpowers?"

## Usage

### Finding skills

Use OpenCode's native `skill` tool to list available skills:

```text
use skill tool to list skills
```

### Loading a skill

Use OpenCode's native `skill` tool to load a specific skill:

```text
use skill tool to load superpowers/brainstorming
```

### Personal skills

Create your own skills in `~/.config/opencode/skills/`:

```bash
mkdir -p ~/.config/opencode/skills/my-skill
```

Create `~/.config/opencode/skills/my-skill/SKILL.md`:

```markdown
---
description: Use when [condition] - [what it does]
name: my-skill
---

# My skill

[Your skill content here]
```

### Project skills

Create project-specific skills in `.opencode/skills/` within your project.

**Skill Priority:** Project skills > Personal skills > Superpowers skills

## Updating

```bash
cd ~/.config/opencode/superpowers
git pull
```

## Troubleshooting

### Plugin not loading

1. Check plugin symlink: `ls -l ~/.config/opencode/plugins/superpowers.js`
2. Check source exists: `ls ~/.config/opencode/superpowers/.opencode/plugins/superpowers.js`
3. Check OpenCode logs for errors

### Skills not found

1. Check skills symlink: `ls -l ~/.config/opencode/skills/superpowers`
2. Verify it points to: `~/.config/opencode/superpowers/skills`
3. Use `skill` tool to list what's discovered

### Tool mapping

When skills reference Claude Code tools:

- `TodoWrite` → `todowrite`
- `Task` with subagents → `@mention` syntax
- `Skill` tool → OpenCode's native `skill` tool
- File operations → your native tools

## Getting help

- Report issues: https://GitHub.com/armstrongl/superpowers/issues
- Full documentation: https://GitHub.com/armstrongl/superpowers/blob/main/docs/README.opencode.md
