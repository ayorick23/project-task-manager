import datetime
from datetime import datetime, timedelta

date_labels = []
day_labels = []
current_date = datetime.today()
def update_week():
        today = datetime.today()
        start_of_week = current_date - timedelta(days=current_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        if start_of_week.month == end_of_week.month:
            month_year = start_of_week.strftime('%B %Y')
        else:
            month_year = f"{start_of_week.strftime('%b')} - {end_of_week.strftime('%b %Y')}"
        #header.configure(text=month_year)

        for i in range(7):
            day = start_of_week + timedelta(days=i)
            is_today = (day.date() == today.date())
            is_current_week = (today >= start_of_week and today <= end_of_week)
            # Default style
            day_labels[i].configure(
                text=day.strftime('%a'),
                fg_color="transparent",
                text_color="black"
            )
            date_labels[i].configure(
                text=day.strftime('%d'),
                fg_color="transparent",
                text_color="black"
            )
            # Highlight today if in current week
            if is_today and is_current_week:
                day_labels[i].configure(
                    fg_color="#fd6868",
                    text_color="black"
                )
                date_labels[i].configure(
                    fg_color="#fd6868",
                    text_color="black"
                )
                
update_week()