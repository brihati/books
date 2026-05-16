<!-- page: 35 -->

## Page 35

Models exhibit distinct language preferences, ranging from Python-dominant to broadly distributed. Since models
are free to choose any language for their reimplementation, we examine which languages each model gravitates
toward. Figure 28 shows the breakdown across all runs. GPT 5.4 is the most skewed, writing 79% of its
solutions in Python, while Gemini 3.1 Pro and Gemini 3 Flash also lean heavily toward Python (56% and
43%). Claude Opus 4.7 and Opus 4.6 instead favor Rust and Go, with Python accounting for only 14% and
20% of their runs respectively. Sonnet 4.6 produces the most balanced distribution, with meaningful fractions
across Rust, Go, Python, and C/C++. These preferences likely reflect differences in training data composition
and instruction tuning rather than task-level signals, as the same tasks elicit different language choices from
different models.
0.0
0.5
1.0
1.5
2.0
LoC ratio (model / ref)
Opus 4.7
Opus 4.6
Sonnet 4.6
Gemini 3.1 Pro
Gemini Flash
GPT 5.4
Figure 29 LoC ratio (model / reference) per model for
solutions passing ≥75% of tests. Dashed line marks parity.
0
1
2
3
LoC ratio (model / ref)
C/C++  (n=36)
Go  (n=47)
Rust  (n=124)
Figure 30 LoC ratio by reference language for solutions
passing ≥75% of tests. C/C++ references see the largest
gap, while Rust references are closest to parity.
Model solutions are consistently shorter than the reference, but the gap varies across models. We compare the
lines of code in model solutions to the reference codebase for runs passing at least 75% of tests, to understand
how much code models need to reproduce equivalent functionality. Figure 29 shows the LoC ratio per model.
All models fall well below parity (the dashed line at 1.0), with medians ranging from roughly 0.15 for Gemini
Flash and GPT 5.4 to 0.35 for Opus 4.7 and Sonnet 4.6. The wide whiskers for Opus 4.7, Opus 4.6, and
Sonnet 4.6 indicate that these models occasionally produce solutions approaching or exceeding the reference
in length, while Gemini Flash and GPT 5.4 are tightly concentrated at the low end.
The LoC ratio gap is largest for C/C++ references and smallest for Rust. We further break down LoC ratios by
reference language to disentangle language-level effects. Figure 30 shows the results. C/C++ references
exhibit the lowest ratios, with a median around 0.2, consistent with models frequently rewriting these tasks in
higher-level languages like Python. Rust references are closest to parity, with a median near 0.5 and several
outliers exceeding 1.0, likely because models that stay in Rust retain similar verbosity to the original. Go falls
in between, with a median around 0.4.
Higher-scoring solutions tend to contain more code, but code volume alone does not guarantee high scores. We
plot test pass rate against model code lines to examine whether there is a relationship between solution size
and performance. Figure 31 shows the result across all 1,788 runs on a log-scaled y-axis. At the low end of
the score spectrum, solutions span a wide range of sizes, from under 10 lines to over 10,000. As pass rates
increase, the floor rises: solutions scoring above 75% cluster between roughly 200 and 10,000 lines, suggesting
that a minimum level of implementation completeness is necessary to pass most tests. However, many large
solutions still score poorly, and the overall relationship is noisy.
35
