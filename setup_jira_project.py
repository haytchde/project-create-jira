import requests

# Define constants here for test purpose
JIRA_URL = 'https://your-domain.atlassian.net'
API_TOKEN = 'your_api_token_here'
PROJECT_NAME = 'Test Project'
PROJECT_KEY = 'TP'

# Function to create a new Jira project
def create_jira_project(jira_url, api_token, project_name, project_key):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    project_data = {
        'name': project_name,
        'key': project_key,
        'projectTypeKey': 'business'
    }
    response = requests.post(f'{jira_url}/rest/api/3/project', headers=headers, json=project_data)
    if response.status_code == 201:
        print('Project created successfully')
    else:
        print('Failed to create project:', response.text)

# Function to create issue types
def create_issue_type(jira_url, api_token, issue_type_name, description):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    issue_type_data = {
        'name': issue_type_name,
        'description': description,
        'iconUrl': 'https://example.com/icon.png'
    }
    response = requests.post(f'{jira_url}/rest/api/3/issuetype', headers=headers, json=issue_type_data)
    if response.status_code == 201:
        print(f'Issue type {issue_type_name} created successfully')
    else:
        print(f'Failed to create issue type {issue_type_name}:', response.text)

# Function to create fields
def create_custom_field(jira_url, api_token, field_name, field_type):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    field_data = {
        'name': field_name,
        'description': f'{field_name} field',
        'type': field_type
    }
    response = requests.post(f'{jira_url}/rest/api/3/field', headers=headers, json=field_data)
    if response.status_code == 201:
        print(f'Field {field_name} created successfully')
    else:
        print(f'Failed to create field {field_name}:', response.text)

# Function to create workflow schemes
def create_workflow_scheme(jira_url, api_token, scheme_name, issue_type_mapping):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    scheme_data = {
        'name': scheme_name,
        'description': f'{scheme_name} workflow scheme',
        'issueTypeMappings': issue_type_mapping
    }
    response = requests.post(f'{jira_url}/rest/api/2/workflowscheme', headers=headers, json=scheme_data)
    if response.status_code == 201:
        print(f'Workflow scheme {scheme_name} created successfully')
    else:
        print(f'Failed to create workflow scheme {scheme_name}:', response.text)

# Example usage of the functions
def example_usage():
    create_jira_project(JIRA_URL, API_TOKEN, PROJECT_NAME, PROJECT_KEY)
    create_issue_type(JIRA_URL, API_TOKEN, 'Marketing Request', 'A request for marketing assets')
    create_issue_type(JIRA_URL, API_TOKEN, 'Asset', 'An asset for marketing use')
    create_custom_field(JIRA_URL, API_TOKEN, 'Marketing Asset', 'string')
    create_custom_field(JIRA_URL, API_TOKEN, 'Asset Type', 'string')
    issue_type_mapping = {
        '10000': 'scrum workflow'
    }
    create_workflow_scheme(JIRA_URL, API_TOKEN, 'Marketing Workflow Scheme', issue_type_mapping)

example_usage()