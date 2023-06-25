import scrapy
from scrapy.crawler import CrawlerProcess

class EuroligueSpider(scrapy.Spider):
    name = "euroligue_crawler"
    start_urls = ["https://www.livescore.in/es/partido/6XNiP0S3/#/resumen-del-partido/punto-a-punto/0"]

    def parse(self, response):
        for match_row in response.css('.matchHistoryRow__scoreBox'):
            score_1 = match_row.css('#detail > div.matchHistoryRowWrapper > div:nth-child(3) > div.matchHistoryRow__scoreBox > div:nth-child(1)::text').get()
            print(score_1)
            score_2 = match_row.css('.matchHistoryRow__score.matchHistoryRow__bold::text').get()
            print(score_2)
            combined_score = f"{score_1}-{score_2}" if score_1 and score_2 else None
            if combined_score:
                data = {'score': combined_score}
                print(data)
                yield data
process = CrawlerProcess(
    settings={"FEEDS": {"items.csv": {"format": "csv"}}}
)
process.crawl(EuroligueSpider)
process.start()