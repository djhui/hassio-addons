# Hass-Panel HAOS加载项

[English](README.en.md) | 简体中文

一个基于React的智能家居控制面板，专为Home Assistant操作系统(HAOS)设计的加载项。它使用Home Assistant的Websocket API，提供美观且功能丰富的控制界面。

## 视频预览
[![一个基于 React 的智能家居控制面板]( https://i.imgur.com/PpbbnAS.png )](https://www.bilibili.com/video/BV1yxfaYHE5A/?share_source=copy_web&vd_source=3ef738469d1538347bdba19ea015dbd7)

## 预览图
![预览图](https://i.imgur.com/ZV71KM8.jpeg)

## 主要特性

- 📱 响应式设计，支持移动端和桌面端
- 🔧 高度可配置，自由拖拽布局
- 🚀 PWA支持，可安装到桌面
- 🎨 美观的用户界面，支持暗色模式
- 🔌 丰富的设备支持:
  - 灯光控制
  - 空调控制
  - 窗帘控制
  - 传感器监控
  - 摄像头查看
  - 场景控制
  - 更多设备支持中...

## 安装说明

1. 在Home Assistant的侧边栏中，点击"配置" -> "加载项" -> "加载项商店"
2. 点击右上角的三个点，选择"存储库"
3. 添加存储库地址：`https://github.com/mrtian2016/hass-panel`
4. 点击"添加"并刷新页面
5. 在加载项商店中找到并安装"Hass Panel"
6. 启动加载项
7. 安装完成后，可以在侧边栏中找到"Hass Panel"入口

或者，您可以直接点击下面的按钮一键添加：

[![添加到Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fmrtian2016%2Fhass-panel)

## 配置说明

### 加载项配置选项

在加载项配置页面，您可以设置以下选项：

1. 端口设置（默认5123）
2. SSL设置（如需要）
3. 访问权限设置

### 支持的卡片类型

1. 时间卡片 (TimeCard)
2. 天气卡片 (WeatherCard) 
3. 灯光状态卡片 (LightStatusCard)
4. 房间灯光概览卡片 (LightOverviewCard)
5. 传感器卡片 (SensorCard)
6. 媒体播放器卡片 (MediaPlayerCard)
7. 窗帘控制卡片 (CurtainCard)
8. 电量监控卡片 (ElectricityCard)
9. 路由器监控卡片 (RouterCard)
10. NAS监控卡片 (NASCard)
11. 摄像头卡片 (CameraCard)
12. 空调控制卡片 (ClimateCard)
13. 人体传感器卡片 (MotionCard)
14. 净水器卡片 (WaterPurifierCard)
15. 光照传感器卡片 (IlluminanceCard)
16. 快捷指令面板 (ScriptPanel)

## 常见问题

1. 加载项无法启动
   - 检查端口是否被占用
   - 确认系统资源是否充足
   - 查看加载项日志以获取详细错误信息

2. 配置不生效
   - 确认实体 ID 是否正确
   - 刷新页面后重试
   - 重启加载项

3. 设备显示离线
   - 检查 Home Assistant 连接状态
   - 验证实体 ID 是否存在
   - 确认设备是否在线

4. 图标不显示
   - 检查图标名称是否正确
   - 确认使用了支持的图标

## 交流群

<img src="https://i.imgur.com/ct6Tu5R.jpeg" width="300" alt="交流群" />

## 赞助

如果您觉得这个项目对您有帮助，欢迎赞助支持！

| 微信赞赏码 | 支付宝赞赏码 |
|--------|--------|
| ![微信赞赏码](https://i.imgur.com/f3Fxtsc.png) | ![支付宝赞赏码](https://i.imgur.com/bdNzzyW.png) |
## 许可证

本项目采用 GNU Affero General Public License v3.0 (AGPL-3.0) 许可证。详细信息请查看[完整许可证文本](https://www.gnu.org/licenses/agpl-3.0.zh-cn.html)。 