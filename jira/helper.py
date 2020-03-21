from jira import JIRA


class JiraHelper:

    def __init__(self, user_name, api_token, server):
        self.jira = JIRA(basic_auth=(user_name, api_token), options={"server": server})

    def create_issue(self, test_data):
        issue_key = self.jira.create_issue(fields=test_data)
        return issue_key

    def update_issue_fields(self, issue_key, updated_test_data):
        issue = self.jira.issue(issue_key)
        issue.update(fields=updated_test_data)

    def delete_issue(self, issue_key):
        issue = self.jira.issue(issue_key)
        issue.delete()
