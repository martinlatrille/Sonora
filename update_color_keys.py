#!/usr/bin/env python3
"""
Script to update top-level keys in color-mapping-updated.json
"""

import json

# Read the file
with open('color-mapping-updated.json', 'r') as f:
    data = json.load(f)

# Define replacements
replacements = {
    # Deep Signal - Dark colors
    # '11111b': '121314',
    # '181825': '16181a',
    # '1e1e2e': '1d2025',
    # '313244': '21252b',
    # '45475a': '282c34',
    # '585b70': '435472',
    # '6c7086': '727480',
    # '7f849c': '8A8B91',
    # '9399b2': '9C9FA9',
    # 'a6adc8': 'b4b5ba',
    # 'bac2de': 'C4C8D4',
    # 'cdd6f4': 'D9DCE8',
    # 'd7dae0': 'D9DCE8',
    # Deep Signal - Bright colors
    'f5e0dc': 'EFCEC7',
    'f2cdcd': 'EDBABA',
    'f5c2e7': 'F1ACDE',
    'cba6f7': 'BD8FF5',
    'f38ba8': 'F17497',
    'eba0ac': 'E68998',
    'fab387': 'F9A26C',
    'f9e2af': 'F7D997',
    'a6e3a1': '93DD8D',
    '94e2d5': '7FDCCD',
    '89dceb': '73D6E7',
    '74c7ec': '5DBEE9',
    '89b4fa': '71A5F9',
    'b4befe': '9AA8FE',
}

# Create new dictionary
new_data = {}

# Track which keys we've processed
processed_keys = set()

for key, value in data.items():
    key_lower = key.lower()

    # Check if this key should be replaced
    if key_lower in [k.lower() for k in replacements.keys()]:
        # Find the original key (case-preserving)
        original_key = None
        for orig_key in replacements.keys():
            if orig_key.lower() == key_lower:
                original_key = orig_key
                break

        if original_key:
            new_key = replacements[original_key]
            new_data[new_key] = value
            processed_keys.add(key_lower)
        else:
            new_data[key] = value
    else:
        # Keep the key as-is
        new_data[key] = value

# Sort the top-level keys
sorted_new_data = dict(sorted(new_data.items(), key=lambda x: x[0].lower()))

# Write back to file
with open('color-mapping-updated.json', 'w') as f:
    json.dump(sorted_new_data, f, indent=2)

print("Successfully updated color-mapping-updated.json")
print(f"Processed {len(processed_keys)} keys for replacement/merge")
print(f"Result contains {len(sorted_new_data)} top-level keys")

