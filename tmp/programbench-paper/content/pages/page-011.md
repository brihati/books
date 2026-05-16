<!-- page: 11 -->

## Page 11

we also found that GPT 5.4 averages just 1.2 file modifications per trajectory, with 39.5% of trajectories
performing zero modifications to any existing files. In contrast, Sonnet 4.6 averages 18.3 modifications and
Gemini 3.1 Pro averages 10.1, consistent with the gradual growth visible in their curves. All together, the
trends suggest that for some models, development is effectively a single-shot generation step, rather than an
iterative write-compile-debug cycle.
6
Related Work
Code from scratch. Several prior works have presented variations of evaluating coding systems on 0 to 1 code
generation. Commit0, an early work in this lineage, converts 54 Python libraries into task instances by erasing
the existing implementations for all functions and classes (Zhao et al., 2024). The model is then asked to
fill in the blanks, and performance is quantified as the percentage of the repository’s original test suite that
passed. Later works follow this paradigm, with differences primarily around how repository specifications
are communicated to the model (Li et al., 2024b; Liu et al., 2025). DevBench uses product requirement
documents (PRDs) and UML diagrams (Li et al., 2024a), while NL2Repo-bench conveys expected structure
via natural language, shifting the burden of creating folders and files onto the agent (Ding et al., 2026). A key
commonality is that LMs are asked to fill in a skeleton of pre-defined method headers and classes. In this way,
models are never actually tested on their software design capabilities, such as what abstractions to introduce,
how to decompose functionality across modules, or what communication protocols to define. By evaluating
against executables rather than source code, ProgramBench eliminates the need to prescribe structure with
natural language or make expected behavior explicit as programmatic definitions. As discussed in §2, our
formulation also yields simpler collection criteria, broader language coverage, and novel reasoning demands.
A few prior and concurrent works have included small-scale case studies and a handful of task instances
that touch on program recreation (Merrill et al., 2026; Chu et al., 2026; Adamczewski et al., 2026). These
works validate the direction but rely on hand-crafted instances and do not address systematic benchmark
construction or scaling; ProgramBench provides both. A related but distinct line of work trains models
to decompile binaries back into source code (Tan et al., 2024). Decompilation aims to recover the original
implementation; ProgramBench instead evaluates behavioral equivalence, permitting any implementation that
reproduces the same input-output behavior.
Issue resolution. SWE-bench (Jimenez et al., 2024) and its variants (Yang et al., 2024b, 2025; Deng et al.,
2025; Rashid et al., 2025; Zan et al., 2025; Zhang et al., 2025; Thai et al., 2026) have become popular
coding benchmarks. Extracted from GitHub issue-pull request pairs, SWE-bench tasks evaluate models on
their ability to address bug fixes or feature requests within an existing codebase. These evaluations are
complementary to ProgramBench, which instead focuses on building a codebase from the ground up.
Automatic environment setup. A few works have examined the task of automatically setting up a development
environment for a given GitHub repository (Bogin et al., 2024; Eliseeva et al., 2025; Hu et al., 2025).
ProgramBench does not evaluate environment setup in isolation, but it arises as a practical prerequisite:
models must develop dependencies and configure build tools to produce a working solution. No specific
toolchain is prescribed; models can use an entirely distinct line of languages and libraries.
Performance optimization. Alongside measuring correctness, a relevant line of works examines algorithmic (Du
et al., 2024; Liu et al., 2024; Waghjale et al., 2024; Huang et al., 2025; Press et al., 2025) and machine-
dependent (He et al., 2025; Ma et al., 2025; Ouyang et al., 2025; Shetty et al., 2025) runtime optimization as
a measure of how well AI systems can speed up software systems while maintaining functional correctness.
The most salient distinction between those works and ProgramBench is that while optimization benchmarks
assume a known specification that a model should preserve (while optimizing speed), ProgramBench requires
models to recover the specification itself from observed behavior. In this respect, ProgramBench shares
motivation with inductive program synthesis benchmarks that require inferring behavior from input-output
examples (Wei et al., 2025), but operates at the scale of full software projects, not individual functions.
11
