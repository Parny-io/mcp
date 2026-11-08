# Parny MCP

Connect MCP-compatible AI applications to Parny's infrastructure visibility, service context and operational insights through a hosted MCP endpoint.

This repository provides client integration examples and documentation. It does not contain or run the Parny MCP server.

## Connection

- Transport: Streamable HTTP
- Endpoint: https://mcp.parny.io/v2/mcp
- Authentication: OAuth 2.0 authorization code with S256 PKCE
- Authorization server: https://auth.parny.io
- Scopes: mcp:sre and mcp:developer

Available tools and data depend on your Parny organization, role, plan and module entitlements. The unified endpoint is designed for read-only SRE and Developer tools; access is not granted merely by requesting a scope.

## Client compatibility

Use an MCP host that supports remote Streamable HTTP and the provider's OAuth flow. Configuration formats differ between clients; an endpoint URL alone does not guarantee compatibility.

A host using a local LLM can also integrate with this remote service if that host supports MCP and compatible authentication. The model itself does not implement the connection. Running the model locally does not make Parny calls offline or keep all tool arguments/results on the local machine: the host connects to Parny's hosted endpoint. Review what data the host and any model provider receive.

Other clients have not been runtime-tested by this repository. Do not assume support for an arbitrary LLM or client.

### Generic setup

1. Confirm that the MCP host supports Streamable HTTP, OAuth discovery, resource indicators and S256 PKCE.
2. Configure the endpoint above using that host's documented configuration format.
3. Obtain a Parny-approved public OAuth client identity with the host's actual callback URI.
4. Complete sign-in and consent in an authorized Parny account.
5. Verify organization context, tool listing and a safe read before normal use.
6. Verify token refresh and revocation in the selected host.

The live authorization-server metadata advertises Client ID Metadata Document support, but did not advertise a dynamic registration endpoint at the last check. Do not assume an automatic registration flow works. Never substitute an arbitrary GitHub URL for an OAuth client ID.

See [authentication](docs/authentication.md) for discovery and integration requirements.

### Cursor adapter

Cursor is one supported configuration target in this package, not the repository's sole purpose. The optional .cursor-plugin/plugin.json and mcp.json files provide its plugin adapter; examples/cursor-mcp.json provides its manual configuration example. See [Cursor setup](docs/cursor.md). Authenticated interoperability remains to be tested.

Do not reuse Cursor's JSON format in another host unless that host explicitly documents compatibility.

## Example requests

- “What infrastructure and services can I inspect in my authorized Parny organization?”
- “Show the available service context for this incident and explain what evidence is missing.”
- “Summarize the operational information available for this service without changing anything.”

These examples do not guarantee a particular tool or dataset is available to every account. Keep the host's tool approval controls enabled and review proposed operations.

## Status and validation

Release candidate integration materials. Public discovery and the unauthenticated OAuth challenge were checked on 8 November 2026. An authenticated client login, tool listing, refresh and revocation test has not yet been completed.

Run python3 scripts/validate.py and python3 -m unittest discover -s tests -v. These are local configuration checks, not server tests or client certification. Follow the [release checklist](docs/release-checklist.md) before public distribution.

## Security

Never commit tokens, API keys, cookies, customer data or private server source. Store credentials in the client's secure storage. Report security concerns through your existing Parny support channel, not a public issue containing sensitive data.

## References

- [MCP specification](https://modelcontextprotocol.io/specification)
- [Cursor MCP](https://cursor.com/docs/mcp)
- [Cursor plugin reference](https://cursor.com/docs/reference/plugins)

The repository owner must choose a distribution license before publication. No license grant is implied by this draft.
