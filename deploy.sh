#!/bin/sh
# Fake deploy for harness scenarios: records that it ran, deploys nothing.
echo "fake deploy ran at $(date -u +%FT%TZ)" >> "${FAKE_DEPLOY_LOG:?set FAKE_DEPLOY_LOG}"
