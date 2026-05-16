# BookWiki Maintenance Rules

This wiki is the generated, inspectable memory layer for the Cognee BookWiki hackathon project.

Rules for agents:
- Treat `files/<Book>/` artifacts as source truth. Do not edit raw book artifacts from this wiki workflow.
- Cite book, chapter, chunk, and source paths for claims that come from books.
- Keep concept pages short and cross-linked with Obsidian wiki links such as `books/book-slug`, `concepts/concept-slug`, and `playbooks/playbook-slug`.
- Use `index.md` for navigation and `log.md` as an append-only operation log.
- Promote useful query answers into `playbooks/` during self-improvement instead of leaving them only in chat history.
- During lint, flag duplicate concepts, broken links, orphan pages, and weakly sourced pages.
