<!-- page: 20 -->

## Page 20

This includes but is not limited to:
- Cloning or browsing the original GitHub repository, its forks, or mirrors
- Downloading the project from package registries: ‘cargo install <project>‘, ‘go get github.com/<org>/<project>‘, ‘pip
install <project>‘, ‘apt-get source <project>‘, ‘npm install <project>‘, etc.
- Fetching source tarballs from project websites (e.g., ‘curl https://lua.org/ftp/lua-5.5.0.tar.gz‘)
- Using a package manager to download the project as a dependency and then reading its cached source (e.g., navigating
into ‘~/.cargo/registry/src/‘ or ‘$(go env GOPATH)/pkg/mod/‘)
- Searching the web for the project’s source code or implementation details
### 2. Wrapping or reusing the original binary
Your submission must be a genuine reimplementation. The provided ‘./executable‘ is for
observation only - your final solution must not depend on it or any other pre-built version
of the same tool at runtime.
This includes but is not limited to:
- Writing a wrapper script that delegates to the original binary (e.g., ‘exec zstd "$@"‘)
- Installing the tool from a package manager and shimming to it (e.g., ‘apt-get install nnn && cp $(which nnn) ./
executable‘)
- Writing a ‘compile.sh‘ that simply makes the provided binary executable (‘chmod +x ./executable‘) or copies it (‘cp ./
executable ./executable‘)
- Building a binary whose main function shells out to an external tool (e.g., ‘Command::new("miniserve").args(args).exec
()‘)
- Re-linking prebuilt ‘.o‘ object files found in the workspace without writing new source code
### 3. Binary analysis of the provided executable
All information about the provided ‘./executable‘ must be obtained by interacting with it
through its normal user interface (CLI flags, stdin/stdout, etc.).
- You MUST NOT decompile ‘./executable‘ or use disassemblers (objdump, Ghidra, etc.) on it
- You MUST NOT use strace, ltrace, or similar tracing/instrumentation tools on ‘./executable‘
Note: this restriction applies ONLY to the provided ‘./executable‘. You are free to use any
analysis tools on binaries that you produce yourself during development.
## What IS allowed
- Running the executable with any inputs, flags, and arguments to observe its behavior
- Reading any documentation files bundled in the workspace
</RULES>
A.2.4
On the Feasability of ProgramBench
The difficulty of the ProgramBench task paired with the constraints we impose at inference time may leave
some readers wondering whether some, or for that matter, any ProgramBench task instances are even possible
to resolve. ProgramBench is a very challenging benchmark by today’s standards. While we do not carry out
any formal human studies, based on the development history, codebase size, and range of functionality, we
venture that an average ProgramBench task instance could take an individual or team days, if not weeks’ or
months’ worth of time to complete.
That said, we argue that while formidable, ProgramBench task instances are certainly solvable by construction.
The key reason ProgramBench is not truly impossible: every test asserts executable behavior that is observable
and deterministic. The same executable is fully accessible to the model, with the necessary permissions to run
with any inputs and see exact outputs. Across the next several paragraphs, we pose and address potential
concerns about ProgramBench’s resolvability.
Can functionality written in one language be reproduced with another? It is possible that models chooses to
implement their solution in different language than one the original source code is written in, which raises the
question: does a solution in an alternative programming language even exist? Computer science theory says
yes. By the Church-Turing thesis (Turing et al., 1936), any deterministic input-output behavior that can be
realized by a program implemented in one Turing-complete language can be realized by a program written in
another Turing-complete language. Simply put, all general-purpose programming languages are equivalent in
computational power. All languages represented across ProgramBench task instances are Turing-complete.
Models are also provided multiple Turing-complete languages in the task environment.
20
