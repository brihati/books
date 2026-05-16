<!-- page: 28 -->

## Page 28

A.4
Dataset Statistics
In the following sections, we provide breakdowns of the ProgramBench dataset by various dimensions, including
programming languages, repository size, and file extensions. These statistics characterize the diversity of the
ProgramBench dataset and can help inform future analyses and evaluations. In general, our typical approach
to these analyses is to perform simple, straightforward aggregations (e.g., line, file counts) or keyword-based
searches (e.g., test_*.go to identify test files), unless specified otherwise explicitly. GitHub community
statistics (stars, contributors, commits) were crawled on April 21, 2026.
0 50
50 100
100 150
150 200
200 250
250 300
300 350
350 400
400 450
500+
Files
0
20
40
60
80
100
120
Count
Total files
Code files
Figure 18 Distribution of total/code files per repository.
0 20k
20k 40k
40k 60k
60k 80k
80k 100k
100k 120k
120k 140k
140k 160k
160k 180k
200k+
Lines
0
25
50
75
100
125
150
Count
Total lines
Code lines
Figure 19 Distribution of total/code lines per repository.
Cargo
(107)
Other (3)
Go Build
(46)
CMake
(43)
Figure 20
Distribution of build systems across
ProgramBench repositories. The build system dis-
tribution closely mirrors the language distribution
(Figure 3), as each language ecosystem has a dom-
inant build tool.
0
10
20
30
40
50+
0
10
20
30
40
50
60
Figure 21 Distribution of runtime dependencies across Pro-
gramBench repositories.
Counts are extracted by parsing
root-level package manifests (Cargo.toml, go.mod, CMake-
Lists.txt, etc.), excluding development and test dependencies.
Number of files and lines. Figures 18 and 19 show the distribution of repository sizes in ProgramBench by
number of files and lines. The median codebase has 93 total files with 50 code files, and 8,635 lines of code
spread across all files. The extremes of the ProgramBench dataset feature several prodigious codebases.
FFmpeg/FFmpeg has the most code files at 4566 total, while php/php-src (the official source code for the
28
