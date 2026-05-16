<!-- page: 19 -->

## Page 19

often miss build artifacts and hidden files. For instance, at one point we added explicit reminders to
remove caches (e.g., ∼/.cargo/, ∼/.cache/**) and build folders (e.g., target/, build/), which contain
direct or suggestive information about the implementation. Furthermore, a handful of repositories,
typically implemented in C/C++ where build systems are much more heterogenous unlike the Rust
or Golang developer ecosystems, would produce artifacts in a much less predictable, uniform manner.
Consequently, the model would frequently fail to explore and remove such artifacts when generating
clean.sh. The artifact would then be discovered at inference time. Therefore, to eliminate any possibility
of such leakage, we opted for the final approach of separating execution compilation and model inference
into two separate containers.
• git history removal: The original repository’s version control history can reveal the remote URL, branch
names, and commit messages that identify the project. During image construction, we wipe the existing
.git/ directory and reinitialize a fresh repository with a single anonymous commit containing only the
documentation and the executable.
Collectively, these steps ensure that decompilation is impossible, submissions that wrap the gold executable
are illegitimate, and local build artifacts that partially or fully give away implementation details do not exist.
We review the restrictions and checks we impose on the inference and evaluation procedures.
• No Internet Access: Early in the project, we experimented with several iterations where we allowed
internet access at inference time, but then prohibited specific behaviors that we deemed cheating by
describing them specifically in the task instructions. We also ran an LM-as-a-judge pipeline that would
flag cheating by checking the agent trajectory corresponding to a solution. Such measures quickly
devolved into a cat-and-mouse game, with more capable models coming up with measures to circumvent
instructions, such as downloading source code by importing via a dependency manager like cargo rather
than directly from Github. Furthermore, verbalizing the fine line of what is (not) permitted also quickly
became tricky. On occasion, models’ thought traces exhibit uncertainty over whether certain actions
were permissible. When working on FFmpeg/FFmpeg, Claude Sonnet 4.6 expressed hesitation over
whether it was allowed to download a dependency that happened to be co-located (implemented in the
same GitHub repository) with the FFmpeg source code. We considered running the LM-as-a-judge
cheat detection with multiple models as a way to address “gray areas”, but found that there were high
rates of disagreements and volatility in the judgments themselves. Therefore, in favor of simplicity and
rigor, we block internet access during ProgramBench inference.
• System prompt instructions: As shown below, the task instructions inform what behaviors are disallowed.
Even though the aforementioned guardrails ensure that disallowed actions are futile, we still include this
text because without it, task workers may waste turns generating unpermitted actions. The full system
prompt is shown below.
You are a helpful assistant that can interact with a computer.
This is a reverse-engineering benchmark. You are given a compiled binary and its documentation.
Your job is to write a new, original codebase from scratch that produces an executable with identical behavior.
You must figure out the behavior solely by running and interacting with the provided binary.
Writing original code based on observed behavior is the entire point of this benchmark.
Any approach that shortcuts this - finding existing source code, wrapping the binary,
or installing the original tool - does not count as a solution. It will be detected by an
automated judge, marked as a disqualification, and scored as a failure.
The trace will be posted to an online wall of shame.
<RULES>
## What is not allowed
### 1. Obtaining source code
The only source of truth about what the executable does is the executable itself and its
bundled documentation. You must not search the internet, package registries, or any external
source for information about this project’s source code. Even if you recognize what the
executable is, you must reimplement it from behavioral observation alone.
19
