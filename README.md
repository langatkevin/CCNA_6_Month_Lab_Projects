# CCNA 6-Month Lab Projects

This repo mirrors the "6-Month CCNA 200-301 Study Plan" so every lab, note, and Packet Tracer file sits in one place.

## Layout
- docs/reference/ keeps the PDF, a plain-text extract, plan_structure.json, and the simplified week_summaries.json.
- docs/roadmaps/monthly-roadmap.md lists each month with quick links to the week folders under labs/.
- labs/ contains Week 01 through Week 19. Every week has a lightweight README plus an empty lab log table ready for evidence.
- 	emplates/lab-log.md is a drop-in template for longer reports or change logs.
- scripts/ hosts helper scripts that rebuild the structure whenever the source plan changes.

## Suggested Daily Loop
1. Open docs/roadmaps/monthly-roadmap.md and jump to the current week folder.
2. Read the week README, run the listed labs, and record results in the log table (or copy 	emplates/lab-log.md for deeper notes).
3. Keep Packet Tracer files, configs, captures, and screenshots beside the week README for easy commits.

Push progress often:

`powershell
git status
git add .
git commit -m "Log Week 01 labs"
git push
`

## Rebuilding From The Study Plan
Drop an updated PDF into docs/reference/, then run:

`powershell
python scripts/extract_plan.py
python scripts/build_lab_structure.py
python scripts/build_roadmap.py
`

## Nice-to-Haves
- Create per-week configs/, captures/, or evidence/ folders if labs grow large.
- Add linting or formatting checks for configs and scripts.
- Track blockers or ideas in GitHub Issues, Discussions, or Projects to keep momentum high.
