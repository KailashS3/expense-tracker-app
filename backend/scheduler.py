from app import app
from models import db, NotificationSetting

import schedule
import time


def check_notifications():

    with app.app_context():

        settings = NotificationSetting.query.filter_by(
            scheduler_enabled=True
        ).all()

        for setting in settings:

            print(
                f"Checking notifications for user "
                f"{setting.user_id}"
            )

            if setting.daily_enabled:

                print("Daily notification")

            if setting.weekly_enabled:

                print("Weekly notification")

            if setting.monthly_enabled:

                print("Monthly notification")


schedule.every(1).minutes.do(
    check_notifications
)

while True:

    schedule.run_pending()

    time.sleep(1)
