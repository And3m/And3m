#!/usr/bin/env python3
"""
Script to fetch repositories worked on yesterday and update README.md
"""

import os
import sys
import json
import re
from datetime import datetime, timedelta
from typing import List, Set
import requests

def get_yesterday_date():
    """Get yesterday's date in ISO format"""
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime('%Y-%m-%d')

def fetch_user_events(username: str, token: str) -> List[dict]:
    """Fetch recent events for a GitHub user"""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    url = f'https://api.github.com/users/{username}/events'
    params = {'per_page': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")
        return []

def filter_yesterday_repos(events: List[dict], target_date: str) -> Set[str]:
    """Filter events to get unique repositories worked on yesterday"""
    yesterday_repos = set()
    
    for event in events:
        event_date = event.get('created_at', '')[:10]  # Extract YYYY-MM-DD
        
        if event_date == target_date:
            repo_name = event.get('repo', {}).get('name', '')
            event_type = event.get('type', '')
            
            # Include relevant event types that indicate "working" on a repository
            relevant_events = {
                'PushEvent', 'PullRequestEvent', 'PullRequestReviewEvent',
                'IssuesEvent', 'CommitCommentEvent', 'CreateEvent'
            }
            
            if repo_name and event_type in relevant_events:
                yesterday_repos.add(repo_name)
    
    return yesterday_repos

def format_repo_list(repos: Set[str]) -> str:
    """Format the repository list for README"""
    if not repos:
        return "🔹 No repositories worked on yesterday"
    
    formatted_repos = []
    for repo in sorted(repos):
        repo_link = f"https://github.com/{repo}"
        formatted_repos.append(f"🔹 [{repo}]({repo_link})")
    
    return '\n'.join(formatted_repos)

def update_readme(readme_path: str, new_content: str) -> bool:
    """Update the README.md file with new yesterday repos content"""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the section to replace
        pattern = r'<!--START_SECTION:yesterday_repos-->.*?<!--END_SECTION:yesterday_repos-->'
        replacement = f'<!--START_SECTION:yesterday_repos-->\n{new_content}\n<!--END_SECTION:yesterday_repos-->'
        
        if re.search(pattern, content, re.DOTALL):
            updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print("✅ README.md updated successfully")
            return True
        else:
            print("❌ Could not find yesterday_repos section in README.md")
            return False
            
    except Exception as e:
        print(f"❌ Error updating README.md: {e}")
        return False

def main():
    """Main function"""
    # Get environment variables
    github_token = os.getenv('GITHUB_TOKEN')
    github_username = os.getenv('GITHUB_ACTOR', 'And3m')
    readme_path = 'README.md'
    
    if not github_token:
        print("❌ GITHUB_TOKEN environment variable is required")
        sys.exit(1)
    
    print(f"🔍 Fetching events for user: {github_username}")
    
    # Get yesterday's date
    yesterday = get_yesterday_date()
    print(f"📅 Looking for repositories worked on: {yesterday}")
    
    # Fetch user events
    events = fetch_user_events(github_username, github_token)
    
    if not events:
        print("❌ No events found")
        sys.exit(1)
    
    print(f"📊 Found {len(events)} recent events")
    
    # Filter for yesterday's repositories
    yesterday_repos = filter_yesterday_repos(events, yesterday)
    
    print(f"📂 Found {len(yesterday_repos)} repositories worked on yesterday")
    for repo in sorted(yesterday_repos):
        print(f"   - {repo}")
    
    # Format content for README
    formatted_content = format_repo_list(yesterday_repos)
    
    # Update README
    if update_readme(readme_path, formatted_content):
        print("🎉 Successfully updated README with yesterday's repositories!")
    else:
        print("❌ Failed to update README")
        sys.exit(1)

if __name__ == '__main__':
    main()