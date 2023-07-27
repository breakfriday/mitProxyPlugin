  # 检查请求的协议是否为 WebSocket
    from mitmproxy import http, ctx

    def request(flow: http.HTTPFlow) -> None:
  
    if flow.websocket:
        # 检查请求的 URL 是否以 .flv 结尾
        if flow.request.path.endswith(".flv"):
            # 终止对此 WebSocket 请求的拦截
            flow.kill()