from weekly_team_feedback_tool.home import home


def test_home_returns_project_name():
    assert home() == "Weekly Team Feedback Tool"
