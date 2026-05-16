<!-- page: 21 -->

## Page 21

Could obscure program behaviors be impossible or arbitrarily hard to discover? A subtler concern is discoverability
of tested behaviors. To elaborate, given that the test generator runs with full access to the source code, it
is possible that some generated tests target hard-to-detect, edge-case behavior. However, this concern is
a reflection of ProgramBench’s difficulty, not feasibility. Models could very well not think of running the
executable with certain permutations of flags and inputs. This does not mean the task is impossible. Rather,
it demonstrates how exploration of program behavior is a key challenge posed by ProgramBench, and that
beyond writing code, models are tested on their thoroughness when it comes to uncovering behaviors and
considering boundary conditions that human developers accounted for.
Conceptually, one scenario where behavior is borderline impossible to discover is if an executable supports
functionality that is not communicated or documented via any observable channel. In other words, there
is functionality that is not revealed by the README.md, –help flag standard output, or any artifacts that
could be unveiled by typical exploratory actions. A corresponding test would then effectively be penalizing
models for failing to discover behavior that was never observable in the first place. Such tests may also
incentivize models to exhaustively and unintelligibly probe an executable with random inputs, rather than
engage in systematic, hypothesis-driven exploration.
In practice, we find that well-maintained programs document their interfaces thoroughly. Flags, subcommands,
supported inputs, and example invocations are frequently surfaced as help output, man pages, or usage
documentation. The above scenario, an executable with important but entirely undiscoverable functionality,
would be considered not only bad practice, but even defective by conventional software engineering practices.
Out of caution, we reviewed all 200 repositories for such discrepancies and did not find any instances where
an executable’s supported behavior was entirely absent from the task instance’s start state.
What if tasks require internet to solve? While creating task instances, we came across several repositories
that require internet access for a variety of reasons. The following are a handful of GitHub repositories
that successfully construct an executable, but were not usable as ProgramBench task instances because the
executable inherently requires communication with one or more endpoints on the web.
• thomas-mauran/chess-tui: A terminal chess client. Its core gameplay requires connecting to lichess.org
to match with remote opponents.
• aquaproj/aqua: A CLI tool manager. It downloads tool binaries from GitHub releases, making the
entire tool lifecycle network-dependent.
• builditluc/wiki-tui: A terminal Wikipedia reader. Every user interaction fetches and renders articles
from the Wikipedia API.
We take care to only admit task instances to the test set that do not have this need. That said, ProgramBench
nonetheless contains networking tools; 18 task instances are utilities such as HTTP clients, DNS resolvers,
and port scanners. While internet access is cut off, ProgramBench task environments still retain loopback
networking (127.0.0.1). The reverse engineering challenge in these tools lies in their protocol handling, output
formatting, and CLI logic, not in reaching a remote host. Therefore, task workers can still develop faithful
implementations by spinning up local servers and exercising program behavior against localhost. We mark
the 18 task instances that involve networking functionality in Table 12.
Do task workers have access to evaluation assets? Some behavioral tests exercise the executable with input files
such as images, audio files, videos, spreadsheets, or domain specific configurations. Coupled with the lack
of internet access, this highlights an unfair asymmetry where evaluation uses assets that either models are
unable to generate on their own or are relatively obscure, executable-specific file formats.
To address this, for each task instance, after generating tests, we run a script to extract such assets. The
script abides by a simple heuristic: keep any files with extensions that aren’t on a “blocklist” of popular,
standardized, text-based file formats. The rationale is that we are not interested in the failure mode where
models fail to develop a solution because it could not come up with characteristic test data. This means
that binaries (e.g., png, mp3, wav, xlsx) are always provided, as today’s models may not be capable of
synthesizing such files directly. A handful of repositories propose and use their own file formats (e.g., .hcl
for HashiCorp configurations); our script also keeps these as well. On the other hand, files represented in
popular formats are not provided; for example, we do not give .php or .c files used by evaluation suites for
21
