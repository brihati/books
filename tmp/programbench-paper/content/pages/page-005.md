<!-- page: 5 -->

## Page 5

queries a product manager: “when a user runs X with flag -y, what should the output be?” The model
must decide which questions to ask and in what order. This setting tests a model’s ability to infer behavior
through systematic, hypothesis-driven exploration, mirroring challenges developers routinely face when probing
partially documented APIs or onboarding to unfamiliar systems by observing behavior in the absence of
complete specifications.
Simple collection criteria.
Our collection pipeline requires only that a repository produce a standalone
executable. No existing test suite, language-specific AST tooling, or ecosystem-reliant test frameworks are
needed. The benchmark is therefore straightforward to extend with new instances over time, a valuable
property for sustaining benchmark relevance (Deng et al., 2025; Zhang et al., 2025). The same pipeline can
also generate training data, similar to how prior benchmark collection schemas have been repurposed for
training (Badertdinov et al., 2025; Pham et al., 2025; Yang et al., 2025).
3
Experiments
Models. We evaluate 9 recent language models that are regarded as strong coding models based on rank on
existing benchmarks, including SWE-bench and Terminal-bench. These include Claude Opus 4.7, Claude
Opus 4.6, Claude Sonnet 4.6, Claude Haiku 4.5, Gemini 3.1 Pro, Gemini 3 Flash, GPT 5.4, GPT 5.4 mini,
and GPT 5 mini. All models use vendor-default hyperparameters.
Agent scaffold. We use mini-SWE-agent because it is both widely adopted as a baseline by other benchmarks
(SWE-bench Verified, Multilingual2, Terminal-bench3), and deliberately minimal in its scaffolding, reducing
confounds between model capability and harness design. Each model runs inside a container with 20 CPUs
and 60GB RAM, with a limit of 1,000 steps and 6 hours per run; full configuration details are in §B.1.
Metrics. We primarily report % Resolved, which refers to the percentage of task instances where the model’s
codebase passes all associated test cases and is not flagged as cheating. Due to the challenging nature of this
benchmark, we also report % Tests Passed per task instance, which captures partial progress even when no
task is fully resolved. However, we note that this softer metric is only meaningful for relative comparisons
between models; even a single failed test can imply a fundamental flaw in a model’s solution. As discussed in
§2.2, % Tests Passed also does not reliably correlate with percentage of working functionality.
4
Results
Our main results are shown in Table 2. ProgramBench is extremely challenging; across the board, no model
fully solves any single ProgramBench task instance. That said, from Figure 4, we find that models make
meaningful progress on a significant proportion of tasks, with Claude Opus 4.7 achieving the highest proportion
of solutions that pass 95+% of tests, at 3.0%.
Task difficulty is largely model-agnostic. As shown in Figure 5, models consistently score higher on simpler
CLI utilities like nnn, fzf, and gron, while complex systems such as FFmpeg, php-src, typst, and ast-grep
remain out of reach. These trends suggest that ProgramBench captures intrinsic variation in task difficulty
that is independent of model choice. The rank order of tasks by pass rate is broadly consistent across models.
4.1
Ablations
We review two alternative evaluation settings to investigate the impact the availability of certain tools and
resources has on solutions and cheating rates.
Different-language constraint. In this setting, we force models to implement their solutions in a different
programming language from the reference repository. In theory, this measure should obviate models’ ability
to simply regurgitate reference code from their pre-training corpora, requiring them to demonstrate deep
understanding of program behavior rather than surface-level recall.
3https://tbench.ai
5
