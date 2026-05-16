<!-- page: 27 -->

## Page 27

Rule
Sev.
Description
no_assertions
HIGH
Test contains no assert statements
trivially_true
HIGH
assert True or assert X or True
sole_returncode
HIGH
Only assertion checks returncode == 0
returncode_in_list
HIGH
assert returncode in [...] launders non-zero exits
pass_body
HIGH
Test body is just pass
assertion_disjunction
HIGH
assert A or B: should assert exact outcome
if_no_else
HIGH
if branch asserts with no else: silently passes when
condition is false
if_else_both_assert
HIGH
Both
if/else
branches
assert:
suggests
non-
deterministic behavior
try_except_swallow
HIGH
except handler with pass swallows failures
all_assertions_weak
HIGH
All assertions only check returncode, len, or isdigit
short_substring
HIGH
Substring check shorter than 15 characters
golden_written_in_test
HIGH
Test writes to its own golden file (always passes)
golden_no_equality
HIGH
Golden file referenced in docstring but never compared
with ==
golden_docstring
HIGH
Golden file mentioned in docstring not found in test
body
for_no_guard
MED
Loop-only assertions with no pre-loop length check
weak_sole_assertion
MED
Sole assertion is len(x) > N
relative_length_assertion
MED
assert len(x) >= N: relative bound verifies nothing
about content
any_all_no_guard
MED
any()/all() with no non-empty guard
file_exists_no_content
MED
path.exists() with no content assertion
only_negative_assertions
MED
All assertions are negative (not in, !=)
catches
LOW
Missing or too-short CATCHES: docstring
Table 8 Assertion lint rules. HIGH rules indicate tests likely to pass trivially incorrect implementations. MED rules
indicate weak but not necessarily vacuous assertions.
A.3.5
Assertion Lint Rules
Table 8 lists all rules checked by the assertion linter.
Examples of Weak Assertions. The following illustrates common failure modes our linter detects, drawn from
real generated tests.
1 def test_help_flag(run_binary):
2
result = run_binary(["--help"])
3
assert result.returncode == 0
Exit-code-only assertion: passes any implementation that
runs without crashing. Ignores the contents of the help
text.
1 def test_list_output(run_binary):
2
result = run_binary(["list"])
3
assert "*" in result.stdout
4
assert result.returncode == 0
Short substring check: the 3-character literal "*" matches
trivially.
1 def test_compile_output(run_binary):
2
result = run_binary(["main.c"])
3
assert result.stdout.startswith("gcc -c ") or \
4
result.stdout.startswith("clang -c ")
Disjunctive assertion: accepts either outcome rather than
asserting the true expected output.
1 def test_parse_output(run_binary):
2
result = run_binary(["input.json"])
3
try:
4
data = json.loads(result.stdout)
5
assert len(data) > 0
6
except Exception:
7
pass
try/except swallowing failures: any exception silently
passes. Also only asserts on content length, not content
itself.
27
