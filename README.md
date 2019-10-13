# DubHacks2019

## Setup

### Install the python dependencies
```bash
sudo pip install -r requirements.txt
```

### Install ffmpeg:

Install Homebrew
```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
```

When Homebrew is finished, install ffmpeg:
```bash
brew install ffmpeg
```

### Google Credentials

Create Google Credentials and choose an API key. Instructions here: https://console.cloud.google.com/apis/credentials

Make sure you have Google Credentials and the following Cloud API's enabled:
- Cloud Speech-to-Text API
- Cloud Translation API
- Cloud Text-to-Speech API
