<!-- page: 4 -->

## Page 4

Rust
(107)
Other (2)
Go
(46)
C/C++
(45)
Figure 3 Distribution of programming lan-
guages across ProgramBench task instances.
To solve the task, models may write their so-
lution in any language they choose.
Metric
Median
Min
Max
Code lines
8,635
212
2,701,283
Code files
50
1
5,342
Runtime dependencies
10
0
113
Max directory depth
3
0
13
Tests
770
224
14,645
GitHub stars
2,124
202
79,693
Contributors
22
1
422
Commits
646
13
145,991
Repo age (years)
7.9
0.3
17.8
Table 1 Summary statistics for the 200 ProgramBench task instances,
illustrating the diversity of the dataset across codebase scale, depen-
dency complexity, and development history. Top rows cover codebase
statistics, while bottom rows quantify community contribution.
et al., 2015). We quantify this risk in §5: our generated suites achieve line coverage broadly comparable to
the native test suites shipped by developers in the same repositories.
Build an inference environment. The starting state for each task consists of the gold executable and usage-
related documentation. To construct the Docker image for the starting state, we first obtain usage-related
documentation removing source code and any implementation details from the repository with a SWE-agent
(Step 3 in Figure 2). The compiled executable is then injected into an independent docker image as the only
artifact carried over from the build step (Step 1). The reason for copying the executable over, rather than
simply rebuilding from source code, is to ensure there are no local build artifacts or dependency caches that
could reveal the original program’s implementation. The executable is also set to execute-only permissions
to prevent reading or reverse engineering of the binary with a tool like ghidra2. Lastly, we also include test
assets that a model cannot reasonably synthesize on its own (e.g., images, domain-specific binary formats).
We review inference guidelines thoroughly in §A.2.
2.3
Dataset Statistics
We created 200 task instances from open-source repositories spanning compression, language interpreters,
visualization, linting, text processing, and more (Figure 3, Table 1). Tasks range from small CLI tools to
large-scale projects such as FFmpeg and the PHP interpreter, and are mostly written in Rust, Go, or C/C++,
with one project in Java and one in Haskell. Our evaluation suite totals 248,853 test functions across all
instances (median 770 per task); additional test generation analyses and dataset statistics in §A.3 and §A.4.
2.4
Task Features
Open-ended software design. In ProgramBench, models receive only an executable and documentation. Every
architectural decision, from choice of language to module decomposition to data structure design, is the
model’s to make. There is no skeleton, mandated abstractions, or preset file organization. Because evaluation
compares executable behavior rather than source code, ProgramBench admits many valid solutions; a model
may choose entirely different languages, algorithms, or architecture and still pass, making models’ design
choices directly comparable across the same task. This is what makes ProgramBench a test of software design,
not just implementation alone.
Burden to discover specifications. In ProgramBench, the executable serves as a comprehensive but opaque
oracle. Expected behavior is fully encoded, but must be queried to be understood. Importantly, the model is
not probing blindly: it has access to the program’s documentation and help output, which surface available
flags and subcommands (§2.2). In practice, interacting with the executable resembles how a developer
2https://github.com/nationalsecurityagency/ghidra
4
