# Set up Copywriter in ChatGPT

You need the files from `copywriter-chatgpt.zip` (from the repo's Releases page, or run `python scripts/build.py`). Unzip it. You get `instructions.md` and a `knowledge` folder with 10 files.

## Option A: a Custom GPT (ChatGPT Plus, Team or Enterprise to build it; anyone can use it once shared)

1. Go to chatgpt.com/gpts/editor and open the **Configure** tab.
2. **Name:** Copywriter
3. **Description:** Writes or rewrites selling copy, then humanizes it.
4. **Instructions:** paste everything in `instructions.md`.
5. **Conversation starters:**
   - Rewrite this cold email so it gets replies:
   - Write 5 hooks for a TikTok about
   - Write a sales page for
   - Make this LinkedIn post sound less like AI:
6. **Knowledge:** upload all 10 files from the `knowledge` folder.
7. **Capabilities:** turn off Image generation. Web search and Code interpreter can stay on or off.
8. Press **Create**, then choose who can see it: only you, anyone with the link, or the GPT Store.

## Option B: a ChatGPT Project (works on more plans)

1. In the ChatGPT sidebar, click **New project** and name it Copywriter.
2. Open the project's **Instructions** and paste everything in `instructions.md`.
3. Add the 10 files from the `knowledge` folder as **project files**.
4. Start every copy chat inside that project.

## Check it works

Paste this and look for 4-5 options, a best pick first, no em dashes and [brackets] where facts are missing:

> Write subject lines for a cold email to dental clinics about an AI receptionist that answers missed calls.
