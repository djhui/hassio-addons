# 家庭助理插件：EmulatorJS
 在浏览器中基于网络的模拟，几乎可以在任何设备上运行，适用于许多复古控制台。使用的是Libretro和EmulatorJS之间的混合模拟器。
 
_感谢每一个给我的仓库点星的人！点击下方的图片进行点星，之后它会显示在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

这个插件基于来自linuxserver的[docker镜像](https://github.com/linuxserver/docker-emulatorjs)。在浏览器中基于网络的模拟，几乎可以在任何设备上运行，适用于许多复古控制台。使用的是Libretro和EmulatorJS之间的混合模拟器。

## 安装

这个插件的安装相当简单，与安装任何其他Hass.io插件没有不同。

1. [将我的Hass.io插件仓库][repository]添加到你的Hass.io实例中。
1. 安装这个插件。
1. 点击 `保存` 按钮以存储你的配置。
1. 创建目录 /share/emulatorjs 来存储你的游戏/艺术文件
1. 创建 /share/emulatorjs/config 和 /share/emulatorjs/data
1. 启动插件。
1. 检查插件的日志以查看一切是否顺利。
1. 将rom文件放置在 /share/emulatorjs/data/EMULATORNAME/roms 的正确文件夹中
1. 进入管理端口
1. 点击扫描为你添加游戏的模拟器
1. 点击模拟器框，执行步骤1和步骤2
1. 打开WebUI应该进入PlayerUI，访问你的本地homeassistant IP:port或管理端口。
1. 你的游戏应该可用
1. 查阅官方文档以获取设置支持：https://github.com/linuxserver/docker-emulatorjs
1. 如果启动插件导致清除你的设置，请停止插件，然后重启。有时映射到 /share/emulatorjs 不会生效。

## 配置

```
adminport : 3000 #你想要运行管理界面的端口。
port: 89 # 你想要运行前端的端口
```

Webui可以在 `<your-ip>:port` 找到。应该可以通过入口访问。管理端口无法通过入口访问。

[repository]: https://github.com/jdeath/homeassistant-addons