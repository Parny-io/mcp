# MCP and A2A

Parny MCP and A2A serve different roles. MCP lets a compatible client retrieve authorized operational evidence and developer context. A2A is an agent-to-agent coordination protocol; pointing a client at an MCP URL does not make it an A2A agent.

## Evidence and service context

The unified MCP endpoint is `https://mcp.parny.io/v2/mcp`. Depending on organization entitlement and granted scope, authenticated tool discovery can expose operational tools (`mcp:sre`) and developer-context tools (`mcp:developer`). Service context and dependencies help relate an incident to the affected infrastructure and service map. Availability and completeness depend on the organization's collected data; do not infer full infrastructure coverage from an empty response.

Use the live authenticated tool schemas rather than hard-coding a tool inventory. Keep discovery and credentials isolated by caller and resource. A missing module or failed request is not evidence of an empty dataset.

## Agent integration boundary

An A2A application can use an MCP client to gather evidence, then exchange investigation context with another agent using its own A2A implementation. This repository supplies MCP client configuration and documentation only; it does not ship an A2A coordinator, customer agent or autonomous remediation runtime.

MCP access does not grant permission to change customer infrastructure. Keep investigation, proposed action, customer approval, execution and verification separate. Never put credentials in prompts, agent messages or this public repository.

For interactive OAuth clients, follow [authentication requirements](authentication.md), including resource binding and a registered client identifier. Server-side integrations must use their separately approved credential flow; do not repurpose a user's OAuth token for a different resource or assume API-key support in every host. This document describes integration boundaries, not a claim of a tested live A2A deployment.
