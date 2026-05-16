<!-- page: 2 -->

## Page 2

To understand what this entails, consider how a human programmer approaches the same task. Before a
single line is written, she asks herself a series of important questions: What programming language and build
system should be used? How should the codebase be organized? What data structures should represent the
program’s core entities? How should errors be detected and communicated? Such requisite questions, which
developers constantly revisit throughout the development lifecycle, lead to pivotal design decisions that shape
the codebase far more profoundly than any individual code change. Although we are progressively entrusting
LMs to similarly build software from the ground up, the ability of LMs to make such architectural decisions,
choose abstractions, and decompose a system into coherent modules has not been studied extensively.
To bridge this gap, we introduce ProgramBench, a benchmark that challenges software engineering (SWE)
agents to produce code that recovers the functionality of a software program (e.g., executables, .dmg’s, .pkg’s).
Given a program and documentation, a SWE-agent, defined as an LM equipped with an agent scaffold to
interact with a terminal environment (Yang et al., 2024a), must write source code and a compile script that
reproduces the original program’s behavior. Every software design decision is entirely the model’s to make.
We synthesize ProgramBench tasks from open-source GitHub repositories. First, we identify repositories
written in compiled languages (e.g., C/C++, Golang, Rust, Java) that build a program. Next, to convert a
repository into a task instance, we compile the program, then strip away all source code and tests, leaving
only the program and its documentation as the task’s starting point.
To evaluate a model’s solution, we generate behavioral tests by prompting a SWE-agent to systematically probe
the original program with varied inputs and codify the observed input-output behavior into assertions that a
candidate reconstruction must satisfy. Crucially, these tests are never revealed to the task worker. Since tests
target executable behavior rather than source code, evaluation is entirely implementation agnostic; a model
may use different algorithms, abstractions, or even programming languages than the original codebase, and
still pass as long as the input-output behavior matches. While any test suite necessarily under-approximates
an executable’s full specification, we empirically demonstrate that our test generation pipeline creates large
suites that reliably capture core functionality.
Using our pipeline, we collect 200 task instances, ranging from compact CLI tools to complex, widely used
software including language interpreters (PHP, Lua, tinycc), databases (DuckDB, SQLite), media and
compression utilities (FFmpeg, zstd, xz), and developer tools (ripgrep, fzf, jq). We evaluate 9 language
models equipped with mini-SWE-agent, a widely adopted coding agent scaffold for open source SWE-agent
research. The results resoundingly confirm ProgramBench’s difficulty for today’s models; no task instance is
fully resolved. However, test pass rates are significantly different between models. The best model, Opus 4.7,
manages to pass 95% of tests for 3% of task instances. Further analysis reveals that model-written codebases
diverge significantly from human-written ones, favoring monolithic file structures with longer functions. Our
trajectory analyses showcase how models vary in the length and make up of the way they develop software.
We open source ProgramBench to enable the community to reproduce and build upon our investigations.
2
ProgramBench
This section describes ProgramBench in detail. We first formalize the task (§2.1), then explain how task in-
stances are semi-automatically constructed from open-source repositories (§2.2). Finally, we review benchmark
statistics (§2.3) and distinguishing features (§2.4).
2.1
Task Formulation
Given a gold (reference) executable and its usage documentation, a task worker is asked to write source code
and a build script that constructs a candidate executable which should reproduce the behavior of the gold
executable. The task worker does not have access to the internet and is free to implement the solution in
any programming language. The task worker is informed of these conditions via the initial prompt, and
no-internet is enforced by running the Docker container without internet.
To evaluate, we run a generated test suite, where each test checks whether the candidate executable exhibits
the same observable behavior as the gold executable for a given input (e.g., matching standard output, exit
2
