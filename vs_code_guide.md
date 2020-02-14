## What is Visual Studio Code?

As a developer, we need a code editor to help us run the code script. Code editor is one of the most important parts of our setup. Visual Studio Code (VS Code) is a free code editor which runs on the macOS, Linux and Windows operating systems. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Java, Python, PHP, Go) and runtimes (such as .NET and Unity).

## VS Code Installation

VS Code can runs on the macOS, Linux and Windows operating systems. Based on its official page, please follow this step to install git on your machine:

### Windows
- Download the [Visual Studio Code](https://code.visualstudio.com/docs?dv=win) installer for Windows.
- Run the installer (VSCodeUserSetup-{version}.exe). This will only take a minute.
- By default, VS Code is installed under C:\users\{username}\AppData\Local\Programs\Microsoft VS Code.

> Note: .NET Framework 4.5.2 or higher is required for VS Code. If you are using Windows 7, make sure you have at least .NET Framework 4.5.2 installed.

### MAC OS
- Download [Visual Studio Code](https://code.visualstudio.com/docs?dv=osx) for macOS.
- Double-click on the downloaded archive to expand the contents.
- Drag Visual Studio Code.app to the Applications folder, making it available in the Launchpad.
- Add VS Code to your Dock by right-clicking on the icon to bring up the context menu and choosing Options, Keep in Dock.

### Linux
You can do the installation method below if the Linux distribution is Debian or Ubuntu.
- Download and install the [.deb package (64-bit)](https://code.visualstudio.com/docs/?dv=linux64_deb), either through the graphical software center if it's available, or through the command line with:

```
sudo apt install ./<file>.deb

# If you're on an older Linux distribution, you will need to run this instead:
# sudo dpkg -i <file>.deb
# sudo apt-get install -f # Install dependencies
```

If you want install manually without download .deb file before, you can follow this script:

```
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
```






## Setup Working Environment
karena kita mau pakai python, dlala yeyeye , kita butuh bebrapa dependency diantaranya : 

Notes: Pastika python sudah terinstall. Jika belum, silakan ikuti [Python Installation Guide disini](google.com)

- untuk menginstall eksensi, go to xxxxx, lalu search ekstensi yang ingin diinstall

#### Python
#### Anaconda



___________________________________________________________

## Working with Python Script

### Select Interpreter
### Open file/folder
### Runing file on terminal
