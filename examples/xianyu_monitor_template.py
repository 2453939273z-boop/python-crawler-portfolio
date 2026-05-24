# 闲鱼商品监控模板
# 可用于帮客户监控二手商品价格变化
import asyncio
from playwright.async_api import async_playwright

async def xianyu_monitor():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # 替换成你要监控的闲鱼搜索链接
        await page.goto('https://2.taobao.com/list?search_keyword=iphone')
        
        items = await page.query_selector_all('.item')
        
        for item in items[:5]:
            title = await item.query_selector_text('.title')
            price = await item.query_selector_text('.price')
            if title and price:
                print(f'商品: {title} | 价格: {price}')
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(xianyu_monitor())