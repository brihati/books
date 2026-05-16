<!-- page: 12 -->

## Page 12

7
Discussion
Limitations. ProgramBench relies on a finite set of behavioral tests, which under-approximates each executable’s
full specification. Evaluation therefore is a “lower bound” on correctness: solutions that fail are definitively
incorrect, while those that pass may still diverge from the original on untested inputs. ProgramBench tests
also currently focus exclusively on input-output equivalence. Non-functional properties like execution speed,
memory usage, or disk footprint are not captured. Therefore, it is possible a model reproduces behavior with
an implementation orders of magnitude slower or more resource intensive than the original. Developing richer
test generation strategies to improve coverage and incorporate system constraints is a promising direction.
Future work. Several technical reports and blogs have suggested the effectiveness of applying multiple SWE-
agents towards long horizon coding tasks (Lin, 2026; Carlini, 2026; Geng and Neubig, 2026; Mishra-Sharma,
2026). ProgramBench can serve as a testbed for such works. Our work uses a single SWE-agent as the baseline;
this design reflects prior benchmark evidence, notably SWE-bench, where well-tuned single-agent systems have
performed competitively, and multi-agent variants have not consistently shown clear advantages. We are excited
to use ProgramBench to delineate the benefits of multi-agent approaches. Similarly, ProgramBench could
further exploration into human-centered coding agents, where a developer, given the executable, iteratively
guides the agent through design decisions (Liu et al., 2025; Baumann et al., 2026; Wang et al., 2026).
Conclusion. We introduce ProgramBench, a benchmark for measuring the ability of software engineering
agents to develop, from scratch, programs that match a given executable’s behavior. Existing models struggle
substantially, and none fully resolve any task. However, via fine-grained metrics, we find that models achieve
meaningful partial progress, with stark differences in how models expend turns and the final form of their
codebases. Our analyses reveal meaningful gaps in models’ decision making in architecting, developing and
testing software. We hope that ProgramBench could serve as a testbed for efforts focused on end-to-end
autonomous software development.
12
