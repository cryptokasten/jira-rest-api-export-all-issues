import json
import requests

URL = "https://admin:password@jira.example.com/"
PROJECT_ID = "HSP"

url = "%s/rest/api/2/search" % URL
data = {
    "jql": "project = %s" % PROJECT_ID,
    "startAt": 0,
    "maxResults": 10000000,
    "fields": [
        "summary",
	"status",
	"assignee",
    ]
}
headers = {"content-type": "application/json"}
r = requests.post(url, json=data, headers=headers)
r.status_code

fn = "data/issues_%s.json" % PROJECT_ID
f = open(fn, "wt")
f.write(json.dumps(r.json(), indent=2))
f.close()
