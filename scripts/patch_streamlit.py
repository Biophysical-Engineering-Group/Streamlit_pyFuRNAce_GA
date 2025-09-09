import os

GA_SNIPPET = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-M1PJP8JM1T"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-M1PJP8JM1T');
</script>
"""

def main():
    # Find unpacked streamlit package folder (e.g., streamlit-1.37.0)
    candidates = [d for d in os.listdir(".") if os.path.isdir(d) and d.startswith("streamlit-")]
    if not candidates:
        raise SystemExit("No unpacked streamlit-* directory found.")
    root = candidates[0]

    # Typical path: <root>/streamlit/static/index.html
    p = os.path.join(root, "streamlit", "static", "index.html")
    if not os.path.isfile(p):
        # Try to find it by walking (future-proof)
        found = []
        for dirpath, _, files in os.walk(root):
            if "index.html" in files and dirpath.endswith(os.path.join("streamlit","static")):
                found.append(os.path.join(dirpath, "index.html"))
        if found:
            p = found[0]
        else:
            raise SystemExit("Could not locate streamlit/static/index.html inside the wheel.")

    with open(p, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("<head>", "<head>\n" + GA_SNIPPET, 1)

    with open(p, "w", encoding="utf-8") as f:
        f.write(html)

    print("Patched:", p)

if __name__ == "__main__":
    main()
