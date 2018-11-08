from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["zCV1AnxDSugArgnp5s/yGcZvPsMz4/kEyE1k/uAYFaMEosqJLnO4/IkSvkpxEUG972gQbIZgAhQYBTxWmftD76LIYp3jsJTwXaszcF5+YU/BGaWF3Seprjamt6w5osBaTTJgr62FX/tL6yi+WWTtGgdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["0e13675cc159d624910c6f468619a61b"]

line_bot_api = LineBotApi(zCV1AnxDSugArgnp5s/yGcZvPsMz4/kEyE1k/uAYFaMEosqJLnO4/IkSvkpxEUG972gQbIZgAhQYBTxWmftD76LIYp3jsJTwXaszcF5+YU/BGaWF3Seprjamt6w5osBaTTJgr62FX/tL6yi+WWTtGgdB04t89/1O/w1cDnyilFU=)
handler = WebhookHandler(0e13675cc159d624910c6f468619a61b)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
