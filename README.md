# aws-sentry-flask-example

Welcome here!

This is base on [aws-line-echo-bot](https://github.com/louis70109/aws-line-echo-bot)'s version,
using serverless to build a line echo bot and import sentry to catch error by flask in AWS.

# Bebore you start

1. Line developer account
2. [Line Message API](https://developers.line.biz/en/docs/messaging-api/getting-started/)
3. Sentry account

# Quick Start

1. Install serverless via npm

```bash
$ npm install -g serverless
```

2. Setup your **AWS** ceritficate

```bash
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
```

3. Clone this project

```bash
$ serverless install --url https://github.com/louis70109/aws-line-wsgi-python -n <YOUR_FILE_NAME>
$ cd <YOUR_FILE_NAME>/
```

4. Rename `.env.sample` to `.env` and insert key in file.

```sh
SENTRY_DSN=
LINE_CHANNEL_TOKEN=
LINE_CHANNEL_SECRET_KEY=
```

5. Deploy the webhhok function

```bash=
npm install
pip install -r requirements.txt
serverless deploy
```

6. You may have like this domain

![](https://i.imgur.com/XCiTkb7.png)

7.  Copy and Paste domain in your LINE bot account

![](https://i.imgur.com/nXFcseH.png)

8. Now you can test you chatbot, have fun!
![Echo bot](https://i.imgur.com/Tn1XS13.png)

9. If have logging `waring`, `error`, Internal(500) or Traceback it will send you Sentry account.

![](https://i.imgur.com/JvVeSdd.png)


# Author

Create by NiJia

# License

The project is available as open source under the terms of the MIT License.
