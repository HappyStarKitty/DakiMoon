---
title: Blog & Notebook
date: 2024-06-29 23:00:41
tags: hexo mkdocs
---
搭建Blog和Notebook在学习中发挥的真正作用因人而异，但对于CS小白依然是件非常有成就感的事情。本篇我们将利用Hexo和Mkdocs分别创建Blog及Notebook。

## Create A Blog
参考 [hexo官方文档](https://hexo.io/zh-cn/docs/)和[tonycrane's notebook](https://note.tonycrane.cc/cs/tools/hexo/)
hexo 需要两个 repo，分别用于存储项目源码和博客源码

### Hexo Command
```bash
hexo new post_name # 创建文章
hexo serve # 本地预览
hexo deploy # 网页部署
hexo clean # 清除缓存
hexo generate # 项目生成
```

## Create A Notebook

mkdocs 只需要一个 repo，其中包含两个 branch。main 存储网站源文件，gh-deploy 存放网页实际渲染文件。

### Mkdocs Command
```bash
mkdocs serve # 本地预览
mkdocs gh-deploy # 网页部署
```

