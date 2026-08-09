"""Instagram shortcode normalization + extraction.

This module is the SINGLE source of truth for turning arbitrary text
(a submission cell, or a wiki file's frontmatter) into a normalized set
of Instagram post shortcodes. The inbox side and the wiki side MUST use
the exact same rules, otherwise the comparison is meaningless.

Rules (see SKILL.md step 2):
  1. Strip escaping backslashes first ("\\_" -> "_", etc.).
  2. Extract with the post regex, tolerating an optional account prefix
     segment and ignoring query strings (?igsh=, ?img_index=, ...).
  3. Shortcodes may contain underscores and hyphens.
  4. A cell that contains instagram text but yields NO post shortcode
     (bare handle like "joy_redpanda", or a profile-only URL) is a data
     problem, surfaced separately by the caller via `has_ig_signal`.
"""

import re

# instagram.com/<optional-account>/(p|reel|tv)/<shortcode>
POST_RE = re.compile(
    r"instagram\.com/(?:[^/\s?]+/)?(?:p|reel|tv)/([A-Za-z0-9_-]+)",
    re.IGNORECASE,
)

# Any mention of instagram at all (used to tell "empty cell" apart from
# "cell has an ig handle / profile but no post URL").
IG_SIGNAL_RE = re.compile(r"instagram\.com|(?<![\w.])@[A-Za-z0-9_.]{2,}", re.IGNORECASE)


def normalize_text(text):
    """Remove escaping backslashes so "\\_" reads as "_" before matching."""
    if text is None:
        return ""
    # Drop every backslash; URLs never legitimately contain one, and this
    # collapses "\_", "\-", "\." share-text escaping into the real chars.
    return str(text).replace("\\", "")


def canonical_post_url(shortcode):
    """A stable, clickable link for a shortcode (used in reports)."""
    return f"https://www.instagram.com/p/{shortcode}/"


def extract_shortcodes(text):
    """Return the list of shortcodes in `text`, in order of appearance
    (duplicates preserved so callers can detect same-page repeats)."""
    cleaned = normalize_text(text)
    return [m.group(1) for m in POST_RE.finditer(cleaned)]


def has_ig_signal(text):
    """True if the text mentions instagram at all (url or @handle)."""
    return bool(IG_SIGNAL_RE.search(normalize_text(text)))
