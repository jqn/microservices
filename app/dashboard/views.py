# app/dashboard/views.py

from flask import render_template, request
from flask_login import login_required
import os
import boto3
from . import dashboard
import json
import requests

ec2_resource = boto3.resource(
    'ec2',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
)

token = os.getenv('GITHUB_TOKEN')


@dashboard.route('/dashboard')
@login_required
def user_dashboard():
    """
    Use the filter() method of the instances collection to retrieve
    all running EC2 instances.
    """
    instances = ec2_resource.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    active_ins = []

    for instance in instances:
        active_ins.append({
            "id": instance.id,
            "type": instance.instance_type,
            "dns": instance.public_dns_name,
            "state": instance.state['Name']
        })

    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('dashboard/user_dashboard.html', title="Dashboard", instances=active_ins)


@dashboard.route('/dashboard/github')
@login_required
def dashboard_github():
    query_url = f"https://api.github.com/users/jqn/repos?type=owner&sort=created&direction=desc&per_page=20"

    headers = {'Authorization': f'token {token}',
               'Accept': 'application/vnd.github.v3+json'}

    params = {
        'type': 'all',
        'sort': 'pushed'
    }

    r = requests.get(query_url, headers=headers)
    # print(r)
    # print(r.json())

    repos = []

    for repo in r.json():
        print(repo.keys())
        # repo_url = repo["html_url"]
        # repos.append({"url": repo_url})
        repos.append(repo)
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('dashboard/github_dashboard.html', title="GitHub Dashboard", context=repos)


# admin dashboard view
@ dashboard.route('/admin/dashboard')
@ login_required
def admin_dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('dashboard/admin_dashboard.html', title="Dashboard")
