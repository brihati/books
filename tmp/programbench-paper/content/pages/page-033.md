<!-- page: 33 -->

## Page 33

0
20
40
60
80
100
Test pass rate (%)
C/C++  (45 tasks)
Go  (46 tasks)
Rust  (107 tasks)
Claude Opus 4.7
Claude Opus 4.6
Claude Sonnet 4.6
Claude Haiku 4.5
Gemini 3.1 Pro
Gemini 3 Flash
GPT 5.4
GPT 5.4 mini
GPT 5 mini
Figure 24 Distribution of per-task test pass rates by reference language across all models. Each box spans the
interquartile range with the median shown in white; individual task scores are overlaid as jittered points. Two tasks
whose reference language is the sole representative of its family (one Haskell, one Java) are omitted.
per-model box plots for each of the three reference languages. Rust and Go tasks yield similar average pass
rates (38.5% and 38.4% respectively), while C/C++ tasks lag behind at 27.7%. The model ranking is largely
preserved across languages, but C/C++ compresses the distribution downward: even the strongest models
see median pass rates drop by 15–20 percentage points relative to Go. The gap likely reflects the greater
complexity of the C/C++ codebases in ProgramBench (which include projects such as FFmpeg, GCC, and
DuckDB) rather than an inherent language disadvantage.
0
100
200
300
400
API calls
0
20
40
60
80
100
Test pass rate (%)
0
5
10
15
20
Cost ($)
0
20
40
60
80
100
Test pass rate (%)
Claude Opus 4.7
Claude Opus 4.6
Claude Sonnet 4.6
Claude Haiku 4.5
Gemini 3.1 Pro
Gemini 3 Flash
GPT 5.4
GPT 5.4 mini
GPT 5 mini
Figure 25 Per-instance test pass rate vs. API calls (left) and cost (right). Each point is one (task, model) run. The
x-axes are clipped at the 95th percentile for readability.
More turns spent does not correlate with improved scores. We plot per-instance test pass rate against API calls
and cost to understand whether additional compute translates to better outcomes. Figure 25 shows scatter
plots across all 1,788 runs, colored by model. The per-instance Pearson correlations are weak (r=0.27 for API
calls, r=0.21 for cost), and the scatter plots show no clear trend: high-scoring runs appear at all turn counts
and cost levels, while many expensive runs still score near zero. The modest positive correlations are largely
driven by model-level differences, as stronger models tend to both use more turns and score higher, rather
than by within-model scaling.
33
