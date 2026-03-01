# Security and Authentication

## 1. Authentication vs Authorization

**Authentication (AuthN)** answers the question: **"Who are you?"**
It is the process of verifying the identity of a user, device, or system. You prove you are who you claim to be by presenting credentials such as a password, biometric data, or a cryptographic token.

**Authorization (AuthZ)** answers the question: **"What are you allowed to do?"**
It is the process of determining whether an authenticated entity has permission to access a specific resource or perform a specific action.

Authentication always comes before authorization. You must first establish identity before you can check permissions.

### Comparison Table

| Aspect              | Authentication (AuthN)              | Authorization (AuthZ)                   |
|----------------------|--------------------------------------|-----------------------------------------|
| Purpose             | Verify identity                      | Verify permissions                      |
| Question            | "Who are you?"                       | "What can you do?"                      |
| Input               | Credentials (password, token, cert)  | User identity + resource policy         |
| Output              | Authenticated identity (session/JWT) | Allow or Deny decision                  |
| Happens             | Before authorization                 | After authentication                    |
| Protocol Examples   | OAuth 2.0, SAML, OIDC, LDAP         | RBAC, ABAC, ACLs, IAM policies          |
| Failure Response    | 401 Unauthorized                     | 403 Forbidden                           |
| Visibility to User  | Login screen, MFA prompt             | "Access Denied" page                    |

### Common Authorization Models

- **RBAC (Role-Based Access Control):** Users are assigned roles (admin, editor, viewer). Permissions are attached to roles, not to individual users. Simple and widely used.
- **ABAC (Attribute-Based Access Control):** Decisions are based on attributes of the user, the resource, the action, and the environment. Example: "Allow if user.department == resource.department AND time is within business hours."
- **ACL (Access Control List):** Each resource has a list of which users or groups can perform which actions on it. Common in file systems.
- **Policy-Based (e.g., AWS IAM):** JSON policy documents that specify Allow/Deny for specific actions on specific resources under specific conditions.

---

## 2. OAuth 2.0

OAuth 2.0 is an **authorization framework** that allows a third-party application to obtain limited access to a user's resources on another service, without exposing the user's credentials to the third-party app.

Key insight: OAuth 2.0 is about **delegation of access**, not authentication. It answers "Can this app access my photos on Google?" not "Is this person who they claim to be?"

### Roles

| Role                 | Description                                                        | Example                        |
|----------------------|--------------------------------------------------------------------|--------------------------------|
| Resource Owner       | The user who owns the data and grants access                       | You (the end user)             |
| Client               | The application requesting access to the user's resources          | A third-party photo editor app |
| Authorization Server | Issues access tokens after authenticating the resource owner       | Google's OAuth server          |
| Resource Server      | Hosts the protected resources; validates access tokens             | Google Photos API              |

### Grant Types

#### Authorization Code Grant (Most Common for Web Apps)

Used by server-side applications. The client never sees the user's password. The authorization server returns an **authorization code** to the client, which the client exchanges for an access token via a back-channel (server-to-server) request.

- Most secure grant type for web applications.
- The access token is never exposed to the browser.

#### Authorization Code with PKCE (Proof Key for Code Exchange)

Extension of the Authorization Code grant designed for **public clients** (mobile apps, SPAs) that cannot securely store a client secret.

- Client generates a random `code_verifier` and derives a `code_challenge` from it.
- `code_challenge` is sent with the authorization request.
- `code_verifier` is sent when exchanging the authorization code for a token.
- The authorization server verifies they match, preventing authorization code interception attacks.

#### Client Credentials Grant

Used for **machine-to-machine** communication where no user is involved. The client authenticates directly with the authorization server using its own credentials (client_id + client_secret) and receives an access token.

- No user interaction.
- Used for service-to-service API calls, background jobs, microservice communication.

### Tokens

| Token          | Purpose                                | Lifetime     | Storage                          |
|----------------|----------------------------------------|--------------|----------------------------------|
| Access Token   | Grants access to protected resources   | Short (5-60 min) | Memory, secure cookie        |
| Refresh Token  | Obtains new access tokens              | Long (days-months) | Secure server-side storage |

- Access tokens are included in API requests (typically in the `Authorization: Bearer <token>` header).
- When an access token expires, the client uses the refresh token to get a new one without requiring the user to log in again.
- Refresh tokens should be stored securely and can be rotated (one-time use).

### Authorization Code Flow

```mermaid
sequenceDiagram
    participant User as Resource Owner
    participant Browser as User Agent
    participant App as Client Application
    participant AuthServer as Authorization Server
    participant API as Resource Server

    User->>Browser: Click "Login with Google"
    Browser->>AuthServer: GET /authorize?response_type=code&client_id=X&redirect_uri=Y&scope=Z
    AuthServer->>User: Show login + consent screen
    User->>AuthServer: Grant consent
    AuthServer->>Browser: Redirect to redirect_uri with authorization code
    Browser->>App: GET /callback?code=AUTH_CODE
    App->>AuthServer: POST /token (code + client_id + client_secret)
    AuthServer->>App: Access Token + Refresh Token
    App->>API: GET /resource (Authorization: Bearer <access_token>)
    API->>App: Protected Resource
```

---

## 3. JWT (JSON Web Tokens)

A JWT is a compact, URL-safe, self-contained token format used to securely transmit information between parties as a JSON object. The information can be verified and trusted because it is digitally signed.

### Structure

A JWT consists of three parts separated by dots: `header.payload.signature`

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.POstGetfAytaZS82wHcjoTyoqhMyxXiWdR7Nn7A29DNSl0EiXLdwJ6xC6AfgZWF1bOsS_TuYI3OG85AmiExREkrS6tDfTQ2B3WXlrr-wp5AokiRbz3_oB4OxG-W9KcEEbDRcZc0nH3L7LzYptiy1PtAylQGxHTWZXtGz4ht0bAecBgmpdgXMguEIcoqPJ1n3pIWk_dUZegpqx0Lka21H6XxUTxiy8OcaarA8zdnPUnV6AmNP3ecFawIFYdvJB_cm-GvpCSbr8G8y_Mllj8f4x9nBH8pQux89_6gUY618iYv7tuPWBFfEbLxtF2pZS6YC1aSfLQxaOoaBSTIUg
```

**Header:** Contains metadata -- the signing algorithm and token type.

```json
{
  "alg": "RS256",
  "typ": "JWT"
}
```

**Payload:** Contains claims -- statements about the user and additional metadata.

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "role": "admin",
  "iat": 1516239022,
  "exp": 1516242622
}
```

**Signature:** Created by signing the encoded header + encoded payload with a secret or private key.

```
RSASHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  privateKey
)
```

### Standard Claims (Registered Claims)

| Claim | Name          | Description                                |
|-------|---------------|--------------------------------------------|
| `iss` | Issuer        | Who issued the token (e.g., auth server)   |
| `sub` | Subject       | Who the token refers to (e.g., user ID)    |
| `aud` | Audience      | Intended recipient of the token            |
| `exp` | Expiration    | Unix timestamp when the token expires      |
| `iat` | Issued At     | Unix timestamp when the token was issued   |
| `nbf` | Not Before    | Token is not valid before this time        |
| `jti` | JWT ID        | Unique identifier for the token            |

Custom claims can be added for application-specific data (e.g., `role`, `permissions`, `tenant_id`).

### Symmetric vs Asymmetric Signing

| Aspect              | Symmetric (HMAC - HS256)                 | Asymmetric (RSA - RS256)                       |
|----------------------|------------------------------------------|------------------------------------------------|
| Key                 | Single shared secret                      | Private key (sign) + Public key (verify)       |
| Who can sign?       | Anyone with the shared secret             | Only the holder of the private key             |
| Who can verify?     | Anyone with the shared secret             | Anyone with the public key                     |
| Use case            | Single service (sign and verify in same place) | Distributed systems (auth server signs, many services verify) |
| Key distribution    | Must be kept secret everywhere            | Public key can be freely distributed (JWKS)    |
| Performance         | Faster                                    | Slower                                         |
| Security risk       | If secret leaks, anyone can forge tokens  | If private key leaks, tokens can be forged     |

In microservices architectures, **asymmetric signing is strongly preferred**. The auth server keeps the private key. All other services only need the public key (published via a JWKS endpoint) to verify tokens. No secret sharing needed.

### JWT vs Opaque Tokens

| Aspect              | JWT (Self-Contained)                     | Opaque Token                                   |
|----------------------|------------------------------------------|------------------------------------------------|
| Format              | Base64-encoded JSON with signature        | Random string (e.g., UUID)                     |
| Contains user info? | Yes (claims embedded in payload)          | No (just a reference/pointer)                  |
| Validation          | Verify signature locally, no DB call      | Requires lookup against token store/auth server|
| Revocation          | Hard (must wait for expiry or use blocklist) | Easy (delete from store)                    |
| Size                | Larger (hundreds of bytes to KBs)         | Small (typically 32-64 bytes)                  |
| Stateless?          | Yes                                       | No (requires server-side state)                |
| Network overhead    | Larger request headers                    | Requires introspection call to auth server     |
| Best for            | Microservices, stateless APIs             | Traditional web apps, when revocation matters  |

### Stateless Authentication Flow with JWT

```mermaid
sequenceDiagram
    participant Client
    participant AuthService as Auth Service
    participant ServiceA as Service A
    participant ServiceB as Service B

    Client->>AuthService: POST /login (username + password)
    AuthService->>AuthService: Validate credentials
    AuthService->>AuthService: Generate JWT (sign with private key)
    AuthService->>Client: JWT (access token)

    Client->>ServiceA: GET /data (Authorization: Bearer <JWT>)
    ServiceA->>ServiceA: Verify JWT signature (public key)
    ServiceA->>ServiceA: Check exp, iss, aud claims
    ServiceA->>Client: 200 OK + data

    Client->>ServiceB: GET /other (Authorization: Bearer <JWT>)
    ServiceB->>ServiceB: Verify JWT signature (public key)
    ServiceB->>ServiceB: Check exp, iss, aud claims
    ServiceB->>Client: 200 OK + data
```

No service needs to call the auth service to validate the token. Each service independently verifies the JWT using the public key. This is what makes it **stateless**.

### JWT Pitfalls in System Design

- **Do not store sensitive data in the payload.** The payload is base64-encoded, not encrypted. Anyone can decode and read it.
- **Always validate `exp`, `iss`, `aud` claims.** Never trust a JWT without checking these.
- **Short-lived access tokens + refresh tokens.** Access tokens should expire in 5-15 minutes. Use refresh tokens to get new ones.
- **Token revocation is hard.** Consider a short-lived token + blocklist approach or use opaque tokens if immediate revocation is critical.

---

## 4. SSO (Single Sign-On)

Single Sign-On allows a user to authenticate once and gain access to multiple independent applications without logging in again. The user's identity is managed by a central **Identity Provider (IdP)**.

### SAML 2.0 (Security Assertion Markup Language)

SAML is an XML-based standard for exchanging authentication and authorization data between an Identity Provider (IdP) and a Service Provider (SP).

**Key Concepts:**

- **Identity Provider (IdP):** The system that authenticates the user and issues SAML assertions. Examples: Okta, Azure AD, OneLogin.
- **Service Provider (SP):** The application that the user wants to access. It trusts the IdP to authenticate users. Examples: Salesforce, Jira, your internal app.
- **SAML Assertion:** An XML document issued by the IdP containing the user's identity and attributes. Three types:
  - **Authentication Assertion:** Confirms the user was authenticated, when, and how.
  - **Attribute Assertion:** Contains user attributes (email, name, roles).
  - **Authorization Decision Assertion:** States whether the user is authorized for a specific action.

SAML is widely used in enterprise environments for SSO with legacy and SaaS applications.

### OpenID Connect (OIDC)

OIDC is an **identity layer built on top of OAuth 2.0**. While OAuth 2.0 is an authorization framework, OIDC adds authentication.

- Uses the same flows as OAuth 2.0 (authorization code, etc.)
- Adds an **ID Token** (a JWT) that contains user identity information.
- Provides a **/userinfo endpoint** to fetch additional user profile data.
- Uses standard scopes: `openid`, `profile`, `email`, `address`, `phone`.

OIDC is the modern standard for SSO in web and mobile applications.

### SAML vs OIDC Comparison

| Aspect              | SAML 2.0                                 | OpenID Connect (OIDC)                          |
|----------------------|------------------------------------------|------------------------------------------------|
| Format              | XML                                       | JSON (JWT)                                     |
| Transport           | HTTP Redirect, HTTP POST                  | HTTP REST                                      |
| Token/Assertion     | SAML Assertion (XML)                      | ID Token (JWT) + Access Token                  |
| Complexity          | High (XML parsing, signatures)            | Lower (JSON, standard OAuth flows)             |
| Mobile friendly     | Poor (verbose XML, no native support)     | Excellent (lightweight JSON, mobile SDKs)      |
| Use case            | Enterprise SSO, legacy apps               | Modern web apps, mobile apps, APIs             |
| Built on            | Its own protocol                          | OAuth 2.0                                      |
| Discovery           | Metadata XML                              | `.well-known/openid-configuration`             |
| Adoption            | Mature, enterprise-heavy                  | Growing, modern apps                           |

### SSO Flow (SP-Initiated, OIDC-Based)

```mermaid
sequenceDiagram
    participant User
    participant AppA as Application A (SP)
    participant IdP as Identity Provider
    participant AppB as Application B (SP)

    User->>AppA: Access protected resource
    AppA->>AppA: No active session
    AppA->>IdP: Redirect to IdP /authorize
    IdP->>User: Show login page
    User->>IdP: Enter credentials
    IdP->>IdP: Authenticate user, create SSO session
    IdP->>AppA: Redirect with auth code
    AppA->>IdP: Exchange code for ID token + access token
    IdP->>AppA: ID token (JWT) + access token
    AppA->>AppA: Create local session
    AppA->>User: Show protected resource

    Note over User,AppB: Later, user visits Application B

    User->>AppB: Access protected resource
    AppB->>AppB: No active session
    AppB->>IdP: Redirect to IdP /authorize
    IdP->>IdP: SSO session exists, user already authenticated
    IdP->>AppB: Redirect with auth code (no login prompt)
    AppB->>IdP: Exchange code for ID token + access token
    IdP->>AppB: ID token (JWT) + access token
    AppB->>AppB: Create local session
    AppB->>User: Show protected resource
```

The key insight: when the user visits Application B, the IdP recognizes the existing SSO session and skips the login prompt entirely.

---

## 5. Session Management

After a user authenticates, the system must maintain the user's authenticated state across subsequent requests. This is session management.

### Cookie-Based Sessions

1. User logs in with credentials.
2. Server creates a session record (session ID, user ID, expiry) and stores it server-side.
3. Server sends a `Set-Cookie` header with the session ID.
4. Browser automatically sends the cookie with every subsequent request to the same domain.
5. Server looks up the session ID to identify the user.

**Cookie attributes for security:**
- `HttpOnly`: Prevents JavaScript access (mitigates XSS).
- `Secure`: Only sent over HTTPS.
- `SameSite=Strict|Lax`: Controls cross-site sending (mitigates CSRF).
- `Path` and `Domain`: Restrict cookie scope.
- `Max-Age` / `Expires`: Set session duration.

### Token-Based Sessions (JWT)

1. User logs in with credentials.
2. Server generates a JWT containing user identity and claims.
3. Client stores the JWT (in memory, localStorage, or a secure cookie).
4. Client includes the JWT in the `Authorization` header of every request.
5. Server validates the JWT signature and claims -- no server-side lookup needed.

### Session Storage Options

| Storage              | Pros                                      | Cons                                           |
|----------------------|-------------------------------------------|------------------------------------------------|
| In-Memory (app)      | Fastest, simplest                          | Lost on restart, not shared across instances   |
| Redis / Memcached    | Fast, shared across instances, TTL support | Additional infrastructure, network hop         |
| Database (SQL/NoSQL) | Persistent, queryable                      | Slower, requires cleanup of expired sessions   |
| JWT (client-side)    | No server storage, stateless, scalable     | Hard to revoke, larger payload size            |

### Cookie-Based vs Token-Based Comparison

| Aspect              | Cookie-Based Sessions                    | Token-Based (JWT)                              |
|----------------------|------------------------------------------|------------------------------------------------|
| State               | Stateful (server stores session)          | Stateless (token contains everything)          |
| Storage             | Server-side (Redis, DB)                   | Client-side (memory, cookie, localStorage)     |
| Scalability         | Requires shared session store             | Horizontally scalable (no shared state)        |
| Revocation          | Easy (delete session from store)          | Hard (requires blocklist or short expiry)      |
| CSRF vulnerability  | Yes (cookies sent automatically)          | No (if stored outside cookies)                 |
| XSS vulnerability   | Mitigated with HttpOnly cookies           | Risk if stored in localStorage                 |
| Cross-domain        | Limited by cookie domain rules            | Works across domains (bearer token in header)  |
| Mobile support      | Awkward (cookies not native to mobile)    | Natural fit (token in header)                  |
| Best for            | Traditional web apps, same-domain         | SPAs, mobile apps, microservices               |

---

## 6. TLS/SSL

**TLS (Transport Layer Security)** is a cryptographic protocol that provides secure communication over a network. SSL (Secure Sockets Layer) is its predecessor and is now deprecated. When people say "SSL," they usually mean TLS.

TLS provides three guarantees:
1. **Confidentiality:** Data is encrypted; third parties cannot read it.
2. **Integrity:** Data cannot be tampered with in transit without detection.
3. **Authentication:** The server (and optionally the client) proves its identity via certificates.

### TLS Handshake (Simplified - TLS 1.3)

```mermaid
sequenceDiagram
    participant Client
    participant Server

    Client->>Server: ClientHello (supported cipher suites, TLS version, client random, key share)
    Server->>Client: ServerHello (chosen cipher suite, server random, key share)
    Server->>Client: Certificate (server's X.509 certificate)
    Server->>Client: CertificateVerify (signature proving ownership of private key)
    Server->>Client: Finished (encrypted with handshake keys)

    Note over Client,Server: Client verifies certificate chain and signature

    Client->>Server: Finished (encrypted with handshake keys)

    Note over Client,Server: Both derive shared session keys from key shares
    Note over Client,Server: All subsequent data encrypted with session keys

    Client->>Server: Application Data (encrypted)
    Server->>Client: Application Data (encrypted)
```

TLS 1.3 completes the handshake in **1 round trip (1-RTT)**, down from 2-RTT in TLS 1.2. It can even achieve **0-RTT** for resumed connections (with some security trade-offs).

### Certificate Chain of Trust

Certificates are organized in a hierarchy:

1. **Root CA (Certificate Authority):** Self-signed certificate, pre-installed in browsers and operating systems. Examples: DigiCert, Let's Encrypt (ISRG Root).
2. **Intermediate CA:** Signed by the Root CA. Acts as a buffer to protect the root key.
3. **Leaf Certificate (Server Certificate):** Signed by the Intermediate CA. Contains the server's public key and domain name.

Verification process: The client walks up the chain, verifying each certificate's signature against its issuer, until it reaches a trusted root CA.

### mTLS (Mutual TLS)

In standard TLS, only the server presents a certificate. In **mutual TLS**, both the client and the server present certificates and verify each other's identity.

Use cases:
- **Service-to-service communication** in microservices (e.g., within a service mesh like Istio).
- **Zero-trust networks** where every connection is verified.
- **API security** where client identity must be cryptographically verified.

How it differs from standard TLS:
- After the server sends its certificate, the server requests the client's certificate.
- The client sends its certificate and proves it owns the corresponding private key.
- The server verifies the client's certificate against a trusted CA.

---

## 7. Encryption

Encryption transforms readable data (plaintext) into unreadable data (ciphertext) using a key. Only someone with the correct key can decrypt it.

### Encryption at Rest

Protects data stored on disk (databases, file systems, backups).

| Method               | Description                                                     |
|----------------------|-----------------------------------------------------------------|
| AES-256              | Industry-standard symmetric encryption algorithm. 256-bit key. Used by AWS, Google Cloud, Azure for storage encryption. |
| Full Disk Encryption | Encrypts the entire disk (e.g., LUKS on Linux, BitLocker on Windows, FileVault on macOS). |
| Database Encryption  | Transparent Data Encryption (TDE) for SQL databases. Column-level or field-level encryption for sensitive fields. |
| Application-Level    | Encrypt specific fields before writing to the database. Gives fine-grained control but adds complexity. |

### Encryption in Transit

Protects data moving between systems over a network.

- **TLS** is the standard protocol (see Section 6).
- All HTTP traffic should use HTTPS (HTTP over TLS).
- Database connections should use TLS (e.g., `sslmode=require` for PostgreSQL).
- Internal service-to-service communication should also be encrypted (mTLS in service meshes).

### End-to-End Encryption (E2EE)

Data is encrypted on the sender's device and only decrypted on the recipient's device. No intermediary (including the service provider) can read the data.

- Used by: WhatsApp, Signal, iMessage.
- The server only relays encrypted blobs. It cannot decrypt them.
- Requires client-side key management, which adds significant complexity.
- Challenge: key exchange, device verification, multi-device support.

### Key Management

Keys are the crown jewels. If keys are compromised, encryption is worthless.

| Component            | Description                                                     |
|----------------------|-----------------------------------------------------------------|
| KMS (Key Management Service) | Cloud-managed service for key lifecycle (generation, rotation, revocation). Examples: AWS KMS, Google Cloud KMS, Azure Key Vault. |
| HSM (Hardware Security Module) | Dedicated hardware for key storage and cryptographic operations. Keys never leave the HSM in plaintext. FIPS 140-2 certified. |
| Envelope Encryption  | Data is encrypted with a Data Encryption Key (DEK). The DEK is encrypted with a Key Encryption Key (KEK) stored in KMS. Only the encrypted DEK is stored alongside the data. |
| Key Rotation         | Periodically generate new keys and re-encrypt data. Limits the blast radius of a compromised key. |

**Envelope encryption in practice:**
1. Generate a random DEK locally.
2. Encrypt the data with the DEK (fast, local operation).
3. Send the DEK to KMS, which encrypts it with the KEK and returns the encrypted DEK.
4. Store the encrypted data + encrypted DEK together.
5. To decrypt: send encrypted DEK to KMS to get plaintext DEK, then decrypt the data locally.

This approach avoids sending large data volumes to KMS (which has rate limits and latency).

---

## 8. Common Vulnerabilities & Prevention

### CSRF (Cross-Site Request Forgery)

An attacker tricks an authenticated user's browser into making unintended requests to a trusted site. The browser automatically includes cookies, so the server thinks the request is legitimate.

**Example:** User is logged into `bank.com`. User visits a malicious page that contains `<img src="https://bank.com/transfer?to=attacker&amount=10000">`. The browser sends the request with the user's session cookie.

**Prevention:**
- **SameSite cookies:** Set `SameSite=Strict` or `SameSite=Lax` to prevent cookies from being sent with cross-origin requests.
- **CSRF tokens:** Generate a unique, unpredictable token per session (or per request). Include it in forms as a hidden field. Server verifies the token matches.
- **Check `Origin` / `Referer` headers:** Verify the request originates from your domain.
- **Use non-cookie authentication for APIs:** Bearer tokens in headers are not sent automatically, so they are immune to CSRF.

### XSS (Cross-Site Scripting)

An attacker injects malicious scripts into web pages viewed by other users. The script runs in the victim's browser with the same privileges as the legitimate page.

**Types:**
- **Stored XSS:** Malicious script is stored in the database (e.g., a forum post) and served to every user who views it.
- **Reflected XSS:** Malicious script is part of the URL and reflected back in the server's response.
- **DOM-based XSS:** Client-side JavaScript processes untrusted data and inserts it into the DOM.

**Prevention:**
- **Output encoding:** Escape all user-generated content before rendering it in HTML (use context-aware encoding: HTML, JavaScript, URL, CSS).
- **Content Security Policy (CSP):** HTTP header that restricts which scripts can execute. `Content-Security-Policy: script-src 'self'` blocks inline scripts and scripts from other domains.
- **HttpOnly cookies:** Prevent JavaScript from accessing session cookies (blocks `document.cookie` theft).
- **Input validation:** Validate and sanitize user input on the server side. Reject unexpected input.
- **Use templating engines** that auto-escape by default (React, Angular, Jinja2 with autoescape).

### SQL Injection

An attacker manipulates SQL queries by injecting malicious input through application inputs.

**Example:**
```
Input: ' OR '1'='1' --
Query becomes: SELECT * FROM users WHERE username = '' OR '1'='1' --' AND password = '...'
```

This returns all users, bypassing authentication.

**Prevention:**
- **Parameterized queries (prepared statements):** Never concatenate user input into SQL strings. Use placeholders: `SELECT * FROM users WHERE username = ? AND password = ?`.
- **ORM (Object-Relational Mapping):** Use an ORM like SQLAlchemy, Hibernate, or Prisma, which generates parameterized queries by default.
- **Input validation:** Validate data types, lengths, and formats. Reject unexpected characters.
- **Least privilege:** Database accounts used by the application should have minimal permissions (no DROP, no access to system tables).

### SSRF (Server-Side Request Forgery)

An attacker tricks the server into making HTTP requests to unintended destinations, typically internal services or cloud metadata endpoints.

**Example:** An application has a feature to fetch a URL and display a preview. An attacker provides `http://169.254.169.254/latest/meta-data/iam/security-credentials/` to access AWS instance metadata and steal IAM credentials.

**Prevention:**
- **URL allowlists:** Only allow requests to known, trusted domains.
- **Block internal IPs:** Reject requests to private IP ranges (10.x.x.x, 172.16-31.x.x, 192.168.x.x, 127.x.x.x, 169.254.x.x).
- **Use a dedicated HTTP proxy** for outbound requests with strict rules.
- **Disable unnecessary URL schemes:** Block `file://`, `gopher://`, `ftp://`.
- **Cloud metadata protection:** Use IMDSv2 (requires a PUT request with a token), which SSRF via GET requests cannot exploit.

### Vulnerability Summary Table

| Vulnerability | Attack Vector                          | Impact                            | Key Prevention                              |
|---------------|----------------------------------------|-----------------------------------|---------------------------------------------|
| CSRF          | Forged cross-site requests             | Unauthorized actions              | SameSite cookies, CSRF tokens               |
| XSS           | Injected scripts in web pages          | Session hijacking, data theft     | Output encoding, CSP, HttpOnly cookies      |
| SQL Injection | Malicious SQL in user input            | Data breach, data manipulation    | Parameterized queries, ORM                  |
| SSRF          | Server-side requests to internal URLs  | Internal network access, cred theft| URL allowlists, block internal IPs         |
| Broken AuthN  | Credential stuffing, weak passwords    | Account takeover                  | MFA, rate limiting, strong password policy  |
| Broken AuthZ  | IDOR, privilege escalation             | Unauthorized data access          | Server-side authz checks, principle of least privilege |
| Sensitive Data Exposure | Unencrypted storage/transit | Data breach                       | Encryption at rest and in transit, TLS      |

---

## 9. API Security

### Authentication Methods for APIs

| Method            | How It Works                                                    | Security Level | Use Case                          |
|-------------------|-----------------------------------------------------------------|----------------|-----------------------------------|
| API Key           | Static key passed in header or query param                      | Low            | Internal APIs, rate limiting      |
| OAuth 2.0 Bearer Token | Short-lived access token from OAuth flow                  | High           | Third-party API access            |
| mTLS              | Client certificate authenticates the caller                     | Very High      | Service-to-service (zero trust)   |
| HMAC Signature    | Request body + timestamp signed with shared secret              | High           | Webhooks, AWS API (Signature V4) |

**API keys** are not a substitute for proper authentication. They identify the calling application, not the user. They are often used for rate limiting and usage tracking, not for authorization decisions.

### Rate Limiting

Protects APIs from abuse, DDoS attacks, and brute-force attempts.

- **Fixed window:** Count requests in fixed time intervals (e.g., 100 requests per minute).
- **Sliding window:** Smoother rate limiting using a rolling time window.
- **Token bucket:** Allows bursts up to a maximum, then throttles to a steady rate.
- **Leaky bucket:** Processes requests at a constant rate, queuing excess requests.

Return `429 Too Many Requests` with a `Retry-After` header when the limit is exceeded.

Rate limit by: API key, user ID, IP address, or a combination.

### CORS (Cross-Origin Resource Sharing)

Browsers enforce the **Same-Origin Policy**: JavaScript on `app.example.com` cannot make requests to `api.other.com` by default. CORS is a mechanism that allows servers to specify which origins are permitted.

**Key headers:**
- `Access-Control-Allow-Origin`: Which origins can access the API (e.g., `https://app.example.com` or `*`).
- `Access-Control-Allow-Methods`: Which HTTP methods are allowed (e.g., `GET, POST, PUT, DELETE`).
- `Access-Control-Allow-Headers`: Which request headers are allowed (e.g., `Authorization, Content-Type`).
- `Access-Control-Allow-Credentials`: Whether cookies/auth headers are allowed in cross-origin requests.

**Preflight requests:** For non-simple requests (e.g., `PUT` with `Content-Type: application/json`), the browser sends an `OPTIONS` request first. The server responds with the allowed origins, methods, and headers. If allowed, the browser proceeds with the actual request.

**Never use `Access-Control-Allow-Origin: *` with credentials.** This is both insecure and rejected by browsers.

### Input Validation

- **Validate on the server side.** Client-side validation is a UX convenience, not a security measure.
- **Validate data types, lengths, ranges, and formats.** Reject anything that does not match the expected schema.
- **Use schema validation** (e.g., JSON Schema, Zod, Joi) to define and enforce API contracts.
- **Reject unexpected fields** (strict mode) to prevent mass assignment vulnerabilities.
- **Sanitize output,** not just input. Defense in depth -- even if input validation is bypassed, output encoding prevents XSS.

---

## 10. Quick Reference Summary

### Protocol Decision Matrix

| Scenario                                    | Recommended Approach                          |
|---------------------------------------------|-----------------------------------------------|
| User login for a web app                    | OAuth 2.0 Authorization Code + OIDC           |
| User login for a mobile app                 | OAuth 2.0 Authorization Code + PKCE + OIDC    |
| User login for a SPA                        | OAuth 2.0 Authorization Code + PKCE + OIDC    |
| Service-to-service authentication           | OAuth 2.0 Client Credentials or mTLS          |
| Enterprise SSO with legacy apps             | SAML 2.0                                      |
| Enterprise SSO with modern apps             | OIDC                                          |
| Third-party API access delegation           | OAuth 2.0                                     |
| Stateless API authentication                | JWT (short-lived) + refresh tokens             |
| Internal microservice communication         | mTLS (service mesh) or JWT                     |
| Webhook verification                        | HMAC signature                                 |

### Security Checklist for System Design Interviews

**Authentication:**
- Use OAuth 2.0 / OIDC for user authentication.
- Enforce MFA for sensitive operations.
- Use bcrypt/scrypt/Argon2 for password hashing (never MD5 or SHA-1).
- Implement account lockout after failed attempts.

**Authorization:**
- Enforce authorization on the server side, never on the client.
- Use RBAC or ABAC depending on complexity.
- Apply the principle of least privilege.
- Validate authorization for every request, not just at login.

**Tokens and Sessions:**
- Use short-lived access tokens (5-15 minutes).
- Store refresh tokens securely (server-side or secure HttpOnly cookies).
- Rotate refresh tokens on use (one-time tokens).
- Implement token revocation for logout and security events.

**Encryption:**
- Encrypt data at rest (AES-256, cloud KMS).
- Encrypt data in transit (TLS 1.2+ everywhere).
- Use envelope encryption for large data volumes.
- Rotate encryption keys periodically.

**API Security:**
- Rate limit all endpoints.
- Validate all input server-side.
- Use CORS with specific origins (not `*`).
- Log all authentication and authorization events.

**Network Security:**
- Use TLS 1.3 where possible.
- Consider mTLS for internal service communication.
- Place sensitive services behind a VPN or private network.
- Use a WAF (Web Application Firewall) for public-facing endpoints.

### Common Interview Discussion Points

**"How would you handle authentication in a microservices architecture?"**
- Centralized auth service issues JWTs signed with a private key.
- All services validate JWTs using the public key (from a JWKS endpoint).
- An API gateway can handle token validation, rate limiting, and CORS at the edge.
- Use short-lived tokens to limit the blast radius of a compromised token.
- For service-to-service calls, use mTLS or internal JWTs with limited scopes.

**"How would you implement token revocation with JWTs?"**
- JWTs are stateless, so revocation is inherently difficult.
- Approach 1: Keep tokens short-lived (5 minutes) so they naturally expire.
- Approach 2: Maintain a blocklist of revoked token IDs (jti) in Redis. Services check the blocklist before accepting a token.
- Approach 3: Use opaque tokens for scenarios where immediate revocation is critical.
- Trade-off: shorter token lifetime = more refresh requests = higher auth service load.

**"How would you secure data at rest in a multi-tenant system?"**
- Use tenant-specific encryption keys (each tenant's data encrypted with a different DEK).
- Store DEKs encrypted with a master key in KMS (envelope encryption).
- Enforce tenant isolation at the application layer (always include tenant_id in queries).
- Consider separate databases per tenant for the highest isolation.
- Audit access to encryption keys and log all decrypt operations.
