from http.client import HTTPException
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
import json
import os
import sentry_sdk
import logging
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


def strip_sensitive_data(event, hint):
    if "exc_info" in hint:
        instance = hint['exc_info'][1]
        if isinstance(instance, HTTPException) and instance.code < 500:
            return None
    return event


sentry_logging = LoggingIntegration(
    level=logging.INFO,  # Capture info and above as breadcrumbs
    event_level=logging.WARNING  # Send errors as events
)

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    before_send=strip_sensitive_data,
    integrations=[FlaskIntegration(), sentry_logging]
)


app = Flask(__name__)


@app.route("/webhook", methods=['POST'])
def webhook():
    line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_TOKEN'))
    handler = WebhookHandler(os.environ.get('LINE_CHANNEL_SECRET_KEY'))

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    event = json.loads(body)
    print(event)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print(
            "Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    token = event['events'][0]['replyToken']
    if token == "00000000000000000000000000000000":
        pass
    else:
        line_bot_api.reply_message(token, TextSendMessage(
                text=event['events'][0]['message']['text']))
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
