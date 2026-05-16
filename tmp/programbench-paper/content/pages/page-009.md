<!-- page: 9 -->

## Page 9

0
126
252
378
504
630
0
50
100
150
200
Action Type
Claude Opus 4.7
0
394
788
1182 1576 1970
Claude Sonnet 4.6
0
44
88
132
176
220
Gemini 3.1 Pro
0
14
28
42
56
70
GPT 5.4
Turn
Read
Write
Probe
Execute
Git
Other
Figure 10 Distribution of action types across agent turns for four representative models. Each bar shows the total
number of actions of each type at a given turn index, aggregated across all task instances. The natural decay in bar
height reflects trajectories of varying length ending at different points.
breakdowns are visualized in Figure 28.
We next draw insights from comparing models’ codebases against the reference solutions. To ensure comparisons
are between codebases that produce functionally similar executables, we only compare against model solutions
that pass 75+% of tests. This yields 207 runs across 88 tasks and 9 models.
Model solutions are significantly shorter. Even among high-scoring solutions, models produce substantially
less code than the references: a median of 1,173 lines compared to 3,068 in the originals (Figure 9). Most
runs (85%) fall below parity. Just 15% of codebases are larger than the reference, typically for smaller tasks.
Models also create far fewer files (median 3 versus 15), with 60% of solutions consisting of 1–3 code files.
Models prefer monolithic files over modular directory structures. We measure the directory structure of model-
generated codebases using maximum directory depth, defined as the deepest nesting level of any file (e.g.,
src/utils/parser.go has depth 3). The majority of runs (67%) produce a strictly shallower maximum depth
than the reference (median depth 1 vs. 2), while only 2% are deeper. Rather than mirroring the modular
decomposition of the original project, models strongly prefer placing most or all code in a single file or a
handful of files at the root level.
Models write fewer, longer functions. Table 5 compares function count and average function length between
model and reference codebases for four representative models. All models write far fewer functions than the
reference (10–29% as many), but compensate with longer functions: Claude Sonnet 4.6 writes functions that
are 1.46× longer on average, while Gemini 3.1 Pro reaches 1.62×. GPT 5.4 writes functions that are 1.08×
longer while still producing very few of them (10% of the reference count).
5.3
Agent Trajectories
We analyze agent trajectories to understand how models approach the task and where they struggle.
We classify actions into one of six types: read (file inspection, searches, directory listing), write (file creation,
editing), probe (any invocation or inspection of the reference executable), git (version control), execute
(compilation, non-probe program execution), and other. To classify, we perform keyword matching on the raw
command string, checking in priority order to distinguish between different usage techniques of bash commands.
For instance, cat<<’EOF’>main.c is classified as write, distinct from cat main.c to read. Figure 10 shows
the action type distributions per turn across all inference runs for four representative models.
Turn counts vary heavily by model. As reflected by Figure 10, Claude Sonnet 4.6 uses a median of 868 commands
per task, with its longest trajectory reaching 1,978 turns. GPT 5.4 sits at the other extreme with a median of
just 17 commands, while Gemini 3.1 Pro and Opus 4.7 fall in between at 92 and 157 respectively.
9
