from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# 1. 启动无头浏览器
opts = Options()
opts.add_argument("--headless")
driver = webdriver.Chrome(options=opts)

all_data = []
base_url = "https://nespa2025.smallworldlabs.com/exhibitors?page={}"

# 2. 循环 1–9 页
for page in range(1, 10):
    driver.get(base_url.format(page))
    # 等待 JS 渲染完成——视具体页面结构而定
    driver.implicitly_wait(5)
    
    # 3. 定位并解析每条记录
    items = driver.find_elements_by_css_selector(".exhibitor-item")  # 示例选择器
    for it in items:
        name = it.find_element_by_css_selector(".company-name").text
        booth = it.find_element_by_css_selector(".booth-number").text
        all_data.append({"公司名称": name, "展位号": booth})

driver.quit()

# 4. 生成 DataFrame 并输出
df = pd.DataFrame(all_data)
print(df.to_markdown(index=False))      # 直接在控制台输出 Markdown 表格
df.to_excel("NESPA2025_Exhibitors.xlsx", index=False)
