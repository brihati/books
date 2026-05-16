<!-- page: 29 -->

## Page 29

0
2k
4k
6k
8k
10k+
0
10
20
30
40
50
60
70
GitHub Stars
0
20
40
60
80
100+
0
10
20
30
40
50
Contributors
0
500
1k
1.5k
2k+
0
10
20
30
40
50
60
Commits
0
2
4
6
8
10
12
14
16
18
0
10
20
30
40
50
Repo Age (years)
Figure 22 Distribution of GitHub community and development history metrics across ProgramBench repositories: stars,
contributors, commits, and repository age.
PHP interpreter) is implemented with 1.97 million lines of code. In comparison to existing benchmarks, these
statistics confirm how ProgramBench is a step function increase in terms of implementation scale.
Build systems. A repository’s primary language is determined by counting lines of code per language (mapped
from file extensions) and selecting the one with the most lines (see Figure 3 in the main paper). From
Figure 20, the distribution of build systems used correspond with these ratios. Build systems are identified
by scanning for sentinel marker files (e.g., Cargo.toml, go.mod, CMakeLists.txt), with the primary build
system being the one whose marker appears at the repository root. For Rust and Golang repositories, the
cargo and native go build constitutes the entirety of build systems with which the corresponding executables
are compiled respectively. There is relatively slightly more variance with C/C++ repositories due to the
differences in libraries that certain projects rely on, but the build procedure generally remains quite uniform.
Directory depth. Repositories in ProgramBench are generally shallow: the median maximum depth is 3, with
an average file depth of 2.5 levels from the repository root, and a median of 13 directories per repository. We
compute depth by measuring each file’s distance from the repository root. While most repositories (73%)
have maximum depth ≤4, deeper hierarchies exist (up to 13 levels). Rust repositories tend to be the flattest
(median 9 directories), while C/C++ projects are structurally more complex (median 32 directories), reflecting
the heavier use of nested module hierarchies, platform-specific source trees, and vendored dependencies
common in C/C++ ecosystems. At the extremes, 3 repositories consist of a single flat directory with no
nesting at all (e.g., seqtk, tty-clock), while the deepest (gromacs/gromacs at depth 13) contains over 850
directories.
Dependency count. Of the 200 repositories, 171 (85.5%) contain a recognized package manifest file; among
these, the median repository declares 17 total dependencies (12 runtime). Dependencies are counted by
29
