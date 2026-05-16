<!-- page: 17 -->

## Page 17

(by git checkout’ing to a commit) where the bug was already fixed, then submitted the git diff between the
task’s “base" commit and future commit as the fix4.
Similarly, we found that by simply asking the SWE-agent to perform a ProgramBench task with no explicit
constraints (e.g., full internet access, read/write permissions for the executable), interesting but undesirable
solution patterns occasionally emerge. As shown in Figure 13, we noticed that if Claude Opus 4.5 was able to
figure out what GitHub repository the executable originates from, typically by inferring from ./executable -h
standard output, it then performed a shallow clone of the remote repository to obtain the source code.
Although the task worker still must generate a compile.sh script that builds the executable, the implementation
effort, which is typically where the majority of a task worker’s efforts are required, becomes trivially simple
and yields no insight into the research questions posed by our work. Another infrequent but still observed
failure mode is that a task worker will simply submit a wrapper around the reference executable and call it a
day (this is fully mitigated as explained below).
A.2.2
Early Mitigation Attempts
Before blocking internet access entirely, we tried allowing it while detecting and penalizing cheating after the
fact. This section describes our LM-as-a-judge cheat detection pipeline, its results, and the limitations that
led us to disable internet access.
Detection pipeline. We built a rubric-based annotation system that classifies agent trajectories into two
violation types: source code lookup (cloning the repository, downloading via package managers, reading cached
dependency source) and binary wrapping (submitting a thin wrapper around the reference executable instead
of a real reimplementation). For each task, 9 LM judges independently review the full command history
and classify the trajectory. To reduce single-model bias, the judges are drawn from three model families: 3
instances of GPT 5.2, 3 of Claude Sonnet 4.5, and 3 of Gemini 3.1 Pro. A task is flagged if a strict majority
(5 or more of 9) judges identify at least one violation.
Cheating rates. We ran this pipeline on internet-access runs for four models: Claude Opus 4.6, Claude
Sonnet 4.6, Gemini 3 Flash, and GPT 5 mini.
As reported in Table 3, cheating rates range from 1%
(GPT 5 mini) to 36% (Claude Sonnet 4.6). Source code lookup is the main violation type, accounting
for 79–95% of flagged tags across the three models with meaningful cheating rates. Models use a range
of strategies: directly cloning the GitHub repository, installing the project via a package manager (cargo
install, go get, apt-get source), or reading cached dependency source from local package caches such as
~/.cargo/registry/src/ and Go’s module cache. This last strategy is especially hard to judge, as it blurs the
line between reading dependency code and looking up the project’s own source (see below).
Inter-judge agreement. Despite using 9 judges from three model families, agreement is moderate at best.
Fleiss’ κ ranges from 0.16 (GPT 5 mini) to 0.60 (Claude Sonnet 4.6), with a pooled κ of 0.57 across all
786 annotated tasks, which falls in the “moderate agreement” range. Judges disagree on 16–57% of tasks
depending on the model, with the highest disagreement rate for Claude Opus 4.6 (57%), whose cheating
strategies tend to be more subtle.
The main source of disagreement is whether reading dependency source code from local package caches
counts as a violation. For example, on the handlr task (a Rust project), Claude Sonnet 4.6 navigated into
~/.cargo/registry/src/ and read the source of dependencies like xdg-mime and clap. Five of nine judges
flagged this as source code lookup; the other four called it legitimate, reasoning that these are third-party
libraries (not the project itself) that happened to be locally available.
Another gray area is consulting API documentation. On the codesnap task, Claude Sonnet 4.6 used curl to
fetch pages from docs.rs (the Rust documentation hosting service) for the project’s published crate. Four
judges flagged this as source lookup; five called it clean, arguing that reading public API docs is closer to
consulting a reference manual than obtaining source code. The task was not flagged (4 of 9 is below the
majority threshold), but the split shows how reasonable judges can disagree on where to draw the line.
4https://github.com/SWE-bench/SWE-bench/issues/465. The loophole was patched in October 2025. Among the 20 most
recent submissions, fewer than 1% of the 500 solutions per submission exhibited such violations.
17
