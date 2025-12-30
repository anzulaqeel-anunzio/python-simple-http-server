# Simple HTTP Server CLI

A zero-dependency command-line tool to instantly turn any directory into a web server. Useful for local development, file sharing, or testing static sites.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Instant Setup**: Serve files with a single command.
*   **Custom Directory**: Serve any folder on your system, not just the current one.
*   **Port Config**: Avoid conflicts by choosing any available port.

## Usage

```bash
python run_server.py [options]
```

### Options

*   `--port`, `-p`: Port number (default: 8000).
*   `--directory`, `-d`: Path to the directory you want to serve.
*   `--bind`, `-b`: Bind address (default: 0.0.0.0).

### Examples

**1. Serve Current Directory on Port 8000**
```bash
python run_server.py
```

**2. Serve Specific Folder on Port 8080**
```bash
python run_server.py -d ./my-website -p 8080
```

**3. Serve to Localhost Only**
```bash
python run_server.py -b 127.0.0.1
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
