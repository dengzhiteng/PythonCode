import openpyxl
import time
from dztModule import sendMail
wb = openpyxl.load_workbook('openpyxl/工资条.xlsx')
sheet = wb.active
sheetName1=wb.sheetnames[0]
rows = sheet.rows
count=0

thead_html='''
<thead>
<th> 邮箱</th>
<th> 姓名</th>
<th> 性别</th>
<th> 部门</th>
<th> 薪资</th>
</thead>
'''
for row in rows:
    if count==0:
        count += 1;
        continue;
    row_values = []
    td_html=''
    for cell in row:
        row_values.append(cell.value)
        td_html += f'<td>{cell.value}</td>'

    body_html='<tr>'+td_html+'</tr>'
    send_msg=f'''
    <table border='1' cellspacing="0">
        {thead_html}
      <tbody>
          {body_html}  
     </tbody>
    </table>
    '''
    subject = f"{row_values[1]}:请查收【{sheetName1}】"
    sender = "mrdengzhiteng@163.com"
    recver = row_values[0]
    sendMail.send(sender, recver, subject, send_msg, 'html')
    time.sleep(2)