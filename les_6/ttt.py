import random
import collections
import sys
from typing import List

count_company = 4
quartes = [4]
company_dict = {i: int(sum([random.randint(1000, 1000000) for _ in range(4)]) / quartes)
                for i in ('Coca Cola', 'Mac Donalds', 'Teremock', 'Crysler')}
print(f'РћР±С‰РёР№ СЂР°Р·РјРµСЂ СЃР»РѕРІР°СЂСЏ company_dict = {test_size(company_dict)}\n')