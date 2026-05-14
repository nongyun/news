#!/usr/bin/env python3
"""
Fetch news from multiple RSS sources and optionally GNews API.
Saves JSON files by date and category under news_data/
"""

import os
import json
import feedparser
import requests
from datetime import datetime
from typing import Dict, List
import time

# 配置
DATA_DIR = "news_data"
CATEGORIES = {
    "military": "军事",
    "entertainment": "娱乐",
    "tech": "电子/科技",
    "auto": "汽车",
    "nba": "NBA",
    "soccer": "足球",
    "headlines": "国内头条"
}

# RSS 源（无 API 密钥，免费可靠）
RSS_FEEDS = {
    "military": "http://www.chinanews.com/rss/mil.xml",
    "entertainment": "http://www.chinanews.com/rss/ent.xml",
    "tech": "http://www.chinanews.com/rss/it.xml",
    "auto": "http://www.chinanews.com/rss/auto.xml",
    "nba": "http://www.espn.com/espn/rss/nba/news",
    "soccer": "http://www.espn.com/espn/rss/soccer/news",
    "headlines": "http://www.chinanews.com/rss/scroll-news.xml"
}

# 备用 BBC 体育 RSS（ESPN 偶尔不稳定）
BACKUP_FEEDS = {
    "nba": "http://feeds.bbci.co.uk/sport/basketball/rss.xml",
    "soccer": "http://feeds.bbci.co.uk/sport/football/rss.xml"
}

def fetch_rss(url: str, max_entries: int = 15) -> List[Dict]:
    """解析 RSS 源，返回新闻列表"""
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:max_entries]:
            articles.append({
                "title": entry.get("title", "无标题"),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", entry.get("description", "")),
                "published": entry.get("published", ""),
                "source": feed.feed.get("title", "未知来源")
            })
        return articles
    except Exception as e:
        print(f"RSS 解析失败 {url}: {e}")
        return []

def fetch_gnews(category: str, api_key: str = None) -> List[Dict]:
    """使用 GNews API 获取新闻（可选，需注册 https://gnews.io/）"""
    if not api_key:
        return []
    # 映射分类到 GNews 查询关键词
    query_map = {
        "military": "military",
        "entertainment": "entertainment",
        "tech": "technology",
        "auto": "car",
        "nba": "NBA",
        "soccer": "football",
        "headlines": "breaking news"
    }
    q = query_map.get(category, "news")
    url = f"https://gnews.io/api/v4/search?q={q}&lang=zh&country=cn&max=10&apikey={api_key}"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        articles = []
        for item in data.get("articles", []):
            articles.append({
                "title": item["title"],
                "link": item["url"],
                "summary": item["description"],
                "published": item["publishedAt"],
                "source": item["source"]["name"]
            })
        return articles
    except:
        return []

def save_news(category: str, news_list: List[Dict]):
    """按日期保存新闻 JSON"""
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(f"{DATA_DIR}/{today}", exist_ok=True)
    filepath = f"{DATA_DIR}/{today}/{category}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(news_list, f, ensure_ascii=False, indent=2)
    print(f"✅ 已保存 {category} -> {len(news_list)} 条新闻")

def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    api_key = os.environ.get("NEWS_API_KEY", "")
    
    for cat_en, cat_zh in CATEGORIES.items():
        print(f"正在抓取 {cat_zh} ({cat_en})...")
        articles = []
        
        # 优先使用 RSS
        if cat_en in RSS_FEEDS:
            articles = fetch_rss(RSS_FEEDS[cat_en])
        
        # 若 RSS 结果很少或失败，尝试备用源
        if len(articles) < 5 and cat_en in BACKUP_FEEDS:
            backup = fetch_rss(BACKUP_FEEDS[cat_en])
            articles.extend(backup)
        
        # 如果仍有 API 密钥且需要更丰富内容，可混合 API 结果
        if api_key and len(articles) < 10:
            api_articles = fetch_gnews(cat_en, api_key)
            # 简单去重（按链接）
            existing_links = {a["link"] for a in articles}
            for a in api_articles:
                if a["link"] not in existing_links:
                    articles.append(a)
        
        # 保留最多 20 条
        articles = articles[:20]
        if articles:
            save_news(cat_en, articles)
        else:
            print(f"⚠️ 未获取到 {cat_zh} 的新闻，请检查网络或源")
        
        time.sleep(1)  # 礼貌性延迟

if __name__ == "__main__":
    main()
