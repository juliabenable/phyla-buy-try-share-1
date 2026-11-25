import re, pathlib
src = pathlib.Path('creator.html').read_text(encoding='utf-8')
i = src.index('const VIDEO = [')
head = src[:i]

def rep(a, b, n=1):
    global head
    assert head.count(a) == n, (head.count(a), a[:60])
    head = head.replace(a, b)

rep('<title>Buy, Try, Share · Creator flow</title>', '<title>Buy, Try, Share · Creator flow v2</title>')
rep('<p class="sub">Creator flow · Phyla pilot<br>Screens 1 and 2 are Amine\'s Figma.</p>', '<p class="sub">Creator flow v2 · Amine\'s Nov 25 designs.<br>Screens marked <em class="new">new</em> are not in Figma yet.</p>')
rep('<a href="brand.html">Brand Portal page →</a>', '<a href="creator-paypal.html">With PayPal version →</a><a href="design-review.html">Design review list →</a><a href="creator.html">Previous version (v1) →</a><a href="brand.html">Brand Portal page →</a>')
rep('"I\'ll be paid back after my posts are live", \'Once I upload my Reel and Story and post them.\'', '"I\'ll be paid back after my post is live", \'Once I upload my video and post.\'')

css = r'''
/* ================= v2: Amine's Nov 25 designs ================= */
.rail .new, .rail button.s em { font-style: normal; font-size: 10px; font-weight: 600; color: var(--accent); background: var(--accent-weak); padding: 1px 6px; border-radius: 999px; margin-left: 6px; }
.cta:disabled { background: #e4e4e4; color: #fff; }
/* flow header + edge-to-edge stepper (16030:61975) */
.fh { height: 48px; flex: none; background: #fff; display: flex; align-items: center; justify-content: space-between; padding: 0 16px 0 12px; }
.fh .bk { width: 32px; height: 32px; display: grid; place-items: center; border-radius: 8px; }
.fh .vb { border: 1px solid var(--line); border-radius: 24px; padding: 8px 12px; font-size: 14px; line-height: 17px; font-weight: 600; background: #fff; }
.fh .vb:hover { background: #f7f7f8; }
.stp { height: 16px; flex: none; background: #fff; display: flex; align-items: flex-end; gap: 6px; }
.stp i { flex: 1; height: 2px; background: #ddd; border-radius: 999px; }
.stp i:first-child { border-radius: 0 999px 999px 0; } .stp i:last-child { border-radius: 999px 0 0 999px; }
.stp i.on { background: #222; }
.fbody { padding: 24px 16px; gap: 0; }
.fbody h2 { font-size: 16px; line-height: 19px; font-weight: 700; letter-spacing: 0; }
.fbody .lead { font-size: 14px; line-height: 17px; color: var(--medium); margin: 4px 0 16px; }
.fbody .lead.lg { font-size: 16px; line-height: 22px; margin-top: 8px; }
/* choice cards, no radio (16030:62096) */
.opt2 { display: grid; gap: 6px; width: 100%; text-align: left; background: #fff; border: 1px solid var(--line); border-radius: 16px; padding: 16px; cursor: pointer; transition: border-color .12s, background-color .12s; }
.opt2 + .opt2 { margin-top: 12px; }
.opt2.on { border-color: var(--text); background: #fcfcfc; }
.opt2 b { font-size: 14px; line-height: 17px; font-weight: 600; color: #000; }
.opt2 span { font-size: 14px; line-height: 20px; color: #8a8a8a; }
.olink { display: inline-flex; align-items: center; gap: 4px; margin-top: 10px; justify-self: start; font-size: 14px; line-height: 20px; font-weight: 500; color: var(--accent); text-decoration: none; }
.olink:hover { text-decoration: underline; }
/* dashed upload zone (16058:62831) */
.zone2 { width: 100%; height: 179px; background: #fcfcfc; border: 1px dashed var(--medium); border-radius: 12px; display: grid; place-content: center; justify-items: center; gap: 8px; text-align: center; }
.zone2:hover { border-color: var(--text); }
.zone2 b { font-size: 16px; line-height: 19px; font-weight: 500; }
.zone2 span { font-size: 14px; line-height: 17px; color: var(--medium); }
.see { margin-top: 24px; } .see h3 { margin: 0 0 8px; font-size: 16px; line-height: 19px; font-weight: 600; }
.see ul { margin: 0; padding-left: 21px; font-size: 14px; line-height: 26px; color: var(--medium); }
.thumbs + .hint { margin: 12px 0 0; }
.rb { display: inline-flex; align-items: center; gap: 8px; font-size: 14px; line-height: 17px; font-weight: 500; margin: -6px 0 16px; justify-self: start; }
.rb:hover { text-decoration: underline; }
.uc-h { margin-bottom: 0; } .uc .lead { margin: 8px 0 12px; }
.uc-item { height: 108px; } .ac-chips { display: flex; flex-wrap: wrap; gap: 8px; } .uc-note { font-size: 12px; line-height: 15px; color: var(--medium); }
.uc-zone2 { height: 120px; }
/* footer (16055:62754) */
.ffoot { padding: 12px 16px 0; box-shadow: 0 -.5px 0 var(--line); }
.due { margin-bottom: 16px; }
.due small { font-size: 10px; line-height: 12px; font-weight: 500; color: #868686; margin-bottom: 4px; }
.due b { font-size: 14px; line-height: 17px; font-weight: 700; color: #000; }
.due .pill { background: #f2edff; }
.ffoot .cta { font-size: 14px; letter-spacing: 0; margin-bottom: 16px; }
/* time to post (16058:63250) */
.lk { background: #fff; border: .5px solid var(--line); border-radius: 12px; padding: 16px; box-shadow: 0 4px 16px rgba(0,0,0,.04); display: grid; gap: 12px; }
.lk + .lk, .lk + .addl { margin-top: 16px; }
.lk-t { display: grid; gap: 4px; } .lk-t b, .lk-h b { font-size: 14px; line-height: 17px; font-weight: 600; } .lk-t span { font-size: 12px; line-height: 15px; color: var(--medium); }
.lk-h { display: flex; align-items: center; justify-content: space-between; height: 20px; }
.dr { display: inline-flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 500; color: #a2a2a2; }
.dr:hover { color: var(--medium); }
.lk input { height: 48px; width: 100%; background: #f5f5f5; border: 1px solid #f1f1f1; border-radius: 8px; padding: 0 16px; font: 400 14px Inter, sans-serif; color: var(--text); }
.lk input::placeholder { color: #a5a5a5; } .lk input:focus { outline: 0; border-color: var(--text); background: #fff; }
.aff { display: flex; align-items: center; justify-content: space-between; gap: 8px; width: 100%; background: #fcfcfc; border: .5px solid var(--line); border-radius: 8px; padding: 4px 16px 4px 4px; }
.aff > span { display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 500; color: var(--text-2); min-width: 0; }
.aff img.t { width: 40px; height: 40px; border-radius: 4px; object-fit: cover; background: #797979; }
.capc { display: flex; flex-wrap: wrap; gap: 8px; }
.capc button { display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 12px; border-radius: 999px; background: #fcfcfc; border: .5px solid var(--line); font-size: 14px; font-weight: 500; }
.addl { width: 100%; height: 48px; background: #fff; border: 1px dashed var(--medium); border-radius: 12px; display: flex; align-items: center; justify-content: center; gap: 12px; font-size: 13px; font-weight: 500; }
/* sheets (16022:61267, 16058:62896) */
.ag { background: #fcfcfc; border-radius: 16px; }
.ag-h span { color: var(--accent); }
.sh-c { text-align: center; font-size: 16px; line-height: 19px; font-weight: 600; margin: -8px 0 22px; }
.ag-h.v b { font-size: 16px; line-height: 22px; font-weight: 500; color: #414141; max-width: 221px; }
.ag-t span strong { font-weight: 500; color: var(--text); }
.say { margin: 0; padding-left: 18px; display: grid; gap: 6px; font-size: 14px; line-height: 19px; color: var(--medium); } .say strong { font-weight: 600; color: var(--text); }
/* good to go sheet (16080:65225) */
.rdy-s { display: grid; justify-items: center; text-align: center; gap: 8px; padding: 8px 0 24px; border-bottom: 1px solid var(--line); }
.rdy-ok { width: 48px; height: 48px; border-radius: 50%; background: #18906c; display: grid; place-items: center; margin-bottom: 8px; }
.rdy-s h2 { margin: 0; font-size: 22px; line-height: 28px; font-weight: 700; letter-spacing: -.3px; }
.rdy-s p { font-size: 16px; line-height: 22px; color: var(--medium); max-width: 300px; }
.rdy-next { padding: 20px 0 8px; margin: 0; border: 0; } .rdy-next .hstep:last-child { padding-bottom: 12px; }
/* celebration */
.yay { position: relative; padding: 132px 24px 24px; display: grid; justify-items: center; text-align: center; gap: 8px; overflow: hidden; }
.confetti { position: absolute; left: 50%; top: 20px; width: 343px; height: 130px; margin-left: -171.5px; }
.confetti i { position: absolute; width: 6px; height: 14px; border-radius: 2px; }
.yay-ok { width: 56px; height: 56px; border-radius: 50%; background: #18906c; display: grid; place-items: center; margin-bottom: 16px; }
.yay h2 { margin: 0; font-size: 28px; line-height: 34px; font-weight: 700; letter-spacing: -.4px; }
.yay p { font-size: 16px; line-height: 22px; color: var(--medium); max-width: 290px; }
.yay-pay { width: 100%; margin-top: 24px; background: #f7f5fd; border-radius: 16px; padding: 16px; display: grid; gap: 4px; text-align: left; }
.yay-pay small { font-size: 12px; font-weight: 600; color: var(--accent); } .yay-pay b { font-size: 16px; line-height: 22px; font-weight: 600; } .yay-pay span { font-size: 14px; line-height: 20px; color: var(--medium); }
/* share your link (16009:68858) */
.shl { padding: 24px 0 24px; }
.shl-h { padding: 0 16px; display: grid; gap: 4px; } .shl-h h2 { margin: 0; font-size: 16px; line-height: 19px; font-weight: 700; } .shl-h p { font-size: 14px; line-height: 17px; color: var(--medium); max-width: 320px; }
.shl-car { display: flex; gap: 16px; overflow-x: auto; padding: 16px 16px 24px; scroll-snap-type: x mandatory; scrollbar-width: none; } .shl-car::-webkit-scrollbar { display: none; }
.shl-car > * { flex: none; width: 331px; height: 454px; border-radius: 28px; scroll-snap-align: center; }
.shl-car img { object-fit: cover; display: block; }
.shl-c { display: grid; align-content: end; justify-items: center; text-align: center; gap: 8px; padding: 0 32px 40px; }
.shl-c b { font-size: 26px; line-height: 28px; font-weight: 800; text-transform: uppercase; letter-spacing: -.5px; } .shl-c span { font-size: 16px; line-height: 19px; font-weight: 500; }
.shl-c.c2 { background: linear-gradient(160deg, #ffc9a3, #ffe9b8 60%, #fff3e6); color: #7a3b00; } .shl-c.c3 { background: linear-gradient(160deg, #b9e6c9, #e3f7d6 60%, #f3fbef); color: #14553a; } .shl-c.c4 { background: linear-gradient(160deg, #b8d4ff, #dbe8ff 60%, #f1f5ff); color: #1c3f7a; }
.shl h3 { margin: 0 16px 16px; font-size: 16px; line-height: 19px; font-weight: 600; }
.shl-p { margin: 0 16px; background: #fff; border: .5px solid var(--line); border-radius: 24px; padding: 8px 8px 16px; display: grid; gap: 12px; box-shadow: 0 4px 16px rgba(0,0,0,.04); }
.shl-img { height: 224px; border-radius: 16px; overflow: hidden; background: #ececec; } .shl-img img { width: 100%; height: 100%; object-fit: cover; object-position: center 60%; display: block; }
.shl-p > b { padding: 0 8px; font-size: 16px; line-height: 19px; font-weight: 600; }
.shl-l { margin: 4px 8px 0; height: 38px; border-radius: 999px; background: #f5f5f5; display: flex; align-items: center; gap: 8px; padding: 0 12px; font-size: 14px; }
.shl-l span { flex: 1; text-align: left; color: var(--medium); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; } .shl-l em { font-style: normal; font-weight: 600; color: var(--accent); }
/* new transition states */
.ilink { color: var(--accent); font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 3px; } .ilink:hover { text-decoration: underline; }
.in-h { display: grid; justify-items: center; text-align: center; gap: 8px; padding: 8px 0 24px; margin-bottom: 24px; border-bottom: 1px solid var(--line); }
.in-h .rdy-ok { margin-bottom: 4px; }
.fbody .in-h h2 { font-size: 22px; line-height: 28px; font-weight: 700; letter-spacing: -.3px; }
.in-h p { font-size: 16px; line-height: 22px; color: var(--medium); max-width: 300px; }
.rdy { width: 100%; margin-top: 24px; display: grid; gap: 8px; text-align: left; }
.rdy-i { display: flex; align-items: center; gap: 12px; background: #fff; border: .5px solid var(--line); border-radius: 16px; padding: 8px 16px 8px 8px; box-shadow: 0 4px 16px rgba(0,0,0,.04); }
.rdy-i img { width: 48px; height: 64px; border-radius: 8px; object-fit: cover; flex: none; }
.rdy-i div { flex: 1; display: grid; gap: 2px; } .rdy-i b { font-size: 15px; line-height: 19px; font-weight: 600; color: var(--text-2); } .rdy-i span { font-size: 13px; line-height: 17px; color: var(--medium); }
.done p + .lk, .done .pc { width: 100%; text-align: left; margin-top: 20px; }
.buy .pc { margin: 0 0 16px; }
.buy ol { margin: 0; padding-left: 20px; display: grid; gap: 10px; font-size: 14px; line-height: 20px; color: var(--medium); } .buy ol strong { color: var(--text); font-weight: 600; }
.buycard { background: #fcfcfc; box-shadow: inset 0 0 0 .5px var(--line); border-radius: 16px; margin-bottom: 16px; }
.buycard .pc { margin: 0; background: none; box-shadow: none; }
.buycard-l { border-top: .5px solid var(--line); padding: 12px 16px; } .buycard-l .olink { margin: 0; }
'''
head = head.replace('</style>', css + '</style>', 1)

js = r'''const ic24 = (f) => `<img src="${f}" width="24" height="24" alt="">`;
const VIDEO = [
  [ic24('m/ck-say.svg'), 'Say it the right way', 'I said <strong>Phyla</strong> (FYE-luh) and <strong>phage</strong> (FAYJ, rhymes with “page”).'],
  [ic24('m/ck-medical.svg'), 'No medical claims', "I didn't say it cures or treats acne."],
  [ic24('m/ck-target.svg'), 'Mention Target', 'I said you can get it at Target.'],
  [ic24('m/ck-bright.svg'), 'Clear, bright shot', 'Good lighting, and the bottle is easy to see.'],
  [ic24('m/ck-tag.svg'), 'Tag the brand', "I'll tag <strong>@phylaskin</strong> in my post and my story."],
];
/* [name, not in Figma yet] */
const NAMES = [['Campaigns'], ['Opportunity'], ['Before you join'], ['Store or online'], ['Time to shop', 1], ['Receipt'], ['Upload content'], ['Good to post', 1], ['Time to post'], ['Done', 1], ['Share your link']];
const fresh = () => ({ s: 0, sheet: null, join: [0,0,0,0], how: '', rc: 0, vid: [0,0,0,0,0], items: [], add: null, links: ['', '', ''], extra: 0 });
let S = fresh();

const fhdr = (n) => `<div class="fh"><button class="bk" data-back aria-label="Back"><img src="m/ic-chev-left.svg" width="16" height="16" alt=""></button><button class="vb" data-sheet="brief">View Brief</button></div><div class="stp" role="img" aria-label="Step ${n} of 4">${[1,2,3,4].map(i => `<i class="${i <= n ? 'on' : ''}"></i>`).join('')}</div>`;
const ffoot = (label, ok, attrs) => `<div class="ffoot"><div class="due"><div><small>Upload post by</small><b>Monday, Dec 14</b></div><span class="pill">10 days left</span></div><button class="cta full" ${attrs} ${ok ? '' : 'disabled'}>${label}</button><div class="home"></div></div>`;
const cks = (list, vals, key) => `<div class="ag" role="group">${list.map(([ic, t, d], i) => `<button class="ag-row" role="checkbox" aria-checked="${!!vals[i]}" data-ck="${key}:${i}">${ic}<span class="ag-t"><b>${t}</b><span>${d}</span></span><span class="ag-ck"><img src="m/ag-check.svg" width="24" height="24" alt=""></span></button>`).join('')}</div>`;
const agHead = (title, vals, cls) => `<div class="ag-h ${cls || ''}"><b>${title}</b><span>${vals.filter(Boolean).length}/${vals.length}</span></div>`;
const pcard = `<div class="pc"><img src="m/sheet-thumb.jpg" alt=""><div><b>Acne Phage Serum</b><span>Phyla</span><em><strong>$55</strong> value · Fully reimbursed</em></div></div>`;
const TARGET_URL = 'https://www.target.com/s?searchTerm=phyla+acne+phage+serum';
const tlink = `<a class="olink" href="${TARGET_URL}" target="_blank" rel="noopener">See it on Target.com<svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h6v6M12 4l-7.5 7.5"/></svg></a>`;

const TYPES = ['Instagram Post', 'Instagram Story', 'TikTok'];
const SHORT = { 'Instagram Post': 'IG Post', 'Instagram Story': 'IG Story', 'TikTok': 'TikTok' };
/* rule (Julia, Nov 25): an Instagram post AND an Instagram story, OR one TikTok */
const has = (ty) => S.items.some(i => i.type === ty);
const tt = () => has('TikTok'), ig = () => has('Instagram Post') || has('Instagram Story');
const need = () => tt() ? 1 : 2;
const done = () => tt() || (has('Instagram Post') && has('Instagram Story'));
const blocked = (ty) => has(ty) ? 'Added' : (ty === 'TikTok' && ig()) ? 'Instagram chosen' : (ty !== 'TikTok' && tt()) ? 'TikTok chosen' : '';
const ring = (f) => `<svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><circle cx="9" cy="9" r="7" stroke="#e3e3e3" stroke-width="2"/>${f > 0 ? `<circle cx="9" cy="9" r="7" stroke="#2caf87" stroke-width="2" stroke-linecap="round" stroke-dasharray="${(f * 43.98).toFixed(1)} 44" transform="rotate(-90 9 9)"/>` : ''}</svg>`;
const thumbOf = (t) => t === 'Instagram Post' ? 'm/video.jpg' : 'm/video2.jpg';
const TAGS = ['@phylaskin', '#target'];
const esc = (x) => x.replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
const capHtml = (x) => esc(x).replace(/(@[\w.]+)/g, '<span class="at">$1</span>').replace(/(#\w+)/g, '<span class="hash">$1</span>');
const hasTag = (g) => S.add.cap.toLowerCase().includes(g);
const CAPS = { 'Instagram Post': '@phylaskin Trying the Acne Phage Serum (phage rhymes with page). Picked it up at Target, and my skin feels calm. #target', 'Instagram Story': '@phylaskin Day 3 with the Acne Phage Serum. Found it at Target! #target', 'TikTok': '@phylaskin One week with the Acne Phage Serum from Target. Honest thoughts. #target' };
const isStory = (ty) => ty === 'Instagram Story'; /* stories have no caption field: tag, hashtag and link go on the story itself */
const addOk = () => S.add && S.add.file && S.add.type && (isStory(S.add.type) || TAGS.every(hasTag));
const addScreen = () => `${SB}<div class="hdr"><button class="ib" data-act="add-x" aria-label="Close"><img src="m/ic-close.svg" width="16" height="16" alt=""></button><div class="t">Add Content</div><span></span></div>
    <div class="scroll pg"><div class="ac">
      <div class="ac-card"><b>Upload Content</b><div class="ac-tiles">${S.add.file ? `<div class="ac-tile"><img src="${thumbOf(S.add.type)}" alt=""><button class="ac-act" data-act="add-file-x" aria-label="Remove video"><img src="m/ic-close-12.svg" width="12" height="12" alt=""></button></div>` : `<button class="ac-tile ac-tile--add" data-act="add-file" aria-label="Choose a video"><span class="ac-act c"><img src="m/ic-plus-12.svg" width="12" height="12" alt=""></span></button>`}</div></div>
      <button class="ac-card ac-type" data-sheet="ctype"><b>Content Type</b><span>${S.add.type || 'Select type'}</span><img src="m/ic-chev-down.svg" width="16" height="16" alt=""></button>
      ${isStory(S.add.type) ? `<div class="ac-card"><b>On Your Story</b><p class="ac-sub">Stories have no caption. Add these on the story itself, as text or stickers:</p><div class="ac-chips">${TAGS.map(g => `<span class="ac-chip">${g}</span>`).join('')}<span class="ac-chip">Link sticker</span></div></div>` : `<div class="ac-card"><b>Add Your Caption</b><p class="ac-sub">Make sure to include the <strong>tag</strong> and the <strong>hashtag</strong></p>
        <div class="ac-chips">${TAGS.map(g => `<span class="ac-chip${hasTag(g) ? ' ok' : ''}" data-tag="${g}"><img src="m/ic-check-12.svg" width="12" height="12" alt="">${g}</span>`).join('')}</div>
        <textarea id="cap" rows="4" placeholder="Write your draft caption here…">${esc(S.add.cap)}</textarea></div>`}
    </div></div>
    <div class="foot" style="padding:12px 16px 0;box-shadow:none;background:var(--page)"><button class="cta full" id="save" data-act="add-save" style="margin-bottom:16px;font-size:14px" ${addOk() ? '' : 'disabled'}>Save</button><div class="home"></div></div>`;
const postOk = () => S.items.length > 0 && S.items.every((_, i) => S.links[i].length > 5) && (!S.extra || S.links[2].length > 5);
const linkCard = (label, i, draft) => `<div class="lk"><div class="lk-h"><b>${label}</b>${draft ? `<button class="dr" data-toast="Opens the video you uploaded"><img src="m/ic-eye.svg" width="16" height="16" alt="">My Draft</button>` : ''}</div><input data-link="${i}" inputmode="url" aria-label="${label} link" placeholder="Paste your live link..." value="${S.links[i]}"></div>`;

'''

tail = src[i:]
# keep SCREENS 0-2 (campaigns, opportunity, join) from v1; rebuild the rest
a = tail.index('const SCREENS = ['); b = tail.index('  /* 3 how */')
screens012 = tail[a:b]
def r2(a_, b_):
    global screens012
    assert screens012.count(a_) == 1, a_[:50]
    screens012 = screens012.replace(a_, b_)
r2('The serum is $55 at Target. We pay back everything you paid, tax included, to your PayPal or Venmo after you post.', 'You receive $55 + tax directly to your PayPal or Venmo after you post.')
r2('Pick it up in store or order on target.com. Keep your receipt.', 'Pick it up in store or order on target.com.')
r2('One feed post and one story. We pay you back as soon as the posts are live.', 'An Instagram post and story, or one TikTok. We reimburse you as soon as they are live.')

rest = r'''  /* 3 how (16030:61975) */ () => `${SB}${fhdr(1)}<div class="scroll"><div class="fbody"><h2>How will you buy it?</h2><p class="lead">Tell us where you’ll buy the product! Next, buy it and save the receipt.</p>
      <div role="radiogroup" aria-label="Where you will buy it">${[['online', 'On target.com', 'Pickup or delivery. Your order confirmation is your receipt.', tlink], ['store', 'At a Target store', 'Find it in the Beauty Studio aisle. Keep your paper receipt.', '']].map(([k, t, d, extra]) => `<div class="opt2${S.how === k ? ' on' : ''}" role="radio" tabindex="0" aria-checked="${S.how === k}" data-how="${k}"><b>${t}</b><span>${d}</span>${extra}</div>`).join('')}</div>
    </div></div>${ffoot('Next', S.how, 'data-go="4"')}`,

  /* 4 go buy it: NOT in Figma, asked for on the Nov 25 call */ () => `${SB}${fhdr(1)}<div class="scroll"><div class="fbody buy"><div class="in-h"><span class="rdy-ok"><svg width="28" height="28" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.5 8.4 6.6 11.3 12.5 4.9" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span><h2>You're in!</h2><p>Your spot in the Phyla collab is saved.</p></div><h2>Time to shop</h2><p class="lead">${S.how === 'online' ? 'Grab your serum on target.com whenever you like.' : 'Grab your serum at Target whenever you like.'}</p>
      ${pcard}
      <ol><li>${S.how === 'online' ? `<a class="ilink" href="${TARGET_URL}" target="_blank" rel="noopener">Order it on target.com<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h6v6M12 4l-7.5 7.5"/></svg></a>, for pickup or delivery.` : '<strong>Buy it in the Beauty Studio aisle</strong> at any Target store.'}</li><li><strong>${S.how === 'online' ? 'Screenshot your order confirmation' : 'Hold on to your receipt'}.</strong> You'll upload it in the next step.</li><li><strong>Come back here!</strong></li></ol>
    </div></div>${ffoot('I have my receipt', true, 'data-go="5"')}`,

  /* 5 receipt (16053:62287) + thumbnails and Add another kept from v1 */ () => `${SB}${fhdr(2)}<div class="scroll"><div class="fbody"><h2>Bought it? Add your receipt</h2><p class="lead lg">${S.how === 'online' ? 'A screenshot of your target.com order confirmation.' : 'A photo of your paper receipt.'}</p>
      ${S.rc ? `<div class="thumbs">${Array.from({ length: S.rc }, (_, i) => `<div class="th"><img src="${S.how === 'online' ? ['m/order-1.svg', 'm/order-2.svg'][i] : ['m/receipt-1.svg', 'm/receipt-2.svg'][i]}" alt="Receipt photo ${i + 1}"><button class="th-x" data-act="rx" aria-label="Remove photo ${i + 1}"><img src="m/ic-close.svg" width="10" height="10" alt=""></button></div>`).join('')}${S.rc < 2 ? `<button class="th-add" data-act="receipt" aria-label="Add a second photo"><svg width="18" height="18" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M8 3v10M3 8h10"/></svg><span>Add another</span></button>` : ''}</div>
        <p class="hint">${S.rc < 2 ? 'Long receipt? Add a second photo so everything is readable.' : '2 photos added.'}</p>`
      : `<button class="zone2" data-act="receipt"><img src="m/ic-share.svg" width="16" height="16" alt=""><b>Add receipt</b><span>Tap to upload a photo or a PDF</span></button>`}
      <div class="see"><h3>Make sure we can see</h3><ul><li>Target as the store.</li><li>Phyla Acne Phage Serum on the list.</li><li>The date and total paid.</li></ul></div>
    </div></div>${ffoot('Next', S.rc > 0, 'data-go="6"')}`,

  /* 6 upload content (16058:63090) + item cards, counter and Add Content kept from v1 */ () => S.add ? addScreen() : `${SB}${fhdr(3)}<div class="scroll"><div class="fbody uc">
      <div class="uc-h"><h2>Upload Content</h2><span class="uc-n">${S.items.length}/${need()}${ring(S.items.length / need())}</span></div>
      <p class="lead lg">Make sure to review the brief before making content!</p>
      <button class="rb" data-sheet="brief">Review campaign brief →</button>
      ${S.items.map((it, i) => `<div class="uc-item"><img class="uc-th" src="${thumbOf(it.type)}" alt=""><div class="uc-c"><div class="uc-top"><span class="uc-chip">${it.type}</span><button data-act="del:${i}" aria-label="Remove ${it.type}"><img src="m/ic-trash.svg" width="16" height="16" alt=""></button></div><p class="uc-cap">${isStory(it.type) ? '<span style="color:var(--medium)">Tag, hashtag and link go on the story itself.</span>' : capHtml(it.cap || '')}</p></div></div>`).join('')}
      ${!done() ? `<button class="zone2${S.items.length ? ' uc-zone2' : ''}" data-act="add"><img src="m/ic-share.svg" width="16" height="16" alt=""><b>Tap to upload content</b>${S.items.length ? '' : '<span>An Instagram post and story, or one TikTok</span>'}</button>` : ''}
    </div></div>${ffoot('Submit', done(), 'data-go="7"')}`,

  /* 7 good to post: NOT in Figma, asked for on the Nov 25 call */ () => `${SB}<div class="hdr"><span></span><div class="t">Phyla</div><span></span></div><div class="scroll"><div class="done">
      <div class="ring"><svg width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.5 8.4 6.6 11.3 12.5 4.9" stroke="#18906c" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <h2>You're good to post</h2><p>Your videos are in. Post them now, then come back with your links.</p>
      <div class="rdy">${S.items.map(it => `<div class="rdy-i"><img src="${thumbOf(it.type)}" alt=""><div><b>${it.type}</b><span>Checked against the brief</span></div><svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-label="Ready"><circle cx="12" cy="12" r="12" fill="#18906c"/><path d="M7.5 12.4 10.6 15.3 16.5 9" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>`).join('')}</div>
    </div></div><div class="foot" style="padding-top:14px"><button class="cta full" data-go="8" style="margin-bottom:16px;font-size:14px">Time to post</button><div class="home"></div></div>`,

  /* 8 time to post (16058:63177) + caption tags kept from v1 */ () => `${SB}${fhdr(4)}<div class="scroll"><div class="fbody"><h2>Time to Post!</h2><p class="lead lg">Post and make sure to give us the links here!</p>
      <div class="lk"><div class="lk-t"><b>Your affiliate link</b><span>Tap to copy. Add it to your Linktree or bio and include it in your story.</span></div>
        <button class="aff" data-toast="Link copied"><span><img class="t" src="m/aff-thumb.png" alt="">benable.com/a/phyla-maya</span><img src="m/ic-copy.svg" width="16" height="16" alt="Copy"></button></div>
      ${S.items.map((it, i) => linkCard(SHORT[it.type], i, true)).join('')}
      ${S.extra ? linkCard('Another link', 2, false) : `<button class="addl" data-act="more"><img src="m/ic-plus-16.svg" width="16" height="16" alt="">Add Another Link</button>`}
    </div></div>${ffoot('I’ve Published My Content', postOk(), 'data-go="9" id="submit"')}`,

  /* 9 done: NOT in Figma. Celebration, then on to Share your link */ () => `${SB}<div class="scroll"><div class="yay">
      <div class="confetti" aria-hidden="true">${[[18,8,'#7a5cfa',20],[62,2,'#e4ffa9',-30],[108,14,'#c05ff0',45],[150,0,'#18906c',10],[196,10,'#f3d55b',-20],[240,4,'#7a5cfa',60],[286,12,'#ffb199',-45],[322,2,'#18906c',25],[40,46,'#f3d55b',70],[88,58,'#18906c',-15],[262,52,'#c05ff0',35],[306,60,'#e4ffa9',-60],[10,96,'#ffb199',15],[334,104,'#7a5cfa',-35]].map(([x, y, c, r], k) => `<i style="left:${x}px;top:${y}px;background:${c};transform:rotate(${r}deg);${k % 3 === 0 ? 'border-radius:50%;width:8px;height:8px' : ''}"></i>`).join('')}</div>
      <div class="yay-ok"><svg width="30" height="30" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.5 8.4 6.6 11.3 12.5 4.9" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <h2>You did it! 🎉</h2>
      <p>Your posts are in. Thank you for sharing Phyla with your followers.</p>
      <div class="yay-pay"><small>Your money back</small><b>On its way to your PayPal</b><span>What you paid for the serum, tax included, in 1 to 3 business days.</span></div>
    </div></div><div class="foot" style="padding-top:14px"><button class="cta full" data-go="10" style="margin-bottom:16px;font-size:14px">Continue</button><div class="home"></div></div>`,

  /* 10 share your link (16009:68858) */ () => `${SB}<div class="hdr"><button class="ib" data-go="9" aria-label="Back"><img src="m/ic-chev-left.svg" width="16" height="16" alt=""></button><div class="t">Share your link</div><span></span></div>
    <div class="scroll pg"><div class="shl">
      <div class="shl-h"><h2>Get Your Affiliate Link Out There</h2><p>The more you share your affiliate link, the more you earn!</p></div>
      <div class="shl-car"><img src="m/share-1.jpg" alt="Add it to your bio: paste your link into your bio on Instagram, TikTok or Linktree.">
        <div class="shl-c c2"><b>Add it to your story</b><span>Post a story and add your link with the link sticker.</span></div>
        <div class="shl-c c3"><b>Reply with it</b><span>When someone asks where you got it, paste your link in the reply.</span></div>
        <div class="shl-c c4"><b>Point to your bio</b><span>When someone asks in the comments, point them to your bio link or DM them the link.</span></div></div>
      <h3>Your Links</h3>
      <div class="shl-p"><div class="shl-img"><img src="m/product.jpg" alt="Phyla Acne Phage Serum bottle"></div><b>Phyla Acne Phage Serum</b>
        <button class="shl-l" data-toast="Link copied"><svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="#717171" stroke-width="1.5" stroke-linecap="round" aria-hidden="true"><path d="M6.7 9.3a3 3 0 0 0 4.2 0l2-2a3 3 0 0 0-4.2-4.2l-.7.7M9.3 6.7a3 3 0 0 0-4.2 0l-2 2a3 3 0 0 0 4.2 4.2l.7-.7"/></svg><span>benable.com/a/phyla-maya</span><em>Copy</em></button></div>
    </div></div><div class="foot" style="padding:12px 20px 0;box-shadow:none;background:var(--page)"><button class="cta full" data-reset style="margin-bottom:16px;font-size:14px">Done</button><div class="home" style="background:var(--page)"></div></div>`,
];

'''
c = tail.index('const SHEETS = {'); d = tail.index('function render()')
sheets = tail[c:d]
s1 = sheets.index('  video: () =>'); s2 = sheets.index('  brief: () =>')
sheets = sheets[:s1] + r'''  ready: () => `<div class="rdy-s"><span class="rdy-ok"><svg width="28" height="28" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.5 8.4 6.6 11.3 12.5 4.9" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
      <h2>You're good to go</h2><p>Nice work. Now it's time to share it with your followers.</p></div>
    <div class="hiw rdy-next"><h3>Next</h3>
      <div class="hstep"><i>1</i><div><b>Post on your socials</b><span>${tt() ? 'Share your video on TikTok.' : 'Share your post and your story on Instagram.'}</span></div></div>
      <div class="hstep"><i>2</i><div><b>Copy links</b><span>You'll paste them for us on the next step.</span></div></div></div>
    <div class="sh-f"><button class="cta full" data-go="8">I'll post it now</button></div>`,
  video: () => `<div class="sh-c">Before you upload</div>${agHead('Check your video against the brief', S.vid, 'v')}${cks(VIDEO, S.vid, 'vid')}<div class="sh-f"><button class="cta full" data-act="checked" ${S.vid.every(Boolean) ? '' : 'disabled'}>Continue</button></div>`,
  ctype: () => `<h2 style="margin-bottom:8px">Content Type</h2>${TYPES.map(t => { const used = blocked(t); return `<button class="ct-opt${S.add && S.add.type === t ? ' on' : ''}" data-act="type:${t}" ${used ? 'disabled' : ''}><i class="rd"></i><span>${t}</span>${used ? `<small>${used}</small>` : ''}</button>`; }).join('')}<div style="height:8px"></div>`,
''' + sheets[s2:]
sheets = sheets.replace('<li>Post one feed post and one story. Tag @phylaskin.</li>', '<li>Post on Instagram (one post and one story) or on TikTok (one video). Tag @phylaskin and add #target to your caption.</li>')
assert '#target' in sheets

logic = r'''function render() {
  const base = S.s === 2 ? 1 : S.s;
  const sheet = S.s === 2 ? 'join' : S.sheet;
  const el = document.getElementById('device');
  const keep = el.querySelector('.scroll')?.scrollTop || 0, same = el.dataset.s === String(base);
  el.dataset.s = base;
  el.innerHTML = SCREENS[base]() + (sheet ? `<div class="scrim" data-sheet=""></div><div class="sheet${sheet === 'brief' ? ' sheet--full' : ''}" role="dialog" aria-modal="true"><div class="grab"><img src="m/pull.svg" width="43" height="3" alt=""></div>${SHEETS[sheet]()}<div class="home"></div></div>` : '') + '<div class="toast" id="toast" role="status"></div>';
  if (same) { const sc = el.querySelector('.scroll'); if (sc) sc.scrollTop = keep; if (sheet) el.querySelectorAll('.scrim, .sheet').forEach(n => n.style.animation = 'none'); }
  document.getElementById('rail').innerHTML = NAMES.map(([n, isNew], i) => `<button class="s" data-jump="${i}" aria-current="${S.s === i}"><span>${i + 1}</span>${n}${isNew ? '<em>new</em>' : ''}</button>`).join('');
}
function openAdd() { const left = TYPES.filter(t => !blocked(t)); S.add = { file: false, type: left[0] || '', cap: '' }; }
function toast() {} /* toasts removed (Julia, Nov 25) */

document.addEventListener('click', (e) => {
  const q = (s) => e.target.closest(s); let el;
  if ((el = q('[data-jump]'))) { const n = +el.dataset.jump; S = fresh(); S.s = n; if (n >= 3) S.join = [1,1,1,1]; if (n >= 4) S.how = 'online'; if (n >= 6) S.rc = 1; if (n >= 7) { S.vid = [1,1,1,1,1]; S.items = [{ type: 'Instagram Post', cap: CAPS['Instagram Post'] }, { type: 'Instagram Story', cap: '' }]; } if (n >= 9 && n < 99) S.links = ['instagram.com/reel/DfQ2x9', 'instagram.com/stories/maya.glows', '']; render(); return; }
  if (q('[data-reset]')) { S = fresh(); render(); return; }
  if ((el = q('[data-go]'))) { if (el.disabled) return; S.s = +el.dataset.go; S.sheet = null; S.add = null; const m = el.dataset.toast; render(); if (m) toast(m); return; }
  if (q('[data-back]') && S.add) { S.add = null; render(); return; }
  if (q('[data-back]')) { S.s = S.s === 3 ? 1 : S.s === 8 || S.s === 7 ? 6 : S.s - 1; S.sheet = null; render(); return; }
  if ((el = q('[data-ck]'))) { const [k, i] = el.dataset.ck.split(':'); S[k][+i] = S[k][+i] ? 0 : 1; render(); return; }
  if (q('.olink') || q('.ilink')) return;
  if ((el = q('[data-how]'))) { S.how = el.dataset.how; render(); return; }
  if ((el = q('[data-sheet]'))) { const v = el.dataset.sheet; if (v === 'join') S.s = 2; else if (S.s === 2 && !v) S.s = 1; else S.sheet = v || null; render(); return; }
  if ((el = q('[data-act]'))) { const a = el.dataset.act;
    if (a === 'receipt') { S.rc = Math.min(2, S.rc + 1); render(); }
    else if (a === 'rx') { S.rc = Math.max(0, S.rc - 1); render(); }
    else if (a === 'add') { if (S.vid.every(Boolean)) openAdd(); else S.sheet = 'video'; render(); }
    else if (a === 'checked') { S.sheet = null; openAdd(); render(); }
    else if (a === 'add-x') { S.add = null; render(); }
    else if (a === 'add-file') { S.add.file = true; if (!S.add.cap && !isStory(S.add.type)) S.add.cap = CAPS[S.add.type] || ''; render(); }
    else if (a === 'add-file-x') { S.add.file = false; render(); }
    else if (a.startsWith('type:')) { S.add.type = a.slice(5); S.sheet = null; render(); }
    else if (a === 'add-save') { if (!addOk()) return; S.items.push({ type: S.add.type, cap: isStory(S.add.type) ? '' : S.add.cap }); S.add = null; render(); }
    else if (a.startsWith('del:')) { S.items.splice(+a.slice(4), 1); render(); }
    else if (a === 'more') { S.extra = 1; render(); }
    return; }
  if ((el = q('[data-toast]'))) toast(el.dataset.toast);
});
document.addEventListener('input', (e) => { if (e.target.id === 'cap' && S.add) { S.add.cap = e.target.value; document.getElementById('save').disabled = !addOk(); document.querySelectorAll('[data-tag]').forEach(c => c.classList.toggle('ok', hasTag(c.dataset.tag))); return; } const k = e.target.dataset.link; if (k !== undefined) { S.links[+k] = e.target.value; const b = document.getElementById('submit'); if (b) b.disabled = !postOk(); } });
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && (S.sheet || S.s === 2)) { if (S.s === 2) S.s = 1; S.sheet = null; render(); } if ((e.key === 'Enter' || e.key === ' ') && e.target.dataset && e.target.dataset.how) { e.preventDefault(); S.how = e.target.dataset.how; render(); } });
render();
</script>
</body>
</html>
'''
out = head + js + screens012 + rest + sheets + logic
pathlib.Path('creator-v2.html').write_text(out, encoding='utf-8')
print(len(out))
