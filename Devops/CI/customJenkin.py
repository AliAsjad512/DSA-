import jenkins
import yaml
import argparse
import os
from pathlib import Path

class JenkinsJobBuilder:
    def __init__(self, url, username, password):
        self.server = jenkins.Jenkins(url, username=username, password=password)
    def create_pipeline_job(self, job_name, repo_url, branch='main', script_path='Jenkinsfile'):
        """Create a multibranch pipeline job"""
        job_config = f"""<?xml version='1.1' encoding='UTF-8'?>
<org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject plugin="workflow-multibranch@2.22">
  <properties/>
  <folderViews class="jenkins.branch.MultiBranchProjectViewHolder" reference="../../.."/>
  <healthMetrics>
    <com.cloudbees.hudson.plugins.folder.health.WorstChildHealthMetric/>
  </healthMetrics>
  <icon class="jenkins.branch.MetadataActionFolderIcon"/>
  <orphanedItemStrategy class="com.cloudbees.hudson.plugins.folder.computed.DefaultOrphanedItemStrategy"/>
  <triggers>
    <com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger>
      <spec>H/5 * * * *</spec>
      <interval>300000</interval>
    </com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger>
  </triggers>
  <sources class="jenkins.branch.MultiBranchProject$BranchSourceList">
    <data>
      <jenkins.branch.BranchSource>
        <source class="jenkins.plugins.git.GitSCMSource">
          <id>{job_name}</id>
          <remote>{repo_url}</remote>
          <credentialsId>github-credentials</credentialsId>
          <traits>
            <jenkins.plugins.git.traits.BranchDiscoveryTrait/>
            <jenkins.plugins.git.traits.CloneOptionTrait>
              <extension class="jenkins.plugins.git.CloneOption">
                <shallow>true</shallow>
                <noTags>false</noTags>
                <reference/>
                <depth>1</depth>
                <honorRefspec>false</honorRefspec>
              </extension>
            </jenkins.plugins.git.traits.CloneOptionTrait>
          </traits>
        </source>
        <strategy class="jenkins.branch.DefaultBranchPropertyStrategy">
          <properties class="empty-list"/>
        </strategy>
      </jenkins.branch.BranchSource>
    </data>
  </sources>
  <factory class="org.jenkinsci.plugins.workflow.multibranch.WorkflowBranchProjectFactory">
    <scriptPath>{script_path}</scriptPath>
  </factory>
</org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject>"""
        self.server.create_job(job_name, job_config)
        print(f"✅ Created pipeline job: {job_name}")

def create_freestyle_job(self, job_name, build_steps):
        """Create freestyle job with shell commands"""
        steps_xml = ""
        for step in build_steps:
            steps_xml += f"""
            <hudson.tasks.Shell>
              <command>{step}</command>
            </hudson.tasks.Shell>"""
        job_config = f"""<?xml version='1.1' encoding='UTF-8'?>
<project>
  <builders>{steps_xml}
  </builders>
  <publishers/>
  <buildWrappers/>
</project>"""
        self.server.create_job(job_name, job_config)
        print(f"✅ Created freestyle job: {job_name}")


def delete_job(self, job_name):
        self.server.delete_job(job_name)
        print(f"🗑️ Deleted job: {job_name}")

