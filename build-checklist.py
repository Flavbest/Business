"""Generate the public GitHub Pages copy of the checklist from our source.

The artifact at notes/checklist-artifact.html is the ONE source of truth.
This script derives github/Business/Checklist.html from it. Never edit the
repo copy by hand — edit the artifact source and re-run this.

Two things it deliberately changes:

1. The state block is emptied. The artifact's state carries real progress
   AND the scratchpad (supplier names, prices, margins). The repo is public.
   Progress must never be committed.

2. A banner is added saying this copy does not sync. GitHub Pages has no
   `artifact` capability, so the page falls back to localStorage — ticking
   boxes here would silently create a second, diverging set of progress.

Usage:  python build-checklist.py
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'checklist-artifact.html')
DST = os.path.join(HERE, '..', 'github', 'Business', 'Checklist.html')

EMPTY_STATE = '{"tasks":{},"open":{"w1":true},"scratch":"","updatedAt":0}'

BANNER_CSS = """
/* ---------- mirror banner (public copy only) ---------- */
.mirror{
  max-width:640px;margin:0 auto 16px;
  background:#FBF3E2;border:1.5px solid var(--amber);border-radius:12px;
  padding:11px 14px;font-size:13.5px;color:#6B4B15;
}
.mirror b{color:var(--ink)}
"""

BANNER_HTML = """<div class="mirror">
  <b>Reference copy — this page does not save.</b> Your live checklist is the
  Claude artifact: it stores progress in the page itself, so phone and PC stay
  in step. Tick boxes there. Anything ticked here stays in this browser only.
</div>
"""


def build():
    src = io.open(SRC, encoding='utf-8').read()

    # 1. progress never reaches the public repo
    out, n = re.subn(
        r'(<script type="application/json" id="state">)(.*?)(</script>)',
        lambda m: m.group(1) + EMPTY_STATE + m.group(3),
        src, count=1, flags=re.S)
    assert n == 1, 'state block not found'

    # 2. banner styles, appended to the existing sheet
    out = out.replace('</style>', BANNER_CSS + '</style>', 1)

    # 3. banner markup above the app's mount point
    assert '<div id="root"></div>' in out
    out = out.replace('<div id="root"></div>', BANNER_HTML + '<div id="root"></div>', 1)

    # 4. the artifact host supplies the document skeleton; Pages does not
    head_end = out.index('<style id="css">')
    head, rest = out[:head_end], out[head_end:]
    doc = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n'
           + head.strip() + '\n'
           + rest[:rest.index('</style>') + len('</style>')] + '\n'
           + '</head>\n<body>\n'
           + rest[rest.index('</style>') + len('</style>'):].strip() + '\n'
           + '</body>\n</html>\n')

    io.open(DST, 'w', encoding='utf-8', newline='\n').write(doc)

    # never ship progress or notes
    assert EMPTY_STATE in doc
    assert '"scratch":""' in doc
    return doc


if __name__ == '__main__':
    d = build()
    print('wrote', os.path.normpath(DST), len(d), 'bytes')
