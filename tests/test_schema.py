import uuid

import pytest
from sqlalchemy import text
from sqlalchemy.exc import DataError, IntegrityError

from weekly_team_feedback_tool.models import Project, ProjectMember, Role, User


def make_user(db_session, email="user@example.com"):
    user = User(email=email, password_hash="hash")
    db_session.add(user)
    db_session.flush()
    return user


def make_project(db_session, name="Project"):
    project = Project(name=name)
    db_session.add(project)
    db_session.flush()
    return project


def test_can_create_user_project_and_membership(db_session):
    user = make_user(db_session)
    project = make_project(db_session)
    membership = ProjectMember(user=user, project=project, role=Role.facilitator)
    db_session.add(membership)
    db_session.commit()

    assert membership.id is not None
    assert membership.role == Role.facilitator


def test_email_must_be_unique(db_session):
    make_user(db_session, email="dup@example.com")
    db_session.commit()

    db_session.add(User(email="dup@example.com", password_hash="hash"))
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_same_user_cannot_join_same_project_twice(db_session):
    user = make_user(db_session)
    project = make_project(db_session)
    db_session.add(ProjectMember(user=user, project=project, role=Role.team_member))
    db_session.commit()

    db_session.add(ProjectMember(user=user, project=project, role=Role.facilitator))
    with pytest.raises(IntegrityError):
        db_session.commit()


def test_user_can_belong_to_multiple_projects(db_session):
    user = make_user(db_session)
    project_a = make_project(db_session, name="A")
    project_b = make_project(db_session, name="B")
    db_session.add_all(
        [
            ProjectMember(user=user, project=project_a, role=Role.facilitator),
            ProjectMember(user=user, project=project_b, role=Role.team_member),
        ]
    )
    db_session.commit()

    assert len(user.memberships) == 2


def test_role_is_constrained_to_known_values(db_session):
    user = make_user(db_session)
    project = make_project(db_session)
    db_session.commit()

    with pytest.raises(DataError):
        db_session.execute(
            text(
                "insert into project_members (id, user_id, project_id, role) "
                "values (:id, :user_id, :project_id, 'owner')"
            ),
            {"id": uuid.uuid4(), "user_id": user.id, "project_id": project.id},
        )
        db_session.commit()
