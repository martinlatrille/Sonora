#!/usr/bin/env python3
"""
Script to regenerate VS Code theme file from color-mapping-grouped.json
Inverts the structure: {color: {alpha: [keys]}} -> {key: color(+alpha)}
"""

import json

# Read the grouped color mapping
with open('color-mapping-bright-colors-updated.json', 'r') as f:
    grouped_data = json.load(f)

# Create inverted structure: {key: color_value}
inverted_data = {}

for color, alpha_groups in grouped_data.items():
    for alpha, keys in alpha_groups.items():
        # Build the color value
        if alpha.lower() == 'ff':
            # Full opacity - don't include alpha
            color_value = f"#{color}"
        else:
            # Include alpha channel
            color_value = f"#{color}{alpha}"

        # Add each key with the color value
        for key in keys:
            inverted_data[key] = color_value

# Sort keys alphabetically for consistent output
sorted_data = dict(sorted(inverted_data.items()))

# Write to a new file
output_file = 'theme-regenerated-bright-colors.json'
with open(output_file, 'w') as f:
    json.dump(sorted_data, f, indent=2)

print(f"Successfully regenerated theme file: {output_file}")
print(f"Total keys: {len(sorted_data)}")
print(f"Sample keys (first 5): {list(sorted_data.keys())[:5]}")

