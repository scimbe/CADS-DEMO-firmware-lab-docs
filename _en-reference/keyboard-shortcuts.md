---
title: Keyboard shortcuts in the browser
order: 5
description: Which VS Code shortcuts reach the workbench in a browser tab, and the safe alternatives
---

code-server is VS Code in a browser tab. The browser sees every keystroke first, and a few
shortcuts belong to it. The table lists what matters in the lab.

| Action | Desktop shortcut | In the browser |
|---|---|---|
| Command palette | Ctrl+Shift+P / ⇧⌘P | **F1** always works. Ctrl+Shift+P can be taken by the browser. |
| Quick open file | Ctrl+P / ⌘P | Ctrl+P is *Print* in some browsers; use F1 and type the file name without `>`. |
| Start debugging | F5 | Works when the workbench has focus; with focus in the address bar the page reloads. Alternative: the green start button in *Run and Debug*. |
| Continue / Step Over / Step Into / Step Out | F5 / F10 / F11 / Shift+F11 | Same rule as F5. F11 toggles full screen in some browsers when the workbench has no focus. |
| Run build task | Ctrl+Shift+B / ⇧⌘B | Works. |
| Toggle terminal | Ctrl+` / ⌃` | Works. |
| Toggle side bar | Ctrl+B / ⌘B | Works. |
| Close tab | Ctrl+W / ⌘W | **Closes the browser tab** on most browsers. Use the editor tab's × or F1 → *View: Close Editor*. |
| New window | Ctrl+Shift+N | Browser window, not VS Code. |
| Save | Ctrl+S / ⌘S | Works; the browser's save dialog only appears when focus is outside the workbench. |
| Find in files | Ctrl+Shift+F / ⇧⌘F | Works. |
| Zoom | Ctrl+= / Ctrl+- | Zooms the whole page; use *View: Zoom In* for the workbench only. |

Lab-specific commands have no default keybinding; open them with F1:

- `CaDS Board: Verbinden`, `Flash`, `Reset`, `Anhalten`, `Konsole öffnen`, `Menü`
- `CaDS Tutor: Tutor öffnen / Open Tutor`, `Checks … ausführen / Run checks`,
  `Frag den Tutor / Ask the tutor`, `Sprache wählen / Set language`,
  `Fortschritt zurücksetzen / Reset progress`, `Nächster Step / Next step`

<figure>
<img src="{{ '/assets/07-command-palette.png' | relative_url }}" alt="Command palette opened with F1 and filtered to CaDS, listing the CaDS Tutor commands">
<figcaption>F1, then type "CaDS" to list every lab command.</figcaption>
</figure>

The board console terminal is a pseudo-terminal of the extension: Ctrl+] does not end it, close
the terminal instead.
