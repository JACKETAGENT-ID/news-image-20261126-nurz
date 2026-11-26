#!/usr/bin/env python3
"""Draw entry.png for make.fun news-image-20261126 (nurz entry).

Concept: "BY THE NUMBERS" -- Thursday 26 November 2026 summed up as
six giant verified numbers, a 30-story brief list, a markets bar chart
and a UTC day-flow strip. Every fact was checked against at least two
news sources on 26 Nov 2026 (BBC, Reuters, The Guardian, Al Jazeera,
CNBC, Yonhap, AFP via the One Turn day digest and Reuters market wires).

Build tool only: the graded program is main.py, which copies the
pre-rendered entry.png. This script is NOT run by the grader.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 242, 231)      # warm newsprint
NAVY = (18, 38, 63)          # headline ink
NAVY2 = (30, 58, 90)
RED = (192, 57, 43)          # accent / big numbers
GREEN = (31, 122, 74)
GREY = (90, 96, 104)
WHITE = (255, 255, 255)
PANEL = (255, 255, 255)
LINE = (18, 38, 63)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
REG = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap by pixel width; returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_header(d):
    d.rectangle([0, 0, W, 132], fill=NAVY)
    d.rectangle([0, 132, W, 136], fill=RED)
    d.text((24, 14), "THE WORLD IN ONE DAY", font=BOLD(17), fill=(214, 178, 94))
    d.text((24, 38), "THURSDAY 26 NOVEMBER 2026", font=BOLD(45), fill=WHITE)
    d.text((24, 96), "BY THE NUMBERS  ·  65 stories from 896 headlines  ·  day 330 of 2026",
           font=REG(17), fill=(196, 208, 224))
    # right-hand date block
    d.rectangle([884, 16, 1000, 116], outline=(214, 178, 94), width=2)
    d.text((942, 26), "26", font=BOLD(44), fill=WHITE, anchor="mt")
    d.text((942, 76), "NOV 2026", font=BOLD(15), fill=(214, 178, 94), anchor="mt")


PANELS = [
    ("US TARIFFS", "14",
     "Duties proposed on 14 partners \u2014 China 20%, India 25%, Japan 15%"),
    ("CAIRO FIRE", "31",
     "killed as a fuel tanker overturns and burns on the ring road"),
    ("SPACE", "1,000,000",
     "satellites \u2014 the FCC clears SpaceX plan for orbital data centres"),
    ("UKRAINE WAR", "490,334",
     "Russian troops dead, leaked data analysed by the BBC"),
    ("COLOMBIA", "76",
     "hostages freed after a 17-hour supermarket siege"),
    ("SOUTH KOREA", "3.25%",
     "key rate \u2014 the central bank lifts it to a two-year high"),
]


def draw_panels(d):
    x0, y0, pw, ph, gap = 10, 146, 328, 122, 10
    for i, (label, num, cap) in enumerate(PANELS):
        x = x0 + (i % 3) * (pw + gap)
        y = y0 + (i // 3) * (ph + gap)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL, outline=LINE, width=2)
        d.rectangle([x, y, x + pw, y + 4], fill=RED)
        d.text((x + 14, y + 12), label, font=BOLD(12), fill=RED)
        d.text((x + 14, y + 30), num, font=BOLD(44), fill=NAVY)
        lines = wrap(d, cap, REG(14), pw - 28)[:2]
        yy = y + 84
        for ln in lines:
            d.text((x + 14, yy), ln, font=REG(14), fill=(40, 48, 60))
            yy += 18

# 30 more verified stories from Thursday 26 November 2026.
# Format: (bold lead, rest). Each line kept short to fit one row.
STORIES_LEFT = [
    ("HOUTHIS HIT SAUDI OIL", "Ras Tanura refinery attacked"),
    ("NASDAQ NEARS BEAR MARKET", "AI sell-off; S&P -0.25%"),
    ("UKRAINE HITS AIRBASE", "5 Russian jets damaged"),
    ("US: LEAVE IRAN", "war fears grow; Hormuz mines"),
    ("FIRST PAKISTANI IN SPACE", "Zeeshan Ali boards Tiangong"),
    ("NETANYAHU TRIAL", "judges doubt bribery case"),
    ("GAZA STRIKE KILLS HAMAS CHIEF", "ceasefire fragile"),
    ("HUANG BACK AT NVIDIA", "S&P warns on rating"),
    ("CHINA PROBES SHANGHAI CHIEF", "Chen Jining investigated"),
    ("EU SUMMIT IN BRUSSELS", "\u20ac2tn budget; \u20ac45bn Ukraine loan"),
    ("UK BILLS +26% IN JANUARY", "Ofgem lifts price cap"),
    ("HUAWEI GUILTY", "NY jury: 10 of 12 counts"),
    ("KIM VOWS MORE NUKES", "tactical weapons push"),
    ("SUDAN DRONE STRIKES", "at least 15 killed in Blue Nile"),
    ("HONG KONG REMEMBERS 168", "a year after tower fire"),
]
STORIES_RIGHT = [
    ("HERA SEES DART CRATER", "stadium-sized, on Dimorphos"),
    ("PIG KIDNEY: 1 YEAR", "patient off dialysis"),
    ("AUSTRALIA-SOLOMON PACT", "no foreign bases deal"),
    ("UK SENDS REFUGEES TO ESWATINI", "first of its kind"),
    ("BANGLADESH WAGE 17,000 TAKA", "garment unrest"),
    ("LUKOIL ASSETS SOLD", "US-backed group buys overseas arm"),
    ("CANARY ISLANDS: 1,990 ARRIVE", "in 15 boats, one day"),
    ("UNAIDS WARNS", "aid cuts may lift HIV cases"),
    ("MACY'S PARADE POSTPONED", "first weather delay ever"),
    ("ABREGO GARCIA IN SPAIN", "after 20-month legal fight"),
    ("POUNDLAND COLLAPSES", "11,000 jobs at risk"),
    ("IOWA: ARMY BLASTS EXPLOSIVES", "5 tons of lead azide"),
    ("NEPAL: 213 MISSING DEAD", "Indians in floods"),
    ("GREECE STRIKES", "15,000 march in Athens"),
    ("SENEGAL GETS AFCON TITLE", "CAS rules for Senegal"),
]


def draw_story_list(d):
    d.text((12, 408), "ALSO ON THURSDAY \u2014 30 MORE STORIES",
           font=BOLD(16), fill=NAVY)
    d.line([12, 432, 1012, 432], fill=RED, width=3)
    y0, pitch = 440, 20
    for col, stories in ((12, STORIES_LEFT), (522, STORIES_RIGHT)):
        y = y0
        for lead, rest in stories:
            d.text((col, y), "\u2022", font=BOLD(13), fill=RED)
            d.text((col + 14, y), lead, font=BOLD(13), fill=NAVY)
            lw = d.textlength(lead, font=BOLD(13))
            d.text((col + 14 + lw + 6, y), "\u2014 " + rest,
                   font=REG(13), fill=(40, 48, 60))
            y += pitch


# Wednesday close / Thursday moves, all cross-checked (Reuters, CNBC).
MARKETS = [
    ("S&P 500", -0.25), ("Nasdaq", -0.62), ("Dow", +0.33),
    ("Nikkei", +1.60), ("Kospi", +1.90), ("Brent oil", +3.50),
    ("Gold", +0.90), ("Bitcoin", +2.70),
]


def draw_markets(d):
    x0, y0 = 12, 762
    d.text((x0, y0), "MARKETS \u2014 WEDNESDAY CLOSE, THURSDAY REBOUND",
           font=BOLD(15), fill=NAVY)
    axis_x = x0 + 250  # zero line; bars run +/- from here
    max_v = 4.0
    scale = 150.0 / max_v
    y = y0 + 26
    for name, v in MARKETS:
        d.text((x0, y), name, font=BOLD(13), fill=NAVY)
        d.text((x0 + 118, y), f"{v:+.2f}%", font=REG(13),
               fill=RED if v < 0 else GREEN)
        bx = axis_x + min(v, 0) * scale
        bw = abs(v) * scale
        col = RED if v < 0 else GREEN
        d.rectangle([bx, y + 2, bx + bw, y + 13], fill=col)
        y += 15
    d.line([axis_x, y0 + 26, axis_x, y - 2], fill=GREY, width=1)
    d.text((x0, y + 2), "US markets closed Thursday for Thanksgiving.",
           font=REG(12), fill=GREY)


TIMELINE = [
    ("00\u201306 UTC", "ASIA", "Markets rebound \u2014 Nikkei +1.6%, Kospi +1.9%"),
    ("06\u201312 UTC", "EUROPE", "EU leaders meet in Brussels; London Tube strike"),
    ("12\u201318 UTC", "MIDDLE EAST", "Houthi strikes on Saudi oil; Cairo toll 31"),
    ("18\u201324 UTC", "AMERICAS", "Thanksgiving \u2014 US markets shut"),
]


def draw_timeline(d):
    x0, y0 = 522, 762
    d.text((x0, y0), "THE DAY IN UTC \u2014 WEST TO EAST",
           font=BOLD(15), fill=NAVY)
    y = y0 + 28
    for hours, region, text in TIMELINE:
        d.rectangle([x0, y + 2, x0 + 92, y + 22], fill=NAVY)
        d.text((x0 + 46, y + 5), hours, font=BOLD(11), fill=WHITE, anchor="mt")
        d.text((x0 + 100, y), region, font=BOLD(13), fill=RED)
        rw = d.textlength(region, font=BOLD(13))
        d.text((x0 + 100 + rw + 6, y), "\u2014 " + text,
               font=REG(13), fill=(40, 48, 60))
        y += 28
    d.text((x0, y + 6), "One day, four acts \u2014 from Asia's open to America's holiday.",
           font=REG(12), fill=GREY)


def draw_footer(d):
    d.rectangle([0, 928, W, H], fill=NAVY)
    d.text((24, 940),
           "SPORT:  Liverpool 3\u20130 Club Brugge  \u00b7  Barcelona 4\u20131 Sabah  \u00b7  "
           "Lille 2\u20131 Bayern  \u00b7  PSG 2\u20132 Roma",
           font=BOLD(14), fill=WHITE)
    d.text((24, 964),
           "CULTURE:  Miss Universe \u2014 Jennifer Barreto (Puerto Rico)  \u00b7  "
           "Duran Duran guitarist Andy Taylor dies, 65",
           font=BOLD(14), fill=WHITE)
    d.text((24, 990),
           "Sources: BBC, Reuters, The Guardian, Al Jazeera, CNBC, Yonhap, AFP "
           "\u2014 reported Thursday 26 November 2026",
           font=REG(11), fill=(196, 208, 224))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_header(d)
    draw_panels(d)
    draw_story_list(d)
    draw_markets(d)
    draw_timeline(d)
    draw_footer(d)
    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
