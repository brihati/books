<!-- page: 23 -->

## Page 23

agent continuously measures the line coverage of the current test suite and iteratively writes new tests
to invoke missing code paths, attempting to achieve full coverage.
Naturally, some generated tests may have missing or trivially true assertions. Therefore, to ensure
assertion quality, tests are flagged if they fail the gold binary or trigger our assertion quality linter, which
detects structurally weak assertion patterns such as exit-code-only checks, short substring matches, and
disjunctive assertions (see A.3.5 for full list of rules). The agent is prompted to revise all flagged tests.
The loop continues until the suite satisfies a target coverage threshold.
At the end of every strategy, we discard any tests that do not pass with the gold binary deterministically or
pass a dummy binary.
A.3.2
Analyses
We provide several statistical and qualitative breakdowns of the proposed test generation strategies.
The coverage-guided iterative strategy does the best. The monolithic strategy averages 27.8 tests per task.
The decomposed strategy does better, averaging 51.7 tests per task. However, the coverage-guided iterative
strategy results in a significantly larger number of tests with a median of 750 tests per task and with most
tasks having between 200 to 2000 tests. It also results in a very high mean line coverage of 79.7%, with a
median of 86.2% (Figure 7). Furthermore, when possible, the agent effectively makes use of existing tests,
e.g., SQLite, PHP, Bedtools2, Proj and Ctags (Figure 17).
The majority of tests are generated, not harvested. Our test generation pipeline combines two sources: tests
generated from scratch via the strategies described above, and tests harvested from existing repository test
suites that exercise executable behavior, as done in the ‘coverage-guided iterative’ strategy. Figure 17 shows
the distribution of total tests per task, and breaks down the proportion from each source. The majority of
tests are self-generated (79.5%), while the remaining 20.5% are harvested from existing suites.
Incorporating assertion-quality signals generates stronger tests. A static linter plus gold/dummy execution
feedback in the test generation loop reduces the mean dummy pass rate from 18.5% to 3.7% (a 5× reduction)
and eliminates the worst-case failure mode where a large fraction of a task’s tests are trivially passable. On the
same set of tasks evaluated across four frontier models (Opus 4.6, Sonnet 4.6, Gemini 3.1 Pro and GPT-5.4),
the resulting tests are 20–30 percentage points harder to pass than tests generated without these signals,
with no change in model rank ordering, confirming the gain comes from stricter assertions rather than from
incidentally harder tests.
Coverage measurement methodology. For each task, we merge all active generated test branches and execute
them against a coverage-instrumented build of the original binary. We measure first-party line coverage
only, excluding system headers, vendored dependencies, and auto-generated code. The coverage scatter plot
(Figure 7) shows a representative subsample of 100 tasks drawn from the 154 tasks where we independently
performed coverage measurement, disregarding the coverage recorded by the test generating agent.
Behavioral suite baseline selection. From our benchmark’s hard tasks (difficulty score ≥4; see §A.4 for the
scoring formula), we selected twelve repositories that maintain an identifiable application-level behavioral or
integration test suite, as opposed to only internal unit tests. The selected suites are: PHP’s .phpt regression
harness, FFmpeg’s FATE suite, Typst’s CLI and rendering tests, Miller’s regression cases, StGit’s shell
Table 7 The six specialized configs used in the decomposed test generation strategy. Each config prompts a SWE-agent
to write tests targeting a narrow behavioral category of the executable.
Type
Description
Args
Flag formats, required/optional arguments, positional args, type validation
Config
Environment variables, config file loading, precedence rules
Help
–help/-h output, usage synopsis, subcommand help text
I/O
Stdin/file input, stdout/stderr separation, exit codes, output formatting
Subcommand
Subcommand dispatch, routing, global vs. local flags, aliases
TUI
Interactive navigation, key bindings, screen state, mode switching
23
