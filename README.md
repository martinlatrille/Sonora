<h1 align="center">
	📡
</h1>
<h3 align="center">
	Sonora for <a href="https://code.visualstudio.com">VSCode</a>
</h3>

<p align="center">
  <strong>A modern, dark color scheme with calming tones.</strong><br/>
  Inspired by space and waves.
</p>

## About

Sonora is a carefully crafted color scheme for Visual Studio Code inspire by space and waves. Designed for extended coding sessions, Sonora offers a soothing visual experience that reduces eye strain while maintaining excellent code readability.

## Variants

### Deep Signal

The darkest variant in the Sonora family, perfect for late-night coding sessions. Deep Signal comes in three distinct flavors:

<details>
<summary>📡 Deep Signal (Default)</summary>
<p>The standard Deep Signal theme with balanced, calming colors.</p>
</details>

<details>
<summary>🌊 Deep Signal (Faded)</summary>
<p>Accent colors are more faded and pastel, creating an even softer visual experience.</p>
</details>

<details>
<summary>⚡ Deep Signal (Vibrant)</summary>
<p>Accent colors are darker and more vibrant, providing stronger visual contrast.</p>
</details>

### Tides

A lighter dark variant that maintains the calming aesthetic while offering a brighter workspace. Still in active development.

<details>
<summary>🌊 Tides</summary>
<p>A less dark scheme that brings the ocean's gentle rhythm to your editor.</p>
</details>

## Usage

### Installation

Install the extension from a Marketplace:

- [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=martinlatrille.sonora)
- [Open-VSX](https://open-vsx.org/extension/martinlatrille/sonora)

### Manual Installation

Download the VSIX from [the latest GitHub release](https://github.com/consioAi/sonora/releases/latest). Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) and select "Extensions: Install from VSIX...", then open the file you just downloaded.

### Activating the Theme

1. Open the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
2. Type "Preferences: Color Theme"
3. Select one of the Sonora variants:
   - Sonora Deep Signal
   - Sonora Deep Signal (vibrant)
   - Sonora Deep Signal (faded)
   - Sonora Tides

## Recommended Settings

For the best experience with Sonora, we recommend the following settings in your `settings.json`:

```jsonc
{
  // Enable semantic highlighting for better syntax colors
  "editor.semanticHighlighting.enabled": true,
  // Prevent VSCode from modifying the terminal colors
  "terminal.integrated.minimumContrastRatio": 1,
  // Make the window's titlebar use the workbench colors
  "window.titleBarStyle": "custom",
}
```

## Support

If you have any questions, suggestions, or encounter issues, please feel free to:

- [Open an issue](https://github.com/consioAi/sonora/issues) on GitHub
- Contribute improvements via pull requests

## Development

1. Clone and open this repository in VSCode.
2. Install dependencies (if any).
3. Make modifications to the theme JSON files in `./themes/`.
4. Test your changes by reloading the extension or using the extension development host.

## License

See [LICENSE.md](LICENSE.md) for more information.

---

<p align="center">Copyright &copy; 2024-present <a href="https://github.com/consioAi" target="_blank">Consio</a></p>
