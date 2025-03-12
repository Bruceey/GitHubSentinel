import datetime
import requests
import os

class GitHubClient:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': f'Bearer {self.token}'}
    
    def fetch_updates(self, repo, since=None, until=None):
        # 获取特定 repo 的更新（commits, issues, pull requests）
        # 键commits、issues、pull_requests对应的值都是原始数据(类型是dict)，需要进一步处理
        updates = {
            'commits': self.fetch_commits(repo),
            'issues': self.fetch_issues(repo),
            'pull_requests': self.fetch_pull_requests(repo)
        }
        return updates

    def fetch_commits(self, repo, since=None, until=None):
        url = f'https://api.github.com/repos/{repo}/commits'
        params = {}
        if since:
            params['since'] = since
        if until:
            params['until'] = until

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def fetch_issues(self, repo, since=None, until=None):
        url = f'https://api.github.com/repos/{repo}/issues'
        params = {
            'state': 'closed',
            'since': since,
            'until': until
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def fetch_pull_requests(self, repo, since=None, until=None):
        url = f'https://api.github.com/repos/{repo}/pulls'
        params = {
            'state': 'closed',
            'since': since,
            'until': until
        }
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def export_daily_progress(self, repo):
        today = datetime.datetime.now().date().isoformat()
        updates = self.fetch_updates(repo, since=today)
        
        repo_dir = os.path.join('daily_progress', repo.replace("/", "_"))
        os.makedirs(repo_dir, exist_ok=True)
        
        file_path = os.path.join(repo_dir, f'{today}.md')
        with open(file_path, 'w') as file:
            file.write(f"# Daily Progress for {repo} ({today})\n\n")
            file.write("\n## Issues Closed Today\n")
            for issue in updates['issues']:
                file.write(f"- {issue['title']} #{issue['number']}\n")
            file.write("\n## Pull Requests Merged Today\n")
            for pr in updates['pull_requests']:
                file.write(f"- {pr['title']} #{pr['number']}\n")
        
        print(f"Exported daily progress to {file_path}")
        return file_path

    def export_time_range_progress(self, repo, days):
        today = datetime.datetime.now().date()
        since = (today - datetime.timedelta(days=days)).isoformat()
        until = today.isoformat()
        
        updates = self.fetch_updates(repo, since=since, until=until)
        
        repo_dir = os.path.join('daily_progress', repo.replace("/", "_"))
        os.makedirs(repo_dir, exist_ok=True)
        
        date_str = f"last_{days}_days"
        file_path = os.path.join(repo_dir, f'{date_str}.md')
        with open(file_path, 'w') as file:
            file.write(f"# Progress for {repo} (Last {days} Days)\n\n")
            file.write(f"\n## Issues Closed in the Last {days} Days\n")
            for issue in updates['issues']:
                file.write(f"- {issue['title']} #{issue['number']}\n")
            file.write(f"\n## Pull Requests Merged in the Last {days} Days\n")
            for pr in updates['pull_requests']:
                file.write(f"- {pr['title']} #{pr['number']}\n")
        
        print(f"Exported time-range progress to {file_path}")
        return file_path
    

if __name__ == '__main__':
    # import os
    # token = os.getenv('GITHUB_TOKEN')
    # client = GitHubClient(token)
    # repo = 'langchain-ai/langchain'
    # updates = client.fetch_updates(repo)
    # print(updates)
    today = datetime.datetime.now().date().isoformat()
    print(today)