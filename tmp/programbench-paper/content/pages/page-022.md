<!-- page: 22 -->

## Page 22

the php/php-src and tinycc/tinycc task instances respectively. Just as a human developer could come up
with sample files, we impose the same expectations on the task worker. Coming up with a diverse range of
inputs that accounts for edge cases is part of tackling a ProgramBench task instance.
As a final note, we have observed evidence of models being able to programmatically generate binary assets.
During test generation for FFmpeg/FFmpeg, models used ffmpeg’s built-in lavfi virtual input device to
synthesize audio and video on the fly (e.g., sine for waveforms, testsrc for video patterns), avoiding the need
for pre-existing media files entirely. Similarly, during inference across several image-processing tasks (e.g.,
cslarsen/jp2a, hpjansson/chafa), models wrote inline Python scripts using Pillow to programmatically create
test images. This suggests that going forwards, the need to provide binary assets may diminish as models
become more adept at generating their own.
A.3
Test Generation
We briefly extend upon our motivation for designing novel test generation pipelines, then explore several
strategies for automated test generation via mini-SWE-agent.
Limitations of skeleton-based evaluations. As alluded to in the related works (§6), the preceding common
approach to evaluating language models on their ability to build projects to scratch has typically abided by
a fill-in-the-blank structure. This is a direct consequence of the collection and evaluation methodology. To
create a task instance, typically from an open source GitHub repository, class and method implementations
are first deleted procedurally using Python-specific libraries like ast. The repository’s original unit test suite is
then used for evaluation. Consequently, if a model deviates from the expected signatures, even if the deviation
is reasonable, the test harness won’t locate or execute that code.
It is effectively impossible to evaluate truly free-form solutions if tests assert against implementation. From
manual inspection of repositories during early stages of the project, we also found that behavioral checks,
such as end-to-end, integration testing, do not exist in the wild anywhere near as frequently as unit testing.
The yield rate of filtering for repositories that not only satisfy ProgramBench’s collection constraints, but also
have high coverage, end-to-end testing suites is extremely low based on our initial attempts.
Frequency of existing testing. To motivate the need to generate behavioral tests, we first check to what extent
repositories already have such testing. As mentioned in §2.2, ProgramBench does not require repositories have
pre-existing tests, nor does the test generation strictly depend on such information. That said, we perform
this investigation to gauge the necessity of our test generation strategies.
Out of all 200 task instances, 141 (70.5%) have tests, while 59 (29.5%) do not have an existing test suite.
We detect tests via filename conventions (e.g., test_*.py, *_test.go) and directory names (e.g., tests/,
__tests__/); a repository is marked as having tests if at least one such file exists. We find that either
the large majority or entirety of existing test suites consist of implementation focused unit tests targeting
code-level correctness. Behavioral test suites that invoke an executable in multiple ways occasionally appear
in the codebase, but not nearly consistently enough to obviate the need for generating additional tests.
A.3.1
Strategies
To generate tests, we generally first give one or more prompts to a SWE-agent. The agent is then asked to
write the behavioral tests. We summarize the approaches we investigate:
• Monolithic: We give the SWE-agent a single prompt, asking it to generate a comprehensive behavioral
test suite in one pass.
• Decomposed: We give the SWE-agent six specialized prompts, each targeting a narrow category:
argument parsing, configuration, help output, I/O behavior, subcommand dispatch, and TUI interaction.
The hypothesis is that more variegated prompting leads to more diverse testing.
• Coverage-Guided Iterative: We use the SWE-agent to explore the program, its source code, existing
tests, and documentation, and then generate behavioral tests. We also prompt the agent to identify
and include in its test suite any existing behavioral tests defined in the repository (harvesting). The
22
