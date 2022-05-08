
import time
import json
from selenium import webdriver

import unittest
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#website 
test_url='https://opensea.io/assets/0x8d04a8c79ceb0889bdd12acdf3fa9d207ed3ff63/46'

driver.maximize_window()


class WebTableTest(unittest.TestCase):
 
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
 
    def test_1_get_num_rows_(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "Blockreact__Block-sc-1xf18x6-0 ldOVZq")))
 
        num_rows = len (driver.find_elements_by_xpath("//*[@id='__next']/div[1]/main/div/div/div/div[2]/div/div[4]/div/div/div/div/div/div/ul/li[2]"))
        print("Rows in table are " + repr(num_rows))
 

    def test_2_get_num_cols_(self):
        driver = self.driver
        driver.get(test_url)
        
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "w3-example")))
        # num_cols = len (driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr/th"))
        num_cols = len (driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[2]/td"))
        print("Columns in table are " + repr(num_cols))
 
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
 
if __name__ == "__main__":
    unittest.main() 






    #<div class="Blockreact__Block-sc-1xf18x6-0 ldOVZq"><ul role="table" class="Tablereact__TableContainer-sc-120fhmz-0 hnDaMs"><li role="row" class="Tablereact__TableRow-sc-120fhmz-1 fwzXIM"><div role="columnheader" class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm">Price</div></div><div role="columnheader" class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm">USD Price</div></div><div role="columnheader" class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"></div></div><div role="columnheader" class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm">Expiration</div></div><div role="columnheader" class="Tablereact__TableCellContainer-sc-120fhmz-2 jKElJJ"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm">From</div></div></li><li role="row" class="Tablereact__TableRow-sc-120fhmz-1 fwzXIM"><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"><div class="Pricereact__DivContainer-sc-t54vn5-0 idXpZg Price--main"><div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 goGidb"><a class="Linkreact__StyledA-sc-18se2b0-0 iWVmEt" href="https://support.opensea.io/hc/en-us/articles/360063498293-What-s-WETH-How-do-I-get-it-" rel="nofollow noopener" target="_blank"><div size="16" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 CenterAlignedreact__CenterAligned-sc-1ek5672-0 Avatarreact__AvatarContainer-sc-sbw25j-0 dcFzHI jYqxGr gXnSUK gJMdLt dpwCtQ dukFGY"><img class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 dcFzHI hzWBaN" src="https://storage.opensea.io/files/accae6b6fb3888cbff27a013729c22dc.svg" size="16"></div></a></div><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount">5.951 <span class="Price--raw-symbol">WETH</span></div></div></div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"><div class="Pricereact__DivContainer-sc-t54vn5-0 idXpZg"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--fiat-amount">$18,695.96</div></div></div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"></div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm">in 4 hours</div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"><div class="AccountLinkreact__DivContainer-sc-4gdciy-0 fkuTPI AccountLink--ellipsis-overflow" data-testid="AccountLink"><a class="Linkreact__StyledA-sc-18se2b0-0 iWVmEt AccountLink--ellipsis-overflow" href="/0x786a0c76494682b3c52f0c566ebd3e8375020b06"><span>786A0C</span></a></div></div></div></li><li role="row" class="Tablereact__TableRow-sc-120fhmz-1 fwzXIM"><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"><div class="Pricereact__DivContainer-sc-t54vn5-0 idXpZg Price--main"><div cursor="pointer" class="Blockreact__Block-sc-1xf18x6-0 goGidb"><a class="Linkreact__StyledA-sc-18se2b0-0 iWVmEt" href="https://support.opensea.io/hc/en-us/articles/360063498293-What-s-WETH-How-do-I-get-it-" rel="nofollow noopener" target="_blank"><div size="16" class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 CenterAlignedreact__CenterAligned-sc-1ek5672-0 Avatarreact__AvatarContainer-sc-sbw25j-0 dcFzHI jYqxGr gXnSUK gJMdLt dpwCtQ dukFGY"><img class="Blockreact__Block-sc-1xf18x6-0 Avatarreact__ImgAvatar-sc-sbw25j-1 dcFzHI hzWBaN" src="https://storage.opensea.io/files/accae6b6fb3888cbff27a013729c22dc.svg" size="16"></div></a></div><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--amount">5.551 <span class="Price--raw-symbol">WETH</span></div></div></div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"><div class="Pricereact__DivContainer-sc-t54vn5-0 idXpZg"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm Price--fiat-amount">$17,439.30</div></div></div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"></div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm">in an hour</div></div><div role="cell" class="Tablereact__TableCellContainer-sc-120fhmz-2 kTLznA"><div class="Overflowreact__OverflowContainer-sc-10mm0lu-0 fqMVjm"><div class="AccountLinkreact__DivContainer-sc-4gdciy-0 fkuTPI AccountLink--ellipsis-overflow" data-testid="AccountLink"><a class="Linkreact__StyledA-sc-18se2b0-0 iWVmEt AccountLink--ellipsis-overflow" href="/0x786a0c76494682b3c52f0c566ebd3e8375020b06"><span>786A0C</span></a></div></div></div></li></ul><div class="Blockreact__Block-sc-1xf18x6-0 Flexreact__Flex-sc-1twd32i-0 FlexVerticalreact__FlexVertical-sc-x35rw8-0 VerticalAlignedreact__VerticalAligned-sc-1v4gkkl-0 CenterAlignedreact__CenterAligned-sc-1ek5672-0 bqHBns jYqxGr gXnSUK gJMdLt dpwCtQ"></div></div>