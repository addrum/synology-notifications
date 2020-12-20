# synology-notifications
Docker for forwarding notifications to various services written in Python.

Inspired by https://github.com/ryancurrah/synology-notifications

Supports:
1. Discord

## Docker Setup
1. Add this repo via Docker
1. Add a `WEBHOOK_URL` environment variable and set it to your service's url.
    1. For discord, you can find this in `Edit channel->Integrations->Webhooks->WebhookName->Copy webhook URL`
    1. You can optionally add a `USERNAME` environment variable to override the webhook's name (Discord only)

## Setup for Synology
1. Add a new SMS provider in `Control Panel`
1. Enter your Synology ip followed by the port you've assigned the Docker container to as the `URL`. e.g. `http://<your-synology-ip>:8686`
1. Set `HTTP Method` to `POST`
1. Currently can hit next on `Edit HTTP Request Header` - future notification endpoints may require things like an API key here
1. On `Edit HTTP Request Body`:
    1. Add `phone_number` parameter; leave the `value` field empty
    1. Add `message` parameter; enter `hello world` as the value
1. Set the `phone_number` parameter category to `Phone number`
1. Set the `message` parameter category to `Message content`
1. Set the `SMS Service provider` to your newly created service
1. Enter in a dummy phone number (it's not used)
1. Hit apply
1. Send a test notification to check you receive it

## Setup for Synology Surveillance Station
1. Add a new SMS provider in `Notification` app
1. Enter your Synology ip followed by the port you've assigned the Docker container to as the `URL`. e.g. `http://<your-synology-ip>:8686`
1. This time you'll also need to add some url parameters; the value of these parameters don't matter they're just required by Surveillance Station: e.g. 'http://your-synology-ip:8686?user=na&password=na&api_id=na&to=na&text=hello+world'
1. Set `HTTP Method` to `GET`
1. Set the `user` parameter category to `Username`
1. Set the `password` parameter category to `Password`
1. Set the `to` parameter category to `Phone number`
1. Set the `text` parameter category to `Message content`
1. Set the `SMS Service provider` to your newly created service
1. Enter in a dummy username, password and confirm password (it's not used)
1. Hit apply
1. Send a test notification to check you receive it

