<!-- page: 24 -->

## Page 24

5 tasks
39 tasks
83 tasks
53 tasks
13 tasks
4 tasks
3 tasks
125
250
500
1k
2k
4k
8k
16k
# tests per task (log scale)
0%
20%
40%
60%
80%
100%
% of harvested tests
chroma (0.5k)
bedtools2 (1.1k)
quickjs (3.0k)
cppcheck (2.1k)
duckdb (4.0k)
ffmpeg (3.0k)
gomplate (2.9k)
chafa (1.9k)
pandoc (5.2k)
miller (14.6k)
jq (6.1k)
proj (5.3k)
php-src (14.3k)
rumdl (3.3k)
samtools (1.4k)
sqlite (13.5k)
ctags (2.3k)
Harvested
(20.5%)
Self-generated
(79.5%)
Figure 17 Distribution of test volume and source across all ProgramBench task instances. Left: each dot is one task;
the x-axis shows the total number of tests (log scale) and the y-axis shows the percentage of tests harvested from
existing repository test suites versus self-generated tests. Bin counts are annotated above the plot. Right: global split
of harvested vs. self-generated tests across all tasks.
workflow tests, Doxygen’s documentation fixtures, Lazygit’s integration tests, Atlas’s CLI/e2e plus SQLite
integration tests, Rumdl’s integration tree, JSON Schema’s CLI plus conformance tests, Zstd’s CLI and fuzzer
suite, and jq’s regression harness. We audited each baseline against upstream CI configurations to ensure the
comparison is integration-test only, excluding src/ unit tests in projects (Rumdl, Atlas) where the default test
runner would otherwise inflate native coverage with code paths our black-box generated tests structurally
cannot reach.
24
