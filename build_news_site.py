#!/usr/bin/env python3
"""
从 news_data 中最新的日期文件夹读取 JSON，生成静态网站到 public/ 目录
"""

import os
import json
import shutil
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

DATA_DIR = "news_data"
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "public"

CATEGORIES = {
    "headlines": "国内头条",
    "military": "军事",
    "entertainment": "娱乐",
    "tech": "电子/科技",
    "auto": "汽车",
    "nba": "NBA",
    "soccer": "足球"
}

def get_latest_data():
    """获取最新日期文件夹下的所有分类 JSON"""
    if not os.path.exists(DATA_DIR):
        return {}
    dates = [d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))]
    if not dates:
        return {}
    latest_date = max(dates)  # 按字符串排序 "YYYY-MM-DD" 有效
    latest_path = os.path.join(DATA_DIR, latest_date)
    news_by_cat = {}
    for cat_en in CATEGORIES.keys():
        json_path = os.path.join(latest_path, f"{cat_en}.json")
        if os.path.exists(json_path):
            with open(json_path, "r", encoding="utf-8") as f:
                news_by_cat[cat_en] = json.load(f)
        else:
            news_by_cat[cat_en] = []
    return news_by_cat, latest_date

def main():
    print("🏗️ 开始构建静态网站...")
    news_data, update_date = get_latest_data()
    if not news_data:
        print("❌ 未找到新闻数据，请先运行 fetch_news.py")
        return

    # 清空并重建 public 目录
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    os.makedirs(os.path.join(OUTPUT_DIR, "category"))

    # 复制静态资源（如果有 style.css 则复制，否则自动生成简单样式）
    style_css = """
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin:0; background:#f5f7fb; color:#1f2937; }
    header { background: #1e3a8a; color: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; }
    .logo a { color: white; font-size: 1.5rem; font-weight: bold; text-decoration: none; }
    nav a { color: #e2e8f0; margin-left: 1.2rem; text-decoration: none; }
    nav a:hover { color: white; }
    main { max-width: 1200px; margin: 2rem auto; padding: 0 1rem; }
    .category-section { background: white; border-radius: 16px; padding: 1.2rem; margin-bottom: 2rem; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
    .category-section h2 { margin-top: 0; border-left: 5px solid #1e3a8a; padding-left: 12px; }
    .news-list { display: flex; flex-direction: column; gap: 1rem; }
    .news-item { border-bottom: 1px solid #e5e7eb; padding-bottom: 0.8rem; }
    .news-item a { font-size: 1.05rem; font-weight: 500; color: #1e3a8a; text-decoration: none; }
    .news-item a:hover { text-decoration: underline; }
    .summary { font-size: 0.9rem; color: #4b5563; margin: 4px 0; }
    .meta { font-size: 0.75rem; color: #6b7280; }
    .more { display: inline-block; margin-top: 12px; color: #1e3a8a; }
    .category-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
    .back { background: #e2e8f0; padding: 0.3rem 1rem; border-radius: 20px; text-decoration: none; color: #1f2937; }
    footer { text-align: center; padding: 1.5rem; background: #f1f5f9; margin-top: 2rem; color: #4b5563; font-size: 0.8rem; }
    @media (max-width: 768px) { header { flex-direction: column; gap: 10px; } nav a { margin: 0 0.8rem; } }
    """
    with open(os.path.join(OUTPUT_DIR, "style.css"), "w", encoding="utf-8") as f:
        f.write(style_css)

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    
    # 生成首页
    index_template = env.get_template("index.html")
    index_html = index_template.render(
        news_data=news_data,
        categories=CATEGORIES.items(),
        update_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    
    # 生成每个分类页
    category_template = env.get_template("category.html")
    for cat_en, cat_zh in CATEGORIES.items():
        articles = news_data.get(cat_en, [])
        page_html = category_template.render(
            category_zh=cat_zh,
            articles=articles
        )
        out_path = os.path.join(OUTPUT_DIR, "category", f"{cat_en}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)
    
    print(f"✅ 网站构建完成！输出目录: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
