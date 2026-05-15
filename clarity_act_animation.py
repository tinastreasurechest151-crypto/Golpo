"""
Golpo Canvas (Golpo 2.0) Animation Script
Title:  The Clarity Act — Crypto's Game Changer
Style:  Sharpie
Orient: Vertical (1080x1920)
Pacing: Normal
Voice:  Male Happy & Upbeat
Length: 55 seconds
"""

import json
import os
import sys
import urllib.request
import urllib.error


# ---------------------------------------------------------------------------
# Canvas & project constants
# ---------------------------------------------------------------------------
PROJECT = {
    "title": "The Clarity Act — Crypto's Game Changer",
    "golpo_type": "canvas",
    "version": "2.0",
    "video_style": "sharpie",
    "orientation": "vertical",
    "resolution": {"width": 1080, "height": 1920},
    "frame_rate": 30,
    "duration_seconds": 55,
    "pacing": "normal",
}

VOICE = {
    "gender": "male",
    "tone": "happy_upbeat",
    "speed": 1.0,
    "pitch": 1.05,
    "volume": 1.0,
}

# ---------------------------------------------------------------------------
# Sharpie palette  (black-ink-on-white with accent highlights)
# ---------------------------------------------------------------------------
PALETTE = {
    "background":  "#FFFFFF",
    "ink":         "#1A1A1A",
    "accent_gold": "#F5A623",
    "accent_green":"#27AE60",
    "accent_red":  "#E74C3C",
    "accent_blue": "#2980B9",
    "accent_gray": "#7F8C8D",
}

SHARPIE_BRUSH = {
    "stroke_type":     "marker",
    "roughness":       0.65,
    "ink_spread":      0.3,
    "line_variation":  0.2,
    "fill_style":      "hatch",
}

# ---------------------------------------------------------------------------
# Text styles
# ---------------------------------------------------------------------------
TEXT_STYLES = {
    "headline": {
        "font_family":  "Permanent Marker",
        "font_size":    72,
        "color":        PALETTE["ink"],
        "stroke_color": PALETTE["ink"],
        "stroke_width": 2,
        "align":        "center",
        "animation":    "draw_on",
    },
    "body": {
        "font_family":  "Patrick Hand",
        "font_size":    52,
        "color":        PALETTE["ink"],
        "stroke_color": PALETTE["ink"],
        "stroke_width": 1,
        "align":        "center",
        "animation":    "draw_on",
    },
    "label_good": {
        "font_family":  "Permanent Marker",
        "font_size":    80,
        "color":        PALETTE["accent_green"],
        "stroke_color": PALETTE["accent_green"],
        "stroke_width": 3,
        "align":        "center",
        "animation":    "bounce_in",
    },
    "label_bad": {
        "font_family":  "Permanent Marker",
        "font_size":    80,
        "color":        PALETTE["accent_red"],
        "stroke_color": PALETTE["accent_red"],
        "stroke_width": 3,
        "align":        "center",
        "animation":    "bounce_in",
    },
    "cta": {
        "font_family":  "Permanent Marker",
        "font_size":    64,
        "color":        PALETTE["accent_gold"],
        "stroke_color": PALETTE["accent_gold"],
        "stroke_width": 2,
        "align":        "center",
        "animation":    "pulse",
    },
}

# ---------------------------------------------------------------------------
# Icon / illustration library (Sharpie-drawn SVG icons referenced by key)
# ---------------------------------------------------------------------------
ICONS = {
    "cowboy_hat":      "icons/cowboy_hat.svg",
    "gavel":           "icons/gavel.svg",
    "sec_shield":      "icons/sec_shield.svg",
    "cftc_shield":     "icons/cftc_shield.svg",
    "wall_street_bull":"icons/wall_street_bull.svg",
    "green_light":     "icons/green_light.svg",
    "vault_open":      "icons/vault_open.svg",
    "audit_clipboard": "icons/audit_clipboard.svg",
    "stablecoin":      "icons/stablecoin.svg",
    "no_interest":     "icons/no_interest.svg",
    "kyc_id_card":     "icons/kyc_id_card.svg",
    "privacy_broken":  "icons/privacy_broken.svg",
    "us_flag":         "icons/us_flag.svg",
    "question_mark":   "icons/question_mark.svg",
    "subscribe_bell":  "icons/subscribe_bell.svg",
}

# ---------------------------------------------------------------------------
# Scene definitions
# Each scene: start/end timestamps, narration, on-screen elements
# ---------------------------------------------------------------------------
SCENES = [
    # ------------------------------------------------------------------
    # Scene 1 — Hook  (0–7 s)
    # ------------------------------------------------------------------
    {
        "id":    "scene_01_hook",
        "start": 0.0,
        "end":   7.0,
        "background_color": PALETTE["background"],
        "transition_in":  "wipe_right",
        "transition_out": "wipe_right",
        "narration": (
            "Is the \"Wild West\" of crypto finally over? "
            "The CLARITY Act is here, and it's a game-changer."
        ),
        "elements": [
            {
                "type":     "icon",
                "asset":    ICONS["cowboy_hat"],
                "x": 540, "y": 700,
                "scale":    1.3,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 0.2, "duration": 1.2},
                "wobble":   True,
            },
            {
                "type":      "text",
                "style":     "headline",
                "content":   "Wild West\nof Crypto…",
                "x": 540, "y": 1000,
                "entrance":  {"animation": "draw_on", "delay": 1.4, "duration": 1.0},
            },
            {
                "type":      "text",
                "style":     "headline",
                "content":   "⚡ CLARITY ACT ⚡",
                "x": 540, "y": 1200,
                "color_override": PALETTE["accent_gold"],
                "entrance":  {"animation": "bounce_in", "delay": 3.0, "duration": 0.8},
            },
            {
                "type":     "underline_scribble",
                "x1": 160, "y1": 1250, "x2": 920, "y2": 1250,
                "color":    PALETTE["accent_gold"],
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 3.8, "duration": 0.5},
            },
            {
                "type":      "text",
                "style":     "body",
                "content":   "Game. Changer.",
                "x": 540, "y": 1380,
                "entrance":  {"animation": "draw_on", "delay": 4.5, "duration": 0.8},
            },
        ],
    },

    # ------------------------------------------------------------------
    # Scene 2 — SEC vs CFTC  (7–16 s)
    # ------------------------------------------------------------------
    {
        "id":    "scene_02_sec_cftc",
        "start": 7.0,
        "end":   16.0,
        "background_color": PALETTE["background"],
        "transition_in":  "wipe_right",
        "transition_out": "wipe_right",
        "narration": (
            "This law finally ends the \"Is it a security or a commodity?\" debate. "
            "It draws a clear line between the SEC and the CFTC."
        ),
        "elements": [
            {
                "type":      "text",
                "style":     "headline",
                "content":   "Security\nor\nCommodity?",
                "x": 540, "y": 500,
                "entrance":  {"animation": "draw_on", "delay": 0.2, "duration": 1.2},
            },
            {
                "type":     "icon",
                "asset":    ICONS["sec_shield"],
                "x": 270, "y": 900,
                "scale":    1.0,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 1.6, "duration": 1.0},
                "label":    {"text": "SEC", "style": "body", "y_offset": 160},
            },
            {
                "type":     "icon",
                "asset":    ICONS["cftc_shield"],
                "x": 810, "y": 900,
                "scale":    1.0,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 2.4, "duration": 1.0},
                "label":    {"text": "CFTC", "style": "body", "y_offset": 160},
            },
            {
                "type":     "divider_line",
                "x1": 540, "y1": 680, "x2": 540, "y2": 1120,
                "color":    PALETTE["accent_blue"],
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 3.4, "duration": 0.7},
            },
            {
                "type":     "icon",
                "asset":    ICONS["gavel"],
                "x": 540, "y": 1300,
                "scale":    1.1,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 4.2, "duration": 1.0},
            },
            {
                "type":      "text",
                "style":     "body",
                "content":   "CLARITY ACT\ndraws the line ✓",
                "x": 540, "y": 1530,
                "color_override": PALETTE["accent_blue"],
                "entrance":  {"animation": "draw_on", "delay": 5.2, "duration": 1.0},
            },
        ],
    },

    # ------------------------------------------------------------------
    # Scene 3 — The Good: Institutional Money  (16–24 s)
    # ------------------------------------------------------------------
    {
        "id":    "scene_03_good_institutions",
        "start": 16.0,
        "end":   24.0,
        "background_color": PALETTE["background"],
        "transition_in":  "wipe_right",
        "transition_out": "wipe_right",
        "narration": (
            "The Good? Massive institutional money. "
            "Wall Street has been waiting for \"permission\" to enter, "
            "and this is the green light."
        ),
        "elements": [
            {
                "type":      "text",
                "style":     "label_good",
                "content":   "✅ THE GOOD",
                "x": 540, "y": 340,
                "entrance":  {"animation": "bounce_in", "delay": 0.1, "duration": 0.6},
            },
            {
                "type":     "icon",
                "asset":    ICONS["wall_street_bull"],
                "x": 540, "y": 780,
                "scale":    1.4,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 0.8, "duration": 1.4},
            },
            {
                "type":      "text",
                "style":     "headline",
                "content":   "Massive\nInstitutional\nMoney 💰",
                "x": 540, "y": 1180,
                "entrance":  {"animation": "draw_on", "delay": 2.4, "duration": 1.0},
            },
            {
                "type":     "icon",
                "asset":    ICONS["green_light"],
                "x": 540, "y": 1530,
                "scale":    0.9,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 3.6, "duration": 0.8},
            },
            {
                "type":      "text",
                "style":     "body",
                "content":   "Wall Street gets\nthe GREEN LIGHT",
                "x": 540, "y": 1720,
                "color_override": PALETTE["accent_green"],
                "entrance":  {"animation": "draw_on", "delay": 4.4, "duration": 0.8},
            },
        ],
    },

    # ------------------------------------------------------------------
    # Scene 4 — The Good: Investor Protections  (24–33 s)
    # ------------------------------------------------------------------
    {
        "id":    "scene_04_good_protections",
        "start": 24.0,
        "end":   33.0,
        "background_color": PALETTE["background"],
        "transition_in":  "wipe_right",
        "transition_out": "wipe_right",
        "narration": (
            "It also adds investor protections — aimed at preventing "
            "the next FTX-style collapse — by requiring proof of reserves and audits."
        ),
        "elements": [
            {
                "type":      "text",
                "style":     "label_good",
                "content":   "✅ THE GOOD",
                "x": 540, "y": 300,
                "entrance":  {"animation": "bounce_in", "delay": 0.1, "duration": 0.5},
            },
            {
                "type":     "icon",
                "asset":    ICONS["vault_open"],
                "x": 300, "y": 750,
                "scale":    1.0,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 0.7, "duration": 1.0},
                "label":    {"text": "Reserves\nProof", "style": "body", "y_offset": 170},
            },
            {
                "type":     "icon",
                "asset":    ICONS["audit_clipboard"],
                "x": 780, "y": 750,
                "scale":    1.0,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 1.5, "duration": 1.0},
                "label":    {"text": "Audits\nRequired", "style": "body", "y_offset": 170},
            },
            {
                "type":      "text",
                "style":     "headline",
                "content":   "No More\nFTX-Style\nCollapses ❌",
                "x": 540, "y": 1250,
                "entrance":  {"animation": "draw_on", "delay": 2.6, "duration": 1.0},
            },
            {
                "type":     "strike_through",
                "label":    "FTX",
                "x": 540, "y": 1320,
                "width":    220,
                "color":    PALETTE["accent_red"],
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 3.7, "duration": 0.5},
            },
            {
                "type":      "text",
                "style":     "body",
                "content":   "Investor protections\nfinally encoded in law",
                "x": 540, "y": 1600,
                "entrance":  {"animation": "draw_on", "delay": 4.4, "duration": 1.0},
            },
        ],
    },

    # ------------------------------------------------------------------
    # Scene 5 — The Bad: No Yield on Stablecoins  (33–41 s)
    # ------------------------------------------------------------------
    {
        "id":    "scene_05_bad_stablecoins",
        "start": 33.0,
        "end":   41.0,
        "background_color": PALETTE["background"],
        "transition_in":  "wipe_right",
        "transition_out": "wipe_right",
        "narration": (
            "The Bad? It's a blow to \"Passive Income.\" "
            "The Act restricts stablecoins from paying interest or yield "
            "to keep banks happy."
        ),
        "elements": [
            {
                "type":      "text",
                "style":     "label_bad",
                "content":   "❌ THE BAD",
                "x": 540, "y": 300,
                "entrance":  {"animation": "bounce_in", "delay": 0.1, "duration": 0.5},
            },
            {
                "type":     "icon",
                "asset":    ICONS["stablecoin"],
                "x": 540, "y": 760,
                "scale":    1.3,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 0.7, "duration": 1.1},
            },
            {
                "type":     "icon",
                "asset":    ICONS["no_interest"],
                "x": 540, "y": 760,
                "scale":    1.6,
                "brush":    SHARPIE_BRUSH,
                "color_override": PALETTE["accent_red"],
                "entrance": {"animation": "draw_on", "delay": 1.9, "duration": 0.7},
            },
            {
                "type":      "text",
                "style":     "headline",
                "content":   "No Interest.\nNo Yield.\non Stablecoins",
                "x": 540, "y": 1200,
                "color_override": PALETTE["accent_red"],
                "entrance":  {"animation": "draw_on", "delay": 2.8, "duration": 1.0},
            },
            {
                "type":      "text",
                "style":     "body",
                "content":   "Banks > Passive Income 🏦",
                "x": 540, "y": 1530,
                "entrance":  {"animation": "draw_on", "delay": 4.0, "duration": 0.9},
            },
        ],
    },

    # ------------------------------------------------------------------
    # Scene 6 — The Bad: KYC & Privacy  (41–48 s)
    # ------------------------------------------------------------------
    {
        "id":    "scene_06_bad_kyc",
        "start": 41.0,
        "end":   48.0,
        "background_color": PALETTE["background"],
        "transition_in":  "wipe_right",
        "transition_out": "wipe_right",
        "narration": (
            "Plus, expect stricter KYC. "
            "Your privacy might take a hit as transactions move closer "
            "to the traditional banking grid. "
            "Innovation is staying in the US, but the \"anonymity\" era is fading."
        ),
        "elements": [
            {
                "type":      "text",
                "style":     "label_bad",
                "content":   "❌ THE BAD",
                "x": 540, "y": 300,
                "entrance":  {"animation": "bounce_in", "delay": 0.1, "duration": 0.5},
            },
            {
                "type":     "icon",
                "asset":    ICONS["kyc_id_card"],
                "x": 300, "y": 780,
                "scale":    1.0,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 0.7, "duration": 1.0},
                "label":    {"text": "Stricter\nKYC", "style": "body", "y_offset": 160},
            },
            {
                "type":     "icon",
                "asset":    ICONS["privacy_broken"],
                "x": 780, "y": 780,
                "scale":    1.0,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 1.5, "duration": 1.0},
                "label":    {"text": "Privacy\nHit", "style": "body", "y_offset": 160},
            },
            {
                "type":     "icon",
                "asset":    ICONS["us_flag"],
                "x": 540, "y": 1280,
                "scale":    0.95,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "draw_on", "delay": 2.6, "duration": 1.0},
            },
            {
                "type":      "text",
                "style":     "body",
                "content":   "Innovation stays 🇺🇸\nbut anonymity fades…",
                "x": 540, "y": 1530,
                "entrance":  {"animation": "draw_on", "delay": 3.7, "duration": 1.0},
            },
        ],
    },

    # ------------------------------------------------------------------
    # Scene 7 — CTA  (48–55 s)
    # ------------------------------------------------------------------
    {
        "id":    "scene_07_cta",
        "start": 48.0,
        "end":   55.0,
        "background_color": PALETTE["background"],
        "transition_in":  "wipe_right",
        "transition_out": "fade_out",
        "narration": (
            "Is this a win or a killjoy for crypto? "
            "Drop a comment and subscribe for the latest!"
        ),
        "elements": [
            {
                "type":     "icon",
                "asset":    ICONS["question_mark"],
                "x": 540, "y": 550,
                "scale":    1.5,
                "brush":    SHARPIE_BRUSH,
                "entrance": {"animation": "bounce_in", "delay": 0.2, "duration": 0.7},
            },
            {
                "type":      "text",
                "style":     "headline",
                "content":   "Win or Killjoy\nfor Crypto? 🚀",
                "x": 540, "y": 900,
                "entrance":  {"animation": "draw_on", "delay": 1.0, "duration": 1.0},
            },
            {
                "type":      "text",
                "style":     "cta",
                "content":   "💬 Drop a\nComment!",
                "x": 540, "y": 1200,
                "entrance":  {"animation": "bounce_in", "delay": 2.2, "duration": 0.7},
            },
            {
                "type":     "icon",
                "asset":    ICONS["subscribe_bell"],
                "x": 540, "y": 1520,
                "scale":    1.1,
                "brush":    SHARPIE_BRUSH,
                "color_override": PALETTE["accent_red"],
                "entrance": {"animation": "draw_on", "delay": 3.2, "duration": 0.8},
            },
            {
                "type":      "text",
                "style":     "cta",
                "content":   "🔔 SUBSCRIBE\nfor the Latest!",
                "x": 540, "y": 1720,
                "entrance":  {"animation": "pulse", "delay": 4.1, "duration": 0.7},
            },
        ],
    },
]

# ---------------------------------------------------------------------------
# Audio track (background music — lo-fi upbeat, ducked under voice)
# ---------------------------------------------------------------------------
AUDIO = {
    "background_music": {
        "style":   "lo_fi_upbeat",
        "bpm":     110,
        "volume":  0.18,
        "fade_in_seconds":  1.0,
        "fade_out_seconds": 2.0,
    },
    "voice_over": {
        **VOICE,
        "text_to_speech_engine": "golpo_tts_v2",
        "scenes": [s["narration"] for s in SCENES],
    },
    "sound_effects": [
        {"trigger": "scene_01_hook",          "sfx": "paper_swoosh",    "volume": 0.5},
        {"trigger": "scene_02_sec_cftc",      "sfx": "gavel_bang",      "volume": 0.6},
        {"trigger": "scene_03_good_institutions", "sfx": "cash_register", "volume": 0.5},
        {"trigger": "scene_04_good_protections",  "sfx": "lock_click",   "volume": 0.5},
        {"trigger": "scene_05_bad_stablecoins",   "sfx": "buzzer",       "volume": 0.55},
        {"trigger": "scene_06_bad_kyc",       "sfx": "shred_paper",     "volume": 0.5},
        {"trigger": "scene_07_cta",           "sfx": "notification_ding","volume": 0.6},
    ],
}

# ---------------------------------------------------------------------------
# Export settings
# ---------------------------------------------------------------------------
EXPORT = {
    "format":         "mp4",
    "codec":          "h264",
    "bitrate_kbps":   8000,
    "audio_bitrate":  "320k",
    "output_filename":"clarity_act_crypto_55s.mp4",
}

# ---------------------------------------------------------------------------
# Build full Golpo Canvas project payload
# ---------------------------------------------------------------------------
def build_project():
    return {
        "project":  PROJECT,
        "voice":    VOICE,
        "palette":  PALETTE,
        "brush":    SHARPIE_BRUSH,
        "scenes":   SCENES,
        "audio":    AUDIO,
        "export":   EXPORT,
    }


def save_project(path="clarity_act_project.json"):
    project = build_project()
    with open(path, "w") as fh:
        json.dump(project, fh, indent=2)
    print("Project saved to:", os.path.abspath(path))
    return project


def validate_timing(project):
    errors = []
    total = project["project"]["duration_seconds"]
    for scene in project["scenes"]:
        if scene["end"] > total:
            errors.append(
                "Scene '{}' ends at {}s — exceeds total {}s".format(
                    scene["id"], scene["end"], total
                )
            )
        if scene["start"] >= scene["end"]:
            errors.append(
                "Scene '{}' has start >= end ({} >= {})".format(
                    scene["id"], scene["start"], scene["end"]
                )
            )
    # verify full coverage (no gap between consecutive scenes)
    sorted_scenes = sorted(project["scenes"], key=lambda s: s["start"])
    for i in range(len(sorted_scenes) - 1):
        gap = sorted_scenes[i + 1]["start"] - sorted_scenes[i]["end"]
        if gap > 0.05:
            errors.append(
                "Gap of {:.2f}s between '{}' and '{}'".format(
                    gap, sorted_scenes[i]["id"], sorted_scenes[i + 1]["id"]
                )
            )
    return errors


def print_scene_summary(project):
    print("\n{} — Scene Breakdown".format(project["project"]["title"]))
    print("=" * 60)
    for scene in project["scenes"]:
        dur = scene["end"] - scene["start"]
        print(
            "  [{:05.2f}s – {:05.2f}s]  ({:.1f}s)  {}".format(
                scene["start"], scene["end"], dur, scene["id"]
            )
        )
    print("=" * 60)
    print("  Total:  {}s".format(project["project"]["duration_seconds"]))
    print(
        "  Style:  {} / {} / {}".format(
            project["project"]["video_style"],
            project["project"]["orientation"],
            project["project"]["pacing"],
        )
    )
    print(
        "  Voice:  {} {} @ speed {}\n".format(
            project["voice"]["gender"],
            project["voice"]["tone"],
            project["voice"]["speed"],
        )
    )


# ---------------------------------------------------------------------------
# Golpo Canvas render call
# ---------------------------------------------------------------------------
GOLPO_API_BASE = "https://api.golpoai.com/v2/canvas"

def render(project):
    api_key = os.environ.get("GOLPO_API_KEY", "")
    if not api_key:
        print("ERROR: GOLPO_API_KEY environment variable not set.")
        sys.exit(1)

    payload = json.dumps(project).encode("utf-8")
    req = urllib.request.Request(
        "{}/render".format(GOLPO_API_BASE),
        data=payload,
        headers={
            "Content-Type":  "application/json",
            "Authorization": "Bearer {}".format(api_key),
            "Accept":        "application/json",
        },
        method="POST",
    )

    print("Submitting to Golpo Canvas renderer…")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            job_id       = body.get("job_id", "—")
            status       = body.get("status", "—")
            download_url = body.get("download_url", "")
            eta          = body.get("eta_seconds", "—")

            print("  Job ID:   {}".format(job_id))
            print("  Status:   {}".format(status))
            print("  ETA:      {}s".format(eta))
            if download_url:
                print("  Download: {}".format(download_url))
            else:
                print("  [Render queued — check Golpo Studio dashboard for progress]")
            return body

    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        print("  HTTP {}: {}".format(exc.code, error_body))
        sys.exit(1)
    except urllib.error.URLError as exc:
        print("  Network error: {}".format(exc.reason))
        sys.exit(1)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    project = build_project()

    errors = validate_timing(project)
    if errors:
        print("TIMING ERRORS:")
        for e in errors:
            print("  •", e)
    else:
        print("Timing validation: OK")

    print_scene_summary(project)
    save_project()
    render(project)
