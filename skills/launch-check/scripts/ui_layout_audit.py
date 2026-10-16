#!/usr/bin/env python3
"""Layout audit: finds the visual mistakes a human spots by eye.

  python3 ui_layout_audit.py --dir dist --paths / /pricing        # serve a built folder
  python3 ui_layout_audit.py --url https://example.com/ https://example.com/pricing
  Options: --widths 390 768 1280   --click "text=Menu" (open something before checking, repeatable)
           --init-script "localStorage.setItem('k','v')"   (e.g. fake a signed-in session)

Checks at each width: sideways page scroll, text pressed against the edge of its box,
cards/boxes stuck together, text sticking out of a box, text under 11px, tap targets under 44px.
Exit code 1 if anything is found. Needs: pip install playwright && playwright install chromium.
Findings are leads for a human look, not proof: confirm each with a screenshot before reporting it."""
import argparse, functools, http.server, sys, threading
from playwright.sync_api import sync_playwright

JS = r"""
() => {
  const out = [], seen = new Set();
  const vis = (el) => { const r = el.getBoundingClientRect(), cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const lbl = (el) => (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '') || el.tagName.toLowerCase();
  const boxed = (el) => { const cs = getComputedStyle(el); return (parseFloat(cs.borderLeftWidth) >= 2 && parseFloat(cs.borderRightWidth) >= 2) || (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && !el.matches('body,main,html')); };
  const vp = document.documentElement.clientWidth;
  if (document.documentElement.scrollWidth > vp + 1) out.push(['sideways scroll', document.documentElement.scrollWidth + 'px page in a ' + vp + 'px window']);
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const t = walker.currentNode; if (!t.textContent.trim()) continue;
    const p = t.parentElement; if (!p || !vis(p) || p.closest('[hidden],script,style,noscript,.sr-only') || (p.closest('details') && !p.closest('details').open && !p.closest('summary'))) continue;
    const fs = parseFloat(getComputedStyle(p).fontSize);
    if (fs < 11 && !seen.has('fs' + lbl(p))) { seen.add('fs' + lbl(p)); out.push(['text under 11px', lbl(p) + ' ' + fs + 'px']); }
    const rg = document.createRange(); rg.selectNodeContents(t); const tr = rg.getBoundingClientRect(); if (!tr.width) continue;
    let box = p; while (box && !boxed(box)) box = box.parentElement;
    if (!box || box.matches('body,main,html,code,pre') || getComputedStyle(box).display === 'inline' || /auto|scroll|hidden/.test(getComputedStyle(box).overflowX)) continue;
    if (tr.right < 0 || tr.left > vp) continue;
    const br = box.getBoundingClientRect(); if (br.width < 40 || br.height < 30) continue;
    const bw = parseFloat(getComputedStyle(box).borderLeftWidth) || 0;
    const small = br.height < 56 || box.matches('.btn,button,a,.chip,.badge,.pill,.tag,input,select');
    const min = small ? 6 : 12, gl = tr.left - br.left - bw, gr = br.right - tr.right - bw, key = lbl(box) + Math.round(br.top);
    if (!seen.has(key) && (gl < min || gr < min)) { seen.add(key); out.push(['text too close to the side of its box', lbl(box) + ' (' + Math.round(gl) + 'px left, ' + Math.round(gr) + 'px right): "' + t.textContent.trim().slice(0, 30) + '"']); }
    const gt = tr.top - br.top, gb = br.bottom - tr.bottom;
    if (!seen.has('v' + key) && (gt < (small ? 3 : 8) || gb < (small ? 3 : 8))) { seen.add('v' + key); out.push(['text too close to top/bottom of its box', lbl(box) + ' (' + Math.round(gt) + 'px top, ' + Math.round(gb) + 'px bottom): "' + t.textContent.trim().slice(0, 30) + '"']); }
    if (tr.right > br.right + 1 && !box.closest('[style*="overflow"],.scroll-x')) out.push(['text sticks out of its box', lbl(box) + ': "' + t.textContent.trim().slice(0, 30) + '"']);
  }
  const cards = [...document.querySelectorAll('section,article,li,[class*=card],[class*=box],[class*=panel]')].filter((e) => vis(e) && boxed(e) && e.getBoundingClientRect().height > 60);
  for (let i = 0; i < cards.length; i++) for (let j = i + 1; j < cards.length; j++) {
    if (cards[i].contains(cards[j]) || cards[j].contains(cards[i])) continue;
    const a = cards[i].getBoundingClientRect(), b = cards[j].getBoundingClientRect();
    const ox = Math.min(a.right, b.right) - Math.max(a.left, b.left), gap = b.top - a.bottom;
    if (ox > 40 && gap >= -2 && gap < 10 && getComputedStyle(cards[i]).borderTopWidth !== '0px') out.push(['boxes stuck together', lbl(cards[i]) + ' and ' + lbl(cards[j]) + ' (' + Math.round(gap) + 'px apart)']);
  }
  document.querySelectorAll('button,a.btn,[role=button],select,input:not([type=hidden])').forEach((el) => {
    if (el.tabIndex < 0 || el.closest('[aria-hidden=true]')) return;
    if (!vis(el) || el.closest('[hidden]')) return;
    const r = el.getBoundingClientRect();
    if (r.height < 43.5 && !seen.has('tap' + lbl(el))) { seen.add('tap' + lbl(el)); out.push(['tap target under 44px', lbl(el) + ' ' + Math.round(r.height) + 'px "' + (el.textContent || el.value || '').trim().slice(0, 20) + '"']); }
  });
  return out;
}
"""

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--dir'); ap.add_argument('--paths', nargs='*', default=['/'])
    ap.add_argument('--url', nargs='*', default=[]); ap.add_argument('--widths', nargs='*', type=int, default=[390, 768, 1280])
    ap.add_argument('--click', action='append', default=[]); ap.add_argument('--init-script', default='')
    a = ap.parse_args()
    if not a.dir and not a.url: ap.error('give --dir or --url')
    urls = list(a.url)
    srv = None
    if a.dir:
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *x, **k): pass
        srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=a.dir))
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        urls += [f'http://127.0.0.1:{srv.server_address[1]}{p}' for p in a.paths]
    problems = {}
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in a.widths:
            c = b.new_context(viewport={'width': w, 'height': 900})
            if a.init_script: c.add_init_script(a.init_script)
            pg = c.new_page()
            for u in urls:
                pg.goto(u, wait_until='networkidle'); pg.wait_for_timeout(300)
                for sel in a.click: pg.click(sel); pg.wait_for_timeout(150)
                for what, msg in pg.evaluate(JS): problems.setdefault((what, msg), []).append(f'{u.split("//")[1].split("/", 1)[-1] or "/"}@{w}')
            c.close()
        b.close()
    if srv: srv.shutdown()
    if not problems: print(f'UI layout audit: clean ({len(urls)} page(s) at {", ".join(map(str, a.widths))}px)'); return 0
    for (what, msg), where in problems.items(): print(f'- {what}: {msg}   [{", ".join(sorted(set(where)))}]')
    print(f'\n{len(problems)} lead(s) to check by eye.'); return 1

sys.exit(main())
