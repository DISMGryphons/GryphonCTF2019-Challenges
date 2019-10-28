# Looks Simple

## Question Text

This web application looks interesting ;)

*The backend uses PostgreSQL*

*Creator - @Jonoans*

### Hints (Optional)
1. `/post/` is vulnerable to SQL injection.

## Setup Guide
1. Enter `service` directory
2. `docker-compose up -d`

## Solution
1. Find the SQL injection vector.
2. Testing the vector will allow user to understand the output is not sanitized.
3. User must also understand how to bypass CSP protections (unsafe-eval is allowed, though Angular can run without eval if `ng-csp="no-unsafe-eval"` specified).
4. Run `solution.py` to inject JavaScript payload.

### Flag
`GCTF{4M4Z1NG_SQ1_X55_W0T}`

## Recommended Reads
* https://stackoverflow.com/questions/44813386/mysqls-hex-and-unhex-equivalent-in-postgres
* https://www.owasp.org/images/4/46/OWASPLondon20170727_AngularJS.pdf