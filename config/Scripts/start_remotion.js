/**
 * Obsidian Templater Script: Start Remotion
 * 
 * This script opens a new terminal window and starts the Remotion 
 * preview player for the project in "07 Workspaces/REMOTION".
 * 
 * Usage in Templater: <% tp.user.start_remotion() %>
 */

async function start_remotion() {
    // We use the 'child_process' module from Node.js (available in Obsidian)
    const { spawn } = require('child_process');
    const path = require('path');

    // Define the absolute path to the Remotion workspace
    // Note: We use the vault's absolute path to ensure accuracy
    const vaultPath = app.vault.adapter.getBasePath();
    const remotionPath = path.join(vaultPath, '07 Workspaces', 'REMOTION');

    // Command to open a new PowerShell window and start Remotion
    // This allows the server to keep running in a separate window
    const command = `Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '${remotionPath}'; npm start"`;

    try {
        // Execute the command via PowerShell
        spawn('powershell.exe', ['-Command', command], {
            detached: true,
            stdio: 'ignore'
        });
        
        new Notice("🚀 Starting Remotion Preview Player...");
    } catch (e) {
        new Notice("❌ Error starting Remotion: " + e.message);
        console.error("Remotion Start Error:", e);
    }
}

module.exports = start_remotion;
