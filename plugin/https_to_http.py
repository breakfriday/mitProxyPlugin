from mitmproxy import http, ctx

def request(flow: http.HTTPFlow) -> None:
    # Only process requests to dev.local.com:3000
    if flow.request.pretty_host == "dev.local.com" and flow.request.port == 3000:
        # Check if the request is a WebSocket or HTTP Secure request
        if flow.request.scheme == "wss":
            # Change the scheme from WSS to WS
            flow.request.scheme = "ws"
            ctx.log.info(f"Converted WSS to WS for request: {flow.request.url}")
        elif flow.request.scheme == "https":
            # Change the scheme from HTTPS to HTTP
            flow.request.scheme = "http"
            ctx.log.info(f"Converted HTTPS to HTTP for request: {flow.request.url}")

def error(flow: http.HTTPFlow):
    ctx.log.error(f"An error occurred with the following request: {flow.request.url}")
