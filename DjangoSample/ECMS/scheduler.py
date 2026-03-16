import os
from apscheduler.schedulers.background import BackgroundScheduler
from .services import run_scheduled_campaigns


def start():

    if os.environ.get('RUN_MAIN') != 'true':
        return

    scheduler = BackgroundScheduler()

    scheduler.add_job(run_scheduled_campaigns, 'interval', seconds=30)

    scheduler.start()

    print("Scheduler started...")