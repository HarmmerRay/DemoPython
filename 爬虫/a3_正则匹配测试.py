import re

data = '''<div class="pic">
                    <em class="">1</em>
                    <a href="https://movie.douban.com/subject/1292052/">
                        <img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" class="">
                    </a>
                </div>
                '''
pattern_pic_name_addr = re.compile(r'''<div class="pic">\s*
                    <em class="">1</em>\s*
                    <a href="(https?.+?)">\s*
                        <img width="100" alt="(.+?)" src="(.+?)" class="">\s*
                    </a>\s*
                </div>''', re.DOTALL)
my = r'<a href="(^[http].+?)">.|\n+<img width="100" alt="(.+?)" src="(.+?[.webp]|[.ipg]$)" class="">.|\n+</a>'
my_list = pattern_pic_name_addr.findall(data)

print(my_list)

# import re
#
# data = '''<div class="pic">
#                     <em class="">1</em>
#                     <a href="https://movie.douban.com/subject/1292052/">
#                         <img width="100" alt="肖申克的救赎" src="图片地址" class="">
#                     </a>
#                 </div>
#                 '''
# pattern_pic_name_addr = re.compile(r'''<div class="pic">\s*
#                     <em class="">1</em>\s*
#                     <a href="(https?.+?)">\s*
#                         <img width="100" alt="(.+?)" src="(.+?)" class="">\s*
#                     </a>\s*
#                 </div>''', re.DOTALL)
#
# match = pattern_pic_name_addr.search(data)
# if match:
#     print(match.group(1), match.group(2), match.group(3))
# else:
#     print("未找到匹配项")
#
