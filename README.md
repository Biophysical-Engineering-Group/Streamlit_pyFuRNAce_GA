# Patched Streamlit Wheel (weekly)

This repo automatically downloads the latest `streamlit` wheel, injects a Google Analytics snippet for pyFuRNAce into `streamlit/static/index.html`, repackages it, and publishes the patched wheel.

- License: Streamlit is distributed under the Apache-2.0 license. This process preserves upstream licensing metadata included in the wheel.
- Provenance: The wheel version is suffixed with `+ga` (e.g., `streamlit-1.51.0+ga-py3-none-any.whl`) to indicate it has been modified while preserving a valid, pip-installable filename.
- Latest wheel is attached to the **latest** GitHub Release and committed to the repo root.

## Manual run

You can manually trigger the workflow in the **Actions** tab (`workflow_dispatch`). The weekly schedule is currently disabled, using Streamlit 1.51.0 as the base wheel.