# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a GitHub profile repository (And3m/And3m) that serves as a personal portfolio and professional showcase for Vijay Andem. The repository contains a README.md that displays on the GitHub profile page, plus GitHub Actions workflows for dynamic content generation.

## Repository Structure

```
And3m/
├── README.md                              # Main GitHub profile content (~144 lines)
├── WARP.md                                # Editor guidance (this file)
├── .github/
│   └── workflows/
│       ├── snake.yml                      # Snake animation generator (every 12h)
│       ├── 3d-contrib.yml                 # 3D contribution calendar (daily)
│       └── update-readme.yml              # GitHub activity updater (daily)
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

The README.md uses 8 lean sections:

1. **Header Banner (Lines 1-8)**: Responsive capsule-render with `<picture>` element for mobile/tablet/desktop
2. **Typing Animation (Lines 10-11)**: readme-typing-svg via demolab.com (3 rotating lines)
3. **Bio + Social Links (Lines 13-22)**: One-line bio, 4 flat-square badges (LinkedIn, Email, X, Views)
4. **About Me (Lines 26-30)**: Two narrative paragraphs, no tables or bullet lists
5. **Tools & Technologies (Lines 34-49)**: skillicons.dev image + 6 supplemental shields.io badges
6. **Featured Projects (Lines 53-92)**: 5 projects in vertical card layout (mobile-friendly)
7. **GitHub Analytics (Lines 95-128)**: Stats, streak, top langs, 3D contrib -- all with dark/light mode
8. **Footer (Lines 130-143)**: Snake animation (dark/light) + capsule-render wave

## Key Design Decisions

### Theme: "Midnight Blue"
- Stats widgets: `github_dark_dimmed` theme
- Streak: `github-dark-blue` theme
- Header/footer gradient: `customColorList=2,3,12,19,21`
- Typing animation color: `#58A6FF`
- All widgets support dark/light mode via `<picture>` + `prefers-color-scheme`

### Badge Strategy
- ~20 total badges (down from 86+)
- Core tools via skillicons.dev single image
- Domain-specific tools (Power BI, Tableau, etc.) via shields.io `flat-square` style
- Social links appear once (in header area only)

### Project Layout
- Vertical card format (stacks naturally on mobile)
- Each project: linked `###` heading + one-sentence description + inline code tech tags
- 5 curated projects covering AI/ML and data analytics

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
| Platane/snk | Snake animation | GitHub Action (output branch) |
| github-profile-3d-contrib | 3D calendar | GitHub Action (profile-3d-contrib/) |

## GitHub Actions Workflows

### snake.yml
- Generates contribution grid snake animation (light + dark variants)
- Runs every 12 hours + on push to main
- Outputs to `output` branch via ghaction-github-pages

### 3d-contrib.yml
- Generates 3D contribution calendar SVGs
- Runs daily at 1 AM UTC
- Commits SVGs to `profile-3d-contrib/` directory on main branch

### update-readme.yml
- Updates README with recent GitHub activity
- Runs daily at midnight UTC
- Uses jamesgeorge007/github-activity-readme

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
4. Keep to 5 projects max (remove least relevant if needed)

### Update Tech Stack
1. Modify the skillicons.dev URL parameter list for core tools
2. Add/remove shields.io flat-square badges for domain-specific tools

### Update Social Links
1. Social links appear once in the header area (lines 17-20)
2. Update URLs there only -- no other locations to sync
