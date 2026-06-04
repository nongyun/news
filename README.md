# 🛠️ Ultimate Online Toolbox (万能在线工具箱)

[![Privacy Guaranteed](https://img.shields.io/badge/Privacy-100%25_Safe-success?style=for-the-badge&logo=shield)](../../)
[![Platform](https://img.shields.io/badge/Platform-Pure_Client--Side-blue?style=for-the-badge&logo=javascript)](../../)
[![Theme](https://img.shields.io/badge/Theme-Dark_First-orange?style=for-the-badge&logo=prodirect)](../../)

一个基于 **纯前端客户端沙箱（Pure Client-Side Sandbox）** 技术构建的高级生产力工具箱。
所有工具的计算与核心逻辑 100% 在用户的本地浏览器中独立运行，**绝不上传任何隐私文件或业务数据到后端服务器**，从根源上杜绝数据泄露。

---

## 🌟 核心特性

*   **🔒 绝对的隐私安全**：100% 离线可用，无任何服务器端日志记录。
*   **🎨 高级极客视觉系统**：默认载入**高级暗黑主题（Dark Mode）**，完美支持一键切换至“浅色微光”皮肤，并自动持久化用户偏好。
*   **🌍 完整多语言（i18n）支持**：内置 **English / 简体中文 / Español / 日本語** 四国语言包，一键无缝无刷新切换。
*   **⚡ 极致性能与轻量化**：完全基于原生 JavaScript 驱动，无沉重的框架依赖，秒级加载，卡片交互支持细腻的物理缩放动效。
*   **💵 商业变现就绪**：预留 3 大 Google AdSense 核心广告位插槽（横幅、信息流卡片），代码结构完备。

---

## 🧰 包含的核心工具矩阵 (11 款)

1.  **🖼️ 智能图片压缩 (`compress.html`)**：本地 JPG/PNG/WebP 压缩，自由调校画质与尺寸边界。
2.  **🎨 图片水印加注 (`watermark.html`)**：为证件或照片快速加注全屏倾斜文本防盗印章。
3.  **🔮 高级格式拓展 (`formatext.html`)**：高级媒体底层元数据提取与多线程虚拟渲染控制台。
4.  **🔄 万能格式转换 (`convert.html`)**：PNG、JPEG、WebP 格式之间的本地零常规损耗互转。
5.  **🔑 Bulk UUID 生成器 (`uuid.html`)**：批量生成符合 RFC4122 标准的高强度 v1/v4 密匙。
6.  **📄 Office 离线提纯 (`office.html`)**：Word (`.docx`) 提纯为 TXT，Excel (`.xlsx`) 转换为标准 CSV。
7.  **📷 二维码配对器 (`qr.html`)**：支持标准文本网址及一扫即连的加密 Wi-Fi 账号密码 QR 码。
8.  **👥 传统亲属关系 (`relation.html`)**：中国传统三代/多代血亲三姑六婆复杂称谓精准双向互查。
9.  **📈 精准贷款计算器 (`loan.html`)**：等额本息、等额本金不同金融方案的本金利息还款明细测算。
10. **💵 极速汇率换算 (`currency.html`)**：多币种双向对冲汇率换算，预留公网实时 Spot 价格管道。
11. **📐 全能单位换算 (`unit.html`)**：覆盖长度、重量、温度、面积等国际标准度量衡的高精度转换。

---

## 📁 项目目录结构

```text
├── index.html          # 工具箱导航主页（包含多语言字典、切肤逻辑、AdSense 代码）
├── compress.html       # 智能图片压缩工具页
├── watermark.html      # 图片水印工具页
├── formatext.html      # 格式拓展工具页
├── convert.html        # 格式转换工具页
├── uuid.html           # UUID 生成工具页
├── office.html         # Office 转换工具页
├── qr.html             # 二维码生成工具页
├── relation.html       # 亲属关系计算页
├── loan.html           # 贷款计算页
├── currency.html       # 汇率换算页
├── unit.html           # 单位换算页
├── privacy.html        # 隐私政策合规页
├── robots.txt          # 搜索引擎爬虫协议文件
└── sitemap.xml         # 站点地图（SEO 优化必备）

```

---

## 🚀 部署与上线指南

由于本项目采用 **100% 纯前端静态架构**，您可以将其部署到任何静态文件托管平台：

### 1. 修改域名与广告位标识

上线前，请全局搜索并替换以下两项关键配置：

* **域名替换**：在 `robots.txt` 和 `sitemap.xml` 中，将 `https://example.com` 批量替换为您网站的 **实际真实域名**。
* **广告商 ID 确认**：主页 `index.html` 中的 `data-ad-client` 已经默认配置为您专有的发布商 ID `ca-pub-1624261597740761`。请确保 3 大广告插槽的 `data-ad-slot` 已经填入您在 Google AdSense 后台生成的对应广告单元 ID。

### 2. 静态托管推荐

* **Vercel / Netlify**：直接关联 GitHub 仓库，一键零配置秒级上线。
* **GitHub Pages**：将代码推送到仓库的 `main` 分支，开启 Pages 托管服务。
* **传统 Nginx**：将所有文件打包直接丢进 Nginx 的 `html` 目录下即可。

---

## ⚖️ 开源许可证与隐私承诺

* **数据安全**：本项目坚守本地沙箱运行体系。用户的任何隐私图片、隐私文件数据均在前端暂存并处理，绝对不会离开用户的浏览器。
* **许可证**：采用 [MIT License](https://www.google.com/search?q=LICENSE) 保护。您可以自由地复制、修改和商业化运行该项目。

```

```
