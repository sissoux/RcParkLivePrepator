# RC Park Live Overlay Preparator

A simple GUI tool to prepare overlay images for RC Park race live streaming.

## Purpose

This script automates the preparation of overlay images for live streaming RC Park races. It takes multiple overlay images, resizes them to fit a 1920x1080 resolution while maintaining aspect ratio and preserving transparency, and saves them with standardized naming conventions.

## Features

- **Easy-to-use GUI**: Simple interface with file browsers for selecting images
- **Automatic resizing**: Resizes images to fit within 1920x1080 while maintaining aspect ratio
- **Non-16:9 handling**: For images that aren't 16:9 ratio, ensures the maximum dimension is either 1920 (width) or 1080 (height)
- **Transparency preservation**: Maintains alpha channel for PNG images with transparency
- **Batch processing**: Processes all 4 overlay types in one click
- **Custom output folder**: Choose where to save processed images (defaults to `c:/RcParkLive/CurrentRace`)
- **Automatic folder creation**: Creates output folder if it doesn't exist

## Required Overlays

The tool processes 7 types of overlays:

1. **ScreenPodiumVide** - Empty podium screen overlay
2. **ScreenRanking** - Ranking display overlay
3. **ScreenStartLineVide** - Empty live start screen overlay
4. **BandeauSeul** - Banner overlay
5. **ScreenPodiumVide_interview** - Empty podium screen overlay for interview mode
6. **ScreenRanking_interview** - Ranking display overlay for interview mode
7. **ScreenStartLineVide_interview** - Empty live start screen overlay for interview mode

## Usage

1. Run the script: `python overlay_preparator.py`
2. Click "Browse" for each overlay type to select your source images
3. (Optional) Change the output folder from the default `c:/RCPARK_Live/CurrentRace/OverlayAssets`
4. Click "Generate" to process all images

## Output

Processed images are saved as:
- `ScreenPodiumVide-1080.png`
- `ScreenRanking-1080.png`
- `ScreenStartLineVide-1080.png`
- `BandeauSeul-1080.png`
- `ScreenPodiumVide-interview-1080.png`
- `ScreenRanking-interview-1080.png`
- `ScreenStartLineVide-interview-1080.png`

All images are saved in PNG format with transparency preserved.

## Requirements

- Python 3.x
- Pillow (PIL) library

Install requirements:
```bash
pip install -r requirements.txt
```

## Technical Details

- Target resolution: 1920x1080
- Aspect ratio preservation: Yes
- Supported input formats: PNG, JPG, JPEG, BMP, TIFF
- Output format: PNG with alpha channel
- Resampling method: LANCZOS (high quality)
