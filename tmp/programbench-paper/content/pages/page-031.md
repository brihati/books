<!-- page: 31 -->

## Page 31

Difficulty
Score Range
Count
Examples
Easy
[0, 2)
28
tty-clock, entr, cmatrix, figlet, seqtk
Medium
[2, 4)
143
ripgrep, fzf, jq, fd, zstd, htop
Hard
[4, 10]
29
lazygit, FFmpeg, typst, php-src, bat
Table 10 Distribution of ProgramBench tasks across difficulty bins, with representative repositories.
Model
Easy
Medium
Hard
Avg
Claude Opus 4.6
73.9%
53.3%
24.7%
52.0%
Claude Opus 4.7
73.8%
52.1%
25.0%
51.2%
Claude Sonnet 4.6
67.1%
48.8%
28.6%
48.5%
GPT 5.4
50.9%
39.9%
18.0%
38.3%
Gemini 3.1 Pro
50.9%
37.7%
17.8%
36.6%
Gemini 3 Flash
49.6%
31.9%
17.9%
32.4%
Claude Haiku 4.5
41.9%
30.6%
15.6%
30.0%
GPT 5.4 mini
24.1%
17.4%
7.8%
16.9%
GPT 5 mini
21.3%
15.9%
11.0%
15.9%
Table 11 Macro-averaged test pass rate by difficulty bin: for each task instance we compute the fraction of tests passed,
then average these fractions within each bin. Rates decrease monotonically from Easy to Hard for every model.
are extracted from root-level package manifests (Cargo.toml, go.mod, CMakeLists.txt, etc.), excluding
development and test dependencies. We assign fixed, dataset-independent thresholds to bin tasks into three
difficulty levels: Easy (< 2), Medium (2 ≤score < 4), and Hard (≥4). To build intuition for the scale:
a small single-file project like pingu (212 lines, 3 dependencies) scores 0.93 and falls squarely in the Easy
range. A moderately-sized project with a handful of libraries (for instance, direnv/direnv at ∼8k lines and
3 dependencies, for instance) lands around 2.5, typical of the Medium bin. Reaching the Hard threshold
generally requires either a very large codebase or a combination of substantial code and many dependencies;
lazygit, with ∼593k lines and 36 dependencies, scores 5.3, while FFmpeg reaches 4.25 on the strength of its
1.8M lines alone.
We note that 22 repositories use custom or non-standard build systems (e.g., hand-written Makefiles or
bespoke ./configure scripts) for which no recognized package manifest was detected, resulting in a runtime
dependency count of zero for those tasks; their difficulty scores therefore reflect code size alone. Table 10
summarizes the distribution across bins; per-task scores and labels are listed in Table 12.
As a sanity check, we look at whether our difficulty score correlates with observed agent performance. Table 11
reports the average test pass rate within each difficulty bin, broken down by model. Pass rates decrease
monotonically from Easy to Hard across all models, suggesting that the metric captures meaningful variation
in task complexity.
31
