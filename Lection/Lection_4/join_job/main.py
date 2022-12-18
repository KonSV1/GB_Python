import html_creater as hc
import xml_generator as xg
import data_provider as dp

print(hc.create())
print(xg.create())

if __name__ == '__main__':
    hc.new_create(xg.new_create(dp.data_collection()))