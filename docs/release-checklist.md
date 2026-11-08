# Parny MCP release checklist

## Before a public repository

- [ ] Review every file for confidential information and customer data.
- [ ] Choose the repository name, owner and license.
- [ ] Add the final public repository URL to the manifest if desired.
- [ ] Optionally add a brand-approved logo and reference its relative path.
- [ ] Verify current Cursor documentation and manifest requirements.
- [ ] Obtain approval for any new OAuth client registration or persistent access.
- [ ] Configure a tested public client ID or confirm the per-install configuration experience.

## Runtime acceptance for each advertised client

- [ ] Verify each intended MCP host and record the tested version.
- [ ] For the optional Cursor adapter, confirm variable substitution in auth.CLIENT_ID.
- [ ] Complete OAuth login and consent in an authorized test account.
- [ ] Check returned tools and organization/module access.
- [ ] Exercise one safe read with non-sensitive test data.
- [ ] Confirm unauthorized organizations and modules are inaccessible.
- [ ] Verify token refresh, logout/revocation and reauthorization.
- [ ] Test desktop; test Web/Agents separately if advertised.
- [ ] Keep a sanitized test record with version and date.

## Optional Cursor Marketplace submission

A repository link alone is not an approval or a working OAuth integration. Once the configuration works and the owner approves publication, create the public repository and submit its URL at https://cursor.com/marketplace/publish. Complete any additional current form fields and wait for Cursor's review.

This package does not create a repository, register a client, grant consent or submit a Marketplace application.
