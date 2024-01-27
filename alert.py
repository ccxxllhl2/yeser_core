import requests

class Teams:
    def __init__(self):
        self.token = "https://f1hk.webhook.office.com/webhookb2/db263cf5-01b0-4b54-9274-beb8b234b282@99f46155-102b-48b4-b7fc-2ce51c500b5e/IncomingWebhook/d7a70939a5284e34a7e3d342d7048e06/30778d1a-5377-4a17-bb7a-907ba351b59c"

    def send_msg(self, msg):
        msg_header = {"Content-Type": "application/json"}
        response = requests.post(self.token, headers=msg_header, json={'text': msg})
        if not response.ok:
            print(f"Teams alert sending error: {response.text}")