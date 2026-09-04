from weekly_team_feedback_tool.db import Session
from weekly_team_feedback_tool.models import Project, ProjectMember, Role, User


def seed() -> None:
    with Session() as session:
        facilitator = User(email="facilitator@example.com", password_hash="not-a-real-hash")
        member = User(email="member@example.com", password_hash="not-a-real-hash")
        project = Project(name="Sample Project")

        session.add_all([facilitator, member, project])
        session.flush()

        session.add_all(
            [
                ProjectMember(user=facilitator, project=project, role=Role.facilitator),
                ProjectMember(user=member, project=project, role=Role.team_member),
            ]
        )
        session.commit()


if __name__ == "__main__":
    seed()
