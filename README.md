# Fortune Hook

Simple script that runs ```fortune -l``` and sends the outputs to Slack via a Webhook. Hook IDs are read from environment variables that match the pattern ```HOOK_ID_*```.

A kubernetes cron template is supplied that gets the environment variables from a secret map.
