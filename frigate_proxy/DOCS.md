这个插件创建了一个代理，用于单独运行在 Home Assistant 之外的 Frigate 服务器，以便您可以在侧边栏中享受访问的好处，而无需将 Frigate 作为插件运行。

请注意，这个插件并不运行 Frigate 本身。

## 配置

### 选项: `server`

`server` 选项设置 Frigate 服务器的地址。

这必须采用 `http[s]://host:port` 的格式。以下是有效的示例：

- `http://frigate.local:5000`
- `http://192.168.0.101:5000`
- `https://192.168.0.101:443`

### 选项: `proxy_pass_host`

确定我们是否应该将我们正在运行的主机（例如，`homeassistant.local`）传递给我们正在代理的服务器。通常情况下，您可能希望将其设置为 `true`。

如果服务器需要接收 Frigate 实例的主机（而不是运行 Home Assistant 或此插件的主机），请设置为 `false`。如果您的 Frigate 实例位于 SSL 代理后面（如 Traefik 或 Caddy），这可能是必须的，因为它需要接收 Frigate 主机以便正确路由请求。

### 选项: `proxy_pass_real_ip`

确定我们是否应该将客户端的真实 IP 地址传递给我们正在代理的服务器。通常情况下，您可能希望将其设置为 `true`。

如果您需要知道请求是来自 HA IP，请设置为 `false`。如果您的 Frigate 实例位于一个只允许特定 IP 连接的代理后面，这可能就是情况。

## 必需的依赖项

- 访问正在运行的 Frigate 服务器的网络访问

## 支持

如果您需要支持，请 [打开一个问题](https://github.com/blakeblackshear/frigate/issues/new/choose)。