# AegisPR controlled PR acceptance fixture

This repository is a deliberately small, public Python fixture for exercising the complete AegisPR GitHub pull-request review path. It is not a real-world benchmark or a production application.

The draft pull request in this repository intentionally introduces a coupon-clamping regression. Existing tests cover an ordinary discount but omit a discount larger than the total, leaving a meaningful boundary for generated tests to discover. Do not merge the draft PR.

Run `python -m pip install -r requirements.txt` and `pytest -q` locally.
