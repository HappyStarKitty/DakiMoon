---
title: Blog & Notebook
date: 2024-06-29 23:00:41
categories: 
    - study log
hidden: true
---
搭建 Blog 和 Notebook 在学习中发挥的真正作用因人而异，但对于CS小白依然是件非常有成就感的事情。本篇我们将利用 Hexo 和 Mkdocs 分别创建 Blog 及 Notebook。

## Create A Blog
参考 [hexo官方文档](https://hexo.io/zh-cn/docs/)和[tonycrane's notebook](https://note.tonycrane.cc/cs/tools/hexo/)
hexo 需要两个 repo，分别用于存储项目源码和博客源码。

### Hexo Command
以下是常用的 hexo 指令。
```bash
hexo new post_name # 创建文章
hexo serve # 本地预览
hexo deploy # 网页部署
hexo clean # 清除缓存
hexo generate # 项目生成
```

### Hexo Format

### Hexo Theme
因为 bz 是车车人，所以采用了一款博丽灵梦的主题 reimu。不过 bz 的好兄弟采用的是经美化过的 butterfly 主题，感兴趣的同学也可以试试，还是挺炫酷的。<del>画个饼，等我学了一点CS技术后可能会开发金发小女孩的主题。</del>

配置跟着教程走就好了。如果采用 butterfly，网上也有魔改教程。

## Create A Notebook

mkdocs 只需要一个 repo，其中包含两个 branch。main 存储网站源文件，gh-deploy 存放网页实际渲染文件。

### Mkdocs Command

以下是常用的 mkdocs 指令。
```bash
mkdocs new # 新建项目
mkdocs serve # 本地预览
mkdocs gh-deploy # 网页部署
mkdocs get-deps # 加载插件
```

更多内容可见``mkdocs -h``指令内容。

### Mkdocs Tools

material 作为一个基础的框架主题基本满足了上传和展示笔记的需求。但是为了美化网站外观和优化协作流程，使用一些工具和插件是不可避免的。

xg 的 mkdocs 工具链比较完善，可以直接使用相应的插件。

### Material Individuation

原生的 material 比较朴素，我目前在用的是 NoughtQ 的美化方案。

