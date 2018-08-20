class CookieTrans:
	
	def __init__(self, cookie):
		self.cookie = cookie
		
	def stringToDict(self):
		itemDict = {}
		items = self.cookie.split(';')
		for item in items:
			key = item.split('=')[0].replace(' ', '')
			value = item.split('=')[1]
			itemDict[key] = value
		return itemDict
	
if __name__ == "__main__":
	cookie = "Hm_lvt_b7ce9c914ab525eed1f6ca8109321b00=1494551515,1494551554,1494897811,1494928729; UM_distinctid=15dca0dc25a669-091d8fddc25ff1-143a6d57-fa000-15dca0dc25b8cd; _user_behavior_=323c3adc-c7e1-4a9a-81ad-4a004712ff60; __DAYU_PP=FbZ2YzMuan6imRJ3qe3y2efc690aea98; gitee-stars-jfinal=1; gr_user_id=12ebd213-8a7d-4a34-abea-53c201bb97e3; Hm_lvt_d237257153dcc02ba4647b448cbafcb8=1511762994,1512093145; aliyungf_tc=AQAAAD3rPgfwbw0AK/bCdpNv2zZWhcgf; _reg_key_=n5UN3jBoXvfK9mcytWqr; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1513301890,1513318930,1513564542,1513586220; oscid=OU%2FiaYHKSKhs%2B%2BxJivq%2F26qHmh9J99mE%2BQXFnFzszOgtCMrhGPfdprDICQvLS9O7aSIZyPIyeTmOaQEuYGXoEcauBjiUd4E4aTPnp2F13A2DQTE1q3B0OOBrdMTVOn1ONCqx0K1O44dPdtaeJ2FApP%2BxdIq5%2BpKs7rlqePyeWCg%3D; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1513586567"
	trans = CookieTrans(cookie)
	print trans.stringToDict()