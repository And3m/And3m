# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a GitHub profile repository (And3m/And3m) that serves as a personal portfolio and professional showcase for Vijay Andem. The repository contains a README.md that displays on the GitHub profile page, plus GitHub Actions workflows for dynamic content generation.

## Repository Structure

```
And3m/
├── README.md                              # Main GitHub profile content (~220 lines)
├── WARP.md                                # Editor guidance (this file)
├── .gitignore                             # Excludes .claude/ from version control
├── assets/
│   └── header.svg                         # Custom animated SVG header banner
├── .github/
│   └── workflows/
│       ├── snake.yml                      # Snake animation generator (every 12h)
│       ├── 3d-contrib.yml                 # 3D contribution calendar (daily)
│       ├── update-readme.yml              # GitHub activity updater (daily)
│       └── blog-posts.yml                 # Blog post auto-fetcher (every 6h)
└── profile-3d-contrib/                    # Generated 3D calendar SVGs (auto-committed)
```

## Content Architecture

The README.md uses a modern bento-grid inspired layout with 9 sections:

1. **Hero Area (Lines 1-18)**: Custom animated SVG banner + typing animation + bio + social badges
2. **Bento Grid (Lines 22-51)**: Two-column layout -- About Me (60%) + Spotify widget & quote (40%)
3. **Tools & Technologies (Lines 55-84)**: Devicon icons (15 core tools) + shields.io badges (6 domain-specific)
4. **Featured Projects (Lines 88-132)**: Collapsible `<details>` sections -- AI/ML (open) + Data Analytics
5. **GitHub Analytics (Lines 136-185)**: Activity graph + stats/languages cards + streak + 3D contrib calendar
6. **Latest Blog Posts (Lines 189-194)**: Auto-fetched via GitHub Action (comment markers)
7. **Daily Dev Quote (Lines 200-205)**: Random programming quote with dark/light mode
8. **Snake Animation (Lines 209-214)**: Contribution grid snake with dark/light variants
9. **Footer (Line 216)**: Capsule-render waving gradient footer

## Key Design Decisions

### Theme: "Midnight Blue"
- Stats widgets: `github_dark_dimmed` theme
- Streak: `github-dark-blue` theme
- Header SVG: Custom dark gradient (#0d1117 to #161b22) with #58a6ff accents
- Footer gradient: `customColorList=2,3,12,19,21`
- All widgets support dark/light mode via `<picture>` + `prefers-color-scheme`

### Bento Grid Layout
- Two-column table for About Me + sidebar widgets
- Inspired by Japanese bento box design trend (2025-2026)
- About Me (60% width) + Spotify/Quote sidebar (40% width)

### Icon Strategy
- Core tools: Devicon CDN (individual SVG icons, 42x42px)
- Domain-specific tools: shields.io `flat-square` badges (Power BI, Tableau, etc.)
- Social links: shields.io `flat-square` badges (appear once in header)

### Project Layout
- Collapsible `<details>/<summary>` sections grouped by category
- AI/ML section open by default, Data Analytics collapsed
- Each project: linked heading + one-sentence description + inline code tech tags

### Interactive Elements
- Custom animated SVG header with CSS keyframe animations
- Typing SVG animation (3 rotating lines)
- Spotify now-playing widget (requires user setup)
- Random dev quote (refreshes on page load)
- Activity graph (contribution timeline)
- 3D contribution calendar (generated daily)
- Snake animation (generated every 12h)

## External Dependencies

| Service | Purpose | URL |
|---------|---------|-----|
| Custom SVG | Header banner | ./assets/header.svg (local) |
| capsule-render | Footer wave | capsule-render.vercel.app |
| readme-typing-svg | Typing animation | readme-typing-svg.demolab.com |
| shields.io | Supplemental badges | img.shields.io |
| komarev | Profile views | komarev.com/ghpvc |
| devicon | Tech stack icons | cdn.jsdelivr.net/gh/devicons/devicon |
| github-readme-stats | Stats + languages cards | github-readme-stats.vercel.app |
| github-readme-activity-graph | Activity timeline | github-readme-activity-graph.vercel.app |
| streak-stats | Streak card | streak-stats.demolab.com |
| quotes-github-readme | Dev quotes | quotes-github-readme.vercel.app |
| spotify-github-profile | Now playing | spotify-github-profile.kittinanx.com |
| Platane/snk | Snake animation | GitHub Action (output branch) |
| github-profile-3d-contrib | 3D calendar | GitHub Action (profile-3d-contrib/) |
| blog-post-workflow | Blog posts | GitHub Action (RSS auto-fetch) |

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

### blog-posts.yml
- Fetches latest blog posts from RSS feed
- Runs every 6 hours
- Populates content between `BLOG-POST-LIST:START` and `BLOG-POST-LIST:END` markers
- Requires user to update RSS feed URL in workflow file

## User Setup Required

### Spotify Widget
1. Visit [spotify-github-profile.kittinanx.com](https://spotify-github-profile.kittinanx.com)
2. Log in with your Spotify account
3. Copy your Spotify user ID
4. Replace `YOUR_SPOTIFY_USER_ID` in README.md (lines 40-42)

### Blog Posts
1. Open `.github/workflows/blog-posts.yml`
2. Replace the `feed_list` URL with your actual blog RSS feed
3. Common feed URLs:
   - Medium: `https://medium.com/feed/@your-username`
   - Dev.to: `https://dev.to/feed/your-username`
   - Hashnode: `https://your-blog.hashnode.dev/rss.xml`

## Commit Message Convention

- `feat:` for new sections or features
- `fix:` for bug fixes and broken link repairs
- `update:` for content updates
- `chore:` for maintenance and automated updates
- `style:` for formatting and visual changes

## Quick Tasks

### Add a New Project
1. Choose the appropriate `<details>` block (AI/ML or Data Analytics)
2. Add a `### [Project Name](repo-url)` block
3. Write a one-sentence description
4. Add inline code tech tags

### Update Tech Stack
1. Add/remove Devicon `<img>` tags for core tools (lines 59-73)
2. Add/remove shields.io flat-square badges for domain-specific tools (lines 77-82)

### Update Social Links
1. Social links appear once in the header area (lines 13-16)
2. Update URLs there only -- no other locations to sync

### Update Header Banner
1. Edit `assets/header.svg` directly
2. CSS animations are defined in the `<style>` block
3. Update text, colors, or animation properties as needed
