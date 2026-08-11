class GitHubClient:
    """GitHub API와 통신하는 클라이언트입니다."""

    def __init__(self, token: str, owner: str, repo: str) -> None:
        self.token = token
        self.owner = owner
        self.repo = repo

    @property
    def issues_url(self) -> str:
        """이슈 생성에 사용할 GitHub API 주소를 반환합니다."""
        return f"https://api.github.com/repos/{self.owner}/{self.repo}/issues"

    def create_issue(self, title: str, body: str) -> dict:
        """GitHub 이슈를 생성합니다."""
        raise NotImplementedError("GitHub API 호출 코드는 다음 단계에서 작성합니다.")
