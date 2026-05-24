import asyncio
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext
from crawlee.storages import Dataset

async def main():
    crawler = PlaywrightCrawler(
        max_requests_per_crawl=5,
        headless=True
    )
    
    @crawler.router.default_handler
    async def handler(context: PlaywrightCrawlingContext):
        print(f"✅ 正在爬取: {context.request.url}")
        
        title = await context.page.title()
        print(f"📌 页面标题: {title}")
        
        quotes = await context.page.query_selector_all("div.quote")
        quote_list = []
        
        for quote in quotes[:3]:
            text = await quote.query_selector_text("span.text")
            author = await quote.query_selector_text("small.author")
            if text and author:
                quote_list.append({"text": text.strip(), "author": author.strip()})
        
        if quote_list:
            await context.push_data({
                "url": context.request.url,
                "title": title,
                "quotes": quote_list
            })
            print(f"💾 已保存 {len(quote_list)} 条数据")
    
    print("🚀 开始爬虫测试...")
    await crawler.run(["https://quotes.toscrape.com/"])
    
    print("🎉 爬虫完成！")

if __name__ == "__main__":
    asyncio.run(main())