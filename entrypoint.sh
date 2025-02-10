#!/bin/bash

set -e

if [ ! -f "/app/.reflex_initialized" ]; then
    echo "Initializing Reflex..."
    reflex init
    touch /app/.reflex_initialized
fi

exec "$@"
