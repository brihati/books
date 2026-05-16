<!-- page: 3 -->

## Page 3

GitHub Repository
Source Code
Documentation
1) “Build .exe;
record steps”
./executable
2) “Write
tests for
executable”
tests/
docs/
3) “Remove
implementation
details”
Figure 2 ProgramBench task collection pipeline. To turn a GitHub repository into an ProgramBench task, we use a
SWE-agent to compile an executable, generate behavioral tests, and strip away implementation details. The sourcing
workflow only requires a repository to produce an executable or program, making it extensible to many codebases.
codes, or file system side effects). The test suite is never revealed at any point to the task worker. While any
test suite checks a finite set of inputs and therefore necessarily under-approximates the gold executable’s full
specification, ProgramBench’s framing makes extending test coverage trivial.
2.2
Benchmark Construction
Next, we discuss our four-stage pipeline for converting open source GitHub repositories into ProgramBench
task instances, as visualized in Figure 2. All construction steps use the mini-SWE-agent1 harness with Claude
Sonnet 4.5, operating inside a Docker container based on ubuntu:22.04.
Identify candidate repositories. We synthesize ProgramBench tasks from open source GitHub repositories.
First, we filter for repositories that may produce a standalone executable or program. A strong heuristic is to
look for projects written in compiled languages (e.g., C/C++, Golang, Rust).
Construct executable from source. Given a repository, we task a SWE-agent with compiling the gold executable
and, if successful, record the commands that reproduce the build in a single build script (Step 1 in Figure 2).
Generate behavioral tests. We use an agent to explore the program, its source code, existing tests, and
documentation, and then generate behavioral tests (Step 2 of Figure 2). The test assertions target externally
observable effects rather than source-level internals. For example, a test might assert that specific strings
appear in stdout or stderr, or that an invocation produces expected files. The agent is also prompted to
identify and include in its test suite any existing behavioral tests defined in the repository (harvesting).
The agent continuously measures the line coverage of the current test suite and iteratively writes new tests to
invoke missing code paths, attempting to achieve full coverage.
Some tests may have missing or trivially true assertions. Therefore, to ensure assertion quality, tests are
flagged if they fail the gold binary or trigger our assertion quality linter (Appendix A.3.5), which detects
structurally weak assertion patterns such as exit-code-only checks, short substring matches, and disjunctive
assertions. The agent is prompted to revise all flagged tests. At the end, any remaining tests that do not pass
with the gold binary deterministically or pass a dummy binary are discarded. More details in §A.3.
Prior work has shown that coding benchmarks, such as SWE-bench, have some test suites with one of the
following two shortcomings (Chowdhury et al., 2024). First, a task’s test suite could be overly stringent,
meaning it checks for criteria not apparent from the initial task definition. Second, a task’s test suite might
not fully check whether a solution actually solves the initially stated task. For the first case, ProgramBench
tests assert only on observable behavior of the reference executable, precluding overspecification of source-level
internals. A subtler concern is whether tests demand exact reproduction of implementation-dependent output
(e.g., floating point precision or rendering discretization). We address this directly: the model has full access
to the gold executable at inference time, so any behavior a behavioral test expects is discoverable by running
that same command. An audit of all 200 task instances found zero tests that invoke flags or subcommands not
surfaced by the executable’s documentation, and only 5 instances where implementation-dependent output
could plausibly appear, none of which contained such assertions in practice (§A.3.4). For the second case, a
finite test suite necessarily under-approximates an executable’s full specification (Liu et al., 2023; Le Goues
1https://mini-swe-agent.com
3
