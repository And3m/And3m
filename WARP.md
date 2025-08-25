# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a GitHub profile repository (And3m/And3m) that serves as a personal portfolio and professional showcase for Vijay Andem. The repository contains a single README.md file that displays on the GitHub profile page.

## Repository Structure

```
And3m/
├── README.md    # Main GitHub profile content (421 lines)
└── .git/        # Git version control
```

## Common Commands

### Viewing Content
```bash
# View the current README content
cat README.md

# Check git status
git status

# View recent changes
git --no-pager log --oneline -10
git --no-pager diff HEAD~1
```

### Making Updates
```bash
# Stage changes
git add README.md

# Commit with descriptive message
git commit -m "✨ Update [section] with [description]"

# Push to GitHub (updates profile immediately)
git push origin main
```

### Preview Changes
```bash
# Preview markdown in terminal (if glow is installed)
glow README.md

# Or open in default markdown viewer
start README.md
```

## Content Architecture

The README.md is structured as a comprehensive portfolio with the following major sections:

1. **Header Section (Lines 1-14)**: Professional title, animated typing SVG, and social media badges
2. **About Me (Lines 18-61)**: Three-pillar approach (Data Analytics, AI/ML Engineering, Business Intelligence)
3. **Tech Stack (Lines 64-101)**: Organized by category - Data Analysis, AI/ML, Development
4. **Featured Projects (Lines 104-248)**: Two main categories:
   - Data Analytics & Visualization Projects (4 projects)
   - AI/ML & LLM Applications (3 projects)
5. **Skills & Competencies (Lines 251-318)**: Core competencies in YAML format
6. **GitHub Analytics (Lines 321-359)**: Stats widgets and streak counter
7. **Contact Section (Lines 362-421)**: Call-to-action and contact information

## Key Content Elements

### Project Showcase Format
Each project follows this structure:
- Project title with emoji
- Repository and live demo badges
- Project highlights (4-5 bullet points)
- Tech stack used

### Visual Elements
- Animated typing SVG for dynamic header
- GitHub stats widgets (theme: tokyonight)
- Animated emoji images from Fluent Emoji collection
- Profile view counter
- Streak statistics

### External Links
- LinkedIn: https://www.linkedin.com/in/vijay-andem-b2092223/
- GitHub: https://github.com/And3m
- Email: vijayandem@gmail.com
- X (Twitter): https://x.com/vjandem

## Development Guidelines

### Commit Message Convention
The repository uses emoji-prefixed commit messages:
- ✨ for enhancements and new features
- 🐛 for bug fixes
- 📝 for documentation updates
- 🎨 for styling/formatting changes
- ♻️ for refactoring

### Content Update Patterns
When updating the README:
1. Maintain consistent formatting with existing sections
2. Use similar emoji patterns for visual consistency
3. Keep badge styles uniform (for-the-badge style)
4. Preserve the three-column layout in table sections
5. Update GitHub stats widgets if needed

### Image and Badge URLs
- Emojis: Now using native Unicode emojis for better compatibility
- Shields.io badges: `https://img.shields.io/badge/`
- GitHub stats: `https://github-readme-stats.vercel.app/api`
- Streak stats: `https://streak-stats.demolab.com/`

## Important Considerations

1. **Profile Visibility**: Changes to README.md are immediately visible on the GitHub profile after pushing
2. **Image Loading**: All images are externally hosted; ensure URLs remain valid
3. **Responsive Design**: Tables and layouts should work on various screen sizes
4. **Professional Tone**: Maintain the balance between technical expertise and approachability
5. **Project Updates**: When adding new projects, follow the existing format exactly

## Quick Tasks

### Add a New Project
1. Choose appropriate section (Data Analytics or AI/ML)
2. Copy existing project table cell structure
3. Update title, badges, highlights, and tech stack
4. Maintain consistent emoji usage

### Update Tech Stack
1. Navigate to lines 64-101
2. Add new badge using shields.io format
3. Maintain category organization

### Refresh GitHub Stats
1. Stats auto-update but can be forced by adding `&cache_seconds=86400` to URLs
2. Verify theme consistency (tokyonight)

### Update Social Links
1. Update both header badges (lines 8-12) and footer section (lines 394-397)
2. Ensure all links are working and consistent
