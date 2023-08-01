import json
import urllib.request

def post_slack(argStr):
    message = argStr
    send_data = {
        "channel": "{SLACK_CHANNEL_NAME}", 
    	"username": "{user_name|service_name}", 
    	"text": "real alarm msg send {SLACK_CHANNEL_NAME}."  + argStr + json.dumps(event)
    }
    send_text = json.dumps(send_data)
    request = urllib.request.Request(
        "https://hooks.slack.com/services/{CUMSTEMED YOUR LINK}", 
        data=send_text.encode('utf-8'), 
    )

    with urllib.request.urlopen(request) as response:
        slack_message = response.read()

def lambda_handler(event, context):
    post_slack("This alarm generated from AWS Lambda to Slack.")

# Welcome! Follow these steps.  github@coding-haniii
# 1. add APP <Incoming WebHooks> on your slack
# 2. create <IAM> in your AWS console "Role:AWSLambdaBasicExecutionRole"
# 3. create <Lambda> function in your AWS console "Python 3.7"
# smaple test : same curl transaction
# curl -X POST --data-urlencode "payload={\"channel\": \"#awsAlarm\", \"username\": \"coding-haniii\", \"text\": \"real alarm msg send to slack channel.\", \"icon_emoji\": \":ghost:\"}" https://hooks.slack.com/services/{CUMSTEMED YOUR LINK}
# icon_emoji : You can change icon in your slack setting
