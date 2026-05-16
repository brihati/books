<!-- page: 32 -->

## Page 32

B
Additional Results
We present additional figures and discussion that complement the experiment setup discussion (§3), main
evaluation (§4), and analyses (§5).
B.1
Experimental Setup
Beyond its adoption by widely used leaderboards (§3), mini-SWE-agent is built to be neutral in how models
interact with a codebase. Each turn, a model simply issues a bash action which is then executed directly; there
are no manually crafted tools or prompts that could unfairly advantage or disadvantage particular models.
This minimal design ensures that performance differences can be attributed directly to model capabilities
rather than idiosyncrasies in agentic harnesses.
All configurations below are specified declaratively in mini-SWE-agent’s YAML configuration files, which
control the agent loop, container provisioning, and model invocation.
• Per-action timeout. Each agent action must complete within 3 minutes; actions exceeding this limit are
terminated with a descriptive error message. Models can work around this by launching background
processes and polling output files.
• Cost limit. No cost limit is imposed. For reported costs, prompt caching is enabled and accounted for
across all models.
• Output truncation. Command outputs exceeding 10,000 characters are truncated, showing the first and
last 5,000 characters with an elision notice.
• Soft warnings. When fewer than 20 steps or 10 minutes remain, the agent receives a warning to wrap up
and ensure its solution compiles.
B.2
Further Findings
0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
100%
Test pass rate
0
100
200
300
Number of runs
median = 32%
N = 1,788 runs
Figure 23 Distribution of test pass rates across all 1,800 leaderboard runs in 5% bins. The median pass rate across all
runs is 32%.
Most runs achieve meaningful partial progress rather than all-or-nothing outcomes. We examine how test pass
rates are distributed across all leaderboard runs to understand how partial progress varies across models and
task instances. Figure 23 shows the distribution across all 1,788 runs. The 0–5% bin is the single largest,
containing roughly 18% of runs, indicating that models do frequently fail to make any meaningful progress on
a task. Beyond that initial spike, however, scores are spread roughly uniformly across the pass-rate spectrum,
with a median of 32%. The distribution tapers gradually at the high end: fewer than 5% of runs exceed 90%,
and near-perfect reimplementations are rare. The large low-scoring bin provides a floor of genuinely difficult
tasks, the uniform middle range rewards incremental progress, and the sparse right tail leaves room for future
models to improve.
Across all models, performance on C/C++ tasks is substantially lower than Go and Rust. We break down pass rates
by reference language to understand whether task difficulty varies across language families. Figure 24 shows
32
