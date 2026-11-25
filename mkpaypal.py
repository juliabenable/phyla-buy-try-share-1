"""Build src/creator-paypal.html from src/creator-v2.html: the same flow plus a payout method (PayPal or Venmo).
Run after mkv2.py, before build.py. v2 stays the "without PayPal" version."""
import pathlib
p = pathlib.Path(__file__).parent / 'src'
s = (p / 'creator-v2.html').read_text(encoding='utf-8')

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70])
    s = s.replace(a, b)

# ---------- page chrome ----------
rep('<title>Buy, Try, Share · Creator flow v2</title>', '<title>Buy, Try, Share · Creator flow v2 with PayPal</title>')
rep('<p class="sub">Creator flow v2 · Amine\'s Nov 25 designs.<br>', '<p class="sub">Creator flow v2 <b>with a payout method</b> (PayPal or Venmo).<br>')
rep('<div id="rail"></div>', '<div id="rail"></div><div class="demo" id="demo"></div>')
rep('<a href="creator-paypal.html">With PayPal version →</a>', '<a href="creator-v2.html">Without PayPal version →</a>')

css = r'''
/* ================= payout method (Figma 12950:41511, adapted) ================= */
.pm-list { display: grid; gap: 12px; width: 100%; }
.pm-row { display: flex; align-items: center; gap: 12px; width: 100%; height: 58px; padding: 0 16px; background: #fff; border: 1px solid var(--line); border-radius: 16px; text-align: left; transition: border-color .12s; }
.pm-row:hover { border-color: var(--text); }
.pm-row b { flex: 1; font-size: 14px; line-height: 17px; font-weight: 600; }
.pm-sel { display: flex; align-items: center; gap: 12px; width: 100%; padding: 12px 16px; background: #fff; border: 1px solid var(--text); border-radius: 16px; }
.pm-sel > div { flex: 1; min-width: 0; display: grid; gap: 2px; text-align: left; }
.pm-sel b { font-size: 14px; line-height: 17px; font-weight: 600; } .pm-sel span { font-size: 13px; line-height: 17px; color: var(--medium); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.pm-chg { display: block; font-size: 14px; line-height: 20px; font-weight: 600; color: var(--accent); margin-top: 12px; text-align: left; }
.pm-chg:hover { text-decoration: underline; }
.pm-hint { font-size: 13px; line-height: 18px; color: var(--medium); margin: 16px 0 0; }
.pm-skip { display: block; margin: 20px auto 0; font-size: 14px; line-height: 20px; font-weight: 600; color: var(--medium); text-decoration: underline; text-underline-offset: 3px; }
.pm-or { font-size: 12px; line-height: 15px; font-weight: 600; color: var(--medium); margin: 16px 0 8px; }
.sheet .pm-list { margin-bottom: 16px; }
/* add payout method screen */
.pf { padding: 24px 16px; display: grid; gap: 16px; }
.pf-logo { text-align: center; font-size: 26px; line-height: 32px; font-weight: 800; font-style: italic; letter-spacing: -.6px; margin-bottom: 8px; }
.pf-logo.pp i { color: #003087; } .pf-logo.pp em { color: #0070e0; } .pf-logo.vm { color: #008cff; }
.pf input { height: 56px; width: 100%; background: #f1f1f1; border: 1px solid #f1f1f1; border-radius: 8px; padding: 0 16px; font: 400 16px Inter, sans-serif; color: var(--text); }
.pf input::placeholder { color: #8a8a8a; } .pf input:focus { outline: 0; border-color: var(--text); background: #fff; }
.pf-err { font-size: 13px; line-height: 18px; color: #c4321c; min-height: 18px; margin: -8px 0 0; }
.pf-note { font-size: 13px; line-height: 18px; color: var(--medium); }
/* payout banner on Share your link */
.pb { margin: 0 16px 20px; display: flex; align-items: center; gap: 10px; background: #fff; border: .5px solid var(--line); border-radius: 16px; padding: 10px 12px; box-shadow: 0 4px 16px rgba(0,0,0,.04); }
.pb .e { width: 36px; height: 36px; border-radius: 50%; background: #f6f3ff; display: grid; place-items: center; font-size: 18px; flex: none; }
.pb > div { flex: 1; min-width: 0; display: grid; gap: 2px; }
.pb b { font-size: 14px; line-height: 17px; font-weight: 600; } .pb span { font-size: 12px; line-height: 15px; color: var(--medium); }
.pb .pl { height: 29px; padding: 0 12px; border-radius: 999px; font-size: 12px; font-weight: 600; display: grid; place-items: center; background: #222; color: #fff; flex: none; }
.pb .pl.g { background: #ececec; color: #9a9a9a; } .pb .pl.ok { background: #e5f5ee; color: #18906c; }
.yay-pay .pm-list { margin-top: 12px; } .yay-pay .pm-chg { margin-top: 8px; }
/* demo switches in the rail */
.demo h2 { font-size: 11px; line-height: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; color: var(--subtle); margin: 16px 8px 4px; }
.dopt { display: block; width: 100%; text-align: left; padding: 6px 8px; border-radius: 8px; font-size: 12px; line-height: 16px; color: #555; }
.dopt[aria-pressed="true"] { background: #fff; color: var(--text); font-weight: 600; box-shadow: 0 1px 2px rgba(0,0,0,.06); }
'''
assert s.count('</style>') == 1
s = s.replace('</style>', css + '</style>')

# ---------- copy: say how they get paid before they join ----------
rep("'Once I upload my video and post.'", "'To my PayPal or Venmo, once I upload my video and post.'")

# ---------- state, helpers ----------
rep("['Share your link']];", "['Share your link'], ['Payout method', 1]];\nconst ORDER = [0, 1, 2, 3, 4, 5, 11, 6, 7, 8, 9, 10]; /* payout sits right after the receipt */")
rep('const fresh = () => (', r'''/* demo switches: who = new (adds it in the flow) | saved (already on file) | skip (adds it at the end); ps = payout status after posting */
const D = { who: 'new', ps: 'way' };
const DEMOPAY = { m: 'PayPal', id: 'maya.glows@gmail.com' };
const PLOGO = {
  PayPal: '<svg width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="16" fill="#f2f4f8"/><path d="M11.6 23.2 13.5 8.8h5.4c2.8 0 4.4 1.6 4 4.1-.5 3-2.6 4.4-5.400 4.4h-2.100l-.8 5.900z" fill="#003087"/><path d="M14.300 25.200 15.600 15.300h3.700c2 0 3.100 1.100 2.800 2.900-.4 2.200-1.900 3.200-3.900 3.200h-1.300l-.5 3.800z" fill="#0070e0"/></svg>',
  Venmo: '<svg width="32" height="32" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="16" fill="#008cff"/><path d="M21.5 9c.5.9.8 1.800.8 3 0 3.600-3.100 8.300-5.600 11.600h-5.700L8.700 9.900l5-.5 1.200 9.700c1.100-1.800 2.500-4.700 2.500-6.700 0-1.100-.2-1.800-.5-2.400z" fill="#fff"/></svg>',
};
const CHK = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-label="Selected"><circle cx="12" cy="12" r="12" fill="#222"/><path d="M7.5 12.4 10.6 15.3 16.5 9" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const pmRow = (m) => `<button class="pm-row" data-act="pm:${m}">${PLOGO[m]}<b>${m}</b><img src="m/ic-chev-right.svg" width="20" height="20" alt=""></button>`;
const pmSel = () => `<div class="pm-sel">${PLOGO[S.pay.m]}<div><b>${S.pay.m}</b><span>${S.pay.id}</span></div>${CHK}</div>`;
const digits = (x) => x.replace(/\D/g, '');
const pfVals = () => { const f = S.pf, v = f.m === 'Venmo'; return v ? [digits(f.a), digits(f.b), v] : [f.a.trim().toLowerCase(), f.b.trim().toLowerCase(), v]; };
const pfValid = (a, v) => v ? a.length === 10 : /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(a);
const pfOk = () => { if (!S.pf) return false; const [a, b, v] = pfVals(); return pfValid(a, v) && a === b; };
const pfErr = () => { const [a, b, v] = pfVals(); if (!b) return ''; if (!a.startsWith(b)) return "These don't match. Check for a typo."; if (a === b && !pfValid(a, v)) return v ? 'Enter a 10-digit phone number.' : 'Enter a full email address.'; return ''; };
const pfScreen = () => { const f = S.pf, v = f.m === 'Venmo'; return `${SB}<div class="hdr"><button class="ib" data-back aria-label="Back"><img src="m/ic-chev-left.svg" width="16" height="16" alt=""></button><div class="t">Add payout method</div><span></span></div>
    <div class="scroll"><div class="pf"><div class="pf-logo ${v ? 'vm' : 'pp'}">${v ? 'venmo' : '<i>Pay</i><em>Pal</em>'}</div>
      <input data-pf="a" type="${v ? 'tel' : 'email'}" placeholder="${v ? 'Venmo phone' : 'PayPal email'}" aria-label="${v ? 'Venmo phone' : 'PayPal email'}" value="${esc(f.a)}" autocomplete="off" autocapitalize="off">
      <input data-pf="b" type="${v ? 'tel' : 'email'}" placeholder="${v ? 'Confirm phone' : 'Confirm email'}" aria-label="${v ? 'Confirm phone' : 'Confirm email'}" value="${esc(f.b)}" autocomplete="off" autocapitalize="off" onpaste="return false">
      <p class="pf-err" id="pferr" role="alert">${pfErr()}</p>
      <p class="pf-note">${v ? 'The phone number on your Venmo account. We send your money to this exact number.' : 'The email you log in to PayPal with. We send your money to this exact address.'}</p>
    </div></div><div class="foot" style="padding:12px 16px 0;box-shadow:none"><button class="cta full" id="pfsave" data-act="pf-save" style="margin-bottom:16px;font-size:14px" ${pfOk() ? '' : 'disabled'}>Save</button><div class="home"></div></div>`; };
/* Done screen card: confirms where the money goes, or catches a creator who skipped the step */
const yayPay = () => S.pay
  ? `<div class="yay-pay"><small>Your money back</small><b>On its way to your ${S.pay.m}</b><span>${S.pay.id} · $55 + tax, in 1 to 3 business days.</span><button class="pm-chg" data-act="pay-change">Change account</button></div>`
  : `<div class="yay-pay"><small>One last thing</small><b>Where should we pay you back?</b><span>Your $55 + tax is ready. Add an account and we send it in 1 to 3 business days.</span><div class="pm-list">${pmRow('PayPal')}${pmRow('Venmo')}</div></div>`;
/* Share your link banner: the four states from Figma, plus "add an account" */
const payBanner = () => { const m = S.pay && S.pay.m;
  const [e, t, d, pl] = !S.pay ? ['💸', 'Your $55 + tax is ready', 'Add PayPal or Venmo to get paid back', '<button class="pl" data-act="pay-change">Add</button>']
    : D.ps === 'paid' ? ['✅', 'You got paid $59.81', `Sent to your ${m}, Dec 8`, '<span class="pl ok">Sent</span>']
    : D.ps === 'failed' ? ['❗', "Your money hasn't landed yet", `We couldn't send to ${S.pay.id}`, '<button class="pl" data-act="pay-fix">Fix</button>']
    : ['🕒', 'Money is on the way', `$55 + tax heading to your ${m}`, '<span class="pl g">Pending</span>'];
  return `<div class="pb"><span class="e" aria-hidden="true">${e}</span><div><b>${t}</b><span>${d}</span></div>${pl}</div>`; };
const dg = (k, opts) => opts.map(([v, t]) => `<button class="dopt" data-demo="${k}:${v}" aria-pressed="${D[k] === v}">${t}</button>`).join('');
const fresh = () => (''')
rep("links: ['', '', ''], extra: 0 });", "links: ['', '', ''], extra: 0, pay: D.who === 'saved' ? { ...DEMOPAY } : null, pf: null });")

# ---------- screens ----------
rep("""ffoot('Next', S.rc > 0, 'data-go="6"')""", """ffoot('Next', S.rc > 0, 'data-go="11"')""")
rep('<div class="yay-pay"><small>Your money back</small><b>On its way to your PayPal</b><span>What you paid for the serum, tax included, in 1 to 3 business days.</span></div>', '${yayPay()}')
rep('<div class="shl-h"><h2>Get Your Affiliate Link Out There</h2>', '${payBanner()}<div class="shl-h"><h2>Get Your Affiliate Link Out There</h2>')
end = '<div class="home" style="background:var(--page)"></div></div>`,\n];'
rep(end, end[:-2] + r'''
  /* 11 payout method: NOT in the Buy, Try, Share Figma. Shown right after the receipt (ORDER) */ () => `${SB}${fhdr(2)}<div class="scroll"><div class="fbody"><h2>Where should we pay you back?</h2><p class="lead lg">We send what you paid for the serum, tax included, as soon as your posts are live.</p>
      ${S.pay ? `${pmSel()}<button class="pm-chg" data-act="pay-change">Use a different account</button><p class="pm-hint">You can change this until the money is sent.</p>`
      : `<div class="pm-list">${pmRow('PayPal')}${pmRow('Venmo')}</div><p class="pm-hint">We can only pay you back once an account is added.</p><button class="pm-skip" data-go="6">I'll add it later</button>`}
    </div></div>${ffoot('Next', !!S.pay, 'data-go="6"')}`,
];''')
rep('  video: () =>', r'''  paym: () => `<div class="sh-h"><h2>Where should we pay you back?</h2></div>${S.pay ? `${pmSel()}<p class="pm-or">Use a different account</p>` : ''}<div class="pm-list">${pmRow('PayPal')}${pmRow('Venmo')}</div>`,
  video: () =>''')

# ---------- logic ----------
rep('el.innerHTML = SCREENS[base]() + (sheet ?', 'el.innerHTML = (S.pf ? pfScreen() : SCREENS[base]()) + (sheet ?')
rep("""document.getElementById('rail').innerHTML = NAMES.map(([n, isNew], i) => `<button class="s" data-jump="${i}" aria-current="${S.s === i}"><span>${i + 1}</span>${n}${isNew ? '<em>new</em>' : ''}</button>`).join('');""",
    """document.getElementById('rail').innerHTML = ORDER.map((i, k) => { const [n, isNew] = NAMES[i]; return `<button class="s" data-jump="${i}" aria-current="${S.s === i}"><span>${k + 1}</span>${n}${isNew ? '<em>new</em>' : ''}</button>`; }).join('');
  document.getElementById('demo').innerHTML = `<h2>Payout method</h2>${dg('who', [['new', 'Adds it in the flow'], ['saved', 'Already has PayPal saved'], ['skip', 'Skips, adds it at the end']])}<h2>After posting</h2>${dg('ps', [['way', 'On its way'], ['paid', 'Paid'], ['failed', "Didn't land"]])}`;""")
rep("if ((el = q('[data-jump]'))) { const n = +el.dataset.jump; S = fresh(); S.s = n;",
    "if ((el = q('[data-demo]'))) { const [k, v] = el.dataset.demo.split(':'); D[k] = v; document.querySelector(`[data-jump=\"${k === 'ps' ? 10 : S.s}\"]`).click(); return; }\n  if ((el = q('[data-jump]'))) { const n0 = +el.dataset.jump, n = n0 === 11 ? 5.5 : n0; S = fresh(); S.s = n0; if (n0 === 11) S.rc = 1; if (n >= 6 && D.who === 'new') S.pay = { ...DEMOPAY };")
rep("if (q('[data-back]') && S.add) {", "if (q('[data-back]') && S.pf) { S.pf = null; render(); return; }\n  if (q('[data-back]') && S.add) {")
rep("S.s = S.s === 3 ? 1 : S.s === 8 || S.s === 7 ? 6 : S.s - 1;", "S.s = S.s === 3 ? 1 : S.s === 11 ? 5 : S.s === 6 ? 11 : S.s === 8 || S.s === 7 ? 6 : S.s - 1;")
rep("else if (a === 'more') {", """else if (a.startsWith('pm:')) { S.pf = { m: a.slice(3), a: '', b: '' }; S.sheet = null; render(); }
    else if (a === 'pf-save') { if (!pfOk()) return; const [id, , v] = pfVals(); S.pay = { m: S.pf.m, id: v ? `(${id.slice(0, 3)}) ${id.slice(3, 6)}-${id.slice(6)}` : id }; S.pf = null; if (D.ps === 'failed') D.ps = 'way'; render(); }
    else if (a === 'pay-change') { S.sheet = 'paym'; render(); }
    else if (a === 'pay-fix') { S.pf = { m: S.pay.m, a: '', b: '' }; render(); }
    else if (a === 'more') {""")
rep("document.addEventListener('input', (e) => { ", "document.addEventListener('input', (e) => { if (e.target.dataset.pf && S.pf) { S.pf[e.target.dataset.pf] = e.target.value; document.getElementById('pfsave').disabled = !pfOk(); document.getElementById('pferr').textContent = pfErr(); return; } ")

(p / 'creator-paypal.html').write_text(s, encoding='utf-8')
print('src/creator-paypal.html', len(s))
