# CCNA 6-Month Lab Projects

A Git-ready home for every Packet Tracer build, config snippet, and write-up you create while following the "6-Month CCNA 200-301 Study Plan for Aspiring Network Engineers". The repo mirrors the reference document month-by-month so you can focus on learning instead of reorganizing notes.

## What's Inside
- docs/reference/ holds the original PDF, a text extract, and the parsed JSON outline used to build everything else.
- docs/roadmaps/monthly-roadmap.md gives a quick view of each month and links directly to the matching lab folders.
- labs/ contains a subfolder for every month and week (Weeks 01-19). Each week ships with a README that lists the study objectives, primary labs, milestones, and an embedded lab log table.
- 	emplates/lab-log.md is a reusable template for detailed lab reports—drop a copy beside configs or Packet Tracer files when you need more space than the weekly README provides.
- scripts/ includes small helpers that rebuild the structure if the study plan changes (extract_plan.py, uild_lab_structure.py, uild_roadmap.py).

## Daily Workflow
1. **Read the plan**: start from docs/roadmaps/monthly-roadmap.md, open the week you are on (for example labs/month-03.../week-08...).
2. **Add evidence**: open the week's README and fill in the lab log table or copy 	emplates/lab-log.md into the week folder for longer notes. Store Packet Tracer files, configs, and captures beside the README.
3. **Reflect + push**: once a week (or after a big lab) run git status, add your changes, and push to GitHub.

`
git init
git add .
git commit -m "Add week 01 lab notes"
git remote add origin https://github.com/<user>/ccna-labs.git
git push -u origin main
`

## Regenerating From The Source Plan
If Cisco updates the reference plan, drop the new PDF in docs/reference/, re-run scripts/extract_plan.py, then rebuild the folders and roadmap:

`
python scripts/extract_plan.py
python scripts/build_lab_structure.py
python scripts/build_roadmap.py
`

## Suggested Enhancements
- Track configs separately under each week (for example, configs/ or captures/).
- Add CI or a pre-commit hook that lints configs or verifies Packet Tracer files are zipped before pushing.
- Use GitHub Projects or Issues to log blockers encountered during labs.

Commit early and often so your GitHub profile shows the full CCNA journey.
