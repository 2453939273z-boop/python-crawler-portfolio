import asyncio
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext

async def main():
    crawler = PlaywrightCrawler(max_requests_per_crawl=5)
    
    @crawler.router.default_handler
    async def handler(context: PlaywrightCrawlingContext):
        print(f'正在爬取: {context.request.url}')
        title = await context.page.title()
        print(f'页面标题: {title}')
        await context.push_data({'url': context.request.url, 'title': title})
    
    await crawler.run(['https://quotes.toscrape.com/'])

if __name__ == '__main__':
    asyncio.run(main())