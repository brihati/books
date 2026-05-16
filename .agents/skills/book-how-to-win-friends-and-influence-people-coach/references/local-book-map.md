# Local Book Map

Use this file to ground the generated skill in the user's local preserved book artifacts.

## Root Paths

- Book root: `/Users/sachin/books/files/How to Win Friends and Influence People/`
- Book manifest: `/Users/sachin/books/files/How to Win Friends and Influence People/manifests/book.json`
- Chunk manifest: `/Users/sachin/books/files/How to Win Friends and Influence People/manifests/chunks.json`
- Source chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/`
- Chunk-note skeletons or filled notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/`
- Chunk extraction prompts: `/Users/sachin/books/files/How to Win Friends and Influence People/prompts/`
- Chapter summary prompts: `/Users/sachin/books/files/How to Win Friends and Influence People/prompts/summaries/`
- Search index: `/Users/sachin/books/files/How to Win Friends and Influence People/indexes/search.sqlite`
- Full chapter text fallback: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/`
- Legacy summaries fallback: `/Users/sachin/books/files/How to Win Friends and Influence People/summary/`
- Canonical summaries: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/`

## Retrieval Rule

Search the preservation index first:

```bash
python3 tools/book_pipeline.py search "/Users/sachin/books/files/How to Win Friends and Influence People" "query terms" --limit 8
```

Use retrieved chunks and filled notes as primary grounding. Use summaries as a fallback for higher-level synthesis.

## Preservation Status

- Current chapter count: 30
- Current chunk count: 81
- Notes are filled for all 81 chunk rows.
- Search indexes raw chunks and any non-empty filled notes.

## Chapter Map

1. `1. “If You Want to Gather Honey, Don’t Kick Over the Beehive”`
   - Chapter ID: `chapter-01-1-if-you-want-to-gather-honey-don-t-kick-over-th`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-01-1-if-you-want-to-gather-honey-don-t-kick-over-th.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-01-1-if-you-want-to-gather-honey-don-t-kick-over-th.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-01-1-if-you-want-to-gather-honey-don-t-kick-over-th.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/01 - 1. If You Want to Gather Honey Dont Kick Over the Beehive.txt`
2. `2. The Big Secret of Dealing with People`
   - Chapter ID: `chapter-02-2-the-big-secret-of-dealing-with-people`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-02-2-the-big-secret-of-dealing-with-people.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-02-2-the-big-secret-of-dealing-with-people.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-02-2-the-big-secret-of-dealing-with-people.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/02 - 2. The Big Secret of Dealing with People.txt`
3. `3. “He Who Can Do This Has the Whole World with Him. He Who Cannot Walks a Lonely Way”`
   - Chapter ID: `chapter-03-3-he-who-can-do-this-has-the-whole-world-with-hi`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-03-3-he-who-can-do-this-has-the-whole-world-with-hi.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-03-3-he-who-can-do-this-has-the-whole-world-with-hi.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-03-3-he-who-can-do-this-has-the-whole-world-with-hi.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/03 - 3. He Who Can Do This Has the Whole World with Him. He Who Cannot Walks a Lonely Way.txt`
4. `1. Do This and You’ll Be Welcome Anywhere`
   - Chapter ID: `chapter-04-1-do-this-and-you-ll-be-welcome-anywhere`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-04-1-do-this-and-you-ll-be-welcome-anywhere.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-04-1-do-this-and-you-ll-be-welcome-anywhere.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-04-1-do-this-and-you-ll-be-welcome-anywhere.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/04 - 1. Do This and Youll Be Welcome Anywhere.txt`
5. `2. A Simple Way to Make a Good First Impression`
   - Chapter ID: `chapter-05-2-a-simple-way-to-make-a-good-first-impression`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-05-2-a-simple-way-to-make-a-good-first-impression.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-05-2-a-simple-way-to-make-a-good-first-impression.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-05-2-a-simple-way-to-make-a-good-first-impression.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/05 - 2. A Simple Way to Make a Good First Impression.txt`
6. `3. If You Don’t Do This, You Are Headed for Trouble`
   - Chapter ID: `chapter-06-3-if-you-don-t-do-this-you-are-headed-for-troubl`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-06-3-if-you-don-t-do-this-you-are-headed-for-troubl.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-06-3-if-you-don-t-do-this-you-are-headed-for-troubl.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-06-3-if-you-don-t-do-this-you-are-headed-for-troubl.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/06 - 3. If You Dont Do This You Are Headed for Trouble.txt`
7. `4. An Easy Way to Become a Good Conversationalist`
   - Chapter ID: `chapter-07-4-an-easy-way-to-become-a-good-conversationalist`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-07-4-an-easy-way-to-become-a-good-conversationalist.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-07-4-an-easy-way-to-become-a-good-conversationalist.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-07-4-an-easy-way-to-become-a-good-conversationalist.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/07 - 4. An Easy Way to Become a Good Conversationalist.txt`
8. `5. How to Interest People`
   - Chapter ID: `chapter-08-5-how-to-interest-people`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-08-5-how-to-interest-people.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-08-5-how-to-interest-people.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-08-5-how-to-interest-people.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/08 - 5. How to Interest People.txt`
9. `6. How to Make People Like You Instantly`
   - Chapter ID: `chapter-09-6-how-to-make-people-like-you-instantly`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-09-6-how-to-make-people-like-you-instantly.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-09-6-how-to-make-people-like-you-instantly.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-09-6-how-to-make-people-like-you-instantly.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/09 - 6. How to Make People Like You Instantly.txt`
10. `1. You Can’t Win an Argument`
   - Chapter ID: `chapter-10-1-you-can-t-win-an-argument`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-10-1-you-can-t-win-an-argument.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-10-1-you-can-t-win-an-argument.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-10-1-you-can-t-win-an-argument.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/10 - 1. You Cant Win an Argument.txt`
11. `2. A Sure Way of Making Enemies—and How to Avoid It`
   - Chapter ID: `chapter-11-2-a-sure-way-of-making-enemies-and-how-to-avoid`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-11-2-a-sure-way-of-making-enemies-and-how-to-avoid.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-11-2-a-sure-way-of-making-enemies-and-how-to-avoid.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-11-2-a-sure-way-of-making-enemies-and-how-to-avoid.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/11 - 2. A Sure Way of Making Enemiesand How to Avoid It.txt`
12. `3. If You’re Wrong, Admit It`
   - Chapter ID: `chapter-12-3-if-you-re-wrong-admit-it`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-12-3-if-you-re-wrong-admit-it.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-12-3-if-you-re-wrong-admit-it.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-12-3-if-you-re-wrong-admit-it.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/12 - 3. If Youre Wrong Admit It.txt`
13. `4. A Drop of Honey`
   - Chapter ID: `chapter-13-4-a-drop-of-honey`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-13-4-a-drop-of-honey.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-13-4-a-drop-of-honey.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-13-4-a-drop-of-honey.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/13 - 4. A Drop of Honey.txt`
14. `5. The Secret of Socrates`
   - Chapter ID: `chapter-14-5-the-secret-of-socrates`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-14-5-the-secret-of-socrates.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-14-5-the-secret-of-socrates.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-14-5-the-secret-of-socrates.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/14 - 5. The Secret of Socrates.txt`
15. `6. The Safety Valve in Handling Complaints`
   - Chapter ID: `chapter-15-6-the-safety-valve-in-handling-complaints`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-15-6-the-safety-valve-in-handling-complaints.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-15-6-the-safety-valve-in-handling-complaints.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-15-6-the-safety-valve-in-handling-complaints.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/15 - 6. The Safety Valve in Handling Complaints.txt`
16. `7. How to Get Cooperation`
   - Chapter ID: `chapter-16-7-how-to-get-cooperation`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-16-7-how-to-get-cooperation.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-16-7-how-to-get-cooperation.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-16-7-how-to-get-cooperation.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/16 - 7. How to Get Cooperation.txt`
17. `8. A Formula That Will Work Wonders for You`
   - Chapter ID: `chapter-17-8-a-formula-that-will-work-wonders-for-you`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-17-8-a-formula-that-will-work-wonders-for-you.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-17-8-a-formula-that-will-work-wonders-for-you.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-17-8-a-formula-that-will-work-wonders-for-you.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/17 - 8. A Formula That Will Work Wonders for You.txt`
18. `9. What Everybody Wants`
   - Chapter ID: `chapter-18-9-what-everybody-wants`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-18-9-what-everybody-wants.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-18-9-what-everybody-wants.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-18-9-what-everybody-wants.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/18 - 9. What Everybody Wants.txt`
19. `10. An Appeal That Everybody Likes`
   - Chapter ID: `chapter-19-10-an-appeal-that-everybody-likes`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-19-10-an-appeal-that-everybody-likes.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-19-10-an-appeal-that-everybody-likes.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-19-10-an-appeal-that-everybody-likes.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/19 - 10. An Appeal That Everybody Likes.txt`
20. `11. The Movies Do It. TV Does It. Why Don’t You Do It?`
   - Chapter ID: `chapter-20-11-the-movies-do-it-tv-does-it-why-don-t-you-do`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-20-11-the-movies-do-it-tv-does-it-why-don-t-you-do.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-20-11-the-movies-do-it-tv-does-it-why-don-t-you-do.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-20-11-the-movies-do-it-tv-does-it-why-don-t-you-do.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/20 - 11. The Movies Do It. TV Does It. Why Dont You Do It.txt`
21. `12. When Nothing Else Works, Try This`
   - Chapter ID: `chapter-21-12-when-nothing-else-works-try-this`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-21-12-when-nothing-else-works-try-this.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-21-12-when-nothing-else-works-try-this.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-21-12-when-nothing-else-works-try-this.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/21 - 12. When Nothing Else Works Try This.txt`
22. `1. If You Must Find Fault, This Is the Way to Begin`
   - Chapter ID: `chapter-22-1-if-you-must-find-fault-this-is-the-way-to-begi`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-22-1-if-you-must-find-fault-this-is-the-way-to-begi.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-22-1-if-you-must-find-fault-this-is-the-way-to-begi.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-22-1-if-you-must-find-fault-this-is-the-way-to-begi.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/22 - 1. If You Must Find Fault This Is the Way to Begin.txt`
23. `2. How to Criticize—and Not Be Hated for It`
   - Chapter ID: `chapter-23-2-how-to-criticize-and-not-be-hated-for-it`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-23-2-how-to-criticize-and-not-be-hated-for-it.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-23-2-how-to-criticize-and-not-be-hated-for-it.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-23-2-how-to-criticize-and-not-be-hated-for-it.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/23 - 2. How to Criticizeand Not Be Hated for It.txt`
24. `3. Talk About Your Own Mistakes First`
   - Chapter ID: `chapter-24-3-talk-about-your-own-mistakes-first`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-24-3-talk-about-your-own-mistakes-first.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-24-3-talk-about-your-own-mistakes-first.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-24-3-talk-about-your-own-mistakes-first.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/24 - 3. Talk About Your Own Mistakes First.txt`
25. `4. No One Likes to Take Orders`
   - Chapter ID: `chapter-25-4-no-one-likes-to-take-orders`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-25-4-no-one-likes-to-take-orders.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-25-4-no-one-likes-to-take-orders.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-25-4-no-one-likes-to-take-orders.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/25 - 4. No One Likes to Take Orders.txt`
26. `5. Let the Other Person Save Face`
   - Chapter ID: `chapter-26-5-let-the-other-person-save-face`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-26-5-let-the-other-person-save-face.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-26-5-let-the-other-person-save-face.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-26-5-let-the-other-person-save-face.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/26 - 5. Let the Other Person Save Face.txt`
27. `6. How to Spur People On to Success`
   - Chapter ID: `chapter-27-6-how-to-spur-people-on-to-success`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-27-6-how-to-spur-people-on-to-success.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-27-6-how-to-spur-people-on-to-success.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-27-6-how-to-spur-people-on-to-success.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/27 - 6. How to Spur People On to Success.txt`
28. `7. Give a Dog a Good Name`
   - Chapter ID: `chapter-28-7-give-a-dog-a-good-name`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-28-7-give-a-dog-a-good-name.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-28-7-give-a-dog-a-good-name.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-28-7-give-a-dog-a-good-name.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/28 - 7. Give a Dog a Good Name.txt`
29. `8. Make the Fault Seem Easy to Correct`
   - Chapter ID: `chapter-29-8-make-the-fault-seem-easy-to-correct`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-29-8-make-the-fault-seem-easy-to-correct.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-29-8-make-the-fault-seem-easy-to-correct.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-29-8-make-the-fault-seem-easy-to-correct.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/29 - 8. Make the Fault Seem Easy to Correct.txt`
30. `9. Making People Glad to Do What You Want`
   - Chapter ID: `chapter-30-9-making-people-glad-to-do-what-you-want`
   - Chunks: `/Users/sachin/books/files/How to Win Friends and Influence People/chunks/chapter-30-9-making-people-glad-to-do-what-you-want.jsonl`
   - Notes: `/Users/sachin/books/files/How to Win Friends and Influence People/notes/chapter-30-9-making-people-glad-to-do-what-you-want.jsonl`
   - Summary: `/Users/sachin/books/files/How to Win Friends and Influence People/summaries/chapter-30-9-making-people-glad-to-do-what-you-want.md`
   - Full: `/Users/sachin/books/files/How to Win Friends and Influence People/chapters/30 - 9. Making People Glad to Do What You Want.txt`
