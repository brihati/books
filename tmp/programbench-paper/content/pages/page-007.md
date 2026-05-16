<!-- page: 7 -->

## Page 7

10%
20%
30%
40%
50%
60%
Mean % tests passed
Claude Opus 4.6
Claude Opus 4.7
Claude Sonnet 4.6
GPT 5.4
Gemini 3.1 Pro
Gemini 3 Flash
Claude Haiku 4.5
GPT 5.4 mini
GPT 5 mini
-3.5%
-8.0%
+1.4%
+4.2%
+0.3%
-1.5%
+2.3%
+4.2%
+4.2%
Default (any language)
Different language required
Figure 6 Effect of requiring a different implementation language. Filled circles
show default scores; open circles show scores under the constraint.
Model
% Cheat
Claude Sonnet 4.6
36%
Claude Opus 4.6
21%
Gemini 3 Flash
20%
GPT 5 mini
1%
Table 3 Cheating rates when mod-
els are given internet access, as
flagged by majority vote of 9 LM
judges. Source code lookup is the
dominant strategy, accounting for
79–95% of flagged runs.
500
5k
50k
500k
Source code, excl. deps (log scale)
0%
20%
40%
60%
80%
100%
Line coverage
ffmpeg (486k)
php-src (278k)
sqlite (75k)
cppcheck (72k)
ctags (63k)
proj (62k)
typst (56k)
miller (49k)
melody (1k)
tinycc (16k)
pier (569)
calcurse (11k)
hashcards (2k)
go-critic (6k)
Figure 7 Line coverage of our generated test
suites versus project size (source lines excluding
dependencies) for a sample of 100 tasks.
Repository
Gen.
Native
∆
ariga/atlas
54.15
28.25
+25.90
johnkerl/miller
85.90
72.18
+13.72
stacked-git/stgit
85.54
82.43
+3.11
rvben/rumdl
68.23
66.80
+1.43
facebook/zstd
76.32
75.10
+1.22
jqlang/jq
82.15
81.69
+0.46
php/php-src
61.60
64.60
−3.00
stranger6667/jsonschema
72.63
78.79
−6.16
doxygen/doxygen
13.00
24.80
−11.80
ffmpeg/ffmpeg
46.70
58.97
−12.27
jesseduffield/lazygit
62.23
74.60
−12.37
typst/typst
65.68
85.12
−19.44
Median
66.96
73.39
−1.27
Table 4 Line coverage (%) for generated vs. native behavioral suites
across 12 repositories that maintain an identifiable integration or
end-to-end test suite, sorted by ∆.
5
Analysis
We study test generation artifacts and evaluation outcomes to better understand the utility of our generated
tests and gauge how performance varies across different tasks and models.
5.1
Test Suite Comparisons
We assess how effective our generated test suites are by measuring two complementary properties: how much of
each program they exercise (coverage), and whether they actually reject incorrect implementations (assertion
strength). Full details on how each analysis was carried out are included in §A.3.2.
Generatedtestsuitesachievecomparablelinecoveragetodeveloper-writtentestsuites. While most ProgramBench
repositories lack a dedicated end-to-end test suite, many maintain unit and integration tests, making them a
natural baseline. We instrument each task’s executable with coverage tracking and measure the fraction of
source lines exercised by our generated suite versus the project’s native suite across 100 repositories (§A.3.2).
Our generated suites average 79.7% line coverage with a median of 86.2% (Figure 7), compared to native
suites that average 56.8% with a median of 64.3%. This places our generated suites comfortably within, and
often above, the coverage range of typical developer-written tests.
Coverage remains comparable even against dedicated behavioral test suites. The comparison above includes many
unit test suites, which can exercise internal code paths that black-box tests structurally cannot reach. To
7
