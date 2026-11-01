# Copywriter skill

Write or rewrite selling copy, then humanize it so it reads like a person wrote it. The skill works for Claude Code, claude.ai and ChatGPT.

It runs two passes:
1. **Copy pass.** It follows the selling order (problem, cost, promise, proof, one next step) and runs Harry Dry's three tests on every line. It only uses persuasion levers backed by real facts. Any number you haven't given stays in [brackets], so it never makes one up.
2. **Humanizer pass.** It strips em dashes, AI words, "not X but Y" lines, stated morals and padding, and keeps your facts, hook and ask.

You get the best version first, a few alternatives with one line each on why they work, and the [brackets] you need to fill in.

Works for hooks, headlines, subject lines, cold emails, DMs, follow-ups, sales pages, landing pages, social posts, video scripts, flyers, ads, sales scripts and offers.

## Install

### Claude Code

```
/plugin marketplace add Okorodavid/copywriter-skill
/plugin install copywriter@okorodavid
```

Restart Claude Code. Then ask for copy ("rewrite this cold email: ...") or type `/copywriter`.

Without the plugin system, copy the skill folder into your skills folder:

```bash
git clone https://github.com/Okorodavid/copywriter-skill
cp -r copywriter-skill/plugins/copywriter/skills/copywriter ~/.claude/skills/
```

On Windows (PowerShell):

```powershell
git clone https://github.com/Okorodavid/copywriter-skill
Copy-Item -Recurse copywriter-skill\plugins\copywriter\skills\copywriter $HOME\.claude\skills\
```

### claude.ai (web, desktop and mobile apps)

1. Download [copywriter-claude-skill.zip](https://github.com/Okorodavid/copywriter-skill/releases/latest/download/copywriter-claude-skill.zip).
2. In Claude, go to **Settings > Capabilities**. Turn on **Code execution and file creation** if it's off.
3. Under **Skills**, click **Upload skill** and pick the zip. Don't unzip it.
4. Ask for copy in any chat. Claude loads the skill when the request fits.

### ChatGPT

Download [copywriter-chatgpt.zip](https://github.com/Okorodavid/copywriter-skill/releases/latest/download/copywriter-chatgpt.zip) and follow [chatgpt/SETUP.md](chatgpt/SETUP.md). You can set it up as a Custom GPT (paste the instructions, upload the 10 knowledge files) or as a ChatGPT Project.

### Other agents

The skill is a plain `SKILL.md` folder. Agents that read skills (Codex CLI, for example) can load it from their skills folder. For Codex that's `~/.codex/skills/copywriter`.

## Try it

```
Rewrite this cold email so it gets a reply: <paste>
Write 5 hooks for a TikTok about my meal-prep service for nurses on night shifts
Write a sales page for a $29 Notion budget template. I have 41 sales and 6 reviews.
Make this LinkedIn post sound less like AI: <paste>
```

## What's inside

```
plugins/copywriter/skills/copywriter/
  SKILL.md                         the two-pass method
  references/
    playbook.md                    read first: three tests, selling order, 7 levers, formats, 10-point check
    headlines.md                   headline types, the 4 U's
    clear-writing-and-selling.md   clarity, benefits, the motivating sequence, USP, research
    print-flyers-and-letters.md    ads, sales letters, flyers, brochures
    landing-pages-and-websites.md  landing page section order
    email.md                       email, cold email, a 4-email sequence
    social-video-ads-content.md    posts, scripts, online ads, PR, content
    persuasion-levers.md           Cialdini's 7 levers, used honestly
    lessons-dry-tyson-georgi.md    Harry Dry, Tyson 4D, Stefan Georgi
    humanizer.md                   the last pass
chatgpt/                           Custom GPT instructions and setup
scripts/build.py                   checks the files and builds both zips into dist/
```

## Credits

The reference files are our own notes on:
- Robert Cialdini, *Influence* (new and expanded edition)
- Robert W. Bly, *The Copywriter's Handbook* (4th edition)
- talks by Harry Dry, Tyson 4D and Stefan Georgi

The humanizer draws on Wikipedia's "Signs of AI writing" guide and the StoryScope paper (COLM 2026).

None of their text is reproduced. Buy the books, because they go much deeper than these notes.

Made by [David Okoro](https://github.com/Okorodavid). MIT licence.
