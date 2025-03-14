# src/notifier.py

import smtplib
import markdown2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logger import LOG

class Notifier:
    def __init__(self, email_settings):
        self.email_settings = email_settings
    
    def notify(self, repo, report):
        if self.email_settings:
            self.send_email(repo, report)
        else:
            LOG.warning("邮件设置未配置正确，无法发送通知")
    
    def send_email(self, repo, report):
        LOG.info("准备发送邮件")
        msg = MIMEMultipart()
        msg['From'] = self.email_settings['from']
        msg['To'] = self.email_settings['to']
        msg['Subject'] = f"[GitHubSentinel]{repo} 进展简报"
        
        # 将Markdown内容转换为HTML
        html_report = markdown2.markdown(report)

        msg.attach(MIMEText(html_report, 'html'))
        try:
            server = smtplib.SMTP_SSL(self.email_settings['smtp_server'], self.email_settings['smtp_port'])
            # QQ邮箱返回的reponse不规范，导致自动关闭时出错，但是邮件已经成功发送，故使用server.quit()；其他的邮箱可以使用下方代码
            # with smtplib.SMTP_SSL(self.email_settings['smtp_server'], self.email_settings['smtp_port']) as server:
            LOG.debug("登录SMTP服务器")
            server.login(msg['From'], self.email_settings['password'])
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            LOG.info("邮件发送成功！")
            server.quit()
        except Exception as e:
            LOG.error(f"发送邮件失败：{str(e)}")


if __name__ == '__main__':
    from config import Config
    config = Config()
    notifier = Notifier(config.email)

    test_repo = "DjangoPeng/openai-quickstart"
    test_report = """
# DjangoPeng/openai-quickstart 项目进展

## 时间周期：2024-08-24

## 新增功能
- Assistants API 代码与文档

## 主要改进
- 适配 LangChain 新版本

## 修复问题
- 关闭了一些未解决的问题。

"""
    notifier.notify(test_repo, test_report)
