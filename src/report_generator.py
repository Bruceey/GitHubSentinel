# src/report_generator.py

import os
from datetime import date


class ReportGenerator:
    """负责导出每日进展和生成每日报告。"""
    def __init__(self, llm):
        self.llm = llm

    def export_daily_progress(self, repo, updates):
        repo_dir = os.path.join('daily_progress', repo.replace("/", "_"))
        os.makedirs(repo_dir, exist_ok=True)
        
        file_path = os.path.join(repo_dir, f'{date.today()}.md')
        with open(file_path, 'w') as file:
            file.write(f"# Daily Progress for {repo} ({date.today()})\n\n")
            file.write("\n## Issues\n")
            for issue in updates['issues']:
                file.write(f"- {issue['title']} #{issue['number']}\n")
            file.write("\n## Pull Requests\n")
            for pr in updates['pull_requests']:
                file.write(f"- {pr['title']} #{pr['number']}\n")
        print(f"Exported daily progress to {file_path}")
        return file_path

    def export_time_range_progress(self, repo, updates, days):
        repo_dir = os.path.join('daily_progress', repo.replace("/", "_"))
        os.makedirs(repo_dir, exist_ok=True)

        date_str = f"last_{days}_days"
        file_path = os.path.join(repo_dir, f'{date_str}.md')
        with open(file_path, 'w') as file:
            file.write(f"# Progress for {repo} (Last {days} Days)\n\n")
            file.write("\n## Issues Closed in the Last {days} Days\n")
            for issue in updates['issues']:
                file.write(f"- {issue['title']} #{issue['number']}\n")
            file.write("\n## Pull Requests Merged in the Last {days} Days\n")
            for pr in updates['pull_requests']:
                file.write(f"- {pr['title']} #{pr['number']}\n")
        print(f"Exported time range progress to {file_path}")
        return file_path

    def generate_daily_report(self, markdown_file_path):
        with open(markdown_file_path, 'r') as file:
            markdown_content = file.read()

        report = self.llm.generate_daily_report(markdown_content)

        report_file_path = os.path.splitext(markdown_file_path)[0] + "_report.md"
        with open(report_file_path, 'w+') as report_file:
            report_file.write(report)

        print(f"Generated report saved to {report_file_path}")

    def generate_time_range_report(self, markdown_file_path, days):
        with open(markdown_file_path, 'r') as file:
            markdown_content = file.read()

        report = self.llm.generate_time_range_report(markdown_content)

        report_file_path = os.path.splitext(markdown_file_path)[0] + f"_report.md"
        with open(report_file_path, 'w+') as report_file:
            report_file.write(report)

        print(f"Generated report saved to {report_file_path}")