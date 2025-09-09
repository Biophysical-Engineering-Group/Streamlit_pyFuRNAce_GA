# Patched Streamlit Wheel (weekly)

This repo automatically downloads the latest `streamlit` wheel, injects a Google Analytics snippet for pyFuRNAce into `streamlit/static/index.html`, repackages it, and publishes the new wheel weekly.

- License: Streamlit is distributed under the Apache-2.0 license. This process preserves upstream licensing metadata included in the wheel.
- Provenance: The wheel filename is suffixed with `+ga` to indicate it has been modified.
- Latest wheel is attached to the **latest** GitHub Release and committed to the repo root.

## Manual run
You can manually trigger the workflow in the **Actions** tab (`workflow_dispatch`).
