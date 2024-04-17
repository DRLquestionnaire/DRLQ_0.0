import requests

headers = {
    'authority': 'www.lediaocha.com',
    'method': 'GET',
    'path': '/ lediaocha - api / v1 / responses / vev95 / page?test = 1',
    'scheme': 'https',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'AGL_USER_ID=07bed094-09a5-4120-8227-84d5ba760a03; device=a8f24f5f5a572d571970c3438cc81d3b7a297a52; LDC_TOKEN=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU5NDcyMiwiZXhwIjoxNzEzMjIzMTEwLCJpYXQiOjE3MTMxNzk5MTAsImlwIjoiMzYuMTUyLjExNS4xMDUifQ.Mzx7tHSe5A1ka_EVTZ4tZxNIrZJGlwJI_g7lUfJBMpo; LDC_RTOKEN=eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU5NDcyMiwiZXhwIjoxNzE1NzcxOTEwLCJpYXQiOjE3MTMxNzk5MTAsImlwIjoiMzYuMTUyLjExNS4xMDUifQ._k6nxtcfpNRB5S0LQDMdgSDmEtyY5By0qm9hQGaUyzw; LDC_EXPRIED=1713223110285; tfstk=fzGmnX62Sxyf_oQ9mbVXZGbO-apJciN_5cCTX5EwUur5DiCx7FfiAmYbDnGTsYmZV-E2fEZwsDo-HPF4X1ci508f6EZxqPmK8EgxXfD5s2gsMEN9lSgb15-pvBFilqNszh7M2j4Pzy0PgPyVesemc5-pvQUxib1Y_Apmor0ozuaguZrqbu5zVr44_oyN4TzU4lPa_cSrzPzC_lz47zlYNOZncDhyRZkRXOl5aba0nlfTP1DsO6egYkrl_hhToGrEuufN_oZUKOuoknfIySGZxynvasmn72MaEfjyxlGozjkZPiYzt4D-p-Dk01q-MP2U_8bN_4042DcaTBSuPYuxQjicS1zjMXegA8YN1RFr9JkEmNTIzSzZfJG9AsZq72GIpWAcArDr-7jzhTWFAqC_zFhPCOw4PzqItQfb0ADQs8Lkr9Oz3zaXZUYlCOw4PzqprUXFU-z7lQf..; Hm_lvt_d67baafd318097a18e70ee8d8d1de57a=1713179893,1713190958; Hm_lvt_ee6df2fcc4a41d9c69a823ade6ef9e0e=1713179892,1713190959; Hm_lpvt_d67baafd318097a18e70ee8d8d1de57a=1713191631; Hm_lpvt_ee6df2fcc4a41d9c69a823ade6ef9e0e=1713191631',
    'Referer': 'https://www.lediaocha.com/r/d65l?test=1&theme=1&template=1',
    'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Uuid': 'c1dca67531e89a3e1a578950483c3df5'
}

url = 'https://www.lediaocha.com/lediaocha-api/v1/responses/no417/page?test=1'  # url

res = requests.get(url, headers=headers)
print(res.status_code)
# print(res.text)
res2 = res.json()
# print(res2)
# print(res2['data'][0]['nodeVos'])
for i in res2['data'][0]['nodeVos']:
    text = i['title'].replace('<font color="#484848" face="Helvetica Neue, PingFang SC, Hiragino Sans GB, HeitiSC, Helvetica, Arial, Microsoft YaHei, WenQuanYi Micro Hei, sans-serif"><span style="word-spacing: 0px;">', '').replace('</p>', '').replace('<p>', '').replace('</span>', '').replace('</font>', '').replace('<br>', '').replace('<div>', '').replace('</div>', '').replace('<span style="color: rgb(72, 72, 72); font-family: &quot;Helvetica Neue&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, HeitiSC, Helvetica, Arial, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; word-spacing: 0px;">', '').replace('<span style="color: rgb(38, 38, 38); font-family: &quot;Helvetica Neue&quot;, Helvetica, Arial, &quot;PingFang SC&quot;, &quot;Microsoft YaHei&quot;, &quot;Microsoft YaHei UI&quot;, 微软雅黑, sans-serif; word-spacing: 0px;">', '').replace('<strong>', '').replace('<strong>', '').replace('</strong>', '')+'\n'
    print(text)
    with open('./texts/关于购房需求的调查问卷.txt', 'a', encoding='utf-8') as f:
        f.write(text)
