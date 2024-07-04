import pymqi
import logging
from jinja2 import Environment, FileSystemLoader
import os

class MQChecker:
    def __init__(self, mq_details):
        self.mq_details = mq_details
        self.results = []
        logging.basicConfig(level=logging.INFO)

    def check_mq_status(self, details):
        conn_info = f"{details['host']}({details['port']})"
        qmgr = None
        status = "Down"
        try:
            qmgr = pymqi.QueueManager(None)
            qmgr.connectTCPClient(details['queue_manager'], pymqi.CD(), conn_info, details['channel'])
            logging.info(f"Queue Manager {details['queue_manager']} is up and running on {details['host']}")
            status = "Up"
        except pymqi.MQMIError as e:
            logging.error(f"Could not connect to Queue Manager {details['queue_manager']} on {details['host']}: {e}")
        finally:
            if qmgr:
                qmgr.disconnect()
        self.results.append({
            'host': details['host'],
            'queue_manager': details['queue_manager'],
            'status': status
        })

    def run_checks(self):
        for mq in self.mq_details:
            self.check_mq_status(mq)
        self.generate_report()

    def generate_report(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('report_template.html')

        html_content = template.render(mqs=self.results)

        with open('mq_status_report.html', 'w') as f:
            f.write(html_content)

        logging.info("Report generated: mq_status_report.html")

