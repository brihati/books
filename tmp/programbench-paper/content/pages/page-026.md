<!-- page: 26 -->

## Page 26

A.3.4
On Test Overspecification
As referenced in §2.2, here we provide an extended discussion about test over-specification and its impact on
the feasibility of accomplishing a ProgramBench task instance.
Overspecified tests are undesirable because they make a ProgramBench task instance infeasible to successfully
complete. Generally, an “overspecified" test checks a solution for details that are not stated explicitly in the
task instructions and impossible to discover during the task solving process. In other words, an overspecified
test asserts a condition that is completely inaccessible to a task worker.
ProgramBench addresses this issue by virtue of how tests are constructed. In lieu of unit tests, which we
define as tests that check against source code, ProgramBench tests assert only on observable behavior of an
executable, such as standard output/error, exit codes, and file system modifications. Therefore, because tests
always involve invocations of an executable, they inherently are incapable of targeting details such as variable
names or method definitions.
A subtler concern is whether tests might demand exact reproduction of implementation-dependent outputs,
such as floating point precision or hash iteration order. A concurrent case study highlights this tension:
MirrorCode (Adamczewski et al., 2026) addresses this explicitly by manually vetting 4 repositories “that
seemed feasible for a human software engineer to reimplement under similar constraints”, where feasibility is
defined as programs where the behavior and documentation are closer to a specification rather than a reverse
engineering challenge.
We take a different approach. Rather than deciding manually which behaviors are reasonable, we treat the
gold executable as the complete specification, which means any deterministic, observable behavior is fair
game. This is a deliberate design choice. First, the model has full access to the executable at inference
time, so any behavior a test checks can be discovered by running the same command. The suite contains
no hidden information that the model cannot obtain itself. Second, after several rounds of annotations, we
came to the conclusion that distinguishing “meaningful behavior” from “implementation artifact” can be very
subjective and does not scale. Whether the 8th decimal digit of a computation matters depends entirely on
the application; for a library used to calculate the trajectory of a satellite in space, precision is of utmost
importance. Third, our gold evaluation procedure filters nondeterministic tests by running each test against
the reference executable multiple times and throwing out any that do not pass consistently. The tests that
remain reliably characterize an executable’s behavior, which is precisely what we ask the model to reproduce.
We audited ProgramBench task instances to investigate whether any task instances are “at risk” of overspeci-
fication. We find that in our setting, there are very limited manners in which overspecification can occur;
namely, floating point precision, hash/map iteration order, and rendering discretization. Other potential
forms of non-determinism such as timestamp formatting or locale-dependent sorting are really an attribute of
environment differences, not implementation differences, which our Docker based set up standardizes. Out of
200 instances, we found only 5 instances where such behavior could plausibly appear in test output:
• oppiliappan/eva: a terminal calculator REPL, where arithmetic results could differ in precision depend-
ing on the floating point library or operation ordering used by a reimplementation.
• gromacs/gromacs: a molecular dynamics simulation toolkit, where simulation outputs involve extensive
floating point computation sensitive to operation ordering.
• rs/jplot: a terminal plotting tool, where mapping continuous values to discrete character-grid positions
involves rounding decisions (e.g., floor vs. round) that affect visual output.
• OSGeo/PROJ: a cartographic projection library, where coordinate transformations involve chained
floating point operations and intermediate rounding.
• OSGeo/gdal: a geospatial data translator, where raster/vector transformations and coordinate repro-
jections involve floating point arithmetic sensitive to operation ordering.
We manually inspected the test suites for these five instances and did not find evidence of assertions on
implementation-dependent numerical output; the tests predominantly check CLI flag behavior, file format
handling, and string output.
26
