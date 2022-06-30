import scrapy
import json


class JurnalInfor(scrapy.Spider):
    name = "jurnal"

    file_json = open("link.json")
    start_urls = json.loads(file_json.read())
    urls = []

    for i in range(len(start_urls)):
        b = start_urls[i]['Link']
        urls.append(b)
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        for jurnal in response.xpath('//*[@id="content_journal"]/ul/li'):
            yield {
                'Judul': jurnal.xpath('div[2]/a/text()').get(),
                'Penulis': jurnal.xpath('div[2]/div[1]/span/text()').get().replace("Penulis : ",""),
                'Dosen Pembimbing I': jurnal.xpath('div[2]/div[2]/span/text()').get().replace("Dosen Pembimbing I : ",""),
                'Dosen Pembimbing II': jurnal.xpath('div[2]/div[3]/span/text()').get().replace("Dosen Pembimbing II :",""),
                'Abstrak': jurnal.xpath('div[4]/div[2]/p/text()').get()
            }