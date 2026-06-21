# 批次 4 — 「報缺」回報處理 SOP（圖鑑還沒有的熊／園）

> 收到一筆從 `/feedback` 來的「報缺」回報後，照這份做。
> 一切遵循 `CLAUDE.md`：`wiki/*.md` 是唯一正本，回報只是提示，校訂後才寫入。
> 動物園名以 `data/zoos.json`（註冊表）為唯一事實來源。

---

## 為什麼要獨立一個入口（與批次 1–3 的差別）

批次 1–3 的回報都從**個體頁**的「✏️ 回報這頁資料／近況」按鈕來，靠 hidden fields（`panda`／`slug`／`url`）把「是哪一隻」帶進收件匣。**那套只能處理「已經存在的熊」。**

`/feedback` 補的是兩個缺口，都**沒有頁面、也沒有某一隻可以掛**：

1. **缺熊** — 圖鑑還沒收錄的個體：沒頁面、又沒親屬可掛的孤兒個體（父母不詳、海外／中國無血統紀錄等）。
2. **缺園** — 註冊表 `data/zoos.json` 還沒有的動物園。

因為個體頁按鈕一定針對「這一隻」，這類報缺**不能走它**（hidden field 會錯標、孤兒個體也無頁面可進）。所以 `/feedback` 改成「圖鑑還沒有的東西，在這裡告訴我們」的萬用入口，熊和園都收，用一張**不綁定某一隻**的獨立表單。

---

## 這類回報長什麼樣

從網站頁尾「🐾 回報圖鑑沒有的熊或動物園」連結進到 `/feedback`，內嵌一張**獨立的「報缺」Tally 表單**（與更正／近況的表單分開）。欄位：

| 欄位 | 說明 | 必填 |
|------|------|------|
| 類型 | 缺熊 / 缺園（單選）| ✅ |
| 名稱 | 熊的名字或動物園名（簡稱也可）| ✅ |
| RPF 或官網連結 | Red Panda Finder profile 或動物園官網 | ⬜（強烈建議）|
| 補充 | 父母、現居園、出生年、別名等任何線索 | ⬜ |
| 暱稱 | 想被列入致謝可留 | ⬜ |

> 沒有 hidden field（缺熊無頁面、缺園不屬於任何一隻）。隱私：不強制 email，致謝用暱稱。
> 三語各一張表（zh／ja／en），可見欄位、選項完全一致，只差文字語言。**改一處要三張一起改。**

收件匣與批次 1–3 共用同一個信箱／Google Sheet，作者逐筆審核。

---

## 步驟 0：分流（缺熊 or 缺園）

看「類型」欄。缺熊走 §A，缺園走 §B。一筆同時報「某園的某隻新熊」很常見：**先處理園（§B 把園登記好），再處理熊（§A）**，否則建熊條目時 `build_db.py` 會因園名未登記而中止。

## 步驟 1：紅綠燈分級（兩類通用）

| 燈號 | 條件 | 動作 |
|------|------|------|
| 🟢 綠 | 有可信來源（RPF profile／動物園官網／官方社群／新聞）可查證 | 進對應流程 |
| 🟡 黃 | 只有名字沒連結、或來源是「我記得／聽說」、或簡稱對不準 | 自己查 RPF／官網補實，查到升🟢、查不到暫不建 |
| 🔴 紅 | 無來源又查無此熊／此園，或明顯灌水／與既有資料矛盾 | 收件匣標「退回＋原因」，**不動 wiki／zoos.json** |

> 報缺寧缺勿濫：查不到可信來源就維持🟡回問，別憑印象硬建。父母不詳沒關係（缺熊本來就常見孤兒），但「這隻熊真的存在」要有依據。

---

## §A 缺熊 → 走 CLAUDE.md「新增成員流程」

確認🟢後，照 `CLAUDE.md`〈新增成員流程〉做，重點：

1. 有 RPF 連結 → 優先用 **`rpf-wiki` skill** 從 RPF 抓資料建條目（RPF 不標性別，需從 Mother／Father／daughters／sons 推斷）。沒有 RPF、只有官網／新聞 → 手動依 `SCHEMA.md` 建。
2. 建 `wiki/<名字-生日>.md`（slug＝名字-生日；只知年份就用 `YYYY`；撞名再加媽媽名消歧，見 `CLAUDE.md`）。
3. **父母不詳就先留空**（frontmatter 欄位空著、`sex` 不確定也留空並備注「待確認」）。孤兒個體不必硬湊親屬。
4. 有已知直系親屬且本身缺條目的，照流程一併補建（父→母→雙胞胎→子女），並回頭把既有條目的純文字親屬改成 `[[wikilink]]`。
5. 居住史只寫 frontmatter `zoos:`（canonical 日文全名，格式 `園名 (起 – 訖)`）。**若該園還沒登記，先做 §B。**
6. 更新 `wiki/index.md`（分類、頁首「最後更新」與「條目總數」）。
7. `wiki/log.md` 末端 append 一筆（名字用 backtick，**絕不用 `[[wikilink]]`**）。

### log 範例（缺熊）

```markdown
## [YYYY-MM-DD] add | 依 /feedback 報缺新增 `名字`

**來源**：
- https://redpandafinder.com/#profile/XXX (名字)

**新增條目**：
- `名字-生日.md` — 名字 日文名（RPF #XXX），生於 YYYY-MM-DD，現居 動物園
  （父母不詳，待確認）

**更新條目**：
- `index.md` — 新增 名字；條目總數更新為 N
```

---

## §B 缺園 → 先補 `data/zoos.json`，再（若有熊）建檔

`build_db.py` 對園名做**精確比對**，寫了註冊表沒有的名會**報錯中止**。所以缺園一定先登記。

### 步驟 B1：確認真的沒有

```bash
python tools/resolve_zoo.py <回報的園名或簡稱>
```

- ✅ 精準命中 → 其實已登記，可能只是回報者用了簡稱；不必新增，需要的話把簡稱補進 aliases（見 B3）。
- 🟡 多／單一候選 → 對照來源挑一個，可能是同園別名。
- 🔴 查無 → 確實是**新園**，走 B2。

### 步驟 B2：在 `data/zoos.json` 加一筆

陣列尾端 append 一個物件，欄位（對齊現有格式）：

```json
{
  "canonical": "○○市□□動物園",
  "lineage_id": null,
  "en": "Xxx Zoo",
  "zh": "某某動物園",
  "country": "Japan",
  "location_ja": "△△県△△市",
  "location_en": "Xxx, Xxx, Japan",
  "lat": 35.0000000,
  "lng": 139.0000000,
  "map": "https://goo.gl/maps/…",
  "website": "https://…",
  "logo": null,
  "aliases": ["回報用的簡稱"]
}
```

- `canonical`：**正式全名**，日本園用日文全名，對外顯示用這個；wiki 條目 `zoos:` 也一律寫這個。
- `lat`／`lng`：查官網／Google 地圖（lineage 僅供初次帶入，非權威）。
- 沒有的欄位填 `null`；`aliases` 把這次回報用的簡稱也放進去。

### 步驟 B3：驗證 + 養 aliases

```bash
python tools/resolve_zoo.py <新園名>          # 應變✅ 精準命中
python tools/resolve_zoo.py --add tama 多摩動物公園   # 把簡稱補進該園別名，下次就精準命中
```

> `resolve_zoo.py` 是缺園的**第二道網**：轉園省核（批次 2）時把簡稱對到 canonical，這裡確認新園登記正確、並把回報用的簡稱養進 aliases。

---

## 步驟 2：重建管線

改完 wiki／zoos.json 後（在 wiki 根目錄執行）：

```bash
python3 tools/gen_residence.py            # 依 zoos: 重生內文「## 居住史」表
python3 tools/build_db.py                 # 重建 DB（園名未登記會在這報錯）
python3 pipeline/scripts/export_json.py   # 重生網站資料
python tools/audit.py                     # 完整度檢查（缺欄位／與 lineage 不符提示）
```

`build_db.py` 沒報錯 = 園名都對得上註冊表。若報「未登記」就回 §B2。

---

## 步驟 3：驗收與收尾

- 缺熊：開新條目頁，確認引言／居住史／家族區塊正確；search 能搜到。
- 缺園：開動物園地圖頁，確認新園標記出現在座標、官網連結可點。
- 收件匣把該筆標「已處理」，要致謝就記下暱稱。
- 推 `main` → GitHub Actions 自動部署。

---

## 退回回報怎麼說（🔴 紅燈／查無依據）

語氣友善、說明資料以作者校訂為準。例：

> 謝謝回報！這隻／這座園我們想先確認一下——方便的話，麻煩附上 Red Panda Finder 連結或動物園官網，查證後就會加進圖鑑。資料都是人工校訂的，會需要一點時間，謝謝你 🙏

---

## 相關檔案

- `web/src/components/Feedback.astro` — `/feedback` 內嵌頁（標題／說明取自 i18n，表單用 `missingFormId`）
- `web/src/lib/feedback.js` — 表單 ID 設定（`MISSING_FORMS` = 報缺；`FEEDBACK_FORMS` = 個體頁更正）
- `web/src/layouts/Layout.astro` — 頁尾「報缺」連結（nav 維持 home/search/zoos 不動）
- `pipeline/src/i18n/{zh-TW,ja,en}.json` — `feedback_title`／`feedback_intro`／`feedback_footer_link`（三語同步）
- `data/zoos.json`、`tools/resolve_zoo.py` — 缺園登記與簡稱解析
- 既有流程參考：`docs/批次2-轉園處理SOP.md`、`docs/批次3-過世處理SOP.md`、`CLAUDE.md`〈新增成員流程〉

---

## 「報缺」Tally 表單（獨立一張，×三語）— 建置記錄

> 與批次 1–3 的「更正／近況」表分開的一張獨立表，**沒有 hidden field**。三語各一張。

| 語系 | 表單名 | 表單 ID | 公開網址 |
|------|--------|---------|----------|
| 中文 | 回報圖鑑沒有的熊或動物園 | `2EVJlb` | https://tally.so/r/2EVJlb |
| 日文 | 図鑑にいない子・動物園の報告 | `ODrJok` | https://tally.so/r/ODrJok |
| 英文 | Report a missing panda or zoo | `RG2JVv` | https://tally.so/r/RG2JVv |

可見欄位（三語一致，只差文字）：

| # | 題目 | 題型 | 必填 |
|---|------|------|------|
| 1 | 類型（缺熊／缺園）| 單選 | ✅ |
| 2 | 名稱（熊的名字或動物園名，簡稱也可）| 短答 | ✅ |
| 3 | Red Panda Finder 或官網連結 | 短答 | ⬜（強烈建議）|
| 4 | 補充（父母／現居園／出生年／別名等任何線索）| 長答 | ⬜ |
| 5 | 你的暱稱（想被列入致謝可留）| 短答 | ⬜ |

設定：表單語言設對應語系；新回報 email 通知開；不強制 email；連接同一個收件匣 Google Sheet。

> **發佈（Publish）屬公開變更，動手前先取得作者同意。** Tally 編輯走 Claude in Chrome（帳號 mumukuma）。
> 建好後把三張表的 ID 填進 `web/src/lib/feedback.js` 的 `MISSING_FORMS`；填好前 `/feedback` 會顯示「建置中」訊息（`feedback_setup`）。
> 維護提醒：三張表的欄位、選項、文案與 i18n 文案一律**同步**，改一處要三張表＋三語一起改。
