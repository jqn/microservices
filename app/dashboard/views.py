# app/dashboard/views.py

from flask import render_template
from flask_login import login_required

from . import dashboard

import os
import boto3


ec2_resource = boto3.resource(
    'ec2',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID", ""),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY", ""),
    region_name=os.getenv("AWS_DEFAULT_REGION", "us-east-1")
)


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
def admin_dashboard_github():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('dashboard/github_dashboard.html', title="GitHub Dashboard")

# admin dashboard view


@dashboard.route('/admin/dashboard')
@login_required
def admin_dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('dashboard/admin_dashboard.html', title="Dashboard")
