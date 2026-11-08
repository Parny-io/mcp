# MCP authentication

The hosted Parny MCP endpoint uses OAuth authorization code flow with S256 PKCE. Choose a client/host that supports this flow over remote Streamable HTTP. A local LLM requires an MCP-capable host to perform discovery, authorization and tool calls on its behalf.

## Public discovery checked on 8 November 2026

Protected resource metadata:
https://mcp.parny.io/.well-known/oauth-protected-resource/v2/mcp

Authorization-server metadata:
https://auth.parny.io/.well-known/oauth-authorization-server

The protected resource advertises https://mcp.parny.io/v2/mcp, auth.parny.io and mcp:sre / mcp:developer scopes. The authorization server advertises authorization-code and refresh-token grants, S256 PKCE and public-client token authentication.

A dynamic client registration endpoint was not advertised. Client ID Metadata Document support was advertised. Neither observation establishes that a particular host will automatically register or authenticate successfully.

## Client identity and callbacks

Use a public client identity approved for the host, with its actual callback URI. Do not invent a client ID or reuse another application's callbacks. Client secrets must not be distributed in this repository.

A client metadata URL is a separate integration mechanism, not an arbitrary GitHub repository link. No hosted metadata document, client registration or persistent access is provisioned by this package.

Client IDs and callbacks for additional hosts require operator verification and host-specific testing. The included Cursor adapter's configuration is documented separately in cursor.md.

## Acceptance tests

Verify discovery, callback, explicit consent, resource audience, correct organization/module access, tool listing, a safe read, token refresh and revocation. Do not request offline_access unless the provider requires and supports it. Do not combine a Bearer token with an API-key header. Keep credentials out of screenshots, logs and public issues.

The MCP service is hosted remotely even when the LLM runs locally. Review data flows and the host's tool approval settings.
