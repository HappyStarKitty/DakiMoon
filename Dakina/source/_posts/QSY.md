---
title: QSY Development Guide
date: 2024-10-26 09:07:15
tags: frondend
---

第一次使用 Next.js 框架写的前端小项目，写得还蛮久的，遂动笔记录一番。

我并不打算写成一篇事无巨细的教程，第一本人没啥实力也没有精力，第二应该学会自己翻阅文档，<del>第三也没有人看</del>。于是随便写写自己遇到的一些坑和感悟。

## 构建页面外观

### 初始化

根据官方文档的指示走就行，而且 Next.js 的安装是交互式的，非常方便。

```bash
npx create-next-app@latest --typescript 
```

然后 `npm run dev` 即可。

有遇到过运行显示 `favicon.ico` 文件过大的情况，如果是在 `app` folder 可以将其移至 `public` folder 下。btw，文件分类管理十分重要。

```bash
-- pages # 页面文件
-- public # 静态资源如icon、picture等
-- components # 可复用组件
```

根页面默认是 `pages/index.tsx`，其路由是 `/`。

### CSS 样式

听说CSS预处理器挺好用，不过我还没学。

在 ts 中 直接糊 CSS 需要使用驼峰命名法，举个栗子：

```ts
```

对于组件嵌套的情况，最好把 `container` 和 `content` 分离出来，即对于一个子组件，其 `margin` 属性不应单独设置，而是由其 `container`（通常是 div） 进行控制。否则你会经常遇到同一组件在不同地方显示怪异的情况（尤其是 `flex` 的排版规则比较“灵活”）。

### Typescript

ts 的类型检查非常实用，比如某个 interface 过了几天你不一定能记住有哪些字段，这是再去 Ctrl+F 之类查找就比较麻烦。但是 ts 的类型可以给出提示。

### 组件化

React 的组件化思想在写静态页面外观的时候就要贯彻。对于可复用的组件，应该将需要的参数打包到一个props interface中。

## 设计页面行为

### API

API 需要与后端和产品提前约定好，apifox 是约定 API 规范不错的工具。实际开发中，可以使用 postman 或者 curl 命令进行测试。

### 请求

响应返回无论正常和异常都不应该影响其他组件的正常工作。

### 状态管理

React 提供了一系列钩子函数。

### 路由

Next.js 的一大优点在于路由管理的确较为方便。pages 页面的 tsx 路由与其文件名绑定。此外，Next.js 提供的 useRouter hook 也比较好用。

```ts
import {useRouter} from "next/router";

const router = useRouter();
router.push("/"); // 跳转至根页面
router.back(); // 路由回退
const { problem_set } = router.query; // 查询参数
```

## 前后端联调

## 杂项

### 开发者工具

DevTools 提供了 Elements、Console、Sources、Network、Application 等开发调试常用的工具。

- Elements
查看每个组件的 margin、padding 等属性
- Console
- Network
查看请求和响应

### 配置文件

如果是手动配置数据库等敏感信息应该将其放进 `.env` 等 `.gitignore` 的文件中，否则传入 github public repo 等公开的地方几乎无法被删净。

### 开发文档

写个开发文档记录自己的进度还挺好玩的。无论是 `fix error` 还是 `add function` 都会给自己带来十足的成就感，也许这就是写代码的乐趣（笑）。

## 结语

仅仅使用 React 和基于 React 的 Next.js 写个简单的页面已经绰绰有余，但在实际的开发环境中代码工程量远远超出于此，我们还有很多工具和技术栈需要学习。
