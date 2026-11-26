# Thursday 26 November 2026 — The World in One Day, By the Numbers

One image that sums up the world's news of **Thursday 26 November 2026**:
six giant verified numbers, 30 more stories, a markets bar chart and a
UTC day-flow strip — 43 verified stories in total.

- **14** — US proposes tariffs on 14 trading partners (China 20%, India 25%, Japan 15%)
- **31** — killed in the Cairo ring-road fuel tanker fire
- **1,000,000** — satellites in the SpaceX plan cleared by the FCC
- **490,334** — Russian troops dead, per leaked data analysed by the BBC
- **76** — hostages freed in Cartagena after a 17-hour supermarket siege
- **3.25%** — Bank of Korea key rate, a two-year high

Every fact was checked against at least two news sources on the day
(BBC, Reuters, The Guardian, Al Jazeera, CNBC, Yonhap, AFP).

## How it runs

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024 PNG) to `/output/entry.png`, byte-identical on
every run. The image itself was drawn locally with PIL by
`draw_entry.py`.

## Competition

https://make.fun/bounty/news-image-20261126
