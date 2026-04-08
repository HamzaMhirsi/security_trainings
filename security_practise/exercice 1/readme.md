# Exercise 1 - Security Log Pipeline

## Goal
Build a small pipeline that:
- collects logs from an API or web page
- extracts useful security fields
- filters suspicious events
- normalizes them
- sends them into a simple security log system file

You will do part in Bash and part in Python.

## Scenario
You are collecting logs from a public endpoint or an internal web page that returns JSON events.
Your mission is to turn this raw data into a security log stream.

## What You Need To Create
You will create the exercise solution files in this directory yourself.

### Part 1: Bash
Create `collect_logs.sh`.

Expected behavior:
1. Fetch logs from an endpoint like `http://localhost:8000/logs` using `curl`.
2. Save raw logs to `raw_logs.json`.
3. Filter suspicious entries where:
   - status is `401`, `403`, or `500`
   - OR path contains `login`, `admin`, or `upload`
4. Append filtered events to `security_events.jsonl`.
5. Print top offending IPs.

Suggested tools: `curl`, `jq`, `grep`, `sort`, `uniq`, shell redirection/appending.

Improvement tasks:
1. Prevent duplicate entries.
2. Add a timestamp when collection ran.
3. Rotate output file if larger than 10 MB.
4. Count failed logins per IP.
5. Trigger an alert if one IP has more than 5 failed logins.

### Part 2: Python
Create `log_pipeline.py`.

Expected behavior:
1. Fetch logs from an API or read from an HTML page.
2. Parse events.
3. Normalize event structure.
4. Score suspicious events.
5. Write results to `normalized_security_logs.jsonl` (JSON Lines format).

Suggested libraries: `requests`, `json`, `beautifulsoup4`.

## Risk Scoring Rules
For each event, compute `risk_score` with these rules:
- `401` or `403` -> `+3`
- `500` -> `+2`
- path contains `admin` -> `+4`
- path contains `login` -> `+2`
- message contains `failed` -> `+3`
- repeated IP more than 3 times -> `+5`

## Output Of This Exercise
All files produced in this folder are considered the exercise solution.
A separate `solution.md` will be added later.
