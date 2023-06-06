import time

import requests

json = {
    "changedBu": False,
    "pm_uids": "",
    "changeType": False,
    "title": "{}我是一个标题".format(time.strftime('%m%d%H%M%S', time.localtime())),
    "scene": "<p data-id=\"p838747a-gUJWb187\">3<cursor /></p><p data-id=\"p838747a-Jgjc9hcQ\">3</p>",
    "resolve_for": "<p data-id=\"p838747a-BbXhbnbj\">3<cursor />33</p><p data-id=\"p838747a-hh27MJdM\">333333333</p>",
    "description": "<p data-id=\"p838747a-5gGXUHMd\">333</p><p data-id=\"p838747a-rqI2Oea3\">333333333333333<cursor /></p>",
    "parent_team_ids": 22430,
    "team_module_id": 22431,
    "org_code": "rdcompcyprodone",
    "bu": "cyjg",
    "type": 1,
    "expected_finish_at": 0,
    "files": [],
    "custom_fields": [
        {
            "field_num": "deliver_effect"
        },
        {
            "field_num": "more_affect"
        }
    ]
}
head = {"Content-Type": "application/json;charset=UTF-8",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdmF0YXIiOiJodHRwczovL3dld29yay5xcGljLmNuL3d3cGljLzkzMzYzMV9PckEybEo0Z1RaaVB3VzFfMTY3NzIyMzgyOC8wIiwiZG9tYWluX2FjY291bnQiOiJjYWliYjAxIiwiZXhwIjoxNjg2MzAzNzIwLCJpZCI6NjU4NzQsIm9yaWdfaWF0IjoxNjg1Njk4OTIwLCJ6aF9uYW1lIjoi6JSh54Wy5aChIn0.Rt83TSiXbfmDP8nyxkNBww3xHhm1ZW_2Dcc2NEVg1So"}
# for i in range(10):
#     rep = requests.post(url='https://process-test.myscrm.cn/cm-rep/api/feedback-online/create',
#                     json=json,
#                     headers=head)
#     print(rep.json())
