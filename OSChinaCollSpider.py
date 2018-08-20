#!/usr/bin/python
#coding:utf-8
import scrapy
import urlparse
import logging

logger = logging.getLogger(__name__)

# scrapy runspider OSChinaCollSpider.py -L WARNING

class OSChinaCollSpider(scrapy.Spider):
	name = 'oschina'
	headers = {
 					'Referer':'https://www.oschina.net',
 					'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
 	}
	cookies = {'_reg_key_': 'n5UN3jBoXvfK9mcytWqr', '__DAYU_PP': 'FbZ2YzMuan6imRJ3qe3y2efc690aea98', 'oscid': 'OU%2FiaYHKSKhs%2B%2BxJivq%2F26qHmh9J99mE%2BQXFnFzszOgtCMrhGPfdprDICQvLS9O7aSIZyPIyeTmOaQEuYGXoEcauBjiUd4E4aTPnp2F13A2DQTE1q3B0OOBrdMTVOn1ONCqx0K1O44dPdtaeJ2FApP%2BxdIq5%2BpKs7rlqePyeWCg%3D', '_user_behavior_': '323c3adc-c7e1-4a9a-81ad-4a004712ff60', 'aliyungf_tc': 'AQAAAD3rPgfwbw0AK/bCdpNv2zZWhcgf', 'gr_user_id': '12ebd213-8a7d-4a34-abea-53c201bb97e3', 'Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b': '1513586567', 'gitee-stars-jfinal': '1', 'Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b': '1513301890,1513318930,1513564542,1513586220', 'UM_distinctid': '15dca0dc25a669-091d8fddc25ff1-143a6d57-fa000-15dca0dc25b8cd', 'Hm_lvt_b7ce9c914ab525eed1f6ca8109321b00': '1494551515,1494551554,1494897811,1494928729', 'Hm_lvt_d237257153dcc02ba4647b448cbafcb8': '1511762994,1512093145'}
	
	def start_requests(self):
 		return [scrapy.FormRequest(
 				url= 'https://my.oschina.net/xiaofang168/favorites',
 				headers=self.headers,
 				cookies=self.cookies,
				callback=self.parse)]

	def parse(self, response):
		# logging.warning(response.css('div.favorites-item.layout-flex'))
		for favorite in response.css('div.favorites-item.layout-flex'):
			link = favorite.css('div.flex-grow').xpath('.//a/@href').extract_first()
			text = favorite.css('div.flex-grow').xpath('.//a/text()').extract_first()
			data = '<a href=\"'+link+'\" target=\"_blank\">'+text.replace('\n', '').strip()+'</a><br/>\n'
			logging.warning(data)
			filename = 'oschina.html'
			with open(filename, 'a') as f:
				f.write(u''.join(data).encode('utf-8'))

		next_page = response.css('ul.paging').xpath(u"//a[contains(., '下一页')]/@href").extract_first()
		
		if next_page is not None:
			next_page = response.urljoin(next_page)
			parsed = urlparse.urlparse(next_page)
			params = urlparse.parse_qs(parsed.query)
			page_num = params['p'][0]
			if int(page_num) < 7 :
				logging.warning(next_page)
				yield scrapy.Request(
					url=next_page,
					headers=self.headers,
					cookies=self.cookies,
					callback=self.parse)