from MessageQueueChecker import MQChecker

if __name__ == "__main__":
    # List of MQ connection details
    mq_details = [
        {
            "host": "your.mq.host1",
            "port": "1414",
            "channel": "YOUR.CHANNEL1",
            "queue_manager": "QM1"
        },
        {
            "host": "your.mq.host2",
            "port": "1414",
            "channel": "YOUR.CHANNEL2",
            "queue_manager": "QM2"
        },
        # Add more MQ details as needed
    ]

    checker = MQChecker(mq_details)
    checker.run_checks()
