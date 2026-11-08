# Optional Cursor adapter

The repository is a general Parny MCP integration package. These instructions apply only to its Cursor adapter.

## Plugin installation

1. Install the repository through Cursor's plugin installation flow.
2. Set the required PARNY_OAUTH_CLIENT_ID variable to a Parny-approved public client ID.
3. Enable the Parny MCP server and complete authorization.
4. Check consent, organization access and available tools.
5. Perform a safe read, refresh and revocation test.

The client ID is public, not a secret. No approved Cursor client ID is bundled. Never enter a client secret or access token in this field.

The manifest is .cursor-plugin/plugin.json. Its mcpServers field references the root mcp.json. Cursor plugin interpolation uses ${PARNY_OAUTH_CLIENT_ID}.

## Manual alternative

Merge examples/cursor-mcp.json into Cursor's MCP configuration and supply the environment variable PARNY_OAUTH_CLIENT_ID to the Cursor process. Manual environment interpolation uses ${env:PARNY_OAUTH_CLIENT_ID}. Do not enable both installation methods simultaneously.

## Callback configuration

Cursor documents:
- Desktop: http://localhost:8787/callback
- Web/Agents: https://www.cursor.com/agents/mcp/oauth/callback

Register only intended surfaces and test them separately. Plugin variable expansion inside auth.CLIENT_ID also requires a runtime check.

## Optional Marketplace distribution

After runtime tests and owner approval, a public repository can be submitted at https://cursor.com/marketplace/publish. A repository URL is not an OAuth integration and does not imply acceptance. No submission is made by this package.

Sources: https://cursor.com/docs/mcp and https://cursor.com/docs/reference/plugins
