# ESPHome 插件
## 安装

这个插件的安装非常简单，与安装任何其他 Home Assistant 插件没有区别。

1. 在 Supervisor 插件商店中搜索“ESPHome”插件。
2. 按下安装以下载插件并在您的机器上解压。这可能需要一些时间。
3. 可选：如果您使用 SSL/TLS 证书并希望加密与此插件的通信，请在 `ssl` 字段中输入 `true`，并相应地设置 `fullchain` 和 `certfile` 选项。
4. 启动插件，检查插件的日志以查看一切是否顺利。
5. 点击“打开 Web UI”以打开 ESPHome 仪表板。系统会要求您输入 Home Assistant 的凭据 - ESPHome 使用 Home Assistant 的身份验证系统进行登录。

您可以在 https://esphome.io/ 查看 ESPHome 文档。

## 配置

**注意**：_记得在配置更改后重启插件。_

示例插件配置：

```json
{
  "ssl": false,
  "certfile": "fullchain.pem",
  "keyfile": "privkey.pem"
}
```

### 选项： `ssl`

启用或禁用与此插件的 web 服务器的加密 SSL/TLS (HTTPS) 连接。
设置为 `true` 以加密通信，反之则设置为 `false`。
请注意，如果您将其设置为 `true`，则还必须为加密生成密钥和证书文件。可以使用 [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/) 或 [自签名证书](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/)。

### 选项： `certfile`

用于 SSL 的证书文件。如果该文件不存在，则插件启动将失败。

**注意**：文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项： `keyfile`

用于 SSL 的私钥文件。如果该文件不存在，则插件启动将失败。

**注意**：文件必须存储在 `/ssl/` 中，这是 Home Assistant 的默认位置。

### 选项： `leave_front_door_open`

将此选项添加到插件配置中可以通过将其设置为 `true` 来禁用身份验证。

### 选项： `relative_url`

在相对 URL 下托管 ESPHome 仪表板，以便可以在相对 URL 下集成到现有的 Web 代理中，例如 NGINX。默认为 `/`。

### 选项： `status_use_ping`

默认情况下，仪表板使用 mDNS 检查节点是否在线。除非您的路由器支持 mDNS 转发或 avahi，否则在子网之间无法使用。

将此设置为 `true` 将使 ESPHome 使用 ICMP ping 请求获取节点状态。如果所有节点总是显示离线状态，即使它们连接时也可以使用此设置。

### 选项： `streamer_mode`

如果设置为 `true`，这将启用流模式，使 ESPHome 隐藏所有潜在的私人信息。例如 WiFi (B)SSIDs（可能会用于查找您的位置）、用户名等。请注意，您需要在 YAML 文件中使用 `!secret` 标签，以防止在编辑和验证时这些信息显示出来。