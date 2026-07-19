/* 四季主題：預設依日期自動（3–5 春、6–8 夏、9–11 秋、12–2 冬），
   可經 header 按鈕手動切換並記住（auto → 春 → 夏 → 秋 → 冬 → auto）。
   與 theme.js 同款做法：在 <head> 同步執行設定 data-season，避免載入閃爍。
   冬季另在 body 動態生成全站飄雪層（reduced-motion 一律不生成）。

   二十四節氣（2026-07 起）：在四季之上再設 data-jieqi 做輕量色彩微調
   （global.css 只覆寫 sky/leaf/accent，背景圖等重資產仍走四季）。
   日期表為 2026–2035 年 JST 實際節氣日（sxtwl 天文計算預產），表外年份
   借用最近一年（節氣逐年僅 ±1 天，UI 換色無妨）。手動切季時節氣採
   該季「月份窗」的第一個節氣（春=驚蟄、夏=芒種、秋=白露、冬=大雪），
   與 byDate 的 3–5／6–8／9–11／12–2 月份窗一致。
   首頁 hero 的節氣標示（#jieqi-mark）也由本檔填字：漢字名（依語系，
   ja=啓蟄、ko=한글）＋直排起始日＋英文小 caps。 */
(function () {
  var KEY = 'rpw-season', d = document.documentElement;
  var SEASONS = ['spring', 'summer', 'autumn', 'winter'];
  var ICONS = { spring: '🌸', summer: '🌻', autumn: '🍂', winter: '❄️' };
  var reduced = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── 二十四節氣 ──────────────────────────────────────────────
     JQ_SLUGS 依年內順序（1 月小寒起）；JQ_MONTHS 為各節氣固定月份；
     JQ_DAYS[年] 為該年 24 個節氣的日（JST）。 */
  var JQ_SLUGS = ['xiaohan', 'dahan', 'lichun', 'yushui', 'jingzhe', 'chunfen',
    'qingming', 'guyu', 'lixia', 'xiaoman', 'mangzhong', 'xiazhi',
    'xiaoshu', 'dashu', 'liqiu', 'chushu', 'bailu', 'qiufen',
    'hanlu', 'shuangjiang', 'lidong', 'xiaoxue', 'daxue', 'dongzhi'];
  var JQ_MONTHS = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12];
  var JQ_DAYS = {
    2026: [5, 20, 4, 19, 5, 20, 5, 20, 5, 21, 6, 21, 7, 23, 7, 23, 7, 23, 8, 23, 7, 22, 7, 22],
    2027: [5, 20, 4, 19, 6, 21, 5, 20, 6, 21, 6, 21, 7, 23, 8, 23, 8, 23, 8, 24, 8, 22, 7, 22],
    2028: [6, 20, 4, 19, 5, 20, 4, 19, 5, 20, 5, 21, 6, 22, 7, 22, 7, 22, 8, 23, 7, 22, 6, 21],
    2029: [5, 20, 3, 18, 5, 20, 4, 20, 5, 21, 5, 21, 7, 22, 7, 23, 7, 23, 8, 23, 7, 22, 7, 21],
    2030: [5, 20, 4, 18, 5, 20, 5, 20, 5, 21, 5, 21, 7, 23, 7, 23, 7, 23, 8, 23, 7, 22, 7, 22],
    2031: [5, 20, 4, 19, 6, 21, 5, 20, 6, 21, 6, 21, 7, 23, 8, 23, 8, 23, 8, 23, 8, 22, 7, 22],
    2032: [6, 20, 4, 19, 5, 20, 4, 19, 5, 20, 5, 21, 6, 22, 7, 22, 7, 22, 8, 23, 7, 22, 6, 21],
    2033: [5, 20, 3, 18, 5, 20, 4, 20, 5, 21, 5, 21, 7, 22, 7, 23, 7, 23, 8, 23, 7, 22, 7, 21],
    2034: [5, 20, 4, 18, 5, 20, 5, 20, 5, 21, 5, 21, 7, 23, 7, 23, 7, 23, 8, 23, 7, 22, 7, 22],
    2035: [5, 20, 4, 19, 6, 21, 5, 20, 6, 21, 6, 21, 7, 23, 8, 23, 8, 23, 8, 23, 7, 22, 7, 22]
  };
  /* 英文小 caps 行：設計元素、全語系相同（採通行譯名），不進 i18n */
  var JQ_EN = ['Minor cold', 'Major cold', 'The beginning of spring', 'Rain water',
    'The awakening of insects', 'The spring equinox', 'Pure brightness', 'Grain rain',
    'The beginning of summer', 'Grain buds', 'Grain in ear', 'The summer solstice',
    'Minor heat', 'Major heat', 'The beginning of autumn', 'The end of heat',
    'White dew', 'The autumn equinox', 'Cold dew', "Frost's descent",
    'The beginning of winter', 'Minor snow', 'Major snow', 'The winter solstice'];
  /* 手動切季 → 該季月份窗的第一個節氣 */
  var SEASON_JQ = { spring: 4, summer: 10, autumn: 16, winter: 22 };

  function jqDays(y) {
    return JQ_DAYS[y] || JQ_DAYS[y < 2026 ? 2026 : 2035];
  }
  /* 回傳 { i: 節氣索引, start: 起始日 Date }（訪客當地日期判斷，±1 天無妨） */
  function byDateJieqi(now) {
    var y = now.getFullYear(), days = jqDays(y);
    var i, start = null, idx = -1;
    for (i = 0; i < 24; i++) {
      var t = new Date(y, JQ_MONTHS[i] - 1, days[i]);
      if (now >= t) { idx = i; start = t; } else break;
    }
    if (idx < 0) {   /* 1 月頭幾天：仍在去年冬至 */
      var py = y - 1, pd = jqDays(py);
      return { i: 23, start: new Date(py, 11, pd[23]) };
    }
    return { i: idx, start: start };
  }

  function byDate() {
    var m = new Date().getMonth() + 1;
    return m >= 3 && m <= 5 ? 'spring' : m >= 6 && m <= 8 ? 'summer' : m >= 9 && m <= 11 ? 'autumn' : 'winter';
  }
  function pref() {
    var s = null;
    try { s = localStorage.getItem(KEY); } catch (e) {}
    return SEASONS.indexOf(s) >= 0 ? s : 'auto';
  }
  function label(p, s, jqName) {
    var T = window.T || {};
    var names = {
      spring: T.season_spring || 'Spring', summer: T.season_summer || 'Summer',
      autumn: T.season_autumn || 'Autumn', winter: T.season_winter || 'Winter'
    };
    var head = T.season_toggle || 'Season';
    var tail = names[s] + (jqName ? ' · ' + jqName : '');
    return p === 'auto'
      ? head + ' · ' + (T.season_auto || 'Auto') + '（' + tail + '）'
      : head + ' · ' + tail;
  }

  function updateSnow(s) {
    var box = document.getElementById('snowfall');
    if (s !== 'winter' || reduced) { if (box) box.remove(); return; }
    if (box || !document.body) return;
    box = document.createElement('div');
    box.id = 'snowfall'; box.className = 'snowfall';
    box.setAttribute('aria-hidden', 'true');
    var n = Math.max(18, Math.min(38, Math.round(innerWidth / 14)));
    for (var i = 0; i < n; i++) {
      var f = document.createElement('span');
      f.className = 'snowflake';
      var dur = 9 + Math.random() * 13;
      f.style.cssText =
        '--x:' + (Math.random() * 100).toFixed(1) + '%;' +
        '--sz:' + (3 + Math.random() * 4.5).toFixed(1) + 'px;' +
        '--dur:' + dur.toFixed(1) + 's;' +
        '--delay:-' + (Math.random() * dur).toFixed(1) + 's;' +   /* 負 delay：一載入天空就已有雪 */
        '--sway:' + (Math.random() * 120 - 60).toFixed(0) + 'px;' +
        '--o:' + (0.5 + Math.random() * 0.45).toFixed(2);
      box.appendChild(f);
    }
    document.body.appendChild(box);
  }

  /* 首頁 hero 節氣標示：漢字名＋英文 caps
     （起始日行已移除：入節日易被誤讀為今日日期，2026-07-20 作者裁定） */
  function updateMark(i) {
    var box = document.getElementById('jieqi-mark');
    if (!box) return;
    var T = window.T || {};
    var name = T['jq_' + JQ_SLUGS[i]];
    if (!name) return;   /* i18n 缺字串就不顯示（保險絲） */
    var el = function (id) { return document.getElementById(id); };
    if (el('jq-name')) el('jq-name').textContent = name;
    if (el('jq-en')) el('jq-en').textContent = JQ_EN[i];
    box.hidden = false;
  }

  function apply(p) {
    var s = p === 'auto' ? byDate() : p;
    d.dataset.season = s;
    var jq = p === 'auto' ? byDateJieqi(new Date()).i : SEASON_JQ[s];
    d.dataset.jieqi = JQ_SLUGS[jq];
    var T = window.T || {};
    var b = document.getElementById('season-toggle');
    if (b) {
      var span = b.querySelector('span') || b;
      span.textContent = ICONS[s];
      span.style.opacity = p === 'auto' ? '.72' : '1';   /* 自動模式：圖示稍淡作區別 */
      var t = label(p, s, T['jq_' + JQ_SLUGS[jq]] || '');
      b.title = t;
      b.setAttribute('aria-label', t);
    }
    updateSnow(s);
    updateMark(jq);
  }

  apply(pref());   /* head 階段：先定 data-season/data-jieqi（此時尚無 body，雪層與標示延後） */
  document.addEventListener('DOMContentLoaded', function () {
    apply(pref());
    var b = document.getElementById('season-toggle');
    if (!b) return;
    b.addEventListener('click', function () {
      var order = ['auto'].concat(SEASONS);
      var next = order[(order.indexOf(pref()) + 1) % order.length];
      try { next === 'auto' ? localStorage.removeItem(KEY) : localStorage.setItem(KEY, next); } catch (e) {}
      apply(next);
    });
  });
})();
