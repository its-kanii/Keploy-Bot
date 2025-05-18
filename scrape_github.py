import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


GITHUB_REPO = "keploy/keploy"
GITHUB_TOKEN = os.getenv("your github token")  # Optional: export this in your terminal

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}" if GITHUB_TOKEN else "",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_issues(state="all", limit=100):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    params = {"state": state, "per_page": 100}
    all_issues = []
    page = 1

    while len(all_issues) < limit:
        params["page"] = page
        res = requests.get(url, headers=HEADERS, params=params)
        if res.status_code != 200:
            print(f"Error: {res.status_code}")
            break
        issues = res.json()
        if not issues:
            break
        for issue in issues:
            if "pull_request" not in issue:  # Skip PRs if fetching issues only
                all_issues.append({
                    "title": issue["title"],
                    "body": issue["body"],
                    "url": issue["html_url"]
                })
        page += 1
    return all_issues

def save_issues(issues, out_path="./data/github_issues/issues.json"):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(issues, f, indent=2)
    print(f"✅ Saved {len(issues)} issues to {out_path}")

if __name__ == "__main__":
    issues = fetch_issues(state="all", limit=200)
    save_issues(issues)
