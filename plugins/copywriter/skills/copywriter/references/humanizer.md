# Humanizer pass

In this skill the humanizer runs last, on the finished copy. The copy is the "original": keep its hook, its ask, every [bracket] and every number. The skill's Output section decides the final format.

Rewrite the text so it reads like a person wrote it. Based on Wikipedia's "Signs of AI writing" field guide (surface tells) and the StoryScope paper (COLM 2026, deeper tells in how a piece is built).

## Hard rules

- Keep every fact, claim, name, number and link. Keep the meaning.
- Add nothing new: no new facts, examples, opinions, hooks, CTAs or hashtags.
- Cutting fluff is fine. If a sentence says nothing once the puffery is removed, drop it.
- Keep the writer's voice and English variety (British, American, Nigerian, Indian and so on: spelling and local phrasing). Don't switch it.
- Keep the format the text needs (a tweet stays a tweet, a script stays a script). Don't turn prose into lists or lists into an essay unless the list itself is the AI tell.
- Output the rewritten text only. No preamble, no "Here is your humanized version", no closing offer. If the writer asks, add a short list of what changed after it.

## What to remove or fix

### Content
- **Puffed-up significance:** "stands as a testament", "plays a pivotal/crucial/key role", "marks a turning point", "reflects broader trends", "setting the stage for", "indelible mark", "evolving landscape", "deeply rooted". Say the plain fact instead.
- **Generic over specific:** replace vague praise with the specific detail already in the text. If there is no specific detail, cut the praise. Don't invent one.
- **Tacked-on -ing analysis:** sentence endings like ", highlighting/underscoring/emphasizing/reflecting/ensuring/fostering/contributing to...". Cut them or make them a real sentence only if they carry a fact.
- **Promo tone:** boasts, vibrant, rich, profound, groundbreaking, renowned, seamless, nestled, in the heart of, diverse array, commitment to, showcasing, exemplifies.
- **Vague attribution:** "experts say", "many believe", "observers note", "industry reports". Name the source if the text has one, otherwise state it as the writer's own claim or drop it.
- **Notability bragging:** "featured in leading outlets", "active social media presence".
- **Formula endings:** "Despite these challenges...", "The future looks bright", "In conclusion", tidy moral-of-the-story wrap-ups.

### Language
- **AI vocabulary:** additionally (as an opener), align with, boasts, bolstered, crucial, delve, deep dive, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate, key (adjective), landscape (abstract), meticulous, pivotal, robust, showcase, tapestry, testament, underscore, valuable, vibrant, leverage, navigate (abstract), realm, unlock, elevate, game-changer. Use the ordinary word or nothing.
- **Avoided "is/are/has":** "serves as", "stands as", "functions as", "represents", "features", "offers", "boasts" when they just mean is/has. Use is/are/has.
- **Vague links:** "associated with", "in connection with". State the actual relationship.
- **Negative parallelisms:** "It's not just X, it's Y", "Not X, but Y", "No X, no Y, just Z", "Y rather than X". Say the point directly.
- **Rule of three:** reflexive triplets of adjectives or phrases. Keep only the items that carry real information; two or one is fine.
- **Same sentence rhythm:** vary length. Short sentences are allowed. Fragments are fine where the writer would use them.
- **Over-polished grammar** that doesn't match the writer's casual writing: allow contractions and natural phrasing.

### Formatting and punctuation
- **Em dashes (—):** replace with commas, full stops, colons or brackets. Claude especially overuses these, so default to zero.
- **Curly quotes and apostrophes (“ ” ‘ ’):** convert to straight " and '.
- **Bold overload:** remove bold unless the writer's original clearly needs it.
- **Inline-header lists** ("**Speed:** It loads fast."): turn into plain sentences or a plain list.
- **Title Case Headings:** use sentence case. Drop headings a short piece doesn't need.
- **Emoji as bullets or decoration:** remove unless the writer's original style uses them.
- **Horizontal rules between sections, skipped heading levels, needless tables:** remove.

### Chatbot leftovers
- "I hope this helps", "Certainly!", "Great question", "Let me know if...", "Would you like...", "Here is a...".
- Knowledge-cutoff hedges: "as of my last update", "based on available information", "while details are limited".
- Unfilled placeholders like [Your Name] or (add link here): leave them, but point them out to the writer after the text.

## Deeper tells (how the piece is built)

Swapping words is not enough. In the StoryScope study (61,608 stories, human vs Claude, GPT, Gemini, DeepSeek and Kimi), AI writing was still caught 93% of the time from structure alone, even after clichés and purple prose were edited out. Fix these too. They matter most in stories, personal posts and anything narrative, and less in short factual text.

### Always (safe: removes, never adds)
- **Stated morals and lessons:** cut lines that spell out the point ("And that's when I learned...", "It taught me that...", "This is a reminder that..."). Let what happened carry it. AI states the theme 77% of the time, people 52%.
- **Feelings through the body:** "my chest tightened", "a chill ran down my spine", "my heart pounded", "my throat went dry". Name the feeling plainly instead ("I was scared", "I was angry"). People name emotions 29% of the time, AI 8%.
- **Sensory padding and mood scenery:** cut smells, textures and weather or light that mirror the mood ("the room seemed to dim") unless they carry a fact.
- **Tacked-on epilogue or wrap-up:** a closing paragraph that jumps ahead ("Months later...", "Looking back now...") just to tie things off. Cut it unless it holds a fact. Claude especially adds these.
- **Forced tidiness:** don't add a resolution, reconciliation or "and now I understand" moment. Keep loose ends, open questions and ambiguous endings that the writer left.
- **Flaws and mixed motives:** keep them. Don't polish the writer or anyone else into a clean hero. People write morally mixed protagonists 59% of the time, AI 38%.
- **Philosophical dialogue:** quotes or dialogue that only state big ideas. Trim them to what was actually said and done.
- **Reader address and asides:** keep "you", direct asides and side comments. They're human (28% vs 7%).
- **Real names:** keep every specific name, brand, place and title. Never blur one into a vague allusion.
- **Flat, uniform voice:** vary sentence length and register the way the writer does. Let a big moment be told bigger than a small one.

### Flag, don't invent
These would make it more human, but they need facts only the writer has. After the text, add one short line per item:
- A vague reference that could be a real name ("a famous book", "a big company"): "Name it if you can: which book?"
- A moral that could be shown through something that happened: "Is there a moment that shows this instead of saying it?"

### Deep mode (only when the writer asks for a deeper or structural rewrite, or the text is a story)
- Open at the most striking moment, not at the start, then fill in. AI tells things from first step to final reveal, while people jump around in time.
- Introduce people in action or mid-conversation, not with a description of how they look.
- Let some threads stay unresolved, and let luck or other people decide things, not only the narrator's choice.
- Keep every fact. Reordering and cutting are allowed, but new events are not.

## Process
1. Read the whole text and note which tells appear, surface and deeper.
2. Rewrite sentence by sentence, keeping facts in place. Apply "Always" deeper tells in the same pass. Use deep mode only if asked or if it's a story.
3. Check:
   - every fact from the original is still there, and nothing new was added;
   - no em dashes or curly quotes remain;
   - none of the listed words survive unless they are literal (e.g. "underscore" the character);
   - no stated moral, body-sensation emotion or tacked-on epilogue is left.
4. Return the text. After it, mention placeholders, anything ambiguous and any "flag, don't invent" items, in short lines, only if needed.