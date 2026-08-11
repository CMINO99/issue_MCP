from mcp.server import MCPServer


mcp = MCPServer("Issue MCP")


@mcp.tool()
def create_issue(title: str, body: str, todos: list[str]) -> str:
    """GitHub 이슈를 생성합니다."""
    todo_text = "\n".join(f"- [ ] {todo}" for todo in todos)

    return (
        f"제목: {title}\n\n"
        f"내용: {body}\n\n"
        f"할 일:\n{todo_text}"
    )


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
