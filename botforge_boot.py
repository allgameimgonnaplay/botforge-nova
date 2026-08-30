# BotForge boot guard — makes a missing DISCORD_TOKEN unable to fail a deploy.
import os
import sys
import time


def _hand_off():
    os.execv(sys.executable, [sys.executable, "main.py"])


def _wait_for_token():
    import http.server
    import socketserver
    import threading

    port = int(os.environ.get("PORT", "10000"))

    class _H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"BotForge: service is UP, waiting for DISCORD_TOKEN to be set.")

        def do_HEAD(self):
            self.send_response(200)
            self.end_headers()

        def log_message(self, *args):
            pass

    def _serve():
        with socketserver.TCPServer(("", port), _H) as httpd:
            httpd.serve_forever()

    threading.Thread(target=_serve, daemon=True).start()
    print("=" * 60)
    print("BotForge boot guard: DISCORD_TOKEN is not set (or empty).")
    print("The service is LIVE and waiting — this is NOT a failure.")
    print("Add DISCORD_TOKEN in BotForge (bot -> Secrets) or the Render")
    print("dashboard (Environment tab). Saving it restarts this process")
    print("and the bot starts automatically.")
    print("=" * 60)
    sys.stdout.flush()
    while True:
        time.sleep(30)
        if os.environ.get("DISCORD_TOKEN", "").strip():
            _hand_off()


if os.environ.get("DISCORD_TOKEN", "").strip():
    _hand_off()
else:
    _wait_for_token()
