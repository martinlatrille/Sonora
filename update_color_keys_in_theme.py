#!/usr/bin/env python3
"""
Script to update top-level keys in color-mapping-updated.json
"""

from copy import deepcopy
import json

# Read the file
with open('themes/sonora-deep-signal-v0_2.json', 'r') as f:
    data = json.load(f)

# Define replacements
replacements = {
    # Deep Signal - Dark colors
    # '#11111b': '#121314',
    # '#181825': '#16181a',
    # '#1e1e2e': '#1d2025',
    # '#313244': '#21252b',
    # '#45475a': '#282c34',
    # '#585b70': '#435472',
    # '#6c7086': '#727480',
    # '#7f849c': '#8A8B91',
    # '#9399b2': '#9C9FA9',
    # '#a6adc8': '#b4b5ba',
    # '#bac2de': '#C4C8D4',
    # '#cdd6f4': '#D9DCE8',
    # '#d7dae0': '#D9DCE8',
    # Deep Signal - Vibrant colors
    # '#f5e0dc': '#EFCEC7',
    # '#f2cdcd': '#EDBABA',
    # '#f5c2e7': '#F1ACDE',
    # '#cba6f7': '#BD8FF5',
    # '#f38ba8': '#F17497',
    # '#eba0ac': '#E68998',
    # '#fab387': '#F9A26C',
    # '#f9e2af': '#F7D997',
    # '#a6e3a1': '#93DD8D',
    # '#94e2d5': '#7FDCCD',
    # '#89dceb': '#73D6E7',
    # '#74c7ec': '#5DBEE9',
    # '#89b4fa': '#71A5F9',
    # '#b4befe': '#9AA8FE',
    # Deep Signal - Midvibrant colors
    '#f5e0dc': '#F3D8D3',
    '#f2cdcd': '#F0C6C6',
    '#f5c2e7': '#F4B9E3',
    '#cba6f7': '#C69DF6',
    '#f38ba8': '#F282A1',
    '#eba0ac': '#E996A3',
    '#fab387': '#F9AB7B',
    '#f9e2af': '#F8DEA5',
    '#a6e3a1': '#9EE199',
    '#94e2d5': '#8BDFD1',
    '#89dceb': '#81D9EA',
    '#74c7ec': '#6BC3EB',
    '#89b4fa': '#80AEFA',
    '#b4befe': '#A9B5FE',
}

updated_count = 0
new_data = deepcopy(data)

def update_color(data):
    global updated_count

    for key, value in data.items():
        if isinstance(value, dict):
            update_color(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    update_color(item)
                elif not isinstance(item, str):
                    print(f"found item: {item}")

        elif isinstance(value, str):
            # Allow for matching hex color values with optional 2 extra chars (alpha channel)
            for rep_key in replacements.keys():
                if value.lower() == rep_key.lower():
                    data[key] = replacements[rep_key]
                    updated_count += 1
                    break
                elif (
                    len(value) == len(rep_key) + 2 and
                    value[:len(rep_key)].lower() == rep_key.lower()
                ):
                    # Conserve alpha (the two trailing chars)
                    alpha = value[len(rep_key):]
                    data[key] = replacements[rep_key] + alpha
                    updated_count += 1
                    break
update_color(new_data)

# Write back to file
with open('themes/sonora-deep-signal-v0_2-midvibrant.json', 'w') as f:
    json.dump(new_data, f, indent=2)

print("Successfully updated themes/sonora-deep-signal-v0_2-midvibrant.json")
print(f"Processed {updated_count} keys for replacement/merge")

