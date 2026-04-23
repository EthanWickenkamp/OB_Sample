# How to Use the Start Remotion Script

Your Remotion studio is now integrated into Obsidian. Here's how to use it:

## 1. Enable User Scripts in Templater
To let the template "talk" to the JavaScript script, you need to tell Templater where the scripts are:
- Open **Obsidian Settings** (`Ctrl + ,`).
- Go to **Community Plugins** → **Templater**.
- Scroll down to **User Script Functions**.
- Click the **Folder Icon** and select `config/Scripts/`.
- Click **Add**.

## 2. Using the Command Palette
Now you can start Remotion without leaving Obsidian:
1. Press `Ctrl + P` (Command Palette).
2. Type `Templater: Insert template`.
3. Search for **Start Remotion**.
4. Press `Enter`.

## 3. What Happens Next
- A **PowerShell window** will pop up on your taskbar.
- The **Remotion Player** will open in your web browser at `http://localhost:3000`.
- You can now edit your video code in the `07 Workspaces/REMOTION` folder and see the results instantly in your browser.

---
**Related Documents:**
- [[07 Workspaces/REMOTION/CLAUDE|Remotion Workspace Context]]
- [[config/Templates/Start Remotion|The Start Remotion Template]]
- [[config/Scripts/start_remotion|The start_remotion Script]]
