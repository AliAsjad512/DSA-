import os
import subprocess
import argparse
import shutil
from pathlib import Path

class GitAutomation:
    def __init__(self, repo_path=None):
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()

    def clone(self, url, branch='main'):
        """Clone a repository"""
        try:
            subprocess.run(['git', 'clone', '-b', branch, url, str(self.repo_path)], check=True)
            print(f"✅ Cloned {url} to {self.repo_path}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Clone failed: {e}")

    def commit(self, message, files=None):
        """Commit changes"""
        if not self.repo_path.exists():
            print("Repository does not exist")
            return
        os.chdir(self.repo_path)
        if files:
            subprocess.run(['git', 'add'] + files, check=True)
        else:
            subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        print(f"✅ Committed with message: {message}")
    def push(self, remote='origin', branch='main'):
        """Push changes"""
        os.chdir(self.repo_path)
        subprocess.run(['git', 'push', remote, branch], check=True)
        print(f"✅ Pushed to {remote}/{branch}")
    def pull(self, remote='origin', branch='main'):
        """Pull latest changes"""
        os.chdir(self.repo_path)
        subprocess.run(['git', 'pull', remote, branch], check=True)
        print(f"✅ Pulled latest from {remote}/{branch}")

    def tag(self, tag_name, message=None):
        """Create a tag"""
        os.chdir(self.repo_path)
        cmd = ['git', 'tag', tag_name]
        if message:
            cmd = ['git', 'tag', '-a', tag_name, '-m', message]
        subprocess.run(cmd, check=True)
        print(f"✅ Created tag {tag_name}")
    def push_tags(self):
        """Push tags to remote"""
        os.chdir(self.repo_path)
        subprocess.run(['git', 'push', '--tags'], check=True)
        print("✅ Tags pushed")

    def delete_repo(self):
        """Delete local repository"""
        shutil.rmtree(self.repo_path)
        print(f"✅ Deleted {self.repo_path}")

        if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Git Automation')
    parser.add_argument('--path', help='Repository path', default='.')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Clone
    clone_parser = subparsers.add_parser('clone')
    clone_parser.add_argument('url', help='Repository URL')
    clone_parser.add_argument('--branch', default='main')

    # Commit
    commit_parser = subparsers.add_parser('commit')
    commit_parser.add_argument('message', help='Commit message')
    commit_parser.add_argument('--files', nargs='+', help='Files to commit')

    # Push/Pull
    push_parser = subparsers.add_parser('push')
    push_parser.add_argument('--remote', default='origin')
    push_parser.add_argument('--branch', default='main')
    pull_parser = subparsers.add_parser('pull')
    pull_parser.add_argument('--remote', default='origin')
    pull_parser.add_argument('--branch', default='main')

    # Tag
    tag_parser = subparsers.add_parser('tag')
    tag_parser.add_argument('tag_name')
    tag_parser.add_argument('--message')

    # Other
    subparsers.add_parser('push-tags')
    subparsers.add_parser('delete')

    args = parser.parse_args()

    git = GitAutomation(args.path)
    if args.command == 'clone':
        git.clone(args.url, args.branch)
    elif args.command == 'commit':
        git.commit(args.message, args.files)
    elif args.command == 'push':
        git.push(args.remote, args.branch)
    elif args.command == 'pull':
        git.pull(args.remote, args.branch)
    elif args.command == 'tag':
        git.tag(args.tag_name, args.message)
    elif args.command == 'push-tags':
        git.push_tags()
    elif args.command == 'delete':
        git.delete_repo()

