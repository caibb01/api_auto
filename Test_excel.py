import requests, pytest, jsonpath, os
from string import Template
from xToolkit import xfile
from gobal_value import g_var

test_list = xfile.read("test.xls").excel_to_dict(sheet=0)

# 自动循环 DDT
@pytest.mark.parametrize('case_info', test_list)
def test_case_ddt(case_info):
    headers = case_info['headers参数']
    dic = g_var().show_dict()
    if "$" in headers:
        headers = Template(headers).substitute(dic)

    rep = requests.request(
        url=case_info['url参数'],
        method=case_info['请求方式'],
        json=eval(case_info['Json请求参数']),
        headers=eval(headers)
    )
    # 数据写入到对象中去
    if case_info["提取参数"] != None or case_info["提取参数"] != '':
        lst = jsonpath.jsonpath(rep.json(), "$.." + case_info["提取参数"])
        g_var().set_dic(case_info['提取参数'], lst[0])
    assert rep.status_code == case_info["预期状态码"]


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--capture=sys', 'Test_excel.py', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate -c -o 测试报告")
