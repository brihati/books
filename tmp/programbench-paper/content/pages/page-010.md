<!-- page: 10 -->

## Page 10

0%
25%
50%
75%
100%
0
1000
2000
3000
4000
5000
Total Lines
Claude Opus 4.7
0%
25%
50%
75%
100%
Claude Sonnet 4.6
0%
25%
50%
75%
100%
Gemini 3.1 Pro
0%
25%
50%
75%
100%
GPT 5.4
Trajectory Progress
Figure 11 Codebase growth over normalized trajectory progress for four models. Each thin line is an individual
trajectory; the bold line shows the median and the shaded region the interquartile range. The y-axis is capped at the
95th percentile of final codebase sizes.
0%
25%
50%
75%
100%
Opus 4.7
Sonnet 4.6
Gemini 3.1 Pro
GPT 5.4
67%
42%
51%
100%
Figure 12 Percentage of the final codebase produced by
the single largest edit, per model. For instance, GPT 5.4
writes a median of 96% of its code in one turn.
Model
Create
Modify
Delete
Claude Opus 4.7
7.7
3.3
0.2
Claude Sonnet 4.6
11.3
18.3
1.5
Gemini 3.1 Pro
61.2
10.1
9.4
GPT 5.4
5.0
1.2
0.3
Table6 Mean file mutations per trajectory. Create, modify,
and delete counts reflect how frequently models revisit
and restructure their codebases. Counts are averaged
across all tasks and models.
Models rarely exceed the turn or time budget. Across all nine models (1,800 runs), the agent voluntarily submits
its solution in 98.1% of trajectories. Just 1.9% exhaust the 6 hour wall clock time limit, and just a single run
reaches the 1,000 turn cap. Timeouts are concentrated in Opus 4.6 (29/200) and Sonnet 4.6 (5/200). All
other models complete all 200 tasks within the time and step budget. This finding suggests that the limits do
not artificially constrain model performance.
Writing dominates most models’ action budgets. Opus 4.7, Sonnet 4.6, Gemini 3.1 Pro, and GPT 5.4 all devote
the largest share of turns to writing code (48.7%, 37.5%, 40.7%, and 40.2% respectively). Probing the reference
executable is the second-largest category for all four, ranging from 22.6% (Opus 4.7) to 34.1% (Gemini 3.1
Pro). Read actions account for 13–16% across all representative models.
Probing trends differently across models. GPT 5.4’s actions are concentrated almost entirely within the first 30
turns. Claude models maintain a steadier mix of probing and writing throughout their trajectories, interleaving
exploration with implementation rather than treating them as distinct phases.
Codebase growth varies between gradual iteration and single-shot generation. To study how a SWE-agent’s
codebase grows across the course of a trajectory, for each trajectory, we replay the subset of commands that
modify files (e.g., touch, sed, rm) and snapshot the file system after each turn. This sequence of snapshots
allows us to recover a ground-truth timeline of how files are updated at different points in a trajectory.
Figure 11 shows all trend lines of a codebase’s total line count with respect to trajectory progress for each
model across all 200 instances. Claude Sonnet 4.6 and Gemini 3.1 Pro tend to ramp up steadily, whereas
GPT 5.4 produces nearly all code in a single turn early on in the trajectory. To highlight this distinction
further, Figure 12 shows that the median fraction of the final codebase written in a single turn ranges from 44%
(Sonnet 4.6) to 100% (GPT 5.4), with Opus 4.7 at 67% and Gemini 3.1 Pro at 53%. As reflected in Table 6,
10
