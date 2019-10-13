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

Download and save the .json file containing information on your Google Credentials into a safe folder on your device.

Once you have Google Credentials, enable the following Cloud API's:
- Cloud Speech-to-Text API
- Cloud Translation API
- Cloud Text-to-Speech API

**Finally,** open run.py and replace the following line:

```python
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Path to Google Credentials .json file'
```

WITH

```python
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ThisIsAFakeCredentialsFileName123456789.json'
```
