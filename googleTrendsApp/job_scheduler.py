from apscheduler.schedulers.background import BackgroundScheduler
import logging
from datetime import datetime

# Get the root logger
error_logger = logging.getLogger('error_logger')
info_logger = logging.getLogger('info_logger')

import pytz

# Set the timezone to Dhaka, Bangladesh
location_tz = pytz.timezone('Asia/Dhaka')



def start():
    print('[Cron jobs Started]: Google Trends Fethcing and saving ...')
    # scheduler = BackgroundScheduler(timezone="UTC")
    # Initialize the scheduler with Dhaka timezone
    scheduler = BackgroundScheduler(timezone=location_tz)
    # scheduler.add_job(execute_update_status_change_every_hour, 'interval', seconds=100)
    # scheduler.add_job(execute_update_status_change_every_hour, 'interval', minutes=5, id=f'{datetime.now()}', max_instances=1)
    # scheduler.add_job(execute_update_status_change_every_hour, 'interval', hours=1)
    scheduler.add_job(execute_save_trends_news_everyday, 'cron', day_of_week='mon-sun', hour=1, minute=55)
    scheduler.start()

# Function to check if there are any cheques in queue approaching clearance date in the current week
def execute_save_trends_news_everyday():
    from .views import Daily_News_Update_Jobs_function
    print('[Function Called]: running - execute_save_trends_news_everyday')
    try:
        Daily_News_Update_Jobs_function()
        info_logger.error(f"[Success]: execute_save_trends_news_everyday worked successfully")
    except Exception as exc:
        error_logger.error(f"[Status Change] Error: {exc}")