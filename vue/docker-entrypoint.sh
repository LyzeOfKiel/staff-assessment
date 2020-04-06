#!/usr/bin/env sh

set -ex

npm install
npm install vuetify --save

exec "$@"
