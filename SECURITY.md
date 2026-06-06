# Security Policy

Best Enterprise AI is a documentation and reference repository. It may contain examples, patterns, and links for enterprise AI systems, but it should not contain secrets, private customer data, internal credentials, or proprietary production configuration.

## Reporting Security Issues

Please open a private security advisory or contact the repository owner if you find:

- A committed secret.
- A harmful command example.
- Unsafe guidance for agentic tools.
- A broken or malicious external reference.
- A security-sensitive mistake in red-team, sandbox, or tool-access guidance.

## Documentation Safety Rules

- Do not commit API keys, tokens, passwords, private SSH keys, cookies, or session data.
- Do not publish real customer data.
- Do not publish exploit steps without defensive context.
- Do not recommend broad production credentials for agents.
- Do not recommend running untrusted skills, MCP servers, browser automation, or shell tools without sandboxing.
- Prefer official documentation and primary security references.

## Agentic AI Safety Baseline

Any example agent workflow should include:

- Clear owner.
- Scoped permissions.
- Human approval for risky writes.
- Audit logging.
- Sandbox or execution boundary.
- Rollback or disable path.
- Evals and red-team regression tests.
