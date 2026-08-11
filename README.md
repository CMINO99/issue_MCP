# Issue MCP

GitHub Issue 생성을 자동화하기 위한 MCP Server 프로젝트입니다.

## Goal

Coding Agent가 MCP Tool을 사용하여 GitHub Issue를 생성할 수 있도록 합니다.

전체 흐름은 다음과 같습니다.

Codex / Agent
→ MCP Server
→ create_issue Tool
→ GitHub REST API
→ GitHub Issue

## Features

현재 개발 예정 기능:

- [ ] GitHub Issue 생성
- [ ] GitHub Issue 조회
- [ ] GitHub Issue 검색
- [ ] Issue Template 적용
- [ ] Label 자동화
- [ ] 중복 Issue 검사

## Project Structure

```text
issue-mcp/
├── pyproject.toml
├── README.md
├── .gitignore
├── .env.example
└── src/
    └── issue_mcp/
        ├── __init__.py
        ├── server.py
        ├── tools/
        │   ├── __init__.py
        │   └── create_issue.py
        └── github/
            ├── __init__.py
            └── client.py