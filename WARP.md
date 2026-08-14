# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a GitHub profile repository (And3m/And3m) that serves as a personal portfolio and professional showcase for Vijay Andem. The repository contains a README.md that displays on the GitHub profile page, plus GitHub Actions workflows for dynamic content generation.

## Repository Structure

```
And3m/
├── README.md                              # Main GitHub profile content (~215 lines)
├── WARP.md                                # Editor guidance (this file)
├── .github/
│   └── workflows/
│       ├── snake.yml                      # Snake animation generator (every 12h)
│       └── 3d-contrib.yml                 # 3D contribution calendar (daily)
└── profile-3d-contrib/                    # Generated 3D calendar SVGs (auto-committed)
```

## Common Commands

### Viewing Content
```bash
cat README.md
git status
git --no-pager log --oneline -10
git --no-pager diff HEAD~1
```

### Making Updates
```bash
git add README.md
git commit -m "update: [section] - [description]"
git push origin main
```

## Content Architecture

The README.md uses 10 lean sections (line numbers shift on edit -- use the `## ` headings as anchors):

1. **Header Banner**: Responsive capsule-render with `<picture>` element for mobile/tablet/desktop. Name + resume title in the `text`/`desc` params
2. **Typing Animation**: readme-typing-svg via demolab.com (3 rotating lines)
3. **Bio + Social Links + Availability**: One-line positioning statement, 5 flat-square badges (LinkedIn, Portfolio, Email, X, Views), "open to" line
4. **About Me**: Two narrative paragraphs, no tables or bullet lists
5. **Experience**: 4 roles (CavinKare, IBM, Indegene, Infosys), bold title + org + dates, one short paragraph each
6. **Tools & Technologies**: skillicons.dev image + shields.io badges grouped under BI / GenAI / Data and Apps
7. **Featured Projects**: 6 projects in vertical card layout (mobile-friendly) + portfolio link
8. **Education & Certifications**: Degree line + IBM/Optimizely certification list
9. **GitHub Analytics**: Stats, streak, top langs, 3D contrib -- all with dark/light mode
10. **Footer**: "Let's Talk" CTA + snake animation (dark/light) + capsule-render wave

### Source of Truth

Content in About Me, Experience, and Education & Certifications mirrors the resume
(`Vijay_Kumar_Andem_Resume CG.pdf`, not stored in this repo). When the resume changes,
update those three sections to match -- do not let claims drift apart between them.

## Key Design Decisions

### Theme: "Midnight Blue"
- Stats widgets: `github_dark_dimmed` theme
- Streak: `github-dark-blue` theme
- Header/footer gradient: `customColorList=2,3,12,19,21`
- Typing animation color: `#58A6FF`
- All widgets support dark/light mode via `<picture>` + `prefers-color-scheme`

### Badge Strategy
- Core tools via skillicons.dev single image
- Domain-specific tools via shields.io `flat-square` style, grouped under bold labels
- Social links appear twice: flat-square in the header, `for-the-badge` in the footer CTA
- **Only badge what the resume or a linked repo actually backs.** No aspirational icons

### Project Layout
- Vertical card format (stacks naturally on mobile)
- Each project: linked `###` heading + one-sentence description + inline code tech tags
- 6 curated projects covering GenAI and data analytics; overflow goes to the portfolio site

## External Dependencies

| Service | Purpose | URL |
|---------|---------|-----|
| capsule-render | Header/footer waves | capsule-render.vercel.app |
| readme-typing-svg | Typing animation | readme-typing-svg.demolab.com |
| shields.io | Supplemental badges | img.shields.io |
| komarev | Profile views | komarev.com/ghpvc |
| github-readme-stats | Stats + languages cards | github-readme-stats.vercel.app |
| streak-stats | Streak card | streak-stats.demolab.com |
| skillicons.dev | Tech stack icons | skillicons.dev |
| Platane/snk | Snake animation | GitHub Action (`output` branch, served via raw.githubusercontent.com) |
| github-profile-3d-contrib | 3D calendar | GitHub Action (profile-3d-contrib/) |

## GitHub Actions Workflows

### snake.yml
- Generates contribution grid snake animation (light + dark variants)
- Runs every 12 hours + on push to main (with `paths-ignore` so the 3d-contrib
  bot commit and README edits don't retrigger it)
- Outputs to `output` branch via ghaction-github-pages
- README must reference the SVGs via `raw.githubusercontent.com`, **not** `github.com/.../blob/...`
  (blob URLs return an HTML page and render as a broken image)

### 3d-contrib.yml
- Generates 3D contribution calendar SVGs
- Runs daily at 1 AM UTC, `concurrency` guarded so a manual dispatch can't race the cron
- Commits SVGs to `profile-3d-contrib/` directory on main branch

### Removed: update-readme.yml
Deleted. It used `jamesgeorge007/github-activity-readme`, which requires
`<!--START_SECTION:activity-->` / `<!--END_SECTION:activity-->` markers in the README.
Those markers were never present, so the job failed on every daily run. If you want the
activity feed back, add the markers **and** the workflow together -- one without the
other is a guaranteed failure.

## Commit Message Convention

- `feat:` for new sections or features
- `fix:` for bug fixes and broken link repairs
- `update:` for content updates
- `chore:` for maintenance and automated updates
- `style:` for formatting and visual changes

## Quick Tasks

### Add a New Project
1. Add a new `### [Project Name](repo-url)` block in the Featured Projects section
2. Write a one-sentence description
3. Add inline code tech tags
4. Keep to 6 projects max (remove least relevant if needed)

### Update Tech Stack
1. Modify the skillicons.dev URL parameter list for core tools
2. Add/remove shields.io flat-square badges under the relevant bold group label

### Update Social Links
Two locations must stay in sync:
1. Header badge row (flat-square: LinkedIn, Portfolio, Email, X, Views)
2. Footer "Let's Talk" CTA (for-the-badge: LinkedIn, Email)

### Update the Header Title
The name and tagline live in the `text=` and `desc=` query params of all three
capsule-render URLs in the `<picture>` block. Change all three (mobile / tablet /
desktop fallback) and keep the `<img>` `alt` text in sync -- the name exists only
inside the image, so alt text is what screen readers and search indexers see.
