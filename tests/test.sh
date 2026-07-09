#!/bin/bash
set +e

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -q --ctrf /logs/verifier/ctrf.json
status=$?

if [ "$status" -eq 0 ]; then
  reward=1
else
  reward=0
fi

echo "$reward" > /logs/verifier/reward.txt

exit 0
