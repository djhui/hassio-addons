# 家庭助理插件: Otter Wiki

# Otter Wiki

Otter Wiki 是基于 Python 的协作内容管理软件，称为 [wiki](https://en.wikipedia.org/wiki/Wiki)。内容存储在 git 仓库中，该仓库跟踪所有更改。
使用 [Markdown](https://daringfireball.net/projects/markdown) 作为标记语言。Otter Wiki 使用微框架 [Flask](http://flask.pocoo.org/) 编写。
使用 [halfmoon](https://www.gethalfmoon.com) 作为 CSS 框架，使用 [CodeMirror](https://codemirror.net/) 作为编辑器。
[Font Awesome Free](https://fontawesome.com/license/free) 提供图标。

## 显著特征

- 极简主义界面（带暗黑模式）
- 支持 markdown 高亮和表格的编辑器
- 可定制的侧边栏：菜单和/或页面索引
- 完整的变更日志和页面历史
- 用户身份验证
- 页面附件
- 扩展的 Markdown：表格、脚注、花哨的块、警报和美人鱼图
- （实验性）Git http 服务器：克隆、拉取和推送您的 wiki 内容
- 一个非常可爱的海獺作为标志（由 [Christy Presler](http://christypresler.com/) 绘制，CC BY 3.0）


_感谢所有为我的仓库点赞的人！要给它点赞，请点击下面的图片，然后它会出现在右上角。谢谢！_

[![Stargazers repo roster for @jdeath/homeassistant-addons](https://reporoster.com/stars/jdeath/homeassistant-addons)](https://github.com/jdeath/homeassistant-addons/stargazers)

## 关于

此插件使用 [docker 镜像](https://github.com/redimp/otterwiki)。

## 安装

此插件的安装非常简单，与安装任何其他 Hass.io 插件没有区别。

1. [将我的 Hass.io 插件仓库][repository] 添加到您的 Hass.io 实例。
1. 安装此插件。
1. 点击 `Save` 按钮以保存您的配置。
1. 启动插件。
1. 检查插件的日志以查看是否一切正常。
1. 打开 WebUI 应该可以通过 <your-ip>:port 访问。
1. 设置将在 /addon_configs/2effc9b9_otterwiki 中。

## 配置

```
port : 8084 #您希望运行的端口。
```

Webui 可以在 `<your-ip>:port` 找到。

[repository]: https://github.com/jdeath/homeassistant-addons