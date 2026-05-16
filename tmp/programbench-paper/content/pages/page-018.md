<!-- page: 18 -->

## Page 18

These disagreements reflect real ambiguity in what counts as “cheating” when models have access to package
ecosystems and documentation. Stricter rubrics risk penalizing legitimate reverse engineering strategies; looser
ones risk missing real violations.
Agent action (handlr task, Claude
Sonnet 4.6):
cat ~/.cargo/registry/src/.../xdg-
mime-0.3.3/src/lib.rs
cat ~/.cargo/registry/src/.../confy
-0.4.0/src/lib.rs
cat ~/.cargo/registry/src/.../
ascii_table-3.0.2/src/lib.rs
Judge verdict: CHEATING (
source_lookup)
The agent accessed cached cargo
registry source
files in ~/.cargo/registry/src/ to
examine the
APIs and implementations of
dependencies like
clap, ascii_table, xdg-mime, and
freedesktop_entry_parser.
Judge verdict: CLEAN
The agent reimplemented the
software in Rust by
reading the source code of its
dependencies
(standard crates like clap, xdg-mime
, ascii_table)
found in the local cargo registry
cache. The agent
did not access the source code of
handlr itself.
Figure 15 Example of a 5–4 judge disagreement. Claude Sonnet 4.6 read dependency source code from the local Cargo
registry cache while working on the handlr task. Five judges flagged this as source code lookup (red); four called it
legitimate, noting the files are third-party libraries, not the project itself (green).
0
1
2
3
4
5
6
7
8
9
0
50
100
150
Tasks
Claude Sonnet 4.6
0
1
2
3
4
5
6
7
8
9
Claude Opus 4.6
0
1
2
3
4
5
6
7
8
9
Gemini 3 Flash
0
1
2
3
4
5
6
7
8
9
GPT 5 mini
Number of judges (out of 9) flagging cheating
Figure 16 Distribution of judge votes per task for each model evaluated with internet access. Each bar shows how many
tasks received exactly k cheating flags from the 9-judge panel. Tasks at k ≥5 are flagged by majority vote. Claude
Sonnet 4.6 shows a bimodal pattern (many tasks at 0 and 9), while Claude Opus 4.6 has more mass in the ambiguous
middle range, explaining its higher disagreement rate.
A.2.3
Guidelines
To address these concerns, we attempt to mitigate potential loopholes by imposing several measures and
restrictions on the image construction, inference, and evaluation pipelines.
For the Docker image construction pipeline, based on what we discussed in §2.2, we highlight several key steps
aimed at making illegitimate solution patterns such as decompilation and re discovering local copies of source
code impossible or more difficult to achieve:
• Execute-only permissions: To prevent task workers from using a tool like ghidra to reverse engineer an
executable into code, we set the permissions of the executable to 111 (execute-only).
• Removal of original executables during evaluation: The model might attempt to submit the original
executable together with a thin wrapper around it as its solution. This is mitigated by removing all files
that match the hash of the original executable prior to evaluation.
• Inject the executable instead of building from source: Early on, we used a simpler workflow to construct
the Docker image for the starting state of a task. Starting with the repository, we would first build
the executable by running the model generated build.sh script, then invoke a model generated clean.sh
script that would wipe the source code and any artifacts that give away implementation details. We
found that although models’ clean.sh scripts were quite capable of wiping out source code, they would
18
