import asyncio
from pyppeteer import launch

async def scraper():

    # launch the browser and a new page instance
    browser = await launch({"headless": False})
    page = await browser.newPage()

    # visit the target website
    await page.goto("https://www.scrapingcourse.com/ecommerce/")

    # select the product parent element (list tags)
    products = await page.querySelectorAll("li.product")

    # loop through the product parent element to extract titles and prices
    for product in products:
        title_element = await product.querySelector("h2")
        title = await title_element.getProperty("textContent")
 
        price_element = await product.querySelector("span.price")
        price = await price_element.getProperty("textContent")

        # output the result
        print(f"Title: {await title.jsonValue()} || Price: {await price.jsonValue()}")

    # close the browser
    await browser.close()

# run your scraper function asynchronously
asyncio.run(scraper())


response = asyncio.get_event_loop().run_until_complete(main())
