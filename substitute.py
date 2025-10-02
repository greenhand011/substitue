'''写⼀一个脚本，允许⽤用户按以下⽅方式执⾏行行时，即可以对指定⽂文件内容进⾏行行全局替换，且替换完毕后打印替
换了了多少处内容
写完后的脚本调⽤用⽅方式：
python your_script.py old_str new_str filename'''

import sys

def substitute(old_str,new_str,filename):
    try:
        with open(filename,'r',encoding="UTF-8",errors='ignore') as f:
            text=f.read()
        new_text=text.replace(old_str,new_str)
        count=text.count(old_str)

        with open(filename,'w',encoding="utf-8") as f:
            f.write(new_text)
        
        print(f"a total of {count} replacements were completed")

    except FileNotFoundError:
        print(f"error:not find {filename}")
    except Exception as e:
        print(f"something went wrong:{e}")

if __name__ =="__main__":
    if len(sys.argv)!=4:
        print("correct format :python your_script.py old_str new_str filename")
    else:
        old_str=sys.argv[1]
        new_str=sys.argv[2]
        filename=sys.argv[3]

        substitute(old_str,new_str,filename)