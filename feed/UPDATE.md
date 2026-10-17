# Weekly update (Thursdays 9:23 AM ET): routine prompt

Paste this as the `michael-levin-wiki-weekly-update` routine prompt:

> Refresh the Morphospace Levin tracker in the Michael-Levin repo (/workspace/levin-wiki; pull first).
> 1. Run `python3 feed/refresh.py`. It adds new YouTube videos, Crossref papers (ORCID 0000-0001-7292-8084) and thoughtforms.life posts to feed/latest.json.
> 2. X: with the X tool, read @drmichaellevin's original posts (user id 1467127267; exclude replies, reposts and #naturephotography) newer than the newest `post` in feed/latest.json. Add each one as {kind:"post", date, title: a short factual description quoting his words exactly, url, source:"X @drmichaellevin"}. Never paraphrase a claim as his.
> 3. For each new Levin-channel video with captions: write videos/YYYY-MM-DD-slug.md in the existing format (plain-language ideas plus word-for-word caption quotes), set its feed item's `page` to the slug, and update the topic hubs, whats-new.md and the companies tracker if anything changed.
> 4. Run `python3 site/build.py` and then `python3 site/check.py --links`. Any ERROR stops the run; fix it or report it. Never publish with errors.
> 5. Publish site/dist to the claimed here.now site `inner-breeze-5fr8` using the account key (`publish.sh site/dist --slug inner-breeze-5fr8`). Never publish anonymously. If the key fails, stop and report.
> 6. Commit and push, add a line to log.md, and report the new items with dates and links, the commit hash and the check output.
> Rules: never invent an item, date or quote; label preprints; keep the public site free of any personal name; private notes go to Command Central (wiki/projects/michael-levin-vision.md).
