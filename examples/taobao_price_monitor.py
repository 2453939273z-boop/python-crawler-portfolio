# 淘宝/天猫价格监控示例模板
# 使用 Playwright 实现
import asyncio
from playwright.async_api import async_playwright
import csv
from datetime import datetime

async def monitor_price():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # 示例商品链接（替换成真实链接）
        await page.goto('https://item.taobao.com/item.htm?id=123456')
        
        price = await page.query_selector_text('.price')
        title = await page.title()
        
        print(f'[{datetime.now()}] {title} - 价格: {price}')
        
        # 保存数据
        with open('price_log.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), title, price])
        
        await browser.close()

if __name__ == '__main__':
    asyncio.run(monitor_price())